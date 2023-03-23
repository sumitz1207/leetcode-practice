def isPalindrome(self, pal: int) -> bool:
	if pal < 0:
		return False
	
	return str(pal) == str(pal)[::-1]
