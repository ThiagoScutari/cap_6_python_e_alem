#------------------------------------| PROPOSTA |------------------------------------#
'''
Título:
Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar com Registro Histórico e Banco de Dados

Objetivo:
Desenvolver um sistema em Python que permita ao produtor rural ou técnico agrícola planejar o escalonamento do plantio e da colheita de cana-de-açúcar de forma otimizada, com base na área disponível e nas máquinas operacionais, registrando essas simulações em arquivos JSON e banco de dados Oracle para fins de histórico e análise.
'''

#------------------------------------| PROGRAMA |------------------------------------#
from banco import criar_tabelas, inserir_area, inserir_dimensoes, mostrar_areas_salvas,visualizar_dimensoes, realizar_escalonamento, exportar_simulacao, exportar_todas_simulacoes

#Cria o banco de dados e as tabelas
criar_tabelas()

print("-" * 90)
print("Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar")
print("-" * 90)

#------------------------------------| CLASSES |------------------------------------#
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

#------------------------------------| FUNÇÕES |------------------------------------#
#Verifica valor digitado pelo usuario
def inserir_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

#Insere nova area no banco de dados
def cadastrar_nova_area():
    print("Escolha a forma da área:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Trapézio")
    print("0 - Sair")
    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha in [0, 1, 2, 3]:
                break
            else:
                print(f'Opção inválida: {escolha}. Tente novamente.')
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    match escolha:
        case 0:
            print("Saindo...")
            return
        case 1:
            area = Quadrado(inserir_valor('Digite a largura do terreno em metros: '))
        case 2:
            base = inserir_valor("Digite a largura do terreno em metros: ")
            altura = inserir_valor("Digite o comprimento do terreno em metros: ")
            area = Retangulo(base, altura)
        case 3:
            base_maior = inserir_valor("Digite a largura maior do terreno em metros: ")
            base_menor = inserir_valor("Digite a largura menor do terreno em metros: ")
            altura = inserir_valor("Digite o comprimento do terreno em metros: ")
            area = Trapezio(base_maior, base_menor, altura)

    area_id = inserir_area(area)

    dimensoes = {
        "lado": getattr(area, 'lado', None),
        "base": getattr(area, 'base', None),
        "altura": getattr(area, 'altura', None),
        "base_maior": getattr(area, 'base_maior', None),
        "base_menor": getattr(area, 'base_menor', None)
    }
    dimensoes = {k: v for k, v in dimensoes.items() if v is not None}

    inserir_dimensoes(area_id, dimensoes)
    exibir_area(area)

#Exibe area calculada
def exibir_area(area: Area) -> None:
    print(f"A área do terreno é: {area.calcular_area()} m²")

#------------------------------------| MENU PRINCIPAL |------------------------------------#

#Calcula a area de acordo com a escolha do usuario
def menu_principal():
    print("\n" + "="*60)
    print("MENU PRINCIPAL")
    print("="*60)
    print("1 - Cadastrar nova área")
    print("2 - Listar áreas cadastradas")
    print("3 - Visualizar dimensões de uma área")
    print("4 - Calcular escalonamento de plantio e colheita")
    print("5 - Exportar simulação em JSON e CSV")
    print("6 - Exportar todas as simulações em JSON e CSV")
    print("0 - Sair")
    print("="*60)
    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha in [0, 1, 2, 3, 4, 5, 6]:
                break
            else:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue
        except ValueError:
                print(f'Opção inválida: {escolha}. Tente novamente.')
                continue
    match escolha:
        case 1:
            cadastrar_nova_area()
        case 2:
            mostrar_areas_salvas()
        case 3:
            visualizar_dimensoes()
        case 4:
            realizar_escalonamento()
        case 5:
            try:
                id_area = int(input("Digite o ID da área que deseja exportar: "))
                exportar_simulacao(id_area)
            except ValueError:
                print("ID inválido.")
        case 6:
            exportar_todas_simulacoes()
        case 0:
            print("Encerrando...")
            return escolha
        case _:
            print("Opção inválida. Tente novamente.")
            
def main():
    while True:
        menu_principal()
        if menu_principal() == 0:
            break
        continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()
        if continuar == 'N':
            print("Encerrando...")
            break
        elif continuar == 'S':
            continue
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

