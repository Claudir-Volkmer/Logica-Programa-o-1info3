#.Meu primeiro programa

from random import randint

print("Jogo dos Dados:")

dado1 = randint (1,6) 
print("dado 1: ", dado1)

dado2 = randint (1,6) 
print("dado 2: ", dado2)

dado3 = randint (1,6) 
print("dado 3: ", dado3)

dado4 = randint (1,6) 
print("dado 4: ", dado4)

Jogador1 = dado1 + dado2
Jogador2 = dado3 + dado4

print("jogador1:", Jogador1)
print("jogador2:", Jogador2)

if Jogador1 > Jogador2:
    print("jogador1 venceu")
else:
 if Jogador2 > Jogador1:
    print("Jogador 2 venceu"!)
else:
    print ("Empate!")
