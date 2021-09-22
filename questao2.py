def recebe_arquivo (nome_do_arquivo):
    entradaarq = open(nome_do_arquivo,'r')
    totalCompetidores =int(entradaarq.readline())
    competidoresLargada = entradaarq.readline().split(sep=",")
    competidoresChegada= entradaarq.readline().split(sep=",")
    primeiroIndiceDiferente = None
    
    if totalCompetidores < 2 or totalCompetidores > 24:
        print('Total de competidores não compativel')
        return

    if (
        (len(competidoresLargada) != totalCompetidores) or
        (len(competidoresChegada) != totalCompetidores)):
        print('Total de competidores não compativel')
        return
        
    for index in range(0, len(competidoresChegada)):	
        if (competidoresLargada[index] != competidoresChegada[index]):
            primeiroIndiceDiferente = {
                'index': index,
       	        'competidor': competidoresChegada[index]
            }
            break

    if primeiroIndiceDiferente:
        print(competidoresLargada.index(primeiroIndiceDiferente.get('competidor')) - primeiroIndiceDiferente.get('index'))
        return competidoresLargada.index(primeiroIndiceDiferente.get('competidor')) - primeiroIndiceDiferente.get('index')
    

recebe_arquivo("entradaexe2.txt")