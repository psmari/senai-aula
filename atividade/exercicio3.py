from datetime import datetime

def celsius_to_fahrenheit(celsius):
  return (celsius * 1.8) + 32

def calc_age(birth_year):
  current_year = datetime.now().year
  return current_year - birth_year

def interactive_menu(option):
  while option != 3:
    print("Menu:")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Calcular idade")
    print("3. Sair")
    option = int(input("Escolha uma opção: "))
    
    print()
    
    if option == 1:
      temperature = float(input("Digite a temperatura em Celsius: "))
      print(f"A temperatura em Fahrenheit é: {celsius_to_fahrenheit(temperature)}")
    elif option == 2:
      birth_year = int(input("Digite o ano de nascimento: "))
      print(f"Sua idade é: {calc_age(birth_year)} anos")
    else:
      print("Opção inválida. Tente novamente.")
    print()
  print("Até logo!")
  
interactive_menu(0)