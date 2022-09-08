import lib.RSAKey as RSA


def main():
  chaves = RSA.gerarRSA(1, 1024)
  print("Fim\n")


if __name__ == '__main__': 
    main()