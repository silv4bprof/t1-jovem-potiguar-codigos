# from classes import Eleitor, Partido [...] Urna

from classes import Eleitor
from classes import Partido
from classes import Candidato
from classes import Voto
from classes import Urna
from classes import Pleito


def menu() -> int:
    print("\nUrna Eletrônica [Python]\n")
    print("1 - Listar os Candidadtos")
    print("2 - Votar")
    print("0 - Sair")
    opcao = int(input("\nOpção: "))
    return opcao


def carga_inicial() -> Pleito:
    pleito = Pleito()
    pt = Partido("Partido dos Trabalhadores", "PT", 13)
    pl = Partido("Partido Liberal", "PL", 22)
    psdb = Partido("Partido da Social Democracia Brasileira", "PSDB", 45)
    pt.set_cnpj("15.555.123/0001-13")
    pl.set_cnpj("52.854.789/0001-22")
    psdb.set_cnpj("46.789.852/0001-45")
    candidato1 = Candidato("Manoel Tavares", "12345678998", pt, 13333)
    candidato2 = Candidato("Josefina Mendes", "78965412332", pl, 22222)
    candidato3 = Candidato("Marcos Araújo", "04855632558", psdb, 45555)
    pleito.adicionar_candidato(candidato1)
    pleito.adicionar_candidato(candidato2)
    pleito.adicionar_candidato(candidato3)
    return pleito


if __name__ == "__main__":
    """
    1. Digitar o Título
    [vai pra urna]
    2. Lista candidatos disponíveis
    3. Escolher o candidato
    3. Confirma o voto (enter)
    """

    # Carga Inicial / Initial Load
    pleito = carga_inicial()

    while True:
        opcao = menu()

        if opcao == 1:
            print("\nListando os Candidatos")
            pleito.exibir_candidatos()
        elif opcao == 2:
            print("\nCabine de Votação")
        elif opcao == 0:
            print("Saindo ...")
            break
        else:
            print("Opção inválida.")
