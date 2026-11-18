# 과제·평가 항목 점검

이 문서는 제출 준비 현황이며 공식 평가의 통과를 보장하지 않는다.

| AI 평가 항목 | 구현 또는 증거 |
|---|---|
| 1. 전체 메뉴 기능 | main.py의 QuizGame, execution.md, 메뉴·기능별 실제 스크린샷 |
| 2. 정오답·입력 검사 | Quiz, 입력 함수, validation.md |
| 3. 재실행 데이터 유지 | 저장/불러오기, 재실행 테스트와 실행 기록 |
| 4. 기본 퀴즈 5개 이상 | main.py의 기본 목록 5개, README |
| 5. 원격 업로드·커밋 10개 이상 | README와 environment.md의 c7e05ac 기준 86개 이력 스냅샷 및 실제 커밋 출력 |
| 6. 브랜치·병합 | README와 environment.md의 `git log --graph`, 실제 merge 커밋 |
| 7. clone·pull | git-practice.md의 GitHub 실습 기록과 screenshots/git-workflow.png의 실제 터미널 캡처 |
| 8. 클래스 책임 | README의 클래스·함수 책임 |
| 9. 입력·진행·파일 처리 분리 | README와 main.py |
| 10. 입출력 시점·순서 | README의 불러오기·저장 순서 |
| 11. 종료·데이터 동기화 | run의 예외 처리/finally, SIGINT·EOF 테스트 |
| 12. 커밋 단위·메시지 규칙 | README의 Git 작업 규칙 |
| 13. 클래스 선택 이유 | README의 역할·재사용 설명 |
| 14. JSON 선택 이유 | README의 장점·단점 |
| 15. 파일 오류·복구 | 읽기/쓰기 오류 mock 테스트, README 복구 절차 |
| 16. 대량 데이터 고려 | performance.md의 실측·분석·개선 방향 |
| 17. 손상 파일 보관·초기화 | backup_corrupt_state, 손상·보관 실패 테스트 |
| 18. 변경 영향 분석 | README의 요구 변경 표 |

## 별도 제출 항목

- 저장소: https://github.com/tikita12/E1-2 / main
- 환경·실행·Git 그래프 텍스트 증거: docs의 각 문서
- **실제 콘솔·Git 스크린샷 7장 첨부 완료**: screenshots/README.md에서 확인

손상 파일 보관은 이전 정상 버전으로 자동 복원하는 기능과 다르다. 정상 파일의 주기적 백업·원자적 저장은 구현하지 않았으며 README에 한계를 명시했다.
