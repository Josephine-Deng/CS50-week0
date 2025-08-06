import random
rand=random.randint(1,10)
num=eval(input("Enter a number between 1 and 10: "))
i=1
while num!=rand:
    if num < rand:
       print('too small')
    elif num>rand:
       print('too big')
    i+=1
    num = eval(input("Enter a number between 1 and 10: "))
else :
    print('right')
    print(f'The number is {num},and you answer {i} times')