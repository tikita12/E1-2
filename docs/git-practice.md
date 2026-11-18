# clone·pull 실제 실습 기록

실습일: 2026-11-17 (Asia/Seoul)

- 원격: `git@github.com:tikita12/E1-2.git`
- 기존 작업 폴더: `/home/bshin/projects/myapp/E1-2`
- 별도 복제 폴더: `/tmp/e12-git-practice-cHUWjP/E1-2`
- 복제본 변경: README 끝에 Git 실습 메모를 추가
- 결과: 복제본 커밋 `72aa641`을 원격에 올리고 기존 폴더에서 pull로 가져옴

아래 출력은 실제 실행 결과다. 출력이 없는 성공 명령은 종료 코드 0으로 기록했다. 임시 복제 폴더는 시스템 정리 시 사라질 수 있으므로 증거를 이 문서에 남긴다.

실제 콘솔 화면: [clone·push·pull 캡처](screenshots/git-workflow.png). 새 캡처는 임시 로컬 원격 저장소에서 실행했고, 아래 기록은 GitHub 원격 저장소에 수행했던 기존 실습 결과다.

## 1. 기존 작업 폴더에서 별도 경로로 복제

```text
$ git clone git@github.com:tikita12/E1-2.git /tmp/e12-git-practice-cHUWjP/E1-2
Cloning into '/tmp/e12-git-practice-cHUWjP/E1-2'...
```

종료 코드: 0

## 2. 복제 폴더에서 실행

```text
$ git add README.md
```

종료 코드: 0

## 3. 복제 폴더에서 실행

```text
$ git commit -m '문서: 복제 저장소에서 README 실습 메모 추가'
[main 72aa641] 문서: 복제 저장소에서 README 실습 메모 추가
 1 file changed, 2 insertions(+)
```

종료 코드: 0

## 4. 복제 폴더에서 실행

```text
$ git push origin main
To github.com:tikita12/E1-2.git
   59c1c80..72aa641  main -> main
```

종료 코드: 0

## 5. 기존 작업 폴더에서 실행

```text
$ git pull --ff-only origin main
From github.com:tikita12/E1-2
 * branch            main       -> FETCH_HEAD
   59c1c80..72aa641  main       -> origin/main
Updating 59c1c80..72aa641
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

종료 코드: 0

## 6. 기존 작업 폴더에서 실행

```text
$ git log -1 --oneline
72aa641 문서: 복제 저장소에서 README 실습 메모 추가
```

종료 코드: 0

## 7. 기존 작업 폴더에서 실행

```text
$ git status --short --branch
## main...origin/main
```

종료 코드: 0

## 8. 기존 작업 폴더에서 실행

```text
$ git diff 59c1c80..HEAD -- README.md
diff --git a/README.md b/README.md
index 00a84e4..106f922 100644
--- a/README.md
+++ b/README.md
@@ -153,3 +153,5 @@ python3 tools/benchmark.py

 이미지를 제외하는 AI 사전평가에서도 읽을 수 있도록 코드와 마크다운 실행 기록을 함께 제출합니다. 과제에서 별도로 요구한 화면 캡처는 [스크린샷 준비 절차](docs/screenshots/README.md)에 따라 첨부해야 합니다.

+Git 실습 메모: 이 문장은 별도로 clone한 저장소에서 README를 수정하는 실습으로 추가했습니다.
+
```

종료 코드: 0

## 확인

`git pull --ff-only origin main`이 README의 2줄 변경을 가져왔고, `git log -1`에서 복제본 커밋을 확인했다. 이어서 `git diff 59c1c80..HEAD -- README.md`로 실습 문장이 반영된 것을 확인했다. `--ff-only`는 기존 로컬에 충돌하는 새 커밋이 없을 때만 앞으로 이동하도록 제한한다.

이 실습은 기존 main을 먼저 푸시한 상태에서 진행했다. 위 status 출력은 증빙 문서를 쓰기 직전의 상태이며, 이후 이 문서 자체를 별도 커밋으로 반영한다.
