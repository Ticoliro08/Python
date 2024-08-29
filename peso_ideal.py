
 
sexo = str(input("Digite seu sexo:"))
altura = float(input("Digite sua altura atual:"))
peso = float(input("Digite seu peso atual:"))


if sexo == "masculino":
 peso_ideal = round(((72.7*altura)-58),2)
 print(f"Seu peso ideal é de{peso_ideal}")
elif sexo == "feminino":
 peso_ideal = round(((62.1*altura)-44.7),2)
 print(f"Seu peso ideal é de {peso_ideal} quilos")
 
 

 




