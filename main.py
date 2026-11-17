class Quiz:
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

def add_quiz():
    new_question = input("새 문제를 입력하세요: ").strip()
    new_choices = []

    for number in range(1,5):
        text = input(f"선택지 {number}: ").strip()
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

best_score = None

while True:
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

    choice = get_menu_choice()

    if choice == 5 :
        print(">>게임을 종료합니다.")
        break
    elif choice == 1 :
        if len(quizzes) == 0:  ##len 목록에 들어있는 항목 수를 알려주는 함수
            print("등록된 퀴즈가 없습니다.")
        else:
            correct_count = 0

            for current_quiz in quizzes:
                result = play_quiz(current_quiz)
 
                if result == True:
                    correct_count += 1
    
            print(f"결과: {len(quizzes)}문제 중 {correct_count}문제 정답")

            score = round(correct_count / len(quizzes) * 100)
            print(f"이번 점수: {score}점")

            if best_score is None or score > best_score:
                best_score = score
                print("최고 점수가 갱신되었습니다!")

    elif choice == 2 :
        add_quiz()
    elif choice == 3 :
        print()
        print("-" * 40 )
        print("퀴즈 목록")
        print("-" * 40)

        if len(quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
        else:
            for number,  quiz in enumerate(quizzes, start=1):
                print(f"{number}. {quiz.question}")
    elif choice == 4 :
        bestscore(best_score)
    else :
        print(">>선택한 기능은 준비 중 입니다..")




 
