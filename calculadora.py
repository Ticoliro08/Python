while True:
 print("Ola, sou gary sua calculadora digital!/n Qual operação deseja realizar:")
 print("Soma - Opção 1")
 print("Subtração - Opção 2")
 print("Multiplicação - Opção 3")
 print("Divisão - Opção 4")
 print("Potência - Opção 5")

 opcao = input("Escolha a opçao:")


 
 match opcao:
  case "1":
   soma1 = float( input("Digite o primeiro numero:"))
   soma2 =float (input("Digite o segundo numero:"))
   soma_total = soma1 + soma2
   print(f"A soma total é de {soma_total}")

  case "2":
   sub1 = float( input("Digite o primeiro numero:"))
   sub2 =float (input("Digite o segundo numero:"))
   sub_total = sub1 - sub2
   print(f"A subtração total é de {sub_total}")

  case "3":
   mult1 = float( input("Digite o primeiro numero:"))
   mult2 =float (input("Digite o segundo numero:"))
   mult_total = mult1 * mult2
   print(f"A multiplicação total é de {mult_total}")

  case "4":
   div1 = float( input("Digite o primeiro numero:"))
   div2 =float (input("Digite o segundo numero:"))
   div_total = div1 / div2
   print(f"A divisão total é de {div_total}")

  case "5":
   pot1 = float( input("Digite o primeiro numero:"))
   pot2 =float (input("Digite o segundo numero:"))
   pot_total = pot1 ** pot2
   print(f"A divisão total é de {pot_total}")
  
  case _:
   print("Opção não encontrada!")  


 resposta = input("Deseja continuar? (s/n): ")
 if resposta == 'n':
  break  

  
