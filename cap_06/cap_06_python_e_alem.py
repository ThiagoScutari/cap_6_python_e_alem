#------------------------------------| PROPOSTA |------------------------------------#
'''
Título:
Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar com Registro Histórico e Banco de Dados

Objetivo:
Desenvolver um sistema em Python que permita ao produtor rural ou técnico agrícola planejar o escalonamento do plantio e da colheita de cana-de-açúcar de forma otimizada, com base na área disponível e nas máquinas operacionais, registrando essas simulações em arquivos JSON e banco de dados Oracle para fins de histórico e análise.
'''

#------------------------------------| PROGRAMA |------------------------------------#
print("-" * 90)
print("Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar")
print("-" * 90)

#Classe para instancias areas
class Area:
    def __init__(self, forma) -> None:
        self.forma = forma

    def calcular_area(self) -> float:
        raise NotImplementedError("Implemente esse método nas subclasses.")

#Classe para calcular area quadrada
class Quadrado(Area):
    def __init__(self, lado) -> None:
        super().__init__("Quadrado")
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

#Classe para calcular area retangular
class Retangulo(Area):
    def __init__(self, base, altura) -> None:
        super().__init__("Retângulo")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

#Classe para calcular area trapézio
class Trapezio(Area):
    def __init__(self, base_maior, base_menor, altura) -> None:
        super().__init__("Trapézio")
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self) -> float:
        return ((self.base_maior + self.base_menor) * self.altura) / 2

#Verifica valor digitado pelo usuario
def inserir_valor(mensagem) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

#Exibe area calculada
def exibir_area(area: Area) -> None:
    print(f"A área do terreno é: {area.calcular_area()} m²")

#Calcula a area de acordo com a escolha do usuario
def calcular_area():
    print("Escolha a forma da área:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Trapézio")
    print("0 - Sair")

    while True:
        try:
            escolha = int(input("Digite o número da forma desejada: "))
            if escolha in [0, 1, 2, 3]:
                break
            else:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue
        except ValueError:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue      
          
    match escolha:
        case 1:
            lado = inserir_valor('Digite a largura do terreno em metros: ')
            return Quadrado(lado)
        case 2:
            base = inserir_valor("Digite a largura do terreno em metros: ")
            altura = inserir_valor("Digite a comprimento do terreno em metros: ")
            return Retangulo(base, altura)
        case 3:
            base_menor = inserir_valor("Digite a largura menor do terreno em metros: ")
            base_maior = inserir_valor("Digite a largura maior do terreno em metros: ")
            altura = inserir_valor("Digite a comprimento do terreno em metros: ")
            return Trapezio(base_maior, base_menor, altura)
        case 0:
            print("Saindo...")
            return None
        case _:
            print("Opção inválida.")
            return None

def main():
    while True:
        area = calcular_area()
        if area is None:
            break
        exibir_area(area)
        try:
            continuar = input("Deseja calcular outra área? (S/N): ").strip().upper()
            if continuar not in ['S', 'N']:
                raise ValueError("Opção inválida.")
            if continuar == 'N':
                print("Saindo...")
                break
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue
if __name__ == "__main__":
    main()

