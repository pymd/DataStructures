def findSubArraysWithZeroSumNaive (arr):
	"""
		A naive approach
		Time Complexity: O(n^2)
	"""
	result = []
	for i,n in enumerate(arr):
		s = n
		if s == 0:
			result.append((i,i))
		j = i+1
		for m in arr[i+1:]:
			s += m
			if s == 0:
				result.append((i,j))
			j += 1
	return result

def findSubArrayWithZeroSumUsingHash (arr):
	"""
		Time Complexity: O(n)		(NOT SURE)
		Space:	O(n)
	"""
	sumHash = {}
	result = []
	s = 0
	for i,n in enumerate(arr):
		s += n
		if s == 0:
			result.append((0,i))
		if s in sumHash:
			sumHash[s].append(i)
			for j in sumHash[s]:
				if i != j:
					result.append((j+1,i))
		else:
			sumHash[s] = [i]
	return result

if __name__ == '__main__':
	#arr = [ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]
	arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
	print 'The array is:',arr
	print 'The length of array is:',len(arr)

	print 'The subarrays start and stop indices with 0 sum are:'
	results = findSubArraysWithZeroSumNaive(arr)
	for result in results:
		print 'start =',result[0],', stop =',result[1]
	print 'Using hashing results are:'
	results = findSubArrayWithZeroSumUsingHash(arr)
	for result in results:
		print 'start =',result[0],', stop =',result[1]