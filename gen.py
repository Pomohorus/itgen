def flat_generator(n):
	for item in n:
		for i in item:
			yield i

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for item in  flat_generator(nested_list):
	print(item)