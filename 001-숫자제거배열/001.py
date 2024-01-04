# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

N, K = user_input.split(' ')
# print("N: {}, K:{}".format(N, K))

answer = []
user_input2 = input()
for item in user_input2.split(' '):
	if K not in item:
		answer.append(int(item))

# print("answer: {}".format(answer))
print(len(answer))
