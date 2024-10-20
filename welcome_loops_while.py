passes = 0

ball_lost = False #o loop while continua executando enquanto a bola não é perdida

while not ball_lost:

    answer = input("Was the pass successful? (yes/no): ").lower()

    #em cada iteração, o programa pergunta se o passe foi certo ou errado
    
    if answer == "yes": #se o passe for certo o contador de passes aumenta em 1

        passes += 1

        print(f"The players exchanged {passes}")

    elif answer == "no": #se o passe for errado o programa para e mostra quantos passes foram certos

        ball_lost = True

    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

print(f"The players exchanged {passes} pass(es) before losing the ball.")