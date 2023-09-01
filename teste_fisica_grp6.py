from time import sleep
import math

titulo = """
-------------------------------------
|  Ondas Eletromagéticas com Python |
-------------------------------------"""
nomes = """
-----------
| Autores |
-----------
GUSTAVO DIAS VICENTIN
LUCAS GABRIEL X DOS SANTOS
IGOR VICENTE CUTALO""".title()
intro = """
--------------------------------
|  Introdução e Funcionamento  |
--------------------------------
Este programa se trata de uma calculadora simples para cálculos de ondas eletromagnéticas.
O usuário pode escolher qual a grandeza física conhecida e, assim que passar suas informações, será retornado valores pertinentes à mesma.

-------------------------------------------------
|  Conceitos básicos de ondas eletromagnéticas  |
-------------------------------------------------
TODO
--------------
| Limitações |
--------------
TODO

"""
menu = """--------
| Menu |
--------
1. Em
2. Bm
3. I
4. f
5. λ (lambda)
6. k
7. ω (omega)
0. Sair
Escolha uma operação (através de seu número ou nome): """

unidades = {"G": 10 ** (9),
            "M": 10 ** (6),
            "k": 10 ** (3),
            "m": 10 ** (-3),
            "u": 10 ** (-6),
            "µ": 10 ** (-6),
            "n": 10 ** (-9)}
c = 3 * (10 ** 8) # m/s
u0 = 4 * math.pi * 10 ** (-7) # Wb * A ** (-1) * m ** (-1)

sleep_time = 0
def valida_input_unidade(valor: "list | str"):
    if type(valor) == str:
        valor = valor.strip()
        valor = valor.split(" ")
    valor = [caractere for caractere in valor if caractere != ""]
    contador_decimal = 0
    if valor[0].replace(".","",1).isdigit():
        if len(valor) > 1:
            if valor[1] in unidades.keys():
                return float(valor[0]) * unidades[valor[1]]
            else:
                print("Unidade invalida")
                return False
        else:
            return float(valor[0])
    else:
        for i in range(len(valor[0])):
            if valor[0][i] == ".":
                if contador_decimal == 0:
                    contador_decimal += 1
                else:
                    print("Valor invalido")
                    return False
            if valor[0][i].isnumeric() or (valor[0][i] == "."):
                continue
            elif not valor[0][i].isnumeric() and valor[0][i] != "." and valor[0][i] in unidades.keys():
                return valida_input_unidade(valor[0][:i] + " " + valor[0][i:i + 1])
            else:
                print("Valor invalido")
                return False

def em_amplitude_campo_eletrico():
    print("Digite a Amplitude do Campo Elétrico (Em) [V/m]")
    print("Unidades aceitas:", ", ".join(unidades.keys()), "ou nenhuma.")
    em = input("Em: ")
    em = valida_input_unidade(em)
    if em == False:
        return
    bm = em/c
    i = (em**2)/(2*u0*c)
    print(f"Em: {em:.2e}[V/m]\nBm: {bm:.2e} [T]\nI: {i:.2e}[W/m^2]")
    return

def bm_amplitude_campo_magnetico():
    print("Digite a Amplitude do Campo Magnético (Bm) [T]")
    print("Unidades aceitas:", ", ".join(unidades.keys()), "ou nenhuma.")
    bm = input("Bm: ")
    bm = valida_input_unidade(bm)
    if bm == False:
        return
    em = bm * c
    i = (em**2)/(2*u0*c)
    print(f"Bm: {bm:.2e} [T]\nEm: {em:.2e} [V/m]\nI: {i:.2e} [W/m^2]")
    return

def i_intensidade():
    print("Digite a Intensidade da onda eletromagnética (I) [W/m^2]")
    print("Unidades aceitas:", ", ".join(unidades.keys()), "ou nenhuma.")
    i = input("I: ")
    i = valida_input_unidade(i)
    if i == False:
        return
    em = math.sqrt(i * 2 * u0 * c) # VAI DAR RUIM COM NEGATIVO
    bm = em/c
    print(f"I: {i:.2e} [W/m^2]\nEm: {em:.2e} [V/m]\nBm: {bm:.2e} [T]")
    return

def f_frequencia():
    print("Digite a Frequência da onda eletromagnética (f) [Hz]")
    print("Unidades aceitas:", ", ".join(unidades.keys()), "ou nenhuma.")
    f = input("f: ")
    f = valida_input_unidade(f)
    if f == False:
        return
    lambida = c / f
    k = 2 * math.pi / lambida
    omega = 2 * math.pi * f
    print(f"f: {f:.2e}[Hz]\nλ: {lambida:.2e} [m]\nk: {k:.2e} [rad/m]\nω: {omega:.2e} [rad/s]\n")
    return

def lambda_comprimento_onda():
    pass
def k_numero_onda():
    pass
def omega_freq_angular():
    pass

calculos_possiveis = {"Em": em_amplitude_campo_eletrico, 
                      "Bm": bm_amplitude_campo_magnetico, 
                      "I": i_intensidade, 
                      "f": f_frequencia, 
                      "λ": lambda_comprimento_onda, 
                      "lambda": lambda_comprimento_onda, 
                      "k": k_numero_onda, 
                      "ω": omega_freq_angular, 
                      "omega": omega_freq_angular}
calculos_possiveis_list = [func for func in calculos_possiveis.values()]

def main():
    print(titulo)
    print(nomes)
    sleep(sleep_time)
    print(intro)
    sleep(sleep_time)
    while True:
        print(menu)
        escolha = input()
        if escolha.isnumeric():
            if int(escolha) == 0:
                return
            if int(escolha) >= 1 and int(escolha) <= 7:
                print("")
                calculos_possiveis_list[int(escolha) - 1]()
                sleep(1)
                print("")
            else:
                print("Operação inválida\n")
        elif escolha in calculos_possiveis.keys():
            print("")
            calculos_possiveis[escolha]()
            sleep(sleep_time)
            print("")
        else:
            print("Operação inválida\n")
main()