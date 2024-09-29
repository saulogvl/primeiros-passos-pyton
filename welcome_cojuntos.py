balls = set(['red', 'blue', 'multicolors', 'pink']) #conjunto

print (type (balls))

balls.add ('green')

balls.discard ('multicolors')

print (balls)

numbers1 = set(['1', '2', '3', '4'])

numbers2 = set(['5', '6', '7', '8'])

lyrics = set(['a', 'b', 'c', 'd', 'e'])

print (numbers1)

numbers1.update (numbers2) #usado para adicionar o segundo com o primeiro ou com o terceiro ou terceiro com segundo e assim por diante

print (numbers1)

numbers1.update (lyrics)

print (numbers1)

for skills in numbers2:
    print(skills)