number  = 11  # Put the number you want to check if it is prime or not a prime over here
flag = False

if number>1:
    for i in range(2,11):

        if (number % i) == 0:
            flag = True
            break

        if flag:
            print(number," is not a prime number")

        else:
            print(number, "is a prime number")
