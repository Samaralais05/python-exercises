numero1=int(input("Digite o primeiro valor: "))
numero2=int(input("Digite o segundo valor: "))
numero3=int(input("Digite o terceiro valor: "))

maiorvalor=numero1

if numero2 > numero1:
    maiorvalor=numero2
    
if numero3 > numero1:
    maiorvalor=numero3
print ("O maior valor é: ", maiorvalor)
