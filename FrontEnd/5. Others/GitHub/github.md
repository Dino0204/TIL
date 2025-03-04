# GitHub

## 용어

---

### 1. 저장소 (Repository)

- 파일이나 폴더를 저장하는 공간,Git으로 관리함
- GitHub에서 프로젝트 호스팅 및 협업 지원.

### 2. 커밋 (Commit)

- 파일을 추가하거나 변경한 내용을 저장소에 **저장** 함.

### 3. 푸시 (Push)

- 로컬 저장소에서 수정된 파일을 원격 저장소로 **업로드** 함.

### 4. 브랜치 (Branch)

- **독립적 작업 공간**, 기능 실험 or 이슈 해결에 사용.

### 5. 풀 리퀘스트(Pull Request) : PR

- 다른 사람의 원격 저장소에서 수정된 내용을 **내 로컬 저장소**로 가져오는 요청.

### 6. 포크 (Fork)

- **다른 사람**의 원격 저장소에 저장된 소스를 내 원격 저장소로 복제할 때 사용하는 명령어.

### 7. 이슈(Issue)

- 버그, 기능 요청 또는 진행 중인 작업에 대한 **토론 포럼**.

## 협업 방법

---

### 1. 저장소(Repository) 생성

- GitHub에서 새로운 레포지토리를 만들고, 원하는 이름으로 레포지토리를 생성하고, 공개 여부를 설정.

### 2. 팀원 초대하기

- GitHub 레포지토리의 설정(Settings)에서 Collaborators(협력자)을 클릭 후,팀원의 GitHub ID 또는 이메일을 추가하면 팀원이 초대수락을 받을 수 있음.

### 3. Git Clone으로 협업하기

- 레포지토리가 공개되어 있다면 누구나 `git clone` 을 통해 컴퓨터로 받을 수 있음.
  레포지토리가 비공개라면 Collaborator로 등록되어야 함.
  `git clone` 은 모든 기록과 역사를 가져오므로, 이전 기록으로 돌아갈 수 있음.
  `git pull, git push` 를 통해 수정사항을 반영하거나 내려받을 수 있음.

### 4. Git Fork로 복제하기

- 다른 사람의 저장소를 복제하여 내 GitHub 저장소에 새로 만드는 방법.
  파일과 commit 기록까지 모두 복제됨.
  `git remote add upstream` (원본 repo 주소)를 통해 원본 저장소를 지정하고, `git pull upstream` (브랜치명)으로 수정사항을 받아올 수 있음.

## 참고자료

---

- [Pull-Request](https://holika.tistory.com/entry/Git-%EC%82%BD%EC%A7%88%EA%B8%B0%EB%A1%9D-PR%EC%9D%84-%EC%98%AC%EB%A6%AC%EB%8B%A4-Pull-Request%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C)
