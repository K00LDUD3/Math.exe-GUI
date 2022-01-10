import math
ts=''
specnum_explain = { 'Armstrong':'Armstrong number is if the sum of the cube of the digits of a number is the number itself',
					'Buzz':'Buzz number is another special number in that ends with digit 7 or divisible by 7',
					'Automorphic':'An automorphic number is an integer whose square ends with the given integer',
					'Capricon':'A Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again', # CHANGE TO 'KAPREKAR'
					'Disarium':'A disarium number is a number in which the sum of the digits to the power of their respective position is equal to the number itself ',
					'Duck':'A Duck number is a positive number which has zeroes present in it',
					'Evil':'An evil number is a non-negative integer that has an even number of 1s in its binary expansion',
					'Odd':'If a given number is divisible by 2, then it is even, otherise odd',
					'Krishnamurthy':'whose sum of the factorial of digits is equal to the number itself',
					'Magic':'A magic number is when the recursive summing of digits equals 1',
					'Neon':'A neon number is a number where the sum of digits of square of the number is equal to the number',
					'Niven':'A niven number is an integer that is divisible by the sum of its digits',
					'Palindrome':'A palindrome number is a number equal to the reverse of itself',
					'Square':'A perfect square is a number which has an integer as its square root',
					'Strong':'Strong number is a number whose sum of the factorial of digits is equal to the original numbes',
					'Pronic':'A pronic number is a number which is the product of two consecutive integers',
					'Spy':'A spy number is a number where the sum of its digits equals the product of its digits',
					'Tech':'A number is called Tech number, if it has an even number of digits, and when we split the number into two halves then the square of the sum of those halves is equal to the number itself',
					'Prime':'A prime number is a number which has no factors except for itself and 1',
					'Factorial':ts}


def evalSpecNum(choice, num):

	if choice == 'Armstrong':
		return isArmstrong(num)
	elif choice == 'Buzz':
		return isBuzz(num)
	elif choice == 'Automorphic':
		return isAutomorphic(num)
	elif choice == 'Capricon':
		return isCapricon(num)
	elif choice == 'Disarium':
		return isDisarium(num)
	elif choice == 'Duck':
		return isDuck(num)
	elif choice == 'Evil':
		return isEvil(num)
	elif choice == 'Odd':
		return isEvenOdd(num)
	elif choice == 'Krishnamurthy':
		return isKrishnamurthy(num)
	elif choice == 'Magic':
		return isMagic(num)
	elif choice == 'Neon':
		return isNeon(num)
	elif choice == 'Niven':
		return isNiven(num)
	elif choice == 'Palindrome':
		return isPalindrome(num)
	elif choice == 'Square':
		return isPerfectSq(num)
	elif choice == 'Strong':
		return isStrong(num)
	elif choice == 'Pronic':
		return isPronic(num)
	elif choice == 'Spy':
		return isSpy(num)
	elif choice == 'Tech':
		return isTech(num)
	elif choice == 'Prime':
		return isPrime(num)
	elif choice == 'Factorial':
		return Factorial(num)

def Factorial(num):
	if num == 1:
		return 1

	else:
		return num * Factorial(num-1)

def isArmstrong(num): # Function to check whether the number is armstrong or not
	d = 0
	s = 0
	n = num
	while(num!=0):
		d = num%10
		s += (d*d*d)
		num = int(num/10)
	if s==n:
		return 'Armstrong number'
	else:
		return 'not an Armstrong number'       

def isPerfect(num): #Eg. 28,8,496
	sum = 0
	for i in range(1,num-1):
		if num%i==0:
			sum+=i

	if num==sum:
		return True
	else:
		return False

def isAutomorphic(num):
	# In mathematics, a number is called an Automorphic number if the square of the number ends with the same number.
	n1 = str(num)
	sq = str(num**2)
	l = len(str(n1))
	leng = len(str(sq))
	le = leng-l
	n2 = sq[le:]
	if(n1==n2):
		return 'Automorphic number'
	else:
		return 'not Automorphic number'

def isBuzz(num):
	# If the number ends with a 7 or is divisible by 7 then the number is a buzz number
	if num%7==0 or num%10==7:
		return 'Buzz number'
	else:
		return 'not Buzz number'

def isCapricon(num):
	# A number whose square divided into two parts, and the sum of the parts is 
	# equal to the original number then it is called Capricon number.
	sq = str(num*num)
	l = len(sq)
	if(l%2==0):
		d = l//2;
		sq1 = int(sq[:d])
		sq2 = int(sq[d:])
		sum = sq1+sq2
		if(sum==num):
			return 'Capricorn number'
		else:
			return 'not Capricorn number'
	else:
		return False            


def isDisarium(num):
	# If the sum of the digit of a number raised to the power of its position is equal to the number 
	# itself the number is said to Disarium number
	n1 = str(num)
	s = 0
	j = 0
	l = len(n1)
	for i in range(0,l):
		j=i+1
		s+=int(math.pow(int(n1[i]),j))
	if(s==num):
		return 'Disarium number'
	else:
		return 'not Disarium number'

def isDuck(num):
	# A number that has atleast one '0' (but not at the beginning of the number ) is called a duck number
	num = str(num)
	n = num[1:]
	count=0
	for i in n:
		if(i=='0'):
			count+=1
	if(count>0):
		return 'Duck number'
	else:
		return 'not Duck number'
	
def isEvil(num):
	# binary expansion has an evil number of 1's if it is evil
	decimal = str(bin(num))
	count_1 = decimal.count('1')
	if count_1 % 2 == 0:
		return 'Evil number'
	return 'not Evil number'

def isEvenOdd(num):
  # If a number is divisible by 2 its said to be an even number
  if(num%2==0):
    return 'Even number'
  return 'Odd number'

def isKrishnamurthy(num):
	# A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself
	fact = math.factorial(num)
	if fact == num:
		return 'Krishnamurthy number'
	return 'not Krishnamurthy number'

def isMagic(num):
	# If the reverse of the sum of digits multiplied by sum of digits is equal to the original number, then its a magic number
	rev_sum = 0
	temp_num = 0
	temp_num_1 = 0
	sum = 0
	while temp_num > 0:
		sum += temp_num % 10
		temp_num //= 10
	temp_sum = sum
	
	while temp_sum > 0:
		rev_sum += rev_sum * 10 + temp_sum % 10
		temp_sum //= 10
	
	if rev_sum * sum == num:
		return 'Magic number'
	return 'not Magic number'

def isNeon(num):
	# sum of the digits of the square of the numbers is equal to the number itself
	num_sqr = num**2
	sum = 0
	while num_sqr > 0:
		sum += num_sqr % 10
		num_sqr //= 10
	if num == sum:
		return 'Neon number'
	return 'not Neon number'
	
def isNiven(num):
	sum = 0
	temp = num
	while temp > 0 :
		sum = sum + temp % 10
		temp = temp // 10
	if num % sum == 0:
		return 'Niven number'
	return 'not Niven number'  
	
def isPalindrome(num): 
	# if the revers of a number is equal to itself
	val = str(num)
	if val == val[::-1]:
		return 'Palindrome'
	return 'not Palindrome'

def isPerfectSq(n):
	if (math.sqrt(n))%1 == 0:
		return 'Perfect Square'
	else:
		return 'not a Perfect Square'
	
def isStrong(n):
	#Strong number is a special number whose sum of the factorial of digits is equal to the original number
	a = str(n)
	sum = 0
	if n<0 or n ==0:
		print("It is not a strong no.")
		quit()
	
	else:
		for i in a:
			b = int(i)
			c = Factorial(b)
			sum += c  
	
	if sum == n:
		return 'Strong number'
	else:
		return 'not Strong number'
	

def isPronic(n):
	#A pronic number is a number which is the product of two consecutive integers, that is, a number of the form n(n + 1)
	if n%2 != 0:
		return False
	else:
		for i in range(1,n+1):
			if i * (i + 1) == n:
				return 'Pronic number'
		else:
			return 'not Pronic number'

def isSpy(n):
	#A positive integer is called a spy number if the sum and product of its digits are equal
	a = str(n)
	product = 1
	sum = 0 
	for i in a:
		b = int(i)
		sum += b
		product *= b
	if (sum == product):
		return 'Spy number'
	else:
		return 'not Spy number'


def isTech(n):
	#A tech number has an even number of digits and it can be divided exactly into two parts from the middle
	n = str(n)
	count = 0
	B = 0
	C = 0
	for i in n:
		count += 1
		if count % 2 != 0:
			return False

	a = int(n)
	B = a // math.pow(10,(count/2))
	C = a % math.pow(10,(count/2)) 

	Sum = B + C

	if (Sum)**2 == a:
		return 'Tech number'
	else:
		return 'not Tech number'

def isPrime(n):
	# A Prime number is a number that is only divisible by itself and 1
	count = 0
	for i in range(1,n):
		if(n%i!=0):
			count+=1
	if(count==n-2):
		return 'Prime number'
	else:
		return 'not Prime number'