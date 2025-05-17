def math_table_recursive(n, i=1):
    """
    Solicite um número e exiba sua tabuada de 1 a 10.
    """
    if i > 10:
        return
    print(f"{n} x {i} = {n * i}")
    math_table_recursive(n, i + 1)

def math_table_with_while(n):
    """
    Solicite um número e exiba sua tabuada de 1 a 10.
    """
    while n <= 10:
      print(f"Tabuada do {n}:")
      i = 1
      while i <= 10:
          print(f"{n} x {i} = {n * i}")
          i += 1
      break

def math_table_with_for(n):
    """
    Solicite um número e exiba sua tabuada de 1 a 10.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Digite um número entre 1 e 10: "))
if n < 1 or n > 10:
    print("Número inválido. Tente novamente.")
else:
  # math_table_recursive(n)
  # math_table_with_while(n)
  math_table_with_for(n)