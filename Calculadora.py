continuar = True

while continuar:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha qual operação deseja fazer (+, *, /, -): ")
    resultado = 0
    op_valida = True

    match operacao:
        case "+":
            resultado = n1 + n2
            print(f"O resultado da operacão é: {resultado}\n")
        case "*":
            if n1 or n2 >= 1:
                resultado = n1 * n2
                print(f"O resultado da operacão é: {resultado}\n")
            else:
                print(f"Digite um número difprinterente de 0\n")
        case "/":
            if n1 or n2 >= 1:
                resultado = n1 / n2
                print(f"O resultado da operacão é: {resultado}\n")
            else:
                print(f"Digite um número diferente de 0\n")
        case "-":
            resultado = n1 - n2
            print(f"O resultado da operacão é: {resultado}\n")
        case _:
            print(f"Digite uma operção válida\n")
    print("---------------------------------------------")


