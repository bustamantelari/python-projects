n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Digite +, -, * ou /: ")

if operacao == "+":
    print("Resultado:", n1 + n2)

elif operacao == "-":
    print("Resultado:", n1 - n2)

elif operacao == "*":
    print("Resultado:", n1 * n2)

elif operacao == "/":
    print("Resultado:", n1 / n2)

else:
    print("Operação inválida")
