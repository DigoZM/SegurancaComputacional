#Giovana Pinho Garcia - 180101374
#Rodrigo Zamagno Medeiros - 170021726

import statistics
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import warnings
warnings.filterwarnings("ignore")
from unidecode import unidecode
import os

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#desconsidera = [' ', ',', '.', '(', ')', ';', '?', '!', '*', ':', '-', '_', '[', ']', '{', '}', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
TAMANHO_MAX_CHAVE = 20

inglesfreq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 
              0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 
              0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 
              0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 
              0.01974, 0.00074]

portuguesfreq = [0.14630, 0.01040, 0.03880, 0.04990, 0.12570, 0.01020, 
                 0.01300, 0.01280, 0.06180, 0.00400, 0.00020, 0.02780, 
                 0.04740, 0.05050, 0.10730, 0.02520, 0.01200, 0.06530, 
                 0.07810, 0.04340, 0.04630, 0.01670, 0.00100, 0.02100, 
                 0.00100, 0.04700]

#funcao que cifra texto
def cifrar():
    chave = input("Defina a sua chave: ")
    arq = input("O arquivo com o texto a deve ser cifrado: ")
    arquivo = open(arq,'r')

    index=0
    chave = chave.lower()
    novo_texto=''

    for texto in arquivo:
        texto = texto.lower()
        texto = unidecode(texto)
        for letra in texto:
            if letra not in alfabeto:
                novo_texto += letra
            else:
                nova_letra = (ord(letra) + ord(chave[index])%97)%123
                
                if(nova_letra < 97):
                    nova_letra += 97
                
                novo_texto += chr(nova_letra)
                index+=1
                index = index%(len(chave))

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n----------------- Texto Cifrado -----------------\n')
    print(novo_texto)
    print()
    arquivo.close()
    input("Pressione enter para retornar ao Menu")
    print()


#funcao que decifra texto
def decifrar(chave, arquivo):

    index=0
    chave = chave.lower()
    novo_texto=''

    for texto in arquivo:
        texto = texto.lower()
        texto = unidecode(texto)
        for letra in texto:
            if letra not in alfabeto:
                novo_texto += letra
            else: 
                nova_letra = (ord(letra) - ord(chave[index])) + 97
                if(nova_letra < 97):
                    nova_letra = 123 - (97 - nova_letra)

                novo_texto += chr(nova_letra)
                index+=1
                index = index%(len(chave))

    arquivo.close()
    print('\n----------------- Texto Decifrado -----------------\n')
    print(novo_texto)
    print()
    input("Pressione enter para retornar ao Menu")
    print()


def getItemAtIndexOne(x): #???
    return x[1]


def encontra_sequencias(texto):
    texto_novo = []
    dic_espacos = {}

    for i in range(len(texto)): #Tirando todos os caracteres que não são letras
        if(ord(texto[i]) >= ord('a') and ord(texto[i]) <= ord('z')):
            texto_novo += texto[i]
    #print(texto)
    #print(texto_novo)
    texto_novo = ''.join(texto_novo)
    #Checar as repetições das sequencias de 3 letras pela mensagem
    tamanho_sequencia = 3
    for inicio_sequencia in range(len(texto_novo) - tamanho_sequencia):
        letras_sequencia = texto_novo[inicio_sequencia:inicio_sequencia + tamanho_sequencia]
        #print("Procurando: ", letras_sequencia)

        for i in range(inicio_sequencia + tamanho_sequencia, len(texto_novo) - tamanho_sequencia):
            compara_sequencia = texto_novo[i: i+tamanho_sequencia]
            #print("Comparando com ", compara_sequencia)
            if (letras_sequencia == compara_sequencia): #Encontro a sequencia de letras mais de uma vez no texto
                #print("ACHEI")
                if letras_sequencia not in dic_espacos: #Primeira vez que encontrou, não esta no dicionário
                    dic_espacos[letras_sequencia] = []
                #Adicionar a distância entre as duas sequencias no dicionário
                dic_espacos[letras_sequencia].append(i - inicio_sequencia)

    #print(dic_espacos)
    return dic_espacos

def valores_possiveis_chave(espacamento):
    
    if espacamento < 2:
        return []
    
    chaves = []

    for i in range(2, TAMANHO_MAX_CHAVE+1):
        if espacamento % i == 0:
            chaves.append(i)
            chaves.append(int(espacamento/i))
        
        if 1 in chaves:
            chaves.remove(1)
    
    #print ("Espaçamento: ", espacamento, "\t|| Chaves: ", chaves)

    return list(set(chaves)) #Retorna a lista eliminando repetições
    


def tamanho_chave2(texto):
    dic_espacos = encontra_sequencias(texto)
    count_rep = {}

    seq_letras = {}
    # Pegar cada espaçamento e retornar os fatores possiveis do tamanho da chave
    for sequencia in dic_espacos:
        seq_letras[sequencia] = []
        for espacamento in dic_espacos[sequencia]:
            seq_letras[sequencia].extend(valores_possiveis_chave(espacamento))


    #print("Seq_letras: ", seq_letras)
    #checando os valores de espaçamento das sequências
    for sequencia in seq_letras:
        lista_rep = seq_letras[sequencia]
        for rep in lista_rep:
            if rep not in count_rep: #Espaçamento não apareceu ainda
                count_rep[rep] = 0
            count_rep[rep] += 1
    
    
    #print("count_rep: ", count_rep)

    count_por_rep = []

    #Seleciona apenas os valores menores que os valores possiveis
    for rep in count_rep:
        if rep <= TAMANHO_MAX_CHAVE:
            count_por_rep.append((rep, count_rep[rep]))
    
    count_por_rep.sort(key=getItemAtIndexOne, reverse=True) #ordena do que mais repete pro que menos repete

    media = 0
    for i in range(len(count_por_rep)):
        media += count_por_rep[i][1]
    teste = [sum(y) / len(y) for y in zip(*count_por_rep)]
    #print(teste)

    #print("Media: ", media/len(count_por_rep))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n----------------- Tamanhos Possiveis -----------------\n')
    for i in range(len(count_por_rep)):
        print("Tamanho possivel: ", count_por_rep[i][0], "\trepete: ", count_por_rep[i][1])
        
    max_rep = count_por_rep[0][1]
    tamanho_possivel = count_por_rep[0][0]
    for i in range(len(count_por_rep)):
        if(count_por_rep[i][1] > 0.75*max_rep):
            tamanho_possivel = count_por_rep[i][0]

    print("O tamanho provável é de: ", tamanho_possivel)
    
    
    

                
    


def tamanho_chave(texto):
    coincidencia = []
    texto_novo = []

    for i in range(len(texto)):
        if(ord(texto[i]) >= ord('a') or ord(texto[i]) <= ord('z')):
            texto_novo.append(texto[i])
   

    for i in range(1, len(texto_novo)):
        num_coincidencia = 0
        for j in range(len(texto_novo)-i):
            if texto_novo[j] == texto_novo[j+i]:
                num_coincidencia+=1
        coincidencia.append(num_coincidencia)

    media = statistics.mean(coincidencia)
    print(media)
    print(coincidencia)

    key_size=[0]

    for i in range(1, 20):
        count=0
        media_aux=0
        for j in range(i-1, (len(coincidencia)-i), i):
            media_aux += coincidencia[j+i]
            count+=1    
        
        key_size.append(media_aux/count)
    
    print(key_size)
    print(max(key_size))

def frequencia_letras(chave, idioma, texto, arq):

    lista_freq = []
    for n in range(chave):
        lista_aux = []
        for i in range(n, len(texto), chave):
            lista_aux.append(texto[i])
        lista_freq.append(lista_aux)

    lista_frequencia_porcentagem = []
    
    #print(lista_freq)

    for k in lista_freq:
        res = dict(Counter(k))
        total = len(k)
        lista_aux = []
        for letra in range(ord('a'),ord('z')+1):
            if(chr(letra) in res.keys()):
                lista_aux.append(res[chr(letra)]/total)
            else:
                lista_aux.append(0)
        lista_frequencia_porcentagem.append(lista_aux)
            
        
    #print(lista_frequencia_porcentagem)
    #fig, ax = plt.subplots()

    chave_final = ''
    
    

    for k in range(chave):
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        index = np.arange(26)
        thickness = 0.7
        f, ((ax1, ax2)) = plt.subplots(2)#, sharex='col', sharey='row')
        #fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        if(idioma == '1'):
            #portugues
            print("Portufues")
            ax1.bar(alfabeto,portuguesfreq, thickness) 

        else:
            #ingles
            print("Ingles")
            ax1.bar(alfabeto,inglesfreq, thickness) 

        
        #print(lista_frequencia_porcentagem[k])
        #ax2.bar(alfabeto,lista_frequencia_porcentagem[k], thickness)
        
        l = plt.bar(alfabeto, lista_frequencia_porcentagem[k], thickness)
        #plt.title('Decifrando Frequencia')



        class Index(object):
            ind = 0

            def next(self, event):
                self.ind += 1
                i = self.ind % len(alfabeto)
                alfabeto.insert(0, alfabeto.pop())
                lista_frequencia_porcentagem[k].insert(0, lista_frequencia_porcentagem[k].pop())
                for r1, r2 in zip(l,lista_frequencia_porcentagem[k]):
                    r1.set_height(r2)
                ax2.set_xticklabels(alfabeto)
                plt.draw()

            def prev(self, event):
                self.ind += 1
                i = self.ind % len(alfabeto)
                alfabeto.append(alfabeto.pop(0))
                
                lista_frequencia_porcentagem[k].append(lista_frequencia_porcentagem[k].pop(0))
                for r1, r2 in zip(l,lista_frequencia_porcentagem[k]):
                    r1.set_height(r2)
                ax2.set_xticklabels(alfabeto)
                plt.draw()




        callback = Index()
        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        bnext = Button(axnext, 'Next')
        bnext.on_clicked(callback.next)
        bprev = Button(axprev, 'Previous')
        bprev.on_clicked(callback.prev)

        #plt.tight_layout()
        plt.show()

        
        
        #plt.show()
        #letra = input("Digite a letra: ")

        chave_final += alfabeto[0]
    
    chave_final = ''.join(chave_final)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nChave do texto: ', chave_final)
    arquivo = open(arq, 'r')
    decifrar(chave_final, arquivo)
        


def quebrar():
    arq = input("Arquivo com texto cifrado: ")
    arquivo = open(arq, 'r')
    texto=''

    for linha in arquivo:
        linha = linha.lower()
        for caractere in linha:
            if caractere in alfabeto:
                texto += caractere
    
    texto = unidecode(texto)
    arquivo.close()
    
    #texto = texto.lower()
    print('foi')
    #tamanho_chave(texto)
    tamanho_chave2(texto)
    tamanho_chave_escolhida = input("Digite o tamanho da chave: ")
    idioma = input("Digite o idioma do texto: \n1-Português \n2-Inglês\n")
    frequencia_letras(int(tamanho_chave_escolhida), idioma, texto, arq)

def menu():
    print('\n----------------- Menu -----------------\n')
    print("1 - Cifrar uma mensagem")
    print("2 - Decifrar uma mensagem")
    print("3 - Quebrar cifra")
    print("4 - Sair")

op = 0
while op != 4:
    menu()
    op = int(input())
    if op == 1:
        cifrar()
    elif op == 2:
        chave = input("Chave do texto: ")
        arq = input("O arquivo com o texto a ser decifrado: ")
        arquivo = open(arq,'r')
        os.system('cls' if os.name == 'nt' else 'clear')
        decifrar(chave, arquivo)
    elif op == 3:
        quebrar()
    else:
        break



# Ainda falta considerar caracteres especiais (acentos etc)
# ignorar e n cifrar ou considerar so a letra ?

