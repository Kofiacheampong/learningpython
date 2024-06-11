def main():
  user_input = input('What is the mass (KG)?')
  if "KG" in user_input.upper():
    x = user_input.replace("KG", "")
  else:
    x = user_input
  x = int(x)
  energy = x * 30000000
  print(f'{energy} Joules')

main()