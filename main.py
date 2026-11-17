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
    Quiz(
        "함수를 정의할 때 사용하는 키워드는?",
        ["class", "def", "return", "for"],
        2
    ),
    Quiz(
        "함수를 끝내고 호출한 곳으로 값을 돌려주는 키워드는?",
        ["print", "break", "return", "continue"],
        3
    ),
    Quiz(
        "퀴즈 객체 5개가 담긴 quizzes에서 len(quizzes)의 결과는?",
        ["5", "4", "첫 번째 퀴즈", "마지막 퀴즈"],
        1
    ),
    Quiz(
        "if result == True: 안쪽 코드는 언제 실행될까?",
        ["항상 실행된다", "result가 False일 때", "반복이 끝난 뒤", "result가 True일 때"],
        4
    ),
    Quiz(
        "Quiz 클래스를 사용하는 이유로 가장 적절한 것은?",
        [
            "모든 오류를 자동으로 해결하기 위해",
            "문제·선택지·정답을 같은 구조로 묶어 관리하기 위해",
            "GitHub에 자동으로 업로드하기 위해",
            "프로그램을 무조건 빠르게 만들기 위해"
        ],
        2
    ),
    Quiz(
        "퀴즈 추가 기능을 완성한 뒤 남길 커밋 메시지로 가장 적절한 것은?",
        [
            "수정",
            "완료",
            "Feat: 퀴즈 추가 기능 구현",
            "아무거나"
        ],
        3
    ),
    Quiz(
        "main으로 이동한 뒤 feature/quiz-add 브랜치를 병합하는 명령은?",
        [
            "git merge feature/quiz-add",
            "git add feature/quiz-add",
            "git push feature/quiz-add",
            "git init feature/quiz-add"
        ],
        1
    ),
    Quiz(
        "퀴즈 데이터를 JSON으로 저장하는 이유로 가장 적절한 것은?",
        [
            "내용을 자동으로 암호화해 주기 때문에",
            "데이터 구조를 표현할 수 있고 사람이 읽기도 쉬워서",
            "파일 오류가 절대 발생하지 않아서",
            "데이터가 많아져도 처리 시간이 늘어나지 않아서"
        ],
        2
    ),
    Quiz(
        "실행 중 Ctrl+C를 눌렀을 때 일반적으로 발생하는 파이썬 예외는?",
        [
            "ValueError",
            "NameError",
            "KeyboardInterrupt",
            "SyntaxError"
        ],
        3
    ),
    Quiz(
        "처음 실행해서 state.json 파일이 없다면 적절한 처리는?",
        [
            "기본 퀴즈로 시작한다",
            "무조건 프로그램을 종료한다",
            "사용자 코드를 삭제한다",
            "파일이 생길 때까지 무한히 기다린다"
        ],
        1
    ),
    Quiz(
        "쓰기 권한이 없어 파일 저장에 실패했을 때 적절한 처리는?",
        [
            "저장에 성공했다고 출력한다",
            "오류를 숨기고 저장된 것으로 간주한다",
            "실패를 안내하고 저장 위치와 권한을 확인하도록 한다",
            "퀴즈 목록을 비운다"
        ],
        3
    ),
    Quiz(
        "퀴즈 1000개의 처리 성능을 설명하기 위해 필요한 것은?",
        [
            "코드 줄 수만 센다",
            "실행하지 않고 빠를 것이라고 예상한다",
            "README에 빠르다고 적는다",
            "실제 데이터로 처리 시간을 측정하고 조건과 결과를 기록한다"
        ],
        4
    ),


]

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
        print("점수 확인")
    else :
        print(">>선택한 기능은 준비 중 입니다..")




 
