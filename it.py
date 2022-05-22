class FlatIterator(list):

	def __iter__(self):
		return self

	def __next__(self):
		index = 0
		while index < len(self):
			if len(self[index]) == 0:
				index += 1
			else:
				return self[index].pop(0)
		raise StopIteration


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)