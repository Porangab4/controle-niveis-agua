from colorama import Fore, Style, init

init()

niveis = ["Muito baixo", "Baixo", "Médio", "Alto", "Muito alto"]

def definir_cor(parametro):
    if parametro == "Muito baixo":
        return Fore.RED
    elif parametro == "Baixo":
        return Fore.YELLOW
    elif parametro == "Médio":
        return Fore.GREEN
    elif parametro == "Alto":
        return Fore.CYAN
    elif parametro == "Muito alto":
        return Fore.BLUE

for nivel in niveis:
    cor = definir_cor(nivel)
    print(f"{cor}{nivel}{Style.RESET_ALL}")