#para ser considerado complex precisa ter a letra 'j' no segundo número 
#o primeiro número é considerado número real e o segundo imaginario
numbers = 15+18j

numbers2 = 19+33j

number = 18+18

print (type(numbers))

print (type(numbers2))

print (type (number))

print (complex (15, 18)) #quando se coloca complex antes, o pyton entende que o usuario quer colocar o 'j' no ultimo número cituado (não é possivel por mais de 2 numeros pois da um erro)

print (complex (19, 33)+ (numbers))

print (complex (20, 18)+ (numbers)+ (number)) #quando se soma primeiro é feito a soma e depois se coloca a letra 'j' no ultimo número