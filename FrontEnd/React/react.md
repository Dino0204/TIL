# React

## 장점

---

- 상호작용(Interaction)이 쉬움
- JSX : Html과 유사한 문법으로 사용하기 쉬움 ( React 코드와 같은 역할을 함 )
- npm create react-app Name → npm start

## Component

---

- React개발 = Component 개발
- 재사용이 가능한 각각의 독립된 모듈 ( 함수 : JSX를 반환 )
- 함수 : React.memo( ) , React.useState( );
- … 배열명 : 배열의 요소만을 가져온다
- 주의 : 무조건 첫글자 대문자 사용

### 1. Arrow Function

```js
  = () ⇒

  function () {
    return
  }
  -> 위 2코드는 같다
```

### 2. State

- modifier 함수 → state을 바꿈 → component 업데이트
- React는 바뀐 부분만 바꿔줌
- useEffect(함수명,[변수명]) : state가 바뀌어도 한번만 실행
- 변수가 변했을 경우 실행

### 3. Prop Types

- JSX의 Props은 기능이 없다
- prop-types으로 prop의 형식을 지정해줄 수 있다.

```js
Button.propTypes = {
  text: PropTypes.string.isRequired,
};
```

### 4. Module

- Name.module.css로 css를 모듈화 할 수 있다.

### 5) Code

1. 기초문법

   ```jsx
   function Title() {
     return (
       <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
         Hello,I'm Fish
       </h3>
     );
   }
   ```

   ```jsx
   const Title = () => (
     <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
       Hello,I'm Fish
     </h3>
   );
   ```

2. 간단한 버튼횟수 출력기

   ```html
   <html>
     <body>
       <div id="root"></div>
     </body>

     <script src="https://www.unpkg.com/react@18.3.1/umd/react.production.min.js"></script>
     <script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js"></script>
     <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

     <script type="text/babel">
       const root = document.getElementById("root");

       function App() {
         const [counter, SetCounter] = React.useState(0);
         const countUp = () => {
           //SetCounter(counter+1);
           SetCounter((current) => current + 1); // 현재 State값을 가지고 계산
         };
         return (
           <div>
             <h3>Total Clicks: {counter}</h3>
             <button onClick={countUp}>Click Me!</button>
           </div>
         );
       }

       ReactDOM.render(<App />, root);
     </script>
   </html>
   ```

3. 단위 변환기

   ```html
   <!DOCTYPE html>
   <html>
     <body>
       <div id="root"></div>
     </body>
     <script src="https://www.unpkg.com/react@18.3.1/umd/react.production.min.js"></script>
     <script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js"></script>
     <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

     <script type="text/babel">
       function MinutesToHours() {
         const [amount, setAmount] = React.useState(0);
         const [flipped, setflipped] = React.useState(false);

         const onChange = () => setAmount(event.target.value);
         const Reset = () => setAmount(0);
         const onFlip = () => {
           Reset();
           setflipped((current) => !current);
         };

         return (
           <div>
             <div>
               <label htmlFor="minutes">Minutes</label>
               <input
                 id="minutes"
                 placeHolder="Minutes"
                 type="number"
                 value={flipped ? amount * 60 : amount}
                 disabled={flipped}
                 onChange={onChange}
               />
             </div>
             <br></br>
             <div>
               <label htmlFor="hours">Hours</label>
               <input
                 id="hours"
                 placeHolder="Hours"
                 type="number"
                 onChange={onChange}
                 value={flipped ? amount : amount / 60}
                 disabled={!flipped}
               />
             </div>
             <h4>Convert to {Math.round(amount / 60)}</h4>
             <button onClick={Reset}>Reset!</button>
             <button onClick={onFlip}>Flipped!</button>
           </div>
         );
       }
       function KmToMiles() {
         return <h3>Km To Miles</h3>;
       }
       function App() {
         const [index, setIndex] = React.useState("xx");
         const onSelect = (event) => {
           setIndex(event.target.value);
         };
         return (
           <div>
             <h1 style={{ color: "tomato" }}>Total Converter</h1>
             <select value={index} onChange={onSelect}>
               <option value="xx">Select Option!</option>
               <option value="0">Minutes & Hours</option>
               <option value="1">KiloMeters & Miles</option>
             </select>
             <hr />
             {index === "xx" ? <b>"Select Option!"</b> : null}
             {index === "0" ? <MinutesToHours /> : null}
             {index === "1" ? <KmToMiles /> : null}
           </div>
         );
       }
       const root = document.getElementById("root");
       ReactDOM.render(<App />, root);
     </script>
   </html>
   ```

4. 복합연습

   ```jsx
   function App() {
     const [counter, setCounter] = useState(0);
     const [keyword, setKeyword] = useState("");
     const [showing, setShowing] = useState(false);

     const onClick = () => setCounter((prev) => prev + 1);
     const onChange = (event) => setKeyword(event.target.value);
     const onClickShowing = () => setShowing((prev) => !prev);

     useEffect(() => {
       keyword && keyword.length > 5
         ? console.log("Search for", keyword)
         : null;
     }, [keyword]);

     function Hello() {
       useEffect(() => {
         console.log("Hi!");
         return () => console.log("by!");
       }, []);
       return <h1>Hello</h1>;
     }

     return (
       <div>
         <input
           type="text"
           placeholder="Type here"
           value={keyword}
           onChange={onChange}
         />

         <h1 className={styles.title}>{counter}</h1>

         <Button text={"Continue"} />
         <button onClick={onClick}>CountUp!</button>
         <button onClick={onClickShowing}>{showing ? "Hide" : "Show"}</button>
         {showing ? <Hello /> : null}
       </div>
     );
   }
   ```

5. To-Do 리스트

   ```jsx
   function App() {
     const [todo, setTodo] = useState("");
     const [todos, setTodos] = useState([]);
     const onChange = (event) => {
       setTodo(event.target.value);
     };
     const onSubmit = (event) => {
       event.preventDefault();
       if (todo === "") {
         return;
       }
       setTodos((currentArray) => [todo, ...currentArray]);
       setTodo("");
     };
     console.log(todos);
     return (
       <div>
         <h1>My To Dos({todos.length})</h1>
         <form onSubmit={onSubmit}>
           <input
             onChange={onChange}
             value={todo}
             type="text"
             placeholder="Write your to do..."
           ></input>
           <button>Add To Do</button>
         </form>
         <hr />
         <ul>
           {todos.map((todo, index) => (
             <li key={index}>{todo}</li>
           ))}
         </ul>
       </div>
     );
   }
   ```

6. 비트코인

   ```jsx
   function App() {
     const [loading, setLoading] = useState(true);
     const [coins, setCoins] = useState([]);
     useEffect(() => {
       fetch("https://api.coinpaprika.com/v1/tickers")
         .then((response) => response.json())
         .then((json) => {
           setCoins(json);
           setLoading(false);
         });
     }, []);

     return (
       <div>
         <h1>The Doge Coins! {loading ? "" : `(${coins.length})`}</h1>
         {loading ? (
           <strong>Loading...</strong>
         ) : (
           <select>
             {coins.map((coin) => (
               <option key={coin.id} value={coin.quotes.USD.price}>
                 {coin.name}
                 {coin.id} ({coin.symbol}): {coin.quotes.USD.price} USD
               </option>
             ))}
           </select>
         )}
       </div>
     );
   }
   ```

# 2. React-Router-Dom

1. Async - Await

- V6 이상부터는 이렇게 바뀜
- Link : 브라우저 새로고침 x → 다른페이지 이동가능

```jsx
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

<Router>
  <Routes>
    <Route path="movie" element={<Detail />}></Route>
    <Route path="/" element={<Home />}></Route>
  </Routes>
</Router>;
```

| 종류          | 내용                          | 방식    |
| ------------- | ----------------------------- | ------- |
| BrowserRouter | http://localhost:3000/movie   | URL     |
| Hash-Router   | http://localhost:3000/#/movie | Hash(#) |

## 출처

---

[Await and Async](https://velog.io/@tosspayments/%EC%98%88%EC%A0%9C%EB%A1%9C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-awaitasync-%EB%AC%B8%EB%B2%95)

[Browser Router VS Hash Router](https://1yoouoo.tistory.com/11)
