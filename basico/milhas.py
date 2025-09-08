#Milhas e quilômetros são unidades de comprimento ou distância.

#Lembrando que 1 milha é igual a aproximadamente 1.61 quilômetros,
#complete o programa no editor para que converta:

    #milhas em quilômetros;
    #quilômetros em milhas.

#Saída esperada
#7.38 milhas é 11.88 quilômetros
#12.25 quilômetros é 7.61 milhas

kilometres=12.25
miles=7.38

miles_to_kilometres= miles * 1.61
kilometres_to_miles= kilometres / 1.61

print(miles, "milhas é", round(miles_to_kilometres, 2),"quilômetros")
print(kilometres, "quilômetros é", round(kilometres_to_miles, 2), "milhas")
