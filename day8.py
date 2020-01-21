 #FORLOOPs iterate over a sequence (string,tuple,list,dictionary)
 # for variable name in thesequence:executes until the last element is reached
 # body
 # x=[1,2,3,4]
 # for each in X :
 # python statement


# numbers = [1,2,3,4,5]
# for eachitem in numbers:
#      # print(eachitem)
#      # print('iteration',eachitem)
#      # print(eachitem )
#      if eachitem%2==0:
#          print(eachitem, 'even')
#      else:
#          print(eachitem,'odd')
# else:
#     print('last item reached')
 # write a program that prints the numbers 1-101,each on a new line
# for i in range(1,101):
#     print(i)
#     if i%3==0:
#         print('fizz')
# for i in range(1,101):
#      if i%5==0 and i%3==0:
#          print(i,'fizzbuzz')
#      elif i%5==0:
#          print('buzz')
#      elif i%3==0:
#          print('fizz')
#      else:
#          print(i)
# else:
#     print('last one')

    # while loop -evaluate as long as the test expression is true
#      while True:
 # #     print("its true")
# while False:
#     print("its true")
i = 1
while i<=10:
    print(i)
    i+=1 # i=i+1
    i = 1
    # while i<=10:
    #     print(i)
    #     i+=1 #i=i+1
    # i=1
    # while i>=1:
    #     print(i)
    #     i-=1
    import random

    randomNum = random.randint(1, 21)
    # print(randomNum)
    start = 1
    while start <= 5:
        guess = int(input('Guess a number:'))
        if randomNum != guess:
            print('Wrong! Try again')
            start += 1
        else:
            print('Yeeees!!!!Correct!!!')
            break
    # modify above to show how close you are to the answer
    