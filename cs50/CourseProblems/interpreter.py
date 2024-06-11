def main():
  input_string = input("Enter a calculation (e.g., 2.5 + 3.7): ")
  num1, operator, num2 = input_string.split()
  num1 = float(num1)
  num2 = float(num2)

  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    result = "Invalid operator"

  print("Result:", result)

main()