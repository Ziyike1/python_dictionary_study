my_dic = {
    'type':'normal',
    'speed':'fast'
}
print(my_dic)

del my_dic['type']
print(my_dic)

print(my_dic['speed'])

my_dic_2 = {
    'type':'normal',
    'speed':'fast',
    'language':'java',
    'race':'white',
}

print(my_dic_2)

type = my_dic_2.get('type')
print(type)

none = my_dic_2.get('kill')
print(none)

for key,value in set(my_dic_2.items()):
    print(key,value)

person_0 = {
    'type':'easy',
    'speed':'fast'
}

person_1 = {
    'type':'easy',
    'speed':'fast'
}

person_2 = {
    'type':'easy',
    'speed':'fast'
}

people = [person_0,person_1,person_2]
print(people)

my_dic_3 = {
    'race':'black',
    'favorite':['bad','good']
}

print(f"The race is {my_dic_3['race']}")

for value in my_dic_3['favorite']:
    print(value)

#在字典中储存列表
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}
print(f"You ordered a {pizza['crust']} - "
      "crust pizza with the following toppings")

for topping in pizza['toppings']:
    print(f"\t{topping}")


#在字典中储存字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}

for user,info in users.items():
    name = f"{info['first']} {info['last']}"
    location = info['location']
    print(user,name,location)