#variables 
#str = textos
#int = inteiros
#float = númericos
#bool = verdadeiro ou falso
#tuple = lista que não pode ser alterada
#list = lista que pode ser alterada
#dict = dicionarios (conjuntos de dados sobre algo ou alguem)
#set = conjuntos (listas que não possuem suas informações ordenadas e não podem ter varias ocorrencias do mesmo elemento)

players = ['Neymar','Ronaldo','Messi'] #lista

players.remove('Neymar') #usado para retirar

players.insert(0,'Pelé') #usado para inserir

print ('name:', players)

print ('name:', players[1]) #usado para dizer somente o "primeiro" item



ages_players = ('82','39','37') #tupla

print ('age:', ages_players[1])

idade1 = ('1')          #como é somente um item, precisa de uma virgula depois se não é considerado string

idade2 = ('2', )          #agora é considerado como tupla

idade3 = (1)

idade4 = (1,)

print (type (idade1))

print (type (idade2))

print (type (idade3))

print (type (idade4))



player_data = {  #dicionários
       'Name': 'Ronaldo',  #para funcionar não usa-se '=' mas sim ':'
       'Age': 39,
       'Hability': ' very good',
       'parents': ('José Diniz', 'Dolores Aveiro')
} 

player_data['children'] = ('Ronaldo Jr')

print (type (player_data['children']))

print (player_data)

player_data.pop ('Age', None)

print (player_data)