"""임시 저장 파일로 실제 앱의 저장/불러오기 비용을 측정한다."""
import contextlib
from datetime import datetime
import io
from pathlib import Path
import platform
import statistics
import sys
import tempfile
import time
import tracemalloc
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main


def measure(count, directory):
    quizzes = [main.Quiz(f"성능 측정 문제 {i}", ["가", "나", "다", "라"], 1) for i in range(count)]
    path = directory / f"state-{count}.json"
    save_times, load_times, scan_times = [], [], []
    with patch("main.STATE_FILE", path), contextlib.redirect_stdout(io.StringIO()):
        # 준비 저장 후, 기존 파일 검사를 포함하는 저장을 측정한다.
        main.save_state(quizzes, 80)
        for _ in range(10):
            start = time.perf_counter()
            main.save_state(quizzes, 80)
            save_times.append((time.perf_counter() - start) * 1000)
            start = time.perf_counter()
            loaded, score = main.load_state([])
            load_times.append((time.perf_counter() - start) * 1000)
            assert len(loaded) == count and score == 80
            target = f"성능 측정 문제 {count - 1}"
            start = time.perf_counter()
            found = next(q for q in loaded if q.question == target)
            scan_times.append((time.perf_counter() - start) * 1000)
            assert found.question == target

        # 시간 측정에 tracemalloc 오버헤드를 섞지 않고 별도로 측정한다.
        tracemalloc.start()
        loaded, score = main.load_state([])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
    return [count, path.stat().st_size, *[statistics.median(v) for v in (save_times, load_times, scan_times)], peak / 1024]


def run():
    print("# 대량 데이터 성능 측정\n")
    print(f"측정 시각: {datetime.now().astimezone().isoformat(timespec='seconds')}\n")
    print(f"환경: Python {platform.python_version()}, {platform.platform()}\n")
    print("실행 명령: `python3 tools/benchmark.py`\n")
    print("짧은 한글 문제와 선택지 4개를 생성하고, 임시 폴더에서 각 크기별 10회 측정한 중앙값이다. 저장에는 기존 JSON 읽기·검사 비용이 포함된다. 터미널 출력과 사용자의 답변 시간은 제외한다.\n")
    print("| 문제 수 | 파일 크기(bytes) | 저장(ms) | 불러오기(ms) | 마지막 문제 선형 탐색(ms) | 불러오기 Python 할당 최대(KiB) |")
    print("|---:|---:|---:|---:|---:|---:|")
    with tempfile.TemporaryDirectory(prefix="quiz-benchmark-") as temp:
        for count in (5, 1000, 10000):
            row = measure(count, Path(temp))
            print(f"| {row[0]} | {row[1]} | {row[2]:.3f} | {row[3]:.3f} | {row[4]:.3f} | {row[5]:.1f} |")
    print("\n## 해석과 개선 방향\n")
    print("- 데이터 크기를 n으로 보면 전체 저장·불러오기·목록 순회는 O(n)이며, 메모리에 전체 목록을 보관한다. 질문 길이도 파일 크기와 메모리에 영향을 준다.")
    print("- 검색 메뉴는 아직 없다. 표의 탐색 값은 목록에서 마지막 문제를 찾는 순차 탐색 실험이다. 검색을 추가한다면 식별자와 딕셔너리 인덱스를 검토한다.")
    print("- tracemalloc 값은 불러오는 동안 새로 할당된 Python 메모리의 최대값이다. 프로세스 전체 RAM 사용량이나 이미 존재하는 퀴즈 목록의 메모리는 포함하지 않는다.")
    print("- OS 파일 캐시가 적용되는 반복 측정이며 다른 기기·긴 문제·느린 디스크에서는 결과가 달라진다. 1,000문제를 직접 출력하고 푸는 체감 시간과는 다르다.")
    print("- 대량 데이터에서는 목록 페이지 나누기, 문제 수 선택, SQLite 저장을 검토한다. 현재 과제에서는 요구된 JSON 형식을 유지한다.")


if __name__ == "__main__":
    run()
