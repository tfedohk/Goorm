https://level.goorm.io/exam/174909/m%EB%B0%B0-%EB%B0%B0%EC%97%B4/quiz/1

# 배운 점
## ```map```
가령 다음과 같은 코드가 있다고 해보자.
```python
n, m = map(int, input().split())
```
이 코드의 의미는, "int로 mapping을 할거야. 뭐를? input().split()을"

## print(*result)**
`*`**은 언패킹(unpacking)을 의미한다. 리스트나 튜플과 같은 iterable한 객체의 요소들을 풀어서 전달하는 역할을 한다.
**`print(*result)`**는 **`result`** 리스트의 각 요소를 공백을 사이에 두고 개별적으로 출력하라는 의미다. 즉, 리스트의 요소들을 풀어서 개별적으로 **`print`** 함수에 전달한다.
예를 들어, **`result`**가 **`[3, 6, 3, 12, 15, 6, 21]`**이라면, **`print(*result)`의 결과로,** "3 6 3 12 15 6 21"이 출력된다.