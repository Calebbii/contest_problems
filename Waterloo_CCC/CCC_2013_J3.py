'''
	x = 3445

	nums = [5,4,3]

	345%10 = 5
	345//10 =34

	34%10 = 4
	34//10 = 3

	3%10 = 3
	3//10 = 0

	nums = [3,4,4,5]
'''

'''
return True if x has distinct digits
return False if x does not have distinct digits

isDistinct(1987) --> True
isDistinct(999) --> False
'''
def nextdistinct(y):

	nums = [] #store each digit from x

	while (y != 0):
		nums.append(y%10) #Takes the units digit of x and appends it to nums
		y = y // 10

	#Sort nums
	nums.sort()

	for i in range(1,len(nums),1):
		if (nums[i] == nums[i -1]):
			return False

	return True

num = int(input())
num = num + 1 #I am looking for the next distinct digit

distinct = nextdistinct(num)

#loop until we find a distinct number
while(distinct == False):
	num = num + 1
	distinct = nextdistinct(num)

print(num)



















