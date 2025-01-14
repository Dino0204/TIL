# MarkDown

## 1. 마크다운이란?

---

> **마크다운(Markdown)이란?**
> 일반 텍스트 기반의 경량 마크업 언어이다.

> **마크업 언어란?a**
> 태그 등을 이용하여 문서나 데이터의 구조 등을 명기하는 언어이다. 텍스트만으로 서식이 있는 문서들을 작성할 때 자주 사용되며, 다른 마크업 언어들에 비해 문법이 쉽고 간단한 것이 특징이다. HTML 등의 서식 문서들로 쉽게 변환되기 때문에 README 파일이나 온라인 게시물 등에 사용된다.

## 2. 마크다운의 장단점

---

### 2-1. 장점

- 문법이 간결하고 쉽다.
- 거의 대부분의 것에 사용할 수 있다. (웹사이트, 문서, 메모, README 기술파일 등)
- 마크다운을 지원하는 플랫폼이 다양하다. (Github, Notion, Discord, Dropbox Paper 등)
- 대부분의 환경에서 작성 및 수정이 가능하다. (일반 Notepad에서도 가능)
- 텍스트로 저장되어 용량을 많이 차지하지 않는다.
- 다양한 형태로 변환이 가능하다.

### 2-2. 단점

- 모든 HTML의 마크업을 대신하지 못한다.
- 표준이 없기 때문에 툴에 따라 생성물이 다르다.
- 마크다운으로 파일을 업로드할 때 저장 이후 파일 경로를 입력해야 한다.

## 3. 마크다운의 문법

---

### 3-1. Header(h1 ~ h6)

- **#** 의 개수가 많을수록 더 작다.

### 3-2. Styling

> **Emphasize**
> 기울임 or 기울임

> **String (bold)**
> 강함 or 강함

> **HighLight**
> ==하이라이트==

> **Cancellation Line**
> 취소선

> **Quoted Line**
> 인용선

> 화학식,수식 적용x

### 3-3. List

- 물건1
  - 물건2
    - 물건3

### 3-4. Link

[Youtube](https://www.youtube.com/watch?v=_nRDC4F0Q6U)

![iPhone](https://image.edaily.co.kr/images/Photo/files/NP/S/2024/09/PS24091000240.jpg)

### 3-5. Code

- 백틱 3개(코드 위와 아래) + c (표현할 언어 이름)

```c
int main(){
 printf("Hello world");
}
```

<br>

### 3-6. Table

| 물건   | 값   |
| ------ | ---- |
| 콜라   | 2.5$ |
| 사이다 | 2.4$ |
| 몬스터 | 3.5$ |

| 프론트 | 백  |
| ------ | --- |
| HTML   | ??? |

### 3-7. Definition List (나열 목록) <x>

GwangJu SoftWare Meister HighSchool

: 광주광역시의 마이스터고

Majors

: SW개발과

: IOT과

: AI과

### 3-8. FootNote <x>

Some text with a footnote.[^1][^1]: The footnote.

### 3-9. Abbreviation (축약) <x>

[HTML] : HyperText Markup Language

### 3-10. LaTex math (수식)

The Gamma function satisfying $\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$ is via the Euler integral

$\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.$

### 줄바꿈

- 스페이스 두번 -> 줄바뀜
