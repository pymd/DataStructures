def search (text, pattern):
	"""
		A naive algorithm to print all occurrences of pattern in text
		Time Complexity:	O((n-m+1) * m)
		where,				n : length of text,
							m : length of pattern
	"""
	for i in xrange(len(text)-len(pattern)+1):
		found = True
		for j in xrange(len(pattern)):
			if text[i+j] != pattern[j]:
				found = False
				break
		if found:
			print 'Pattern found at index:', i
	return


if __name__ == '__main__':
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	print "Finding",pat,"in",txt
	search (txt, pat)

	txt = "AAAAAAAAAAAAAAAAAA"
	pat = "AAAAA"
	print "Finding",pat,"in",txt
	search (txt, pat)

	txt = "AAAAAAAAAAAAAAAAAB"
	pat = "AAAAB"
	print "Finding",pat,"in",txt
	search (txt, pat)