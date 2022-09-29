#Calcular IMC de acordo com a fórmula
#IMC = peso/(altura*altura)
#Abaixo do peso quando for menos de 18,5kg/m2;
#Normal quando for entre 18,5 e 24,9kg/m2;
#Sobrepeso quando for entre 24,9 e 30kg/m2;
#Obeso quando for maior que 30kg/m2;
#Quando for numero quebrado usar ponto e não vírgula
altura=float(input("Sua altura é: "))
peso=float(input("Seu peso é: "))
IMC=(peso/(altura*altura))
print("Seu IMC é ", IMC)
if IMC<=18.5:
    print("Você está abaixo do peso")
elif IMC>18.5 and IMC<=24.9:
    print("Seu peso está normal")
elif IMC>24.9 and IMC<=30:
    print("Você está com sobrepeso")
else:
    print("Você está obeso")
