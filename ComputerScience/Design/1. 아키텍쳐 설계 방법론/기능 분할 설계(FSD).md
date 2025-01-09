## 기존 구조와의 차이점

---

이전 프로젝트의 폴더 구조

```
src
├─components
├─context
├─imgs
└─pages
-> 1depth
```

```

```

## 기능 분할 설계(FSD)

---

![fsd](https://aw-download-file.hmg-corp.io/3m5b8c7d9k/01HVNTPT61W77JYET86YA7EEH4)
FSD는 layer, slice, segment의 3depth로 이루어져 있음

### layer

**특징**

- 최상위 depth
- 최대 6개
- src 폴더 아래에서 바로 나타나는 구조
- 관심사에 따른 분리

**종류**

1. app

- 전체 app의 로직 초기화 장소
- app의 entry point 역할을 함

2. pages

- app의 페이지를 포함

3. widgets
4. features
5. entities
6. shared

> **진입점(entry point)란?**
> 사용자가 초기에 접근하는 점점 또는 요청의 시작점 (url 또는 엔드포인트)

### slice

### segment

### 공개 api

[참고 자료](https://developers.hyundaimotorgroup.com/blog/399)
