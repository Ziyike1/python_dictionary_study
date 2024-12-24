alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yello','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


#在列表中储存字典
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")


aliens = []
for alien_number in range(30):
    new_alien = {'color':'yellow','points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == "green":
        alien['color'] = "yellow"
        alien['speed'] = "medium"
        alien['points'] = 10

    elif alien['color'] == "yellow":
        alien['color'] = "red"
        alien['speed'] = "fast"
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")


#在字典中储存列表
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}
print(f"You ordered a {pizza['crust']} - "
      "crust pizza with the following toppings")

for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phili':['python','haskell'],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are")
    for language in languages: 
        print(f"\t{language.title()}")


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

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
