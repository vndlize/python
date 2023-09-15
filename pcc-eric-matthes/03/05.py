gl = ['tom','jim','mark','brian','tim','cypher']
for name in gl :
    print (f'Hello {name.title()}, You are invited to Hridyesh\'s dinner party.')
print (f'Nevermind, {gl[3].title()} is unable to attend. Redo ->\n')
del gl[3]
for name in gl :
    print (f'Hello {name.title()}, You are invited to Hridyesh\'s dinner party.')