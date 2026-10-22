for i in range(1,101):
    b = str(i)
    # print(b)
    if((i%3==0 or ("3" in b)) and (i%5==0 or ("5" in b))):
        print(i,'FizzBuzz')
    elif(i%3==0 or ("3" in b)):
        print(i,'Fizz')
    elif(i%5==0 or ("5" in b)):
        print(i,'Buzz')
    else:
        print(i)