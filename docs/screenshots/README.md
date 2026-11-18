# 실제 실행 화면

Windows 콘솔 호스트에서 WSL의 Python 프로그램을 실제로 실행하고 창 자체를 캡처했습니다. 이미지 내용을 열어 확인했습니다. 자동 입력을 표준 입력으로 전달했으므로 입력한 글자는 콘솔에 별도로 에코되지 않습니다. 임시 폴더의 main.py 복사본과 별도 state.json을 사용했으며 사용자 저장 데이터는 변경하지 않았습니다.

| 화면 | 증거 |
|---|---|
| [메뉴](menu.png) | 저장 파일 없는 첫 실행과 종료 |
| [추가](add.png) | 새 퀴즈 등록 및 저장 완료 |
| [목록](list.png) | 기본 5개와 추가한 문제 1개 |
| [플레이](play.png) | 6문제 정답 결과와 최고점 갱신 |
| [재실행 점수](score.png) | 새 프로세스에서 저장된 100점 불러오기 |
| [환경·Git](environment.png) | Python/Git/WSL 버전과 커밋 그래프 |
| [Git clone·push·pull](git-workflow.png) | 임시 로컬 원격에서 실제 명령을 실행한 터미널 캡처. GitHub 원격 실습 로그는 `docs/git-practice.md` 참조 |

프로그램 화면 6장은 38993b5 기준이며, Git clone·push·pull 화면은 c7e05ac 기준 코드에서 별도 임시 로컬 원격을 실제로 조작해 촬영했습니다. 모든 화면은 실제 Windows 콘솔 창을 캡처했으며 터미널 출력을 이미지로 합성하지 않았습니다. 화면 캡처에는 Windows 창 API를 사용했습니다. clone/push/pull 작업은 임시 경로에서만 수행했습니다. GitHub 원격을 사용한 실제 실습 출력은 상위 폴더의 `git-practice.md`에서 확인할 수 있습니다. 프로그램 실행 입력과 상세 출력은 `execution.md`에 있습니다.
