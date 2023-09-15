pizzas = ['chicken','pepperoni','cheese']
friends_pizzas = pizzas[:] #without the [:] both lists append values
pizzas.append('tomato')
friends_pizzas.append('mutton')
print (f'my favourite pizzas are {pizzas}')
print (f'my friend\'s favourite pizzas are {friends_pizzas}')
