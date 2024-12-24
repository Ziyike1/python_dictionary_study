#6.1
person_info = {
    'first_name':'yuan',
    'last_name': 'ryan',
    'age' : 22,
    'city': 'New Zealand',
}

print(f"This is my bor, {person_info['first_name']} {person_info['last_name']},\
 he is {person_info['age']} years old, and he lives in {person_info['city']}.")


#6.2
liked_number = {
    'gav': 2,
    'roger': 9,
    'leo': 6,
    'andrew': 3,
}

print(f"gav like {liked_number['gav']}")
print(f"roger like {liked_number['roger']}")
print(f"leo like {liked_number['leo']}")
print(f"andrew like {liked_number['andrew']}")


#6.3
my_dictionary = {
    'key-value pair':'键值对',
    'key':'键',
    'value': '值',
    'dictionary':'字典',
    'tuple': '元组',
}

print(f"key-value pair: {my_dictionary['key-value pair']}")
print(f"key: {my_dictionary['key']}")
print(f"value: {my_dictionary['value']}")
print(f"dictionary: {my_dictionary['dictionary']}")
print(f"tuple: {my_dictionary['tuple']}")


#6.4
my_dictionary = {
    'key-value pair':'键值对',
    'key':'键',
    'value': '值',
    'dictionary':'字典',
    'tuple': '元组',
    'set':'集合',
}

for k,v in my_dictionary.items():
    print(f"\nthe english version is {k}")
    print(f"the chinese version is {v}")


#6.5
rivers = {
    'nile':'egypt',
    'east lake':'china',
    'chang jiang':'china',
}

for river, nation in rivers.items():
    print(f"The {river} runs through {nation}.")

for river in rivers.keys():
    print(river)

for nation in rivers.values():
    print(nation)

#6.6
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phili':'python',
}

ready_poll_people = ['jen','allen','edward','jack']

for people in favorite_languages.keys():
    if people in ready_poll_people:
        print(f"{people}, Thanks to join our poll.")
    else:
        print(f"{people}, please come to join our poll.")


#6.7
person_info = {
    'first_name':'yuan',
    'last_name': 'ryan',
    'age' : 22,
    'city': 'New Zealand',
}

person_info_2 = {
    'first_name':'roger',
    'last_name': 'liu',
    'age' : 23,
    'city': 'New Zealand',
}

person_info_3 = {
    'first_name':'leo',
    'last_name': 'liu',
    'age' : 24,
    'city': 'New Zealand',
}

people = []
people.append(person_info)
people.append(person_info_2)
people.append(person_info_3)

for person in people:
    print(f"Name:{person['first_name']} {person['last_name']} "
          f"Age:{person['age']} Location:{person['city']}")
    

#6.8
pet_0 = {
    'type':'cat',
    'master':'ryan',
}

pet_1 = {
    'type':'dog',
    'master':'roger',
}

pet_2 = {
    'type':'turtle',
    'master':'leo',
}

pets = []
pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    print(f"Pet name is {pet['type']}, master name is {pet['master']}")


#6.9
favorite_place = {
    'gav':['New York','New Zealand'],
    'roger':['China','England'],
    'leo':['China','German'],
}

for person,place in favorite_place.items():
    print(f"My friend {person} like {place[0]} and {place[1]}")


#6.10
liked_number = {
    'gav': [2,3,4],
    'roger': [2,6],
    'leo': [7,9],
    'andrew': [1,2,3],
}

for person,number in liked_number.items():
    print(f"My friend {person} like {number}")


#6.11
cities = {
    'Shanghai':{
        'country':'China',
        'population':14,
        'fact':'skyscraper',
    },
    'Beijing':{
        'country':'China',
        'population':14,
        'fact':'gate',
    },
    'Guizhou':{
        'country':'China',
        'population':14,
        'fact':'mountain',
    },
}

for city,info in cities.items():
    print(f"The city name is {city}, it belongs to {info['country']},"
        f" its population is {info['population']}, and its fact is {info['fact']}")
    

#6.12
aliens = []
for alien_number in range(10):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    new_alien_2 = {'color':'red','points':15, 'speed':'fast'}
    new_alien_3 = {'color':'yellow','points':10, 'speed':'medium'}
    aliens.append(new_alien)
    aliens.append(new_alien_2)
    aliens.append(new_alien_3)

for alien in aliens:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")