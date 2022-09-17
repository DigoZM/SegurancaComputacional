import lib.Chave as RSA


def main():
  chaves = RSA.gerar_chave_RSA(1024)
  print("Chaves: ")
  print("Publica: ", chaves[0])
  print("Privada: ", chaves[1])
  print("Fim\n")


if __name__ == '__main__': 
    main()