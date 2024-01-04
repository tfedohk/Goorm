# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
S = input()

result = ""
for s in S:
	if s == str.upper(s):
		result += str.lower(s)
	else:
		result += str.upper(s)
		
print(result)
