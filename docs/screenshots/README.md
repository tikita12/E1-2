# 제출용 화면 캡처

아직 실제 화면 스크린샷은 없다. 실행 로그는 `docs/execution.md`, 환경·Git 기록은 `docs/environment.md`에 준비했다. 아래 화면은 사용자의 터미널/편집기에서 직접 캡처해 추가해야 한다. 로그를 이미지로 꾸며 실제 스크린샷으로 대신하지 않는다.

## 캡처 순서

1. `environment.png`: 편집기에서 프로젝트를 연 화면과 터미널의 `python3 --version`, `git --version`, `git config user.name` 결과. 공개하지 않을 이메일·토큰은 제외한다.
2. `menu.png`: `python3 main.py` 실행 후 메뉴.
3. `add_quiz.png`: 2번 문제·선택지 4개·정답 입력과 등록·저장 완료.
4. `list.png`: 3번에서 추가한 문제까지 표시한 목록.
5. `play.png`: 1번의 정오답 안내와 전체 문제 풀이 결과.
6. `score.png`: 4번 최고 점수.
7. `restart.png`: 5번 종료 후 재실행하여 추가한 문제와 점수가 남은 화면.
8. `git_graph.png`: `git log --oneline --graph --all -20` 결과.
9. `clone_pull.png`: 실제 실습 로그 확인 화면. 명령 실행 당시 화면을 요구하면 `docs/git-practice.md` 절차를 별도 폴더에서 다시 수행하며 캡처한다.

Windows/WSL에서는 `Win + Shift + S`로 영역을 캡처할 수 있다. 파일을 이 폴더에 저장한 뒤 제출 저장소에 반영한다.

```bash
git add docs/screenshots
git commit -m "문서: 개발 환경과 프로그램 실행 화면 첨부"
git push origin main
```

## 제출 전 확인

- [ ] 개발 환경 화면
- [ ] 추가·목록·플레이·점수·재실행 화면
- [ ] Git 그래프 화면
- [ ] 저장소 URL과 main 브랜치 확인

이미지를 평가하지 않는 AI 사전평가를 위해 마크다운 실행 기록도 함께 유지한다.
