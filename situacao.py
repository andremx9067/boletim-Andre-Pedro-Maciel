# Autor:Pedro Henrique De Abreu Maia
#git hub usuario: PedroMaia-10
#Papel ALuno B

def situacao(m):
    """Devolve "Aprovado" se a media for 60 ou mais;
    senao, devolve "Reprovado".
    Ex.: situacao(60) -> "Aprovado"
    """
    if m >= 60:
        return "Aprovado"
    else:
        return "Reprovado"
