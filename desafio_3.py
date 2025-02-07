# TERCEIRO DESAFIO

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Operação inválida")
