# 1. 리액트 시작하기

---

## 🤔리액트란?

리엑트는 프론트엔드 프레임워크 중 하나이다.

### **어떤 프레임워크를 공부해야 할까?**

현재 가장 많이 사용되는 프레임워크는 **React, Vue, Angular, Svelte**등이 있다.

**위 프레임워크를 더 알아보고 싶다면?**

1. React
2. Vue
3. Angular
4. Svelte

→ 리액트는 개발시장에서 빠질 수 없는 프레임워크이기 때문에 꼭 공부해야 한다!

### 리액트의 개념과 장점은 무엇일까?

리액트는 페이스북을 개발할 때 사용한 기술으로 가장 큰 특징은 **화면 출력에 특화된 프레임워크**라는 것 이다.

**이게 무슨 말일까?**

(1) **컴포넌트**라고 불리는 독립적인 코드 블록들을 조합하여 빠르고 효율적으로 화면을 구성 할 수 있다.

예를 들어 하나의 컴포넌트가 레고 조각이고 이 조각들을 하나로 합친다고 생각하면 된다.

![lego.png](https://cdn3d.iconscout.com/3d/premium/thumb/lego-bricks-3d-icon-download-in-png-blend-fbx-gltf-file-formats--logo-kids-toy-cubes-activities-pack-people-icons-9802168.png?f=webp)

![react.png](https://cdn3d.iconscout.com/3d/free/thumb/free-react-9294867-7578010.png?f=webp)

또한 가상 화면 기술로 화면 출력 속도가 빠르며 코드의 복잡성이 낮다.

(2) **게임 엔진 원리**를 도입하여 화면 출력 속도가 빠르다.

자바스크립트에는 JQuery와 Handlebars라는 라이브러리가 있다. 이 라이브러리들은 아주 간결한 코드로 화면을 구성할 수 있지만 **화면이 커질수록 화면 출력 시간이 늘어난다**는 단점이 있다. **이유는 일부분만 바뀌어도 화면 전체가 다시 그려지기 때문이다.**

이 방식을 쉽게 **트리**로 생각해보면 트리 내에서 노드를 바꿨을 때 자식 노드가 모두 다시 그려진다고 생각하면 된다. 이러한 문제를 해결하기 위해서 등장한 것이 **게임 엔진 원리**(다음 장면에 필요한 화면을 미리 그려 두는 방식)를 사용하는 가상 화면 즉, **VDOM(Virtual DOM)**입니다.

→ 가상화면 VDOM!

### 노드 패키지 매니저(NPM)은 무엇일까?

자바스크립트 라이브러리는 **노드 패키지 매니저**로 관리한다.

(1) NPM의 동작 방식

**NPM**은 필요한 라이브러리의 설치 및 삭제등의 **관리**를 해주는 프로그램이다.

NPM은 실제로 **node_modules** 폴더에 라이브러리를 저장하고 **package.json**이라는 파일에 설치된 라이브러리의 정보를 저장한다. 그렇다면 왜 **실제 파일**과 **명세 파일**을 따로 저장하는 것일까? 이유는 실제 파일의 용량이 굉장히 크기 때문이다. 한 상황을 예시로 들어보자면 **A라는 개발자**가 **B라는 개발자**에게 프로젝트를 공유하려고 한다. 이 프로젝트를 공유하는 상황에서 실제 라이브러리 파일을 담아서 보내면 어떻게 되겠는가?

당연히 큰 프로젝트일수록 더더욱 오래 걸릴 것이다. 따라서 명세 파일과 실제 파일이 따로 저장을 하는 것이고 B개발자는 명세 파일만 보고 라이브러리를 다운로드하면 되는 것 이다!

(2) 웹팩이란 무엇일까?

**웹팩(WebPack)**은 프로젝트에 사용된 파일을 분석하여 **기존 웹 문서 파일로 변환하는 도구**이다.

그렇다면 웹팩이 필요한 이유는 무엇일까? 프레임워크는 **기존 파일 형식**인 .js , .css등을 사용하지 않는 경우가 많다. 예를 들어 .jsx등이 있다. 그런데 웹 브라우저는 이러한 독자적인 파일 형식을 이해하지 못한다. 따라서 이를 **해석해주는 도구**가 필요한데 그 역할을 해주는 도구가 바로 **웹팩**이다!

![bundling.png](https://velog.velcdn.com/images/rlagurtn1/post/cf356167-1430-480d-b575-e49719c35e7b/image.png)

웹팩은 웹 브라우저가 파일을 해석할 수 있도록 **해석**해주고 **불필요한 파일을 삭제**하거나 **압축**하여 **용량을 줄여주는 역할**을 하기도 한다.

# 2. ES6 문법

---

## [1] 템플릿 문자열

### 기존 자바스크립트와 ES6 문자열 사용 방법 알아보기

자바스크립트로 문자열을 연결하려면 병합 연산자(+)를 사용해야 합니다.

이와 같이 병합 연산자로 문자열을 연결하면 문제점이 생깁니다. 바로 코드가 복잡해 보인다는 것이죠.

따라서 ES6에서는 템플릿 문자열을 사용합니다. 템플릿 문자열은 **‘ ’** 대신 **` `** 를 사용합니다.

또 **${}**를 사용하여 변수와 식을 문자열에 포함 시킬 수 있습니다.

병합 연산자 vs 템플릿 문자열

```jsx
"제품" +
  name +
  "의 가격은" +
  cost +
  "입니다."`제품 ${name}의 가격은 ${cost}입니다.`;
```

한 눈에 봐도 아랫부분이 더 쉬워 보입니다.

3분 코딩

```jsx
var cart = { name: "도서", price: 1500 };
var getTotal = function (cart) {
  return cart.price;
};
var myCart =
  "장바구니에" + cart.name + "가 있습니다. 총 금액은" + getTotal(cart);

var cart = { name: "도서", price: 1500 };
var getTotal = function (cart) {
  return cart.price;
};
var myCart = `장바구니에 ${cart.name}가 있습니다. 총금액은 ${getTotal(cart)}`;
```

## [2] 전개 연산자(Spread Operator)

### 기존 자바스크립트와 ES6 배열 전개 연산자 사용 방법 알아보기

전개 연산자는 나열형 자료(배열등)를 추출, 연결할 때 사용하는 연산자 입니다.

사용 방법은 배열, 객체, 변수명 앞에 **…**를 입력하여 사용합니다. 다만 배열, 객체, 함수 인자 표현식([],{},()) 내에서만 사용해야 합니다.

자바스크립트에서는 배열의 일부분만 나타내거나 연결하려면 인덱스와 배열 내장 함수등을 사용해야 합니다.

(자바스크립트 배열 내장 함수인 **concat()**등을 사용하여 배열을 합침)

```jsx
// arr1 + arr2
var arr1 = ['One', 'Two']
var arr2 = ['Three', 'Four']
const combined = [...arr1, ...arr2]
-> 결과 : ['One','Two','Three','Four']

// arr1의 각 요소들을 추출하여 할당
const [first,second,three = 'empty',...others] = arr1
-> 결과
	 first = 'One'
	 second = 'Two'
	 three = 'empty'
	 others = []

// 잘못된 예시
var wrongArr = ...arr1
-> 표현식 없이 전개 연산자를 사용 했으므로 잘못되었습니다.
```

또한 객체도 전개 연산자를 통해 간략화 할 수 있습니다.

## [3] 가변 변수 & 불변 변수

### 기존 자바스크립트와 ES6의 가변(let) & 불변(const) 변수 사용법 알아보기

기존 var 변수 대신에 왜 let, const를 쓰는지 알아보겠습니다.

가변 변수는 let 키워드로 선언하고, 읽거나 수정할 수 있다는 특징이 있습니다.

불변 변수는 const 키워드로 선언하고, 읽기 작업만 수행할 수 있습니다. 그런데, 불변 변수는 값 재 할당만 안 될 뿐 값을 변경할 수는 있습니다. 이게 무슨 말일까요? 불변 변수로 선언하고 자바스크립트 내장 함수로 값을 변경할 수 있습니다. 앞서 불변 변수는 값을 변경할 수 없다고 하였는데 이상하지 않나요? 이러한 것을 무결성 제약 조건을 위배했다고 합니다. 암묵적으로 내장 함수로 값을 바꾸는 것을 금지하면 이러한 무결성을 지킬 수 있습니다. 그리고 값을 수정하는 것이 아닌 기존의 값을 이용하여 새 변수에 할당하여 반환하는 함수를 사용하여 무결성을 지킬 수 있습니다.

| 가변 내장 함수 | 무결성 내장 함수 |
| -------------- | ---------------- |
| push           | concat           |
| splice         | slice.concat     |
| pop            | slice            |
| shift          | slice            |

이처럼 불변 변수를 사용하면 변수가 변하는 시점과 수정 전, 후 값을 비교할 수 있어서 유용하게 사용할 수 있습니다.

## [4] 클래스

### 기존 자바스크립트와 ES6의 클래스 표현법 알아보기

기존 자바스크립트에서는 함수를 생성자로 선언 후, 상속이 필요한 변수, 함수등을 이 protype 객체에 할당하는 방법을 사용했습니다. 이 방식은 굉장히 복잡해 보인다는 단점이 있습니다. 따라서 Java와 같이 Class 키워드를 통해 클래스를 정의하게 되었습니다. (주의: 클래스 내에서는 var,let,const등을 사용하지 않습니다.)

그리고 extends를 통해 클래스를 상속할 수 있는데요. 이 상속한 부모 클래스를 super를 통해 참조할 수 있습니다.(주의: 다중 상속, 인터페이스는 지원하지 않습니다.)

## [5] 화살표 함수(Arrow Function)

### 기존 자바스크립트와 ES6의 함수 사용법 알아보기

화살표 함수는 새롭게 추가된 함수의 표현식으로 **⇒**를 사용하여 함수를 선언합니다.

기존 자바스크립트의 함수 선언 방식

```jsx
// 1. 함수
function add(n1, n2) {
  return n1 + n2;
}

// 2. 익명 함수
var add = function (n1, n2) {
  return n1 + n2;
};

// 위 함수들을 출력하면?

// 1. f add(n1,n2){중략...}
// 2. f (n1,n2){중략...}
```

위 함수 선언 방식을 보면 첫 번째 함수 선언 방식은 함수에 이름이 있고 두 번째 선언 방식은 함수에 이름이 없는 것을 볼 수 있습니다.

기존 자바스크립트에서는 위와 같은 두가지 방법으로 함수를 선언 할 수 있었는데요. 화살표 함수는 이 중 익명함수와 방식이 유사합니다. 다른 점은 function 대신 인자를 받는 **()** 와 본문인 **{}** 사이에 **⇒** 를 표기한다는 것입니다.

화살표 함수 선언 방식

```jsx
// 1. 화살표 함수
var add = (n1, n2) => {
  return n1 + n2;
};

// 2. 바로 결과값을 반환하는 경우 {}, return의 생략이 가능합니다.
var add = (n1, n2) => n1 + n2;

// 3. 객체를 화살표 함수로 표현하는 방법
var add_Multiple = (n1, n2) => ({ add: n1 + n2, multiple: n1 * n2 });

// 4. 계단형 함수 구조
function addNum(n) {
  return function (value) {
    return num + value;
  };
}

var addNum = (num) => (value) => num + value;

// 5. this의 범위
var addThis = function (n1, n2) {
  return this.value + n1 + n2;
}.bind(this);

var addThis2 = (n1, n2) => this.value + n1 + n2;
```

이처럼 화살표 함수의 장점으로는 함수의 표현식을 간단하게 표기하는 것이 가능하다는 점과 계단형 함수와 같은 구조가 나타나지 않게 해준다는 장점이 있습니다. 또다른 장점으로는 콜백 함수의 this 범위를 bind 함수를 통하여 this 객체에 전달해 오류를 줄입니다. (bind 함수는 this의 범위를 유지해주는 함수이고 화살표 함수는 이 과정이 생략 됩니다.)

## [6] 객체 확장 표현식 & 구조 분해 할당

### 기존 자바스크립트와 ES6 객체 확장 표현식 사용 방법 알아보기

기존 자바스크립트에서는 객체의 키와 키 값을 각각 할당해야 했지만 ES6에서는 이를 개선 하여 키 값만 할당해도 키가 자동으로 할당되게 개선했습니다.

```jsx
// 1. 기존 자바 스크립트의 객체 확장 표현식
var obj = { x : x, y : y };

var combined = {};
combined['one' + randomKey] = 'value';

var obj2 = {
	x : x,
	methodA: function() {console.log('method A');},
	methodB: function() {return 0;},
};

// 2. ES6의 객체 확장 표현식
var obj = {x,y};

var combined = {
	['one' + randomKey]: 'value';
};

var obj2 = {
	x,
	methodA() {console.log('method A');},
	methodB() {return 0;},
};
```

### 기존 자바스크립트와 ES6 구조 분해 사용 방법 알아보기

기존 자바스크립트의 불편했던 식을 ES6에서 개선하였습니다. 또한 구조 할당은 전개 연산자를 같이 사용합니다.

```jsx
// 1. 기존 자바스크립트의 구조 분해
var list = [0, 1];

var item1 = list[0];

var item3 = list[2] || -1;

// swap 생략...
var temp = item1;

var obj = {
  key1: "one",
  key2: "two",
};

var key1 = obj.key1;
var ket3 = obj.key3 || "default key3 value";

// 2. ES6의 구조 분해
var [item1, item2, item3 = -1] = list;

// swap
[item2, item1] = [item1, item2];

var { key1: newKey1, key2, key3 = "default key3 value" } = obj;

// 3. 전개 연산자와 구조 분해 할당
var [item1, ...other] = [0, 1, 2];
var { key1, ...other } = { key1: "one", key2: "two" };
```

## [7] 라이브러리 의존성 관리

### 기존 자바스크립트와 ES6의 라이브러리 의존성 관리 방법 알아보기

기존 자바스크립트에서는 의존성을 <script>를 통해 관리하였고 참조 순서에 따른 의존성 문제가 발생하여 ES6 문법을 통해 이를 해결하였습니다. ES6 문법은 import 구문을 사용하여 구동 합니다.

```js
// 1. 기존 자바스크립트
<script src="example.com"> </script>

// 2. ES6 문법

// 기본 공유모듈 불러오기
import Example from './Example.js';

// 모듈 내의 특정 함수 또는 변수 불러오기
import {ExampleModule} from './Example.js';

// 모듈 이름 다른 이름으로 변경하여 불러오기
import {ExampleModule as RenamedModuleName} from './Example.js';

// 변수 내보내기
export const VALUE = 0;

// 기본으로 참조되는 항목 내보내기
export default class new ExampleClass();
```

## [8] 배열 함수

### 기존 자바스크립트와 ES6의 다양한 함수 사용을 통한 차이점 알아보기

기존 자바스크립트로 코드를 작성 했을 때와 ES6 함수(자주 사용하는 배열 함수)를 사용했을 때의 차이점을 **쿼리 문자열**을 통해 알아보겠습니다.

**쿼리 문자열이란?**

> 웹 주소에 포함 시키는 문자열

**다양한 배열 함수**

1. forEach
   1. 가변 변수 let
   2. 반복문의 순번, 배열의 크기 표기를 생략 가능함
2. map

   1. 불변 변수 const
   2. 각 배열 요소를 정의된 함수를 통해 변환하여 새 배열을 반환함

   → forEach, map 함수의 결과 값은 같음

3. reduce
   1. 배열을 객체로 변환

```jsx
// 1. forEach()

// [1] for문을 통한 분리
function parse(qs) {
  // query_string = 'id=0204&password=2008'
  var query_string = qs.substr(1);
  var split_string = query_string.split("&");
  var result = {};

  for (var i = 0; i < split_string.length; i++) {
    var parts = split_string[i].split("=");

    // key = 'id'
    var key = parts[0];

    // (1) 문자열 value = '0204'
    var value = parts[1];

    // (2) 숫자 value = 0204
    // NaN = Not A Number의 약자
    // 값이 NaN이 아니라면 Number로 변환하여 할당
    var value = Number.isNaN(Number(parts[1])) ? parts[i] : Number(parts[1]);

    // result = { id : 0204 }
    result[key] = value;
  }
  return result;
}

// [2] forEach & 구조 분해 할당을 통한 분리
function parse(qs) {
  const query_string = qs.substr(1);
  const split_strings = query_string.split("&");

  let result = split_strings.forEach((split_string) => {
    const [key, value] = split_string.split("=");
    result[key] = value;
  });
  return result;
}

// 2. map()
function parse(qs) {
  const query_string = qs.substr(1);
  const split_strings = query_string.split("&");

  const result = split_strings.map((split_string) => {
    const [key, value] = split_string.split("=");
    return { key: key, value: value };
  });
  return result;
}

// 3. reduce()
function parse(qs) {
  const query_string = qs.substr(1);
  const split_strings = query_string.split("&");

  return split_strings
    .map((split_string) => {
      const [key, value] = split_string.split("=");
      return { key: key, value: value };
    })
    .reduce((result, item) => {
      result[item.key] = item.value;
      return result;
    }, {});
}
```

## [9] 비동기 함수

비동기 함수는 **비동기 처리**를 위해 사용합니다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a58d5064-1880-4de1-a993-b4d5cddafd5a/aea7f8e2-ad90-457a-bcd1-080f42fee8c2/image.png)

**비동기 처리란?**

> 오래 걸리는 작업 때문에 다른 작업들이 지연이 된다면 다른 작업들을 먼저 진행하고 오래 걸리는 작업을 이후에 처리하는 방식 (대표적인 예로 서버에 데이터 요청 및 결과 값을 기다리는 과정이 있음)

따라서 비동기 함수와 처리 방식은 효율적인 작업 처리를 위해 꼭 필요합니다!

### 기존 자바스크립트와 ES6의 비동기 함수 처리 방법 알아보기

기존 자바스크립트는 비동기 작업을 위해서 지연이 필요한 함수에 setTimeout 함수를 사용하였고 이 이후에 실행하여야 하는 함수는 지연 작업 함수의 인자인 콜백 함수로 전달하여 처리하였습니다.

```jsx
function work1(onDone) {
  setTimeout(() => onDone("작업 1 완료!"), 100);
}

function work2(onDone) {
  setTimeout(() => onDone("작업 2 완료!"), 200);
}

function work3(onDone) {
  setTimeout(() => onDone("작업 3 완료!"), 300);
}

function urgentWork() {
  console.log("긴급 작업!");
}

// 1. 콜백함수 & 지옥
work1(function (msg1) {
  console.log("done after 100ms:" + msg1);
  work2(function (msg2) {
    console.log("done after 200ms:" + msg2);
    work1(function (msg3) {
      console.log("done after 300ms:" + msg3);
    });
  });
});

urgentWork();

// 실행 과정
// 1. urgentWork() -> 비동기 함수가 아님
// 2. work1() -> 100ms 후
// 3. work2() -> 100 + 200 ms 후
// 4. work4() -> 100 + 200 + 300 ms 후

// 2. Promise
const work1 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve("작업1 완료!"), 100);
  });

const work2 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve("작업2 완료!"), 200);
  });

const work3 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve("작업3 완료!"), 300);
  });

function urgentWork() {
  console.log("긴급 작업");
}

const nextWorkOnDone = (msg1) => {
  console.log("done after 100ms" + msg1);
  return work2();
};
```

콜백함수의 계단 구조를 콜백 지옥이라 부르며 이러한 방식은 매우 비효율적입니다.

따라서 이런 작업들을 Promise 문법을 통해 해결 할 수 있습니다.

## [10] 디바운스 & 스로틀(Debounce & Throttle)

디바운스와 스로틀은 서버에 데이터를 요청할 때 생기는 지연등을 처리하여 부하를 줄일 수 있는 문법입니다.

### 디바운스의 개념 알아보기

디바운스는 내용을 입력하다가 특정 시간 동안 대기하고 있으면 마지막 입력된 내용을 바탕으로 서버에 요청하는 방법입니다. 쉽게 예시를 들어보면 구글 검색창에 검색어를 입력할 때 입력중에는 연관 검색어가 나타나지 않다가 입력을 멈추면 연관 검색어가 나타납니다.

> g → s → m
> 1s 1s 1s → 🔍검색!

위 부분을 보면 각각을 입력하는데 1초 이상이 걸리는지 검사하고 마지막 m을 입력하고 1초가 지났을 때만 검색이 일어납니다.

```jsx
function debounce(func, delay) {
  let inDebounce;
  return function (...args) {
    if (inDebounce) {
      clearTimeout(inDebounce);
    }
    inDebounce = setTimeout(() => func(...args), delay);
  };
}

const run = debounce((val) => console.log(val), 100);
run("a");
run("b");
run(2);

// 100ms 이후
// 출력: 2
```

### 스로틀의 개념 알아보기

스로틀은 디바운스와 개념이 비슷하지만 입력되는 동안 이전 요청 작업을 주기적으로 실행한다는 점이 다릅니다. 쉽게 예시를 들자면 인스타 릴스를 볼 때 계속해서 다음 내용이 나오는 무한 스크롤 기능이 구현되어 있는데 만약 이 기능을 디바운스로 구현한다면 스크롤을 멈출 때까지 내용은 로딩 되지 않을 것 입니다. 하지만 스로틀로 이 기능을 구현한다면 이를 해결할 수 있습니다.

```jsx
function throttle(func, delay) {
  let lastFunc;
  let lastRun;

  return function (...args) {
    const context = this;
    if (!lastRun) {
      func.call(context, ...args);
      lastRun = Date.now();
    } else {
      if (lastFunc) clearTimeout(lastFunc);
      lastFunc = setTimeout(function () {
        if (Date.now() - lastRun >= delay) {
          func.call(context, ...args);
          lastRun = Date.now();
        }
      }, delay - (Date.now() - lastRun));
    }
  };
}

var checkPosition = () => {
  const offset = 500;
  const currentScrollPosition = window.pageYOffset;
  const pageBottomPosition =
    document.body.offsetHeight - window.innerHeight - offset;
  if (currentScrollPosition >= pageBottomPosition) {
    console.log("다음 페이지 로딩");
  }
};

var infiniteScroll = throttle(checkPosition, 300);
window.addEventListener("scroll", infiniteScroll);
```

# 3. Component

---

## [1] JSX

JSX는 JavaSciprt XML의 줄임말로 자바스크립트에 XML 문법을 추가한 확장형 문법으로 이해하시면 됩니다.

HTML과 자바스크립트를 한번에 작성하여 편리합니다.

### JSX 사용해 보기

JSX는 return 함수 내에 HTML을 표현하고 HTML 태그의 끝에 /> 마침 표시가 있다는 차이점이 있습니다.

## [2] 컴포넌트와 구성 요소

### 컴포넌트의 개념

이전에 컴포넌트를 레고로 비유하여 설명한 적이 있는데 정확한 개념을 이해하기 위해서 기존 프레임워크와의 차이점을 들어 다시 정리해보겠습니다. 기존의 프레임워크는 MVC라는 패턴으로 작동했습니다. 각각 정보를 담당하는 Model, 화면을 담당하는 View, 구동을 담당하는 Controller로 MVC 패턴이라고 부릅니다. 이 방식의 장점은 코드 관리를 효율적으로 할 수 있다는 장점이 있지만 각 요소의 의존성이 높아 재활용은 어렵다는 단점이 있었습니다.

하지만 웹사이트에서는 재활용이 필수적입니다. 웹사이트의 요소는 비슷하고 반복적으로 사용되는 경우가 많습니다. 따라서 이러한 단점을 해결하기 위해 나온 방식이 컴포넌트 방식입니다. 유튜브의 영상 검색 결과를 예시로 들어보겠습니다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a58d5064-1880-4de1-a993-b4d5cddafd5a/0f8eb63a-7d05-41d2-8cfa-5d07a944bf87/image.png)

영상 각각에 해당하는 컴포넌트와 이 영상들 전체를 감싸는 영상 목록 컴포넌트를 만들면 다른 검색결과를 나타낼 때에도 이 컴포넌트를 재활용할 수 있겠죠?

컴포넌트를 작성할 때 유의해야 하는 규칙이 있습니다. 바로 첫 글자는 무조건 대문자로 작성해야한다는 규칙이죠. JSX문법에서 HTML 마크업과 컴포넌트를 구분하기 위해서 첫 글자를 대문자로 작성해야 합니다.

### 컴포넌트 구성 요소 미리 살펴보기

| 데이터 구성 요소 | 특징                                                        |
| ---------------- | ----------------------------------------------------------- |
| Property         | 상위 → 하위 컴포넌트로 전달 되는 읽기 전용 데이터입니다.    |
| State            | 컴포넌트의 상태를 저장하고 변경할 수 있는 데이터입니다.     |
| Context          | 부모에서 생성 → 모든 자식 컴포넌트로 전달하는 데이터입니다. |

## [3] 데이터 전달 프로퍼티

프로퍼티는 상위 컴포넌트가 하위 컴포넌트에 수정할 수 없는 값을 전달할 때 사용합니다.

### 프로퍼티의 기초 알아보기

> <Profile name=”Dino”/>

위 컴포넌트를 보면 상위 컴포넌트에서 하위 컴포넌트를 호출할 때 하위 컴포넌트에 값을 넘겨주는 모습을 볼 수 있습니다. 그리고 이 값은 하위 컴포넌트에서 참조할 수 있습니다. (단방향으로 데이터가 흐릅니다.)

### 프로퍼티의 다양한 사용 방법 알아보기

상위 컴포넌트에서 하위 컴포넌트로 값을 전달 할 때에는 문자열은 “”에 변수, 숫자등은 {}에 담아 전달합니다.

## [4] 상태 관리

### State로 상태 관리하기

State는 값을 저장하거나 변경할 수 있는 객체입니다.

> const [data,setData] = useState(True)

상태 관리는 이와 같은 문법으로 작성할 수 있습니다.

## [5] 생명주기(LifeCycle)

나중에 찾아보자

## [6] 클래스형 컴포넌트

나중에 찾아보자

## [7] 함수형 컴포넌트

나중에 찾아보자

## [8] 배열 컴포넌트

유튜브 영상 목록등은 어떻게 구현할까요? 배열을 사용해서 구현할 수 있습니다.

> const mixedList = [1,’string’,<Component/>]

이 처럼 자바스크립트의 배열에는 다양한 자료형을 저장할 수 있습니다.

### 배열 컴포넌트를 위한 map()함수 사용 방법

map 함수를 사용하면 배열로 저장된 데이터를 바로 JSX로 변경할 수 있습니다.

```jsx
const todoList = [
  { taskName: "운동하기", finished: true },
  { taskName: "공부하기", finished: false },
];

// 1. 객체 -> JSX
const todos = todoList.map((todo) => <div>{todo.taskName}</div>);

// 2. 객체 -> 컴포넌트
const todos = todoList.map((todo) => <TodoTask />);

// 3. 객체 -> 프로퍼티
const todos = todoList.map((todo) => <TodoTask taskName={todo.taskName} />);
```

이와 같은 배열 컴포넌트를 사용할 때 주의할 점이 하나 있습니다. key값을 사용해야 한다는 것이죠. key값을 사용하게 되면 React 엔진이 기존 컴포넌트를 재활용하여 성능을 더 좋은 상태로 유지 시켜 주기 때문에 key값을 정의해 주어야 합니다.

## [9] 컴포넌트에서 콜백 함수와 이벤트 처리하기

하위 컴포넌트에서 상위 컴포넌트에서 전달받은 프로퍼티를 수정하려면 어떻게 해야 할까요? 바로 프로퍼티 원본을 수정할 수 있는 함수를 하위 컴포넌트에 제공하면 됩니다. 즉, 콜백 함수를 프로퍼티로 전달하면 됩니다.

> 콜백함수란?
> 정의된 위치에서 실행되지 않고, 특정 상황에서 실행되는 함수를 뜻합니다.

### 콜백 함수로 프로퍼티 수정해 보기

버튼을 눌렀을 때 카운트가 올라가는 구조를 예시로 들어보겠습니다.

```jsx
// 1. 상위 컴포넌트
const [count, setCount] = useState(0);

return (
  <div>
    <Counter count={count} onChange={setCount} />
    <p>{count}</p>
  </div>
);

// 2. 하위 컴포넌트

return (
  <div>
    <button onClick={setCount(count + 1)}>➕</button>
  </div>
);
```

다음과 같이 프로퍼티의 원본을 수정할 수 있는 함수를 프로퍼티로 보내 count를 변경할 수 있도록 하였습니다. 콜백 함수를 호출하게 되면 상위 컴포넌트에서 원본 데이터를 수정한 후 다시 자식 컴포넌트로 값을 전달해 줍니다.

### 컴포넌트에서 DOM 이벤트 사용하기

| 이벤트 명 | 이벤트 호출 시점                    | JSX DOM 이벤트 프로퍼티 |
| --------- | ----------------------------------- | ----------------------- |
| click     | 요소에 마우스, 키보드가 클릭될 때   | onClick                 |
| submit    | 폼에 데이터가 전송될 때             | onSubmit                |
| mousemove | 요소 위의 마우스 커서가 움직일 때   | onMouseMove             |
| mouseover | 요소 위로 마우스 커서가 돌아다닐 때 | onMouseOver             |
| mouseout  | 요소 위의 마우스 커서가 떠날 때     | onMouseOut              |
| keydown   | 키보드가 눌렸을 때                  | onKeyDown               |
| keypress  | 키보드 입력이 완료 되었을 때        | onKeyPress              |

### 단방향 흐름 방식

React는 단방향 흐름을 따르며 이러한 방식은 원본 데이터의 무결성을 지켜주므로 데이터 수정으로 인한 데이터 파편화를 줄여줍니다.

# 4. 디자인 시스템

---

## [1] 비주얼 테스트

웹 사이트들은 상황에 따라 오류 메시지, 로딩 화면등을 출력합니다. 이러한 화면은 제작 및 확인이 굉장히 번거롭습니다. 따라서 컴포넌트들을 쉽게 관리하기 위해서 비주얼 테스트를 위한 스토리북을 사용합니다. 스토리북을 쉽게 예를 들자면 갤럭시 플립을 생각하시면 됩니다. 갤럭시 플립의 커버 색상을 고를 때 안내 페이지에 나온 컬러들을 기반으로 사용할 컬러를 결정하는데 이와 비슷하다고 생각하시면 됩니다.

### 스토리북 설치하고 사용해 보기

1. 스토리북 설치하기
2. package.json에 스토리북 실행 명령어 추가하기
3. 스토리 파일 만들기
4. 스토리북 config.js에 스토리 연결하기
5. 스토리북 실행하기

### 스토리북 더 똑똑하게 사용하기

스토리에 여러 컴포넌트를 추가하고, 새 스토리를 자동으로 스토리북에 연결되게 하기

1. 스토리에 다른 컴포넌트 추가하기
2. 스토리 추가하기
3. 스토리북에 스토리 추가하기
4. 스토리가 자동으로 스토리북에 추가되도록 config.js 설정하기

### 스토리북 확장 도구 사용하기

스토리북은 여러가지 확장 도구인 addon을 추가할 수 있습니다.
