# taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
# print(type(taskList))
# x=(type(taskList))
# print(taskList[2][1]["KES"])
# Dictionaries
# this_dict={}
# print(type(this_dict))
# syntax
thisdict={

    # "key":"value",
    # Key must be unique and wrapped between single or double quote
    # value can be any dattype eg tuple,list,int,float,string

    "name":"wamuyu",
    "int":["swimming",'dancing'],
    "age":10,
    "workDays":('mon','tue'),
    "parents":{
        "mother":"molly"
    }
}
# print the dictionary
print(thisdict)
# retrieve the name
print(thisdict['parents']['mother'])
print(thisdict["workDays"])
dict={
    'name':'wamuyu',
   'primary': {'primary1':'hezta',
            "total population":{'male':'70',
                          'female':'30'},
     'headteacher':{'firstName':'Kahero',
                    'lastName':'maina'},
               'primary2':'vantage',
      "total population2":{'male':'40',
                          'female':'30'},
     'headteacher2':{'firstName':'mwangi',
                    'lastName':'Job'}
     },
    'Language':('English','French')
}
print(dict)
# Task 3
numbers =[1023,43546,678345,54767]
print(max(numbers))
print(numbers[::2])
num=(1,2,3,4,5,6,7,8,9,10)
# print(num[::9])
for x in num:
    print (x)
firsthalf=num[0:5]
lasthalf=num[5:]
first_to_string= str (firsthalf)
print(first_to_string.strip('()'))
