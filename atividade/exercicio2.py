import random

def discover_password(guess, password):
  attempts = 0
  while guess != password:
    print("Senha incorreta.", end=" ")
    if guess < password:
      print("A senha é maior.")
    else:
      print("A senha é menor.")
    guess = int(input("Digite seu palpite: "))
    attempts += 1
  print(f"Acesso permitido após {attempts} tentativas.")

      
guess = int(input("Digite seu senha: "))
password = random.randint(100, 999)
discover_password(guess, password)
  