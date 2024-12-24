user_0 = {
    'username':'efemi',
    'first':'enrico',
    'last':'fermi',
}

# .item() 方法返回一个键值对列表
for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phili':'python',
}

for name,language in favorite_languages.items():
    print(f"\nname:{name}")
    print(f"language:{language}")

print("\n")
for name in favorite_languages.keys():
    print(name.title())

print("\n")
for name in favorite_languages:
    print(name.lower())

print("\n")
friends = ['phili','sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

# .key() 方法会返回字典中的所有键
print(favorite_languages.keys())

# .values() 方法会返回字典中的所有值
print(favorite_languages.values())

print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# set() 集合方法可以剔除列表中的所有重复元素
print("\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 直接用花括号创建集合，容易和字典混淆
language_2 = {'python','rust','python','c'}
print(language_2)

