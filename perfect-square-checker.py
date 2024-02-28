#Given a number, determine if it's a perfect square
#(like 1, 4, 9, 16, …).
#Hint: You might need
#the exponentiation operator for this.

num = 2
print(num **2)

square_num = (num **2)
if square_num // num == num:
    print(True)