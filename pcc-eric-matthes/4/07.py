# multiplication table
multiples_of_three = list(range(3,31,3))
multiples_of_one = list (range(1,11,1))
for i in multiples_of_one :
    print (f'3 x {i} = {multiples_of_three[i-1]}')
