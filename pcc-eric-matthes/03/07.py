gl = ['tom', 'jim', 'mark', 'brian', 'tim', 'cypher']

for name in gl:
    print(f'Hello {name.title()}, You are invited to Hridyesh\'s dinner party.')

print(f'\nNevermind, {gl[3].title()} is unable to attend. Redo ->\n')

del gl[3]

for name in gl:
    print(f'Hello {name.title()}, You are invited to Hridyesh\'s dinner party.')

print('\nOkay, New dinner table acquired, we may invite more people\n    ')

middle_index = int(len(gl) / 2)
gl.insert(0, 'jacob')
gl.insert(middle_index, 'joe')
gl.append('sarah')

for name in gl:
    print(f'Hello {name.title()}, You are invited to Hridyesh\'s dinner party.')

print('\nDue to certain circumstances, we can only invite two people unfortunately.\n')

while len(gl) > 2:
    print(f'Sorry {gl[-1]}, but you\'ve been uninvited.')
    gl.pop()  

print(f'\nThe only two guests invited are {gl[0]} and {gl[1]}!')
del gl[0]
del gl[0]  

print(gl)
