from datetime import datetime
import json
import random
from pathlib import Path

STATE_FILE = Path(__file__).resolve().parent / "state.json"

class Quiz: #문제의 정보를 관리하는 클래스
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print()
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt).strip())
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if number in [1, 2, 3, 4 ]:
            return number
        
        print("1~4 사이의 번호를 입력해주세요")

def play_quiz(current_quiz):
    current_quiz.display()

    answer = get_number("정답 번호를 입력하세요: ")

    if current_quiz.check_answer(answer):
        print("정답입니다")
        return True
    else:
        print(f"오답입니다. 정답은 {current_quiz.answer}번입니다.")
        return False

def get_text(prompt):
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print("내용을 입력해주세요.")

quizzes = [
    Quiz("현재 작업 디렉터리를 확인하는 명령어는?", ["ls", "pwd", "cd", "mkdir"], 2),
    Quiz("숨김 파일까지 파일 목록을 보는 명령어는?", ["ls", "ls -a", "pwd", "cp"], 2),
    Quiz("파일을 복사하는 명령어는?", ["mv", "rm", "cp", "cat"], 3),
    Quiz("파일 권한을 변경하는 명령어는?", ["chown", "chmod", "touch", "grep"], 2),
    Quiz("변경 내용을 스테이징 영역에 올리는 Git 명령어는?", ["git push", "git add", "git log", "git pull"], 2),

]

def save_state(quizzes, best_score):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
        validate_state(existing_data)
    except FileNotFoundError:
        pass
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"기존 파일을 보호하기 위해 저장을 중단합니다: {error}")
        return
    
    quiz_data = []

    for quiz in quizzes:
        quiz_data.append({
            "question": quiz.question,
            "choices": quiz.choices,
            "answer": quiz.answer

        })
    data = {
        "quizzes": quiz_data,
        "best_score": best_score
    }

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"저장에 실패했습니다: {error}")
    else:
        print("퀴즈와 최고 점수를 저장했습니다.")

def validate_state(data):
    if not isinstance(data, dict):
        raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

    if not isinstance(data.get("quizzes"), list):
        raise ValueError("퀴즈 목록은 리스트여야 합니다.")

    for item in data["quizzes"]:
        if not isinstance(item, dict):
            raise ValueError("각 퀴즈는 딕셔너리여야 합니다.")

        question = item.get("question")
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있지 않은 문자열이어야 합니다.")

        choices = item.get("choices")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")

        for choice in choices:
            if not isinstance(choice, str) or not choice.strip():
                raise ValueError("선택지는 비어 있지 않은 문자열이어야 합니다.")

        answer = item.get("answer")
        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4 사이의 정수여야 합니다.")

    best_score = data["best_score"]
    if best_score is not None:
        if type(best_score) is not int or not 0 <= best_score <= 100:
            raise ValueError("최고 점수는 0~100 사이의 정수여야 합니다.")
def backup_corrupt_state():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup_path = STATE_FILE.with_name(
        f"state.corrupt-{timestamp}.json"
    )

    try:
        STATE_FILE.rename(backup_path)
    except OSError as error:
        print(f"손상 파일 보관에 실패했습니다: {error}")
    else:
        print(f"손상 파일을 보관했습니다: {backup_path.name}")


def load_state(default_quizzes):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        validate_state(data)

        loaded_quizzes = []

        for item in data["quizzes"]:
            quiz = Quiz(
                item["question"],
                item["choices"],
                item["answer"]
            )
            loaded_quizzes.append(quiz)

        loaded_best_score = data["best_score"]

    except FileNotFoundError:
        print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
        return default_quizzes, None

    except (ValueError, KeyError, TypeError) as error:
        print(f"저장 데이터에 문제가 있습니다: {error}")
        backup_corrupt_state()
        print("기본 퀴즈로 시작합니다.")
        return default_quizzes, None

    except OSError as error:
        print(f"파일을 읽을 수 없습니다: {error}")
        return default_quizzes, None

    else:
        print("저장된 퀴즈와 최고 점수를 불러왔습니다.")
        return loaded_quizzes, loaded_best_score

def get_menu_choice():
    while True:
        try:
            choice = int(input("번호를 선택하세요: ").strip())
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if choice in [1, 2, 3, 4, 5]:
            return choice

        print("1~5 사이의 번호를 입력해 주세요.")


class QuizGame:
    def __init__(self, quizzes, best_score): #퀴즈목록, 최고점수
        self.quizzes = quizzes
        self.best_score = best_score

    def show_menu(self):
        print()
        print("=" * 40)
        print("<나만의 시험 대비 퀴즈>")
        print("=" * 40)
        print(" [1]. 퀴즈 풀기")
        print(" [2]. 퀴즈 추가")
        print(" [3]. 퀴즈 목록")
        print(" [4]. 점수 확인")
        print(" [5]. 종료")
        print("-" * 40)

    def play(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        play_order = self.quizzes.copy()
        random.shuffle(play_order)

        for current_quiz in play_order:
            result = play_quiz(current_quiz)

            if result:
                correct_count += 1

        print(f"결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답")

        score = round(correct_count / len(self.quizzes) * 100)
        print(f"이번 점수: {score}점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

        self.save()

    def add_quiz(self):
        question = get_text("새 문제를 입력하세요: ")
        choices = []

        for number in range(1, 5):
            choice = get_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = get_number("정답 번호를 입력하세요: ")

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")
        self.save()

    def show_list(self):
        print()
        print("-" * 40)
        print("퀴즈 목록")
        print("-" * 40)

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def save(self):
        save_state(self.quizzes, self.best_score)

    def load(self):
        self.quizzes, self.best_score = load_state(self.quizzes)

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = get_menu_choice()

                if choice == 5:
                    break
                elif choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.show_score()

        except KeyboardInterrupt:
            print("\nCtrl+C로 종료를 요청했습니다.")

        except EOFError:
            print("\n입력이 종료되어 게임을 종료합니다.")

        finally:
            self.save()
            print(">>게임을 종료합니다.")

if __name__ == "__main__":
    game = QuizGame(quizzes, None)
    game.load()
    game.run()

