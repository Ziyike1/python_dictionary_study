favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phili':'python',
}

laguage = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {laguage}")


alien_0 = {'color':'green','speed':'low'}
# .get() 方法可以返回字典的特定值，在找不到值的情况下会返回提前设定好的值
point_value = alien_0.get('points','No point value assigned')
# point_value = alien_0.get('points')
print(point_value)