
import json
from pathlib import Path

STATE_FILE = Path(__file__).resolve().parent / "state.json"

class Quiz: #문제의 정보를 관리하는 클래스
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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
    print()
    print(current_quiz.question)

    for number, choice in enumerate(current_quiz.choices, start=1):
        print(f"{number}, {choice}")

    answer = get_number("정답 번호를 입력하세요: ")

    if answer == current_quiz.answer:
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

def add_quiz(quizzes):
    new_question = get_text("새 문제를 입력하세요: ").strip()
    new_choices = []

    for number in range(1,5):
        text = get_text(f"선택지 {number}: ").strip()
        new_choices.append(text)

    new_answer = get_number("정답 번호를 입력하세요 : ")

    new_quiz = Quiz(new_question, new_choices, new_answer)
    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다.")



quizzes = [
    Quiz("현재 작업 디렉터리를 확인하는 명령어는?", ["ls", "pwd", "cd", "mkdir"],
2),
    Quiz("숨김 파일까지 파일 목록을 보는 명령어는?", ["ls", "ls -a", "pwd", "cp"],
2),
    Quiz("파일을 복사하는 명령어는?", ["mv", "rm", "cp", "cat"], 3),
    Quiz("파일 권한을 변경하는 명령어는?", ["chown", "chmod", "touch", "grep"], 2),
    Quiz("변경 내용을 스테이징 영역에 올리는 Git 명령어는?", ["git push", "git add", "git log", "git pull"], 2),
 Quiz(
        "input()으로 받은 값의 기본 자료형은?",
        ["정수 int", "문자열 str", "실수 float", "불리언 bool"],
        2
    ),
    Quiz(
        "문자열의 앞뒤 공백을 제거하는 메서드는?",
        ["split()", "append()", "strip()", "replace()"],
        3
    ),
    Quiz(
        'int("3")의 결과는?',
        ["정수 3", '문자열 "3"', "True", "오류 발생"],
        1
    ),
    Quiz(
        'int("abc")를 실행하면 발생하는 오류는?',
        ["NameError", "TabError", "SyntaxError", "ValueError"],
        4
    ),

]

def save_state(quizzes, best_score):
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

def load_state(default_quizzes):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

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

    except (json.JSONDecodeError, UnicodeDecodeError, KeyError, TypeError):
        print("저장 데이터에 문제가 있어 기본 퀴즈로 시작합니다.")
        return default_quizzes, None

    except OSError as error:
        print(f"파일을 읽을 수 없습니다: {error}")
        return default_quizzes, None

    else:
        print("저장된 퀴즈와 최고 점수를 불러왔습니다.")
        return loaded_quizzes, loaded_best_score

def bestscore(best_score):
    if best_score is None:
        print("아직 퀴즈를 풀지 않았습니다.")
    else:
        print(f"최고점수 {best_score}점")


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

        for current_quiz in self.quizzes:
            result = play_quiz(current_quiz)

            if result:
                correct_count += 1

        print(f"결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답")

        score = round(correct_count / len(self.quizzes) * 100)
        print(f"이번 점수: {score}점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

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
                    add_quiz(self.quizzes)
                elif choice == 3:
                    print()
                    print("-" * 40)
                    print("퀴즈 목록")
                    print("-" * 40)

                    if len(self.quizzes) == 0:
                        print("등록된 퀴즈가 없습니다.")
                    else:
                        for number, quiz in enumerate(self.quizzes, start=1):
                            print(f"{number}. {quiz.question}")

                elif choice == 4:
                    bestscore(self.best_score)

        except KeyboardInterrupt:
            print("\nCtrl+C로 종료를 요청했습니다.")

        except EOFError:
            print("\n입력이 종료되어 게임을 종료합니다.")

        finally:
            save_state(self.quizzes, self.best_score)
            print(">>게임을 종료합니다.")    

quizzes, best_score = load_state(quizzes)
game = QuizGame(quizzes, best_score)
game.run()

while True:
    game.show_menu()

    choice = get_menu_choice()

    if choice == 5 :
        save_state(game.quizzes, game.best_score)
        print(">>게임을 종료합니다.")
        break
    elif choice == 1 :
        game.play()
    elif choice == 2 :
        add_quiz(game.quizzes)
    elif choice == 3 :
        print()
        print("-" * 40 )
        print("퀴즈 목록")
        print("-" * 40)

        if len(game.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
        else:
            for number,  quiz in enumerate(game.quizzes, start=1):
                print(f"{number}. {quiz.question}")
    elif choice == 4 :
        bestscore(game.best_score)
    else :
        print(">>선택한 기능은 준비 중 입니다..")




 
