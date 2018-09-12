def main():
	k = addThree(7,8,9.5)
	print (divideByThree(k))
	
def addThree(n1,n2,n3):
	return n1+n2+n3

def divideByThree(num):
	return num/3
	
if __name__ == "__main__":
	main()