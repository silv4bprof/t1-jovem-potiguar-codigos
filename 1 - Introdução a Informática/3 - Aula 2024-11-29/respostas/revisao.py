# condicionais

numero = 10

fato = 10 < 0
fato2 = 10 == '10'

if 10 < 0:  # True
    print("Entrou no if")
    print("Esse print() está no escopo")

if (10 == '10'):
    print("Entrou no segundo if")
else:
    print("Entrou no else")


valor_verdade = True  # verdadeiro
valor_mentira = False  # false

# and
if valor_verdade and valor_mentira: # não entra
    print("[and] Entrou no primeiro if")
if valor_verdade and valor_verdade: # entra
    print("[and] Entrou no segundo if")
if valor_mentira and valor_mentira: # não entra
    print("[and] Entrou no terceiro if")

# or
if valor_mentira or valor_verdade or valor_mentira: # entra
    print("[or] Entrou no primeiro if")
if valor_verdade or valor_verdade: # entra
    print("[or] Entrou no segundo if")
if valor_mentira or valor_mentira: # não entra
    print("[or] Entrou no terceiro if")