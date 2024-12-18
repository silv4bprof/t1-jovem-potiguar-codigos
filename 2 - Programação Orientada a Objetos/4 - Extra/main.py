from classes import Eleitor
from classes import Voto
from datetime import datetime
from urna import UrnaEletronica

print("Eleições Python".capitalize().upper())

urna = UrnaEletronica()

while True:
    print("Bem-vindo à Urna Eletrônica")
    nome = input("Digite o seu nome: ")
    titulo_eleitor = input("Digite o numero do titulo de eleitor: ")
    print("\nCandidados Disponíveis P/ Votação")

    for candidato in urna.recuperar_candidatos():
        print(f"{candidato.get_nome()} - {candidato.get_partido()}")

    numero = int(input("\nCandidato que deseja votar para presidente: "))

    try:
        candidato = urna.recuperar_candidato(numero)
        eleitor = Eleitor(nome, titulo_eleitor)
        voto = Voto(datetime.now(), eleitor, candidato)
        urna.adiciona_voto(voto)

        sair = input("Deseja sair? (sim, nao): ")

        if sair == "sim":
            break
    except Exception as e:
        print(f"Candidato não existe.\n{e}")

print("\nVotação Encerrada")
print("----------------\n")

todos_votos = urna.listar_votos()
print("Total de Votos: ", len(todos_votos))
for voto in todos_votos:
    print(voto)

print("----------------\n")
haddad = urna.recuperar_candidato(13)
votos_haddad = urna.listar_votos(haddad)
print("Total de Votos de Fernando Haddad: ", len(votos_haddad))
for voto in votos_haddad:
    print(voto)

print("----------------\n")
bolsonaro = urna.recuperar_candidato(22)
votos_bolsonaro = urna.listar_votos(bolsonaro)
print("Total de Votos de Jair Bolsonaro: ", len(votos_bolsonaro))
for voto in votos_bolsonaro:
    print(voto)
