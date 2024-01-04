# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

summed_num = 1
for num in range(int(user_input), 1, -1):
	summed_num *= num

# print("summed_num: {}".format(summed_num))
print(summed_num % 1000000007)
