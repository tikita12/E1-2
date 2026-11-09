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
    print("<나만의 시험 대비 퀴즈>")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")

    choice = get_menu_choice()

    if choice == 5 :
        print(">>게임을 종료합니다.")
        break
    else :
        print(">>선택한 기능은 준비 중 입니다..")

