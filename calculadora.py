def boas():
    print("Seja bem vindo")
    print("Bem vindo a calculadora do Banco do Santander")
    print("Podemos errar, podemos acertar, mas de braços cruzados não vamos ficar.")  #Introdução base

boas()
vet = []
r=0
while True:
 number_One = int(input("Solicite ao usuario o primeiro número"))
                                                                #Solicitando os dois numeros que seram usados para a calc
 number_Two = int(input("Solicite ao usuario o segundo número"))



#teste_Soma = len(number_One,number_Two)
#print(number_One,number_Two)              #Numeros que foram digitados,posso deixar isso ou não já que a soma vai estar em diante
#print (teste_Soma)

#Daqui em diante todo o "corpo". Subtração,divisão e etc sempre retornado o valor digitado como na linha 12



 escolha = input('''A seguir ,você deverá escolher uma das 5 opções abaixo conforme sua vontade \n
 A para a opção de adição \n
 B para a opção de subtração \n
 C  para a opção de multiplicação \n
 D  para a opção de divisão \n
 E para a opção de  sair \n '''                
 )



 



 if escolha == "A" :
  r=number_One+number_Two
     
 
 elif escolha == "B" :
  r=number_One-number_Two
  
 
 elif escolha == "C" :
  r=number_One * number_Two
  
 
 elif escolha == "D" :
   r=number_One//number_Two
   
 
 elif escolha == "E" :
   print("Tudo bem,vamos sair da calculadora")
   break
 print("RESULTADO: ", r)
 vet.append(r)
print(vet)

#escolha = input("Deseja fazer uma nova operação (S para sim,qualquer outra para sair)")

#if escolha.lower() != "s" :
   

