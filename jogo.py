print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numerosecreto = 40 

chute = input("Digite o seu número: ")
print("Você digitou: ", chute )

chuteNumerico = int(chute)

acertou = chuteNumerico == numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto


#se voce digitar qualque número vou verificar se acertou ou erro
if(numerosecreto == chuteNumerico):
    print("você acertou!") 
else:
    print("vovê errou!")

print("fim do jogo")