"""표준 라이브러리만 사용하며 저장 파일은 임시 폴더에 만든다."""
import contextlib
import io
import json
import os
from pathlib import Path
import selectors
import shutil
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import main


class GameTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="quiz-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = self.root / "state.json"
        self.script = self.root / "main.py"
        shutil.copy2(main.__file__, self.script)

    def run_game(self, inputs):
        result = subprocess.run(
            [sys.executable, str(self.script)], input=inputs,
            text=True, capture_output=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        return result.stdout

    def read_state(self):
        return json.loads(self.state.read_text(encoding="utf-8"))

    def test_first_run_and_menu_input(self):
        output = self.run_game("abc\n\n9\n 4 \n5\n")
        self.assertIn("숫자를 입력해주세요.", output)
        self.assertIn("1~5 사이", output)
        self.assertIn("아직 퀴즈를 풀지 않았습니다.", output)
        self.assertEqual(len(self.read_state()["quizzes"]), 5)
        self.assertIsNone(self.read_state()["best_score"])

    def test_add_validation_and_restart(self):
        output = self.run_game("2\n\n   \n새 문제\n\n가\n나\n다\n라\nabc\n0\n5\n 2 \n3\n5\n")
        self.assertGreaterEqual(output.count("내용을 입력해주세요."), 3)
        self.assertIn("1~4 사이", output)
        self.assertEqual(self.read_state()["quizzes"][-1], {
            "question": "새 문제", "choices": ["가", "나", "다", "라"], "answer": 2,
        })
        self.assertIn("6. 새 문제", self.run_game("3\n5\n"))

    def test_score_and_lower_score(self):
        self.seed_same_answer_quizzes()
        answers = "\n".join("1" for q in main.quizzes)
        self.run_game("1\n" + answers + "\n4\n5\n")
        self.assertEqual(self.read_state()["best_score"], 100)
        wrong = "\n".join("2" for q in main.quizzes)
        output = self.run_game("1\n" + wrong + "\n4\n5\n")
        self.assertIn("이번 점수: 0점", output)
        self.assertIn("최고 점수: 100점", output)
        self.assertEqual(self.read_state()["best_score"], 100)

    def test_first_zero_score_is_not_unplayed(self):
        self.seed_same_answer_quizzes()
        wrong = "\n".join("2" for q in main.quizzes)
        self.run_game("1\n" + wrong + "\n5\n")
        self.assertIn("최고 점수: 0점", self.run_game("4\n5\n"))

    def seed_same_answer_quizzes(self):
        data = {"quizzes": [{"question": q.question, "choices": q.choices, "answer": 1} for q in main.quizzes], "best_score": None}
        self.state.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_shuffled_play_preserves_original_and_saved_order(self):
        original = main.quizzes.copy()
        game = main.QuizGame(original.copy(), None)
        with patch("main.STATE_FILE", self.state), contextlib.redirect_stdout(io.StringIO()), patch("main.random.shuffle", side_effect=lambda order: order.reverse()) as shuffle, patch("main.play_quiz", return_value=True) as play:
            game.play()
            self.assertEqual([call.args[0] for call in play.call_args_list], original[::-1])
            self.assertEqual(game.quizzes, original)
            self.assertEqual([q["question"] for q in self.read_state()["quizzes"]], [q.question for q in original])
            self.assertEqual(game.best_score, 100)
            game.play()
            self.assertEqual(shuffle.call_count, 2)

    def test_empty_quizzes(self):
        self.state.write_text('{"quizzes": [], "best_score": null}', encoding="utf-8")
        output = self.run_game("1\n3\n5\n")
        self.assertEqual(output.count("등록된 퀴즈가 없습니다."), 2)

    def test_eof_during_registration_keeps_only_complete_quizzes(self):
        output = self.run_game("2\n미완성 문제\n보기 하나\n")
        self.assertIn("입력이 종료되어", output)
        self.assertEqual(len(self.read_state()["quizzes"]), 5)

    @unittest.skipUnless(os.name == "posix", "POSIX SIGINT 실습")
    def test_sigint(self):
        process = subprocess.Popen(
            [sys.executable, "-u", str(self.script)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        try:
            with selectors.DefaultSelector() as selector:
                selector.register(process.stdout, selectors.EVENT_READ)
                received = b""
                while "번호를 선택하세요: ".encode() not in received:
                    self.assertTrue(selector.select(5), "메뉴 대기 시간 초과")
                    chunk = os.read(process.stdout.fileno(), 4096)
                    self.assertTrue(chunk, "메뉴 전에 프로세스 종료")
                    received += chunk
            process.send_signal(signal.SIGINT)
            output, error = process.communicate(timeout=5)
            self.assertEqual(process.returncode, 0, error)
            self.assertIn("Ctrl+C로 종료".encode(), output)
            self.assertTrue(self.state.exists())
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()

    def test_corrupt_json_is_preserved_and_reset(self):
        self.state.write_text("broken json", encoding="utf-8")
        output = self.run_game("5\n")
        self.assertIn("손상 파일을 보관했습니다", output)
        backups = list(self.root.glob("state.corrupt-*.json"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "broken json")
        self.assertEqual(len(self.read_state()["quizzes"]), 5)

    def test_invalid_fields_are_rejected(self):
        good = {"question": "문제", "choices": ["가", "나", "다", "라"], "answer": 1}
        invalid = [
            [], {}, {"quizzes": {}, "best_score": None},
            {"quizzes": [good], "best_score": "100"},
            {"quizzes": [good], "best_score": True},
            {"quizzes": [good], "best_score": 101},
        ]
        for field, value in [("question", " "), ("choices", ["가"]), ("choices", ["", "나", "다", "라"]), ("answer", 9), ("answer", True)]:
            invalid.append({"quizzes": [dict(good, **{field: value})], "best_score": None})
        for data in invalid:
            with self.subTest(data=data):
                with self.assertRaises((ValueError, KeyError, TypeError)):
                    main.validate_state(data)

    def test_read_permission_error(self):
        with patch("builtins.open", side_effect=PermissionError("테스트 읽기 거부")), contextlib.redirect_stdout(io.StringIO()) as output:
            quizzes, score = main.load_state(main.quizzes)
        self.assertIs(quizzes, main.quizzes)
        self.assertIsNone(score)
        self.assertIn("파일을 읽을 수 없습니다", output.getvalue())

    def test_write_permission_error(self):
        with patch("main.STATE_FILE", self.state), patch("builtins.open", side_effect=[FileNotFoundError(), PermissionError("테스트 쓰기 거부")]), contextlib.redirect_stdout(io.StringIO()) as output:
            main.save_state(main.quizzes, None)
        self.assertIn("저장에 실패했습니다", output.getvalue())
        self.assertNotIn("저장했습니다.", output.getvalue())

    def test_backup_failure_does_not_overwrite_original(self):
        self.state.write_text("broken json", encoding="utf-8")
        with patch("main.STATE_FILE", self.state), patch.object(Path, "rename", side_effect=PermissionError("테스트 보관 거부")), contextlib.redirect_stdout(io.StringIO()) as output:
            quizzes, score = main.load_state(main.quizzes)
            main.save_state(quizzes, score)
        self.assertIn("보관에 실패했습니다", output.getvalue())
        self.assertIn("저장을 중단합니다", output.getvalue())
        self.assertEqual(self.state.read_text(), "broken json")

    def test_changes_are_saved_before_exit(self):
        with patch("main.STATE_FILE", self.state), contextlib.redirect_stdout(io.StringIO()):
            game = main.QuizGame([], None)
            with patch("builtins.input", side_effect=["즉시 저장", "가", "나", "다", "라", "1"]):
                game.add_quiz()
            self.assertEqual(len(self.read_state()["quizzes"]), 1)
            with patch("builtins.input", return_value="1"):
                game.play()
            self.assertEqual(self.read_state()["best_score"], 100)


if __name__ == "__main__":
    unittest.main()
