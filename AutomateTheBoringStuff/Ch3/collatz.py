def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return(3*number+1)
try:
    num=int(input("Enter number: "))
    while True:
        num=collatz(num)
        if num==1:
            break
except ValueError:
    print('You must enter an integer')