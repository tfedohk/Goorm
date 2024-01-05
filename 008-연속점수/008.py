# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
S = list(map(int, input().split()))

def next_number_is_bigger(prev, _next) -> bool:
    return prev + 1 == _next

summed_num = 0
max_num = S[0]

for idx in range(1, len(S)):
    prev = S[idx-1]
    _next = S[idx]
    if next_number_is_bigger(prev=prev, _next=_next):
        if summed_num == 0:
            summed_num = prev
        summed_num += _next
    else:
      if summed_num > max_num:
        max_num = summed_num
      summed_num = 0
    if S[idx] > max_num:
        max_num = S[idx]
    # print("summed_num: {}".format(summed_num))
    # print("max_num: {}".format(max_num))
				

print(max(summed_num, max_num))

