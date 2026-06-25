import random
print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numerosecreto = random.randrenge(1,100)
totaldedentativas = 10 

chute = input("Digite o seu número: ")
print("Você digitou: ", chute)

chuteNumerico = int (chute)

while(totaldedentativas > 0):
    print("Voce tem", totaldedentativas,"tentativas")
    totaldedentativas = totaldedentativas - 1 
    print("tentativa restante:", totaldedentativas)
    

if(totaldedentativas == 0):
    print("Voc não tem mais  ")
    
    
    print("Voce não tem mais tentativas. fim de jogo.")
    break

chuteNumerico = int(chute)

acertou = chuteNumerico == numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto

#se voce digitar qualque número vou verificar se acertou ou erro
if(acertou):
    print("você acertou! fim de jogo") 
else:
    if(maior):
        print("vovê errou! o seu chute foi maior que o número secreto.")
    elif("menor"):
        print("voce errou! O seu chute foi menor que o número secreto")

print("fim do jogo")