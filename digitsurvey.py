# We need to enter a number first read it as a string then add all it's digit and print digit in reverse fashion
# Enter a string number 
# use // 100
# convert that number to int and the store the value of a as i nput/100
# then use %100 to ignore the foirts letter
# then in b store number//10 
# then in c store number %10
# then add a,b,c o get the output
# then print c*100 + b*10 + a

Input_num = int(input("Enter a number: "))
a = Input_num // 100
reminder = Input_num % 100
b = reminder // 10
c = reminder % 10
print(f"Input: {Input_num}")
print(f"Sum of digits: {a+b+c}")
print(f"Reversed: {c * 100 + b * 10 + a}")