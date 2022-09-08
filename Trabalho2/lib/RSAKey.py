import secrets
import random

def testeMillerRabin(n, tentativas):
  #Utiliza o teorema de miller rabin para verificar se a chave é primo ou não
  max_i = 20


  if(n % 2 == 0):
    return False
  
  #Primeiro passo do algoritmo
  num = n-1
  k = 0
  while(num % pow(2, (k+1)) == 0):
    k +=1
  m = int(num//(pow(2, k)))
  #print(num, " = 2^(",k,")*",m)

  for i in range(tentativas):
    possivel_primo = False
    #Segundo passo, definir a
    a = random.randint(2, n-1)
    #print("\n\na: ", a)

    #terceiro passo, calcular b e comparar
    b = pow(a, m, n) #Base, expoente e módulo
    #print("b: ", b)
    if (b == 1):
      return False
    if (b == n-1):
      continue
    count = 1

    while(b != 1 and b != -1):
      count += 1
      b = pow(b, 2, n)
      #print("b: ", b)
      if (b == 1):
        return False
      if (b == n-1):
        possivel_primo = True
        break
      if(count == max_i):
        break

    if(possivel_primo):
      continue
    return False
    
  return True






def gerarRSA(numero_chaves, tamanho_chave):

  chaves = []
  for i in range(numero_chaves):
    primo = False
    while primo is False:
      possivel_chave = secrets.randbits(tamanho_chave)
      #print(possivel_chave)
      primo = testeMillerRabin(possivel_chave, 5)
      if(primo):
        chaves.append(possivel_chave)
  print(chaves)

