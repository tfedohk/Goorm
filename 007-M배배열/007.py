N, M = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
		
result = [item * M if item % M != 0 else item for item in array]
		
print(*result)
