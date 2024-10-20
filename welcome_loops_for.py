all_goals = 0

for chute in range(1, 6): #o loop for é usado para repetir o processo 5 vezes, uma para cada chute.
    
    resposta = input(f"kick {chute}: maked goal? (yes/no): ").lower()
    
    #em cada pergunta, o programa pergunta ao usuário se o chute foi gol ou não, esperando uma resposta

    if resposta == "yes":

        print ('Goooooooooaaal beautiful kick!!')

        all_goals += 1 #se o pessoa responder sim, a variável all_goals aumenta em 1.

    elif resposta == "no":

        print ('soo close!')
    
    else :
        print ('Goal not registred')

print(f"you scored {all_goals} goal(s) with 5 kicks.") #no final, o programa exibe quantos gols foram feitos nos 5 chutes
