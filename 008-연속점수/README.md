https://level.goorm.io/exam/174924/%EC%97%B0%EC%86%8D-%EC%A0%90%EC%88%98/quiz/1

# 배운 점

## 코딩 스킬적인 부분

next_number_is_bigger() 메서드의 조건문은 원래 아래와 같았다.

```python
def next_number_is_bigger(prev, _next) -> bool:
	if prev + 1 == _next:
		return True
    return False
```
이거는 prev + 1 == _next이면, True를 반환하라는 단순한 논리인데, 이를 세 줄이 아닌 그저 한 줄로 다음과 같이 처리할 수 있다.
```python
def next_number_is_bigger(prev, _next) -> bool:
    return prev + 1 == _next
```

### 결론
- if문을 쓸 때, return 하나로 처리할 수 있는지를 잘 살피자!

## 논리적인 부분

원래 else문 이하는 다음과 같았다.

```python
else:
  summed_num = 0
```

하지만 테스트 케이스에서 계속 에러가 났는데, 디버깅을 하던 중 다음과 같은 상황이라면 어떻게 될까?를 실험해보았다.
N = 3

S = [7, 8, 14]
원하는 답은 7과 8이 연속된 값이므로 15이고, 14 단일값보다 더 큰 값이기 때문에 결국 15가 나와야 한다.
하지만 프로그램에선 14가 나왔다.
이는 else문에서, 연속되지 않은 수가 나오면 무조건적으로 summed_num을 0으로 초기화해버리게 되어 있었기 때문이다. 그래서 다음과 같이 수정했다.

```python
else:
      if summed_num > max_num:
        max_num = summed_num
      summed_num = 0
```

### 결론
- 문제를 풀 때, 발생 가능한 케이스들에 대해서 건너뛰지 말고 직접 손으로 시뮬레이션해보고, 내 코드도 해당 결과를 내는지를 확인해야 한다.
- 습관적으로 print문을 넣어서 디버깅하자!