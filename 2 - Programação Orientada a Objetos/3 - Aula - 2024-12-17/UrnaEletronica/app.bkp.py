# from classes import Eleitor, Partido [...] Urna

from classes import Eleitor
from classes import Partido
from classes import Candidato
from classes import Voto
from classes import Urna

if __name__ == "__main__":
    print("\nPartido(s)")
    # criando uma instância
    pt = Partido("Partido dos Trabalhadores", 13)
    pl = Partido("Partido Liberal", 22)
    pt.set_cnpj("15.555.123/0001-13")
    pl.set_cnpj("52.854.789/0001-22")

    print("\nCandidatos(as)")
    candidato1 = Candidato("Manoel Tavares", "12345678998", pt, 13333)
    candidato2 = Candidato("Josefina Mendes", "78965412332", pl, 22222)

    print("\nEleitor(es)")
    eleitor1 = Eleitor("Manoel Medeiros", "85245696558", 78954655)
    eleitor2 = Eleitor("João da Silva", "85245696558", 78954655)

    print("\nVotação")
    urna = Urna()

    # adicionar um voto
    voto1 = Voto(eleitor1, candidato2)
    voto2 = Voto(eleitor2, candidato1)
    voto3 = Voto(eleitor2, candidato1)
    voto4 = Voto(eleitor2, candidato1)

    urna.adicionar_voto(voto1)
    urna.adicionar_voto(voto2)
    urna.adicionar_voto(voto3)
    urna.adicionar_voto(voto4)

    urna.exibe_votos()
