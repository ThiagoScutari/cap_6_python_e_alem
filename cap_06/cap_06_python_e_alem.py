#------------------------------------| PROPOSTA |------------------------------------#
'''
Título:
Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar com Registro Histórico e Banco de Dados

Objetivo:
Desenvolver um sistema em Python que permita ao produtor rural ou técnico agrícola planejar o escalonamento do plantio e da colheita de cana-de-açúcar de forma otimizada, com base na área disponível e nas máquinas operacionais, registrando essas simulações em arquivos JSON e banco de dados Oracle para fins de histórico e análise.
'''

#------------------------------------| PROGRAMA |------------------------------------#
from banco import criar_tabelas, inserir_area, inserir_dimensoes, listar_areas_salvas
from datetime import datetime

#Cria o banco de dados e as tabelas
criar_tabelas()

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

#Exibe as areas cadastradas
def mostrar_areas_salvas()-> None:
    registros = listar_areas_salvas()
    if not registros:
        print("Sem registros cadastrados no banco.")
        return
    print("\nÁreas cadastradas:")
    for id_area, forma, area, data in registros:
        print(f"ID: {id_area} | Forma: {forma} | Área: {area:.2f} m² | Data: {data}")

#Calcula a area de acordo com a escolha do usuario
def calcular_area():
    print("Escolha a forma da área:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Trapézio")
    print("4 - Listar areas cadastradas")
    print("0 - Sair")

    while True:
        try:
            escolha = int(input("Digite o número da forma desejada: "))
            if escolha in [0, 1, 2, 3, 4]:
                break
            else:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue
        except ValueError:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue      
          
    match escolha:
        case 1:
            base = inserir_valor('Digite a largura do terreno em metros: ')
            return Quadrado(base)
        case 2:
            base = inserir_valor("Digite a largura do terreno em metros: ")
            altura = inserir_valor("Digite a comprimento do terreno em metros: ")
            return Retangulo(base, altura)
        case 3:
            base_maior = inserir_valor("Digite a largura maior do terreno em metros: ")
            base_menor = inserir_valor("Digite a largura menor do terreno em metros: ")
            altura = inserir_valor("Digite a comprimento do terreno em metros: ")
            return Trapezio(base_maior, base_menor, altura)
        case 4:
            mostrar_areas_salvas()
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
        area_id = inserir_area(area)
        dimensoes = {
            "lado": getattr(area, 'lado', None),
            "base": getattr(area, 'base', None),
            "altura": getattr(area, 'altura', None),
            "base_maior": getattr(area, 'base_maior', None),
            "base_menor": getattr(area, 'base_menor', None)
        }
        # Remove as dimensões com valor None
        dimensoes = {k: v for k, v in dimensoes.items() if v is not None}
        inserir_dimensoes(area_id, dimensoes)
        exibir_area(area)
        continuar = input("Deseja calcular outra área? (S/N): ").strip().upper()
        if continuar == 'N':
            print("Encerrando...")
            break
        elif continuar == 'S':
            continue
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

