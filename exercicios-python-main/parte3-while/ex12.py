soma = 0 
numero =float(input("Digite um numero ou caso queira sair digite 0"))

while numero != 0:  
    soma = soma + numero
    numero = float(input("Digite outro numero casa deseje continuar, senao digite 0"))

print("A soma total é: ", soma)