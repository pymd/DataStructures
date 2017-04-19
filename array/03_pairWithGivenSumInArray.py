# Given an unsorted array of integers, find a pair with given sum in it.

def pairWithGivenSumNaive (arr, s):
	"""
		A Brute force approach
		Time Complexity: O(n^2)
	"""
	found = False
	for i,n in enumerate(arr):
		for j in arr[i+1:]:
			if n + j == s:
				found = True
				print 'Pair found at index:',i,arr.index(j,i+1)
	if not found:
		print 'Pair not found'

def pairWithGivenSumUsingSorting (arr, s):
	"""
		Time Complexity: O(nlogn) 		(for sorting)
	"""
	arr.sort()	
	i = 0
	j = len(arr)-1
	found = False
	
	while i < j:
		if arr[i] + arr[j] == s:
			print 'Pair found is:',arr[i],arr[j]
			found = True
			i += 1
			j -= 1
		elif arr[i] + arr[j] < s:
			i += 1
		else:
			j -= 1
	if not found:
		print 'Pair not found'

def pairWithGivenSumUsingHashing (arr, s):
	"""
		Time Complexity: O(n)
	"""
	index = dict()
	found = False
	for i,n in enumerate(arr):
		if (s-n) in index:
			print 'Pair found is:',n,s-n,'at indices:',
			for j in index[s-n]:
				print j,i
			found = True
		
		if n not in index:
			index[n] = [i]
		else:
			index[n].append(i)
	if not found:
		print 'Pair not found'
		

if __name__ == '__main__':
	arr = [8, 7, 2, 5, 3, 1, 5, 9, 1]
	s = 10
	print 'Using naive approach:'
	pairWithGivenSumNaive (arr, s)
	print 'Using Hashing:'
	pairWithGivenSumUsingHashing (arr, s)
	print 'Using Sorting:'
	pairWithGivenSumUsingSorting (arr, s)