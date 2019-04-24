def merge(l,start,mid,end):
	if start > mid or mid > end:
		return None
	c = list()
	i = start; j = mid+1
	while i <= mid and j <= end:
		if l[i] <= l[j]:
			c.append(l[i])
			i += 1
		else:
			c.append(l[j])
			j += 1
	while i <= mid:
		c.append(l[i])
		i += 1
	while j <= end:
		c.append(l[j])
		j += 1
	i=start; k = 0
	while k < len(c):
		l[i] = c[k]
		k += 1
		i += 1
	return l

def mergeSort(l,start,end):
	if l is None:
		return None
	if start >= end:			# 1 element list, already sorted
		return l
	mid = (start + end)/2
	mergeSort(l, 0, mid)
	mergeSort(l, mid+1, end)
	l = merge(l, start, mid, end)
	return l

if __name__ == '__main__':
	l = [2,701,12,141,14,11,41,20,1]
	#l = [2,1]
	print('Original array:',l)
	print('The sorted array is:',mergeSort(l, 0, len(l)-1))