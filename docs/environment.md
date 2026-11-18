# 실행 환경과 Git 기록

## 2026-11-18 평가 보완 시점

기준 원격 커밋: `c7e05ac` (`origin/main`). 이 기록은 README의 평가 보완 문서를 작성하기 직전의 스냅샷이며, 그 뒤에 추가되는 문서 커밋은 아래 숫자와 그래프에 포함되지 않습니다.

- OS: `Linux-6.18.58.1-microsoft-standard-WSL2-x86_64-with-glibc2.43`
- Python: `3.14.4`
- Git: `2.53.0`
- 원격: `git@github.com:tikita12/E1-2.git`

```text
$ git rev-list --count origin/main
86
```

아래는 실제 구현과 테스트에 영향을 준 커밋 12개의 출력입니다.

```text
$ git log --oneline --no-merges -12 origin/main -- main.py tests/test_game.py
4c006db 기능: 보너스 과제 랜덤 퀴즈 출제 구현
ad5bd9a 문서: 제출 설명과 실행 검증 및 성능 측정 자료 준비
2534a84 게임 기능을 메서드로 정리하고 들여쓰기 오류 수정
cd16402 Refactor: Quiz 클래스에 문제 출력과 정답 확인 메서드 추가
1b99363 Feat: 손상 파일 보관 및 기본 데이터 복구
3055bde Feat: 저장 데이터의 자료형과 값 범위 검사
f2f6ef0 수정-메뉴중복
1df9a4f 입력중단 시 저장 및 종료처리
ba4a44e 퀴즈 진행과 점수 계산을 quizgmae메서드로 이동
4656003 quizgame 속성으로 퀴즈, 최고점수 관리
c311843 game 클래스 추가
12d57f6 빈문제 등록 방지 처리
```

브랜치와 병합 커밋은 다음 실제 그래프에서 확인할 수 있습니다.

```text
$ git log --oneline --graph --all -7
*   c7e05ac Merge branch 'feature-show-complete-scoring-loop'
|\
| * e160ef7 점수 계산 코드 전체를 25페이지에 표시
|/
*   30a6947 Merge branch 'feature-use-actual-play-quiz-argument'
|\
| * 8ae311c play_quiz 실제 인자 이름으로 수정
|/
*   22b6b86 Merge branch 'feature-visual-function-terms'
|\
| * 3cf5f0f 함수 용어를 카드와 색상으로 구분
|/
*   f954518 Merge branch 'feature-simplify-oop-slide'
```

실제 GUI 터미널 화면은 [clone·push·pull 캡처](screenshots/git-workflow.png)에 첨부했습니다. 캡처는 원격 `main`에 쓰지 않도록 `/tmp`의 임시 로컬 원격 저장소에서 실제 clone, push, pull 명령을 실행했습니다. GitHub 원격을 사용한 이전 clone/push/pull 실습 출력은 [git-practice.md](git-practice.md)에 있습니다.
