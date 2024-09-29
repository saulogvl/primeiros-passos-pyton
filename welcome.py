print ('welcome')

age: int = int(input('how old are you? '))

name: str = input('what is your name? ')

goalkeeper: str = input('you is goalkeeper? ')

heigth: float = input('how tall are you? ')

ativo: bool = input('yous stay active?(yes/no) ').lower() == 'yes'

print(f'Age: {age}, name: {name}, are you tall: {heigth}, you are goalkeeper? {goalkeeper}, you stay active? {ativo}')