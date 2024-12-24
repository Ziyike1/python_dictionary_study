#字典是一系列的键值对(key-value pair)
alien_0 = {'color':'green','points':'5'}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")


alien_0 = {'color':'green','points':'5'}

alien_0['x_positions'] = 0
alien_0['y_positions'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
print(alien_1['color'])
alien_1['color'] = 'yellow'
print(alien_1['color'])


alien_0 = {'x_positions':0,'y_positions':25,'sepped':'medium'}
print(f"\nThe original positions is {alien_0['x_positions']}")

alien_0['sepped'] = 'fast'

if alien_0['sepped'] == 'slow':
    x_increment = 1
elif alien_0['sepped'] == 'medium':
    x_increment = 2
else:
    x_increment =3

alien_0['x_positions'] = alien_0['x_positions'] + x_increment
print(f"New position: {alien_0['x_positions']}")


alien_0 = {'color':'green','points':'5'}
print(alien_0)

del alien_0['points']
print(alien_0)