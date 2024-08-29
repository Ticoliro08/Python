nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if idade>17:
    print("Você esta liberado!")
    with open ("Aprovados.csv","a") as arquivo: 
        arquivo.write(f"Seja bem vindo(a) {nome}")
else:
 print("Você nn esta liberado!")

with open ("Rprovados.csv","a") as arquivo:
    arquivo.write(f"Ola {nome}, vc nn foi liberado pois possui {idade} anos")