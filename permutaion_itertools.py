import itertools
def permute(s):
	print(list(map("".join, itertools.permutations(s,len(s)))))


permute('abc')

	