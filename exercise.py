taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
x = type(taskList)
print(x)
# print kes
print(taskList[2][2]['currency'])

# print 560
print(taskList[2][1])

# len of tsk
print(len(taskList))

# change 987 to 787 using an inbult function
num =987
num =str(num)
print(num[::-1])

# change the name john to jane
name ='Jane'
print(name.replace('John','Jane'))

x=taskList
print(x)

