def recebe_arquivo(nome_do_arquivo):  
    entradaarq = open(nome_do_arquivo,'r')
    entradas = entradaarq.readline().split(sep=",")
    for entrada in entradas:
        x = 0 
        andar_atual = 0
        teste = True
        while teste == True:
            if "4" in str(x)  or "13" in str(x):
                andar_atual = andar_atual - 1
            andar_atual +=1
            x +=1
            if andar_atual == int(entrada):
                while "13" in  str(x):
                    x = x + 1
                while "4" in  str(x):
                    x = x + 1    
                teste = False
                print(x)                       
recebe_arquivo("entradaexe1.txt")