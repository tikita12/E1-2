class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

quizzes = [
    Quiz("현재 작업 디렉터리를 확인하는 명령어는?", ["ls", "pwd", "cd", "mkdir"],
2),
    Quiz("숨김 파일까지 파일 목록을 보는 명령어는?", ["ls", "ls -a", "pwd", "cp"],
2),
    Quiz("파일을 복사하는 명령어는?", ["mv", "rm", "cp", "cat"], 3),
    Quiz("파일 권한을 변경하는 명령어는?", ["chown", "chmod", "touch", "grep"], 2),
    Quiz("변경 내용을 스테이징 영역에 올리는 Git 명령어는?", ["git push", "git add", "git log", "git pull"], 2),
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
        print("퀴즈 풀기")
    elif choice == 2 :
        print("퀴즈 추가")
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




 
