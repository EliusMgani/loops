# for loop
def f_r():
	num = 2

	for a in range(1,6):
		print (num * a)
f_r()

def f_t():
	sum = 0

	for n in range(1,11):
		sum+=n
		print(sum)
f_t()

# while loop
def a_r():
	a = 10
	while a > 0:
		a-=2
		print("The value of a is", a)
	print ("Loop is completed")
a_r()

def a_t():
	n = 153
	sum = 0
	while n > 0:
		r = n%10
		sum += r
		n = n/10
		print(sum)
a_t()

# break statement
number = 0
for number in range(10):
	number += 1
	if number == 7:
		break
	print("The number is " + str(number))
print("Out of Loop")

# continue statement
def tr():
	a = 0

	while a<=5:
		a+=1
		if a%2==0:
			continue
		print(a)
	print("End of tha Loop")
tr()

def td():
	number = 0
	for number in range(10):
		number += 1
		if number == 7:
			continue
		print("The number is " + str(number))
	print("Out of Loop")
td()
	
# pass statement(excute empty)
number = 0
for number in range(10):
	number += 1
	if number == 7:
		pass
	print("The number is " + str(number))
print("Out of Loop")