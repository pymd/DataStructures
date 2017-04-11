#https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/
#http://quiz.geeksforgeeks.org/binary-search/
#http://www.spoj.com/problems/AGGRCOW/

def binarySearch(arr, start, end, ele):
	if start > end:
		return -1
	mid = (start+end)/2

	if arr[mid] == ele:
		return mid
	elif arr[mid] < ele:
		# Search in the right subarray
		return binarySearch(arr, mid+1, end, ele)
	else:
		# Search in the left subarray
		return binarySearch(arr, 0, mid-1, ele)

def binarySearchIterative(arr, ele):
	size = len(arr)
	start = 0
	end = size-1
	
	while True:
		if start > end:
			return -1
		mid = (start+end)/2
		if arr[mid] == ele:
			return mid
		elif arr[mid] < ele:
			start = mid+1
		else:
			end = mid-1


if __name__ == '__main__':
	#a = [4,5,9,10,14,66,69,100,512,1255]
	a = [1,10]
	print 'Array is:',a
	ele = input('Enter the element you want to search:')
	#pos = binarySearch(a, 0, len(a)-1, ele)
	pos = binarySearchIterative(a, ele)
	if pos != -1:
		print 'Element:',ele,'is present in the array at index:',pos
	else:
		print 'Element:',ele,'is NOT present in the array'