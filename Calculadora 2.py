# importando system e o math
import os
import math
import time
from datetime import datetime

# grupos de resultados as operação
resultados_divisao = []
resultados_multiplicacao = []
resultados_soma = []
resultados_subtracao = []
resultados_porcentagem = []
resultados_raiz_quadrada = []
resultados_potencia = []

# use para exibir os textos do código, ele limpa a tela, escreve e cerca com -
def exibir_texto(texto):
    limpar_tela()
    linha = "-" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# exibi o nome do programa
def exibir_nome_calculadora():
    print("""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄    ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄ 
█       █      █   █   █       █  █ █  █   █   █      █      ██       █   ▄  █ █      █  █       █    █  ▄    █
█       █  ▄   █   █   █       █  █ █  █   █   █  ▄   █  ▄    █   ▄   █  █ █ █ █  ▄   █  █▄▄▄▄   █    █ █ █   █
█     ▄▄█ █▄█  █   █   █     ▄▄█  █▄█  █   █   █ █▄█  █ █ █   █  █ █  █   █▄▄█▄█ █▄█  █   ▄▄▄▄█  █    █ █ █   █
█    █  █      █   █▄▄▄█    █  █       █   █▄▄▄█      █ █▄█   █  █▄█  █    ▄▄  █      █  █ ▄▄▄▄▄▄█▄▄▄ █ █▄█   █
█    █▄▄█  ▄   █       █    █▄▄█       █       █  ▄   █       █       █   █  █ █  ▄   █  █ █▄▄▄▄▄█   ██       █
█▄▄▄▄▄▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █▄█▄█ █▄▄█  █▄▄▄▄▄▄▄█▄▄▄██▄▄▄▄▄▄▄█
""")
    
def carregando():
    exibir_texto("CARREGANDO....")
    loop = 0
    time.sleep(1.0)

# ele limpa a tela e depois mostra um botão para reiniciar o codigo
def voltar_ao_menu_principal(): 
    input("Digite uma tecla para voltar ao menu principal\n")
    carregando()
    main()

# exibi as opções do programa
def main():
    limpar_tela()
    exibir_nome_calculadora()
    exibir_opcoes()
    escolher_opcao()

# limpa a tela usando o system cls
def limpar_tela():
    os.system("cls")

# faz as contas de divisão e adiciona o resultado nos grupos acima
def operacao_divisao():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝘿𝙞𝙫𝙞𝙨𝙖𝙤")
    n1 = float(input("Digite o prímeiro número da equação: "))
    n2 = float(input("Digite o segundo número da equação: "))
    resultado = n1 / n2
    exibir_texto(f"O resultado da equação de divisão é iqual a: {resultado:,.2f}")
    resultados_divisao.append(resultado)
    voltar_ao_menu_principal()

# faz as contas de multiplicação e adiciona o resultados nos grupos acima
def operacao_multiplicacao():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙈𝙪𝙡𝙩𝙞𝙥𝙡𝙞𝙘𝙖𝙘𝙖𝙤")
    n1 = float(input("Digite o prímeiro número da equação: "))
    n2 = float(input("Digite o segundo número da equação: "))
    resultado = n1 * n2
    exibir_texto(f"O resultado da equação de multiplicação é iqual a: {resultado:,.2f}")
    resultados_multiplicacao.append(resultado)
    voltar_ao_menu_principal()

# faz as contas de soma e adiciona o resultado nos grupos acima
def operacao_soma():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙎𝙤𝙢𝙖")
    n1 = float(input("Digite o prímeiro número da equação: "))
    n2 = float(input("Digite o segundo número da equação: "))
    resultado = n1 + n2
    exibir_texto(f"O resultado da equação de soma é iqual a: {resultado:,.2f}")
    resultados_soma.append(resultado)
    voltar_ao_menu_principal()

# faz as contas de subtração e adiciona o resultado nos grupos acima
def operacao_subtracao():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙎𝙪𝙗𝙩𝙧𝙖𝙘𝙖𝙤")
    n1 = float(input("Digite o prímeiro número da equação: "))
    n2 = float(input("Digite o segundo número da equação: "))
    resultado = n1 - n2
    exibir_texto(f"O resultado da equação de subtração é iqual a: {resultado:,.2f}")
    resultados_subtracao.append(resultado)
    voltar_ao_menu_principal()

# faz as contas de porcentagem e adiciona o resultado nos grupos acima
def operacao_porcentagem():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙋𝙤𝙧𝙘𝙚𝙣𝙩𝙖𝙜𝙚𝙢")
    n1 = float(input("Digite o número desejado: "))
    n2 = float(input("Digite a porcentagem desejada: "))
    resultado = n1 * (n2 / 100)
    exibir_texto(f"O resultado da porcentagem é iqual a: {resultado:,.2f}")
    resultados_porcentagem.append(resultado)
    voltar_ao_menu_principal()

# faz a operção de calcular o imc, e te informal qual o grau voce está, sendo ele usando if
def operacao_imc():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙄𝙈𝘾")
    altura = float(input("Digite sua altura para medição: "))
    peso = float(input("Digite seu peso para a medição: "))
    altura_ao_quadrado = altura **2
    imc = peso / altura_ao_quadrado

    if imc <= 18.5:
        exibir_texto(f"Seu IMC é de {imc:,.2f}, voçê está abaixo do normal.")
        voltar_ao_menu_principal()
    elif imc <= 24.9:
        exibir_texto(f"Seu IMC é de {imc:,.2f}, voçê esta no peso normal.")
        voltar_ao_menu_principal()
    elif imc <= 29.9:
        exibir_texto(f"Seu IMC é de {imc:,.2f}, voçê está sobrepeso")
        voltar_ao_menu_principal()
    elif imc <= 34.9:
        exibir_texto(f"Seu IMC é de {imc:,.2f}, voçê está com obesidade grau I")
        voltar_ao_menu_principal()
    elif imc <= 39.9:
        exibir_texto(f"Seu IMC é de {imc:,.2f}, voçê está com obesidade grau II")
        voltar_ao_menu_principal()
    else:
        exibir_texto(f"Seu IMC é de {imc}, voçê está com obesidade grau III")
        voltar_ao_menu_principal

# faz a operação de raiz quadrada e adiciona o resultados nos grupos acima
def operacao_raiz_quadrada():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙍𝙖𝙞𝙯 𝙌𝙪𝙖𝙙𝙧𝙖𝙙𝙖")
    n1 = float(input("Digite o numero desejado: "))
    resultado = math.sqrt(n1)
    exibir_texto(f"A Raiz Quadrada de {n1} é iqual à {resultado:,.2f}.")
    resultados_raiz_quadrada.append(resultado)
    voltar_ao_menu_principal()

# faz a operacao de potencia e adiciona nos grupoas acima
def operacao_potencia():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝙋𝙤𝙩𝙚𝙣𝙘𝙞𝙖")
    n = float(input("Digite o número desejado: "))
    potencia = float(input("Digite a Potencia desejada: "))
    resultado = n **potencia
    resultados_potencia.append(resultado)
    exibir_texto(f"O Resultado da potencia é {resultado:,.2f}")
    voltar_ao_menu_principal()

def operacao_datas():
    carregando()
    exibir_texto("𝘾𝙖𝙡𝙘𝙪𝙡𝙤 𝙙𝙚 𝘿𝙖𝙩𝙖𝙨")
    data1 = input("Digite a primeira data (dd/mm/yyyy): ")
    data2 = input("Digite a segunda data (dd/mm/yyyy): ")
    formato = "%d/%m/%Y"
    d1 = datetime.strptime(data1, formato)
    d2 = datetime.strptime(data2, formato)

    diferenca = abs((d2 - d1).days)
    exibir_texto(f"A Diferença é de {diferenca} dias")
    voltar_ao_menu_principal()

# caso coloque nas opções algo que nao seja numero, ele limpa a tela e volta ao inicio
def opcao_invalida():
    exibir_texto("𝘿𝙞𝙜𝙞𝙩𝙚 𝙪𝙢𝙖 𝙧𝙚𝙨𝙥𝙤𝙨𝙩𝙖 𝙫á𝙡𝙞𝙙𝙖!!")
    voltar_ao_menu_principal()

# lista os grupos acima de cada opereracao
def listar_contas():
    carregando()
    exibir_texto("𝙃𝙞𝙨𝙩𝙤𝙧𝙞𝙘𝙤")
    print(f"- Divições: {resultados_divisao}\n")
    print(f"- Multiplicação: {resultados_multiplicacao}\n")
    print(f"- Soma: {resultados_soma}\n")
    print(f"- Subtração: {resultados_subtracao}\n")
    print(f"- Porcentagem: {resultados_porcentagem}\n")
    print(f"- Raizes Quadradas: {resultados_raiz_quadrada}\n")
    print(f"- Potencias: {resultados_potencia}\n")
    voltar_ao_menu_principal()

# pergunta na tela inicial as opcoes possiveis para o programa usando try, usando apenas numeros
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Digite a operação desejada: "))

        if opcao_escolhida == 1:
            operacao_divisao()
        elif opcao_escolhida == 2:
            operacao_multiplicacao()
        elif opcao_escolhida == 3:
            operacao_soma()
        elif opcao_escolhida == 4:
            operacao_subtracao()
        elif opcao_escolhida == 5:
            operacao_porcentagem()
        elif opcao_escolhida == 6:
            operacao_potencia()
        elif opcao_escolhida == 7:
            operacao_raiz_quadrada()
        elif opcao_escolhida == 8:
            operacao_imc()
        elif opcao_escolhida == 9:
            operacao_datas()
        elif opcao_escolhida == 0:
            listar_contas()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# exibi na tela as opcoes abaixo do nome do programa
def exibir_opcoes():
    print("1. Divisão")
    print("2. Multiplicação")
    print("3. Soma")
    print("4. Subtração\n")
    print("5. Porcentagem")
    print("6. Potencia")
    print("7. Carcular Raiz Quadradra\n")
    print("8. Calcular IMC")
    print("9. Calcular Datas\n")
    print("0. Histórico\n")

if __name__ == "__main__":
    main()
