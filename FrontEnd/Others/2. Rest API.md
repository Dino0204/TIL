## 제목

---

### 개념

- REST를 기반으로 만들어진 API

### 설명

```notion
REST(Representational State Transfer)란?
자원을 이름으로 구분하여 해당 자원의 상태를 주고받는 모든 것

1. HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시
2. HTTP Method를 통해 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미합니다.
3. REST에서의 CRUD Operation 동작 예시

	- [HTTP Method] : (POST, GET, PUT, DELETE, PATCH 등)
	- Create : 데이터 생성(POST)
  - Read   : 데이터 조회(GET)
  - Update : 데이터 수정(PUT, PATCH)
  - Delete : 데이터 삭제(DELETE)
```

## 내용

---

### 특징

- REST 구성 요소

  1. 자원**(Resource)** : HTTP URI
  2. 행위**(Verb)** : HTTP Method
  3. 내용**(Representations)**: HTTP Message Pay Load

- 특징

  1. Server-Client
  2. Stateless
  3. Cacheable
  4. Layered System
  5. Uniform Interface

- REST API 설계 규칙

  1. URI 작성

     ```notion
     Bad Example http://khj93.com/Running/
     Good Example  http://khj93.com/run/

     동사보다는 명사
     대문자보다는 소문자
     ```

  2. 마지막 / 포함 x

     ```notion
     Bad Example http://khj93.com/test/
     Good Example  http://khj93.com/test
     ```

  3. \_ 대신 -

     ```notion
     Bad Example http://khj93.com/test_blog
     Good Example  http://khj93.com/test-blog
     ```

  4. 파일확장자 포함 x

     ```notion
     Bad Example http://khj93.com/photo.jpg
     Good Example  http://khj93.com/photo
     ```

  5. 행휘 포함 x

     ```notion
     Bad Example http://khj93.com/delete-post/1
     Good Example  http://khj93.com/post/1
     ```

- RESTFUL
  - REST의 원리를 따르는 시스템 → 설계 규칙이 올바른 시스템

### 장단점

- 장점
  1. HTTP 인프라 그대로 사용
  2. HypeMedia API 기본 충실 & 범용성 보장
  3. 의도 쉽게 파악 가능
  4. 서버, 클라이언트의 역할 분리
- 단점
  1. 표준 정의 x
  2. HTTP Method가 제한적
  3. 브라우저를 자주 통한다면 URl보다 어려움
  4. 구형 브라우저에 호환 x

### 요약

- REST API : REST의 원리를 따르는 API
- RESTFUL : REST의 원리를 지켜 작성한 시스템을 RESTFUL 하다고 함

## 출처

---

[[네트워크] REST API란? REST, RESTful이란?](https://khj93.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-REST-API%EB%9E%80-REST-RESTful%EC%9D%B4%EB%9E%80)

[URL,URI](https://www.notion.so/URL-URI-14950f0028938039be99faf45687bb7f?pvs=21)
