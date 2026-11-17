# 실행 환경과 Git 기록

기록 시각: 2026-11-17T18:52:06+09:00

OS: `Linux-6.18.58.1-microsoft-standard-WSL2-x86_64-with-glibc2.43`

아래는 문서 작성 시점의 실제 명령 출력이다. 이후 문서 커밋은 이 그래프에 포함되지 않는다.

```text
$ /usr/bin/python3 --version
Python 3.14.4
```

```text
$ git --version
git version 2.53.0
```

```text
$ git config user.name
jangboyoon
```

```text
$ git remote -v
origin	git@github.com:tikita12/E1-2.git (fetch)
origin	git@github.com:tikita12/E1-2.git (push)
```

```text
$ git rev-list --count HEAD
32
```

```text
$ git log --oneline --graph --all -40
*   0084a1f 게임 기능 메서드 정리 작업을 메인 브랜치에 병합
|\  
| * 2534a84 게임 기능을 메서드로 정리하고 들여쓰기 오류 수정
|/  
*   31f4622 Merge branch 'refactor-quiz-methods'
|\  
| * cd16402 Refactor: Quiz 클래스에 문제 출력과 정답 확인 메서드 추가
|/  
*   4865f49 Merge branch 'feature-state-recovery'
|\  
| * 1b99363 Feat: 손상 파일 보관 및 기본 데이터 복구
|/  
*   d7bc356 Merge branch 'feature-state-validation'
|\  
| * 3055bde Feat: 저장 데이터의 자료형과 값 범위 검사
|/  
* f2f6ef0 수정-메뉴중복
* 1df9a4f 입력중단 시 저장 및 종료처리
* ba4a44e 퀴즈 진행과 점수 계산을 quizgmae메서드로 이동
* 4656003 quizgame 속성으로 퀴즈, 최고점수 관리
* c311843 game 클래스 추가
* 12d57f6 빈문제 등록 방지 처리
*   83a6156 Merge branch 'feature-load-state'
|\  
| * 74d5031 기능구현-저장기능
|/  
*   4d7a0eb Merge branch 'feature-save-state'
|\  
| * 80c6ca5 기능구현-점수저장
|/  
* bcd8db5 기능구현-점수확인
*   be4a8b5 :wq
|\  
| * 84e684b 퀴즈 추가
| * 5bec1df 퀴즈 추가 기능 추가
| * ebf7c5f 퀴즈 풀기 정답 번호 1~4로 제한
| * 1a20f0c 퀴즈 문제 추가 및 수정
| * 47fdf47 퀴즈 풀기 메뉴 활성화
| * 272f659 퀴즈 목록 기능 구현
| * e1e9a13 메뉴 꾸미기
* | badf9ef Quiz 클래스 구현 및 역할 문서화
|/  
* 7e7e538 메뉴 기본 설정
* 423802f 메뉴입력 공백제거
* 2f0c3f9 메뉴 구현
* e4b103f .gitignore, README.md생성
```
