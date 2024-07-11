from art import logo

print(logo)
def add(n1,n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

operators = {"+":add,
             "-":substract,
             "*":multiply,
             "/":divide
             }

num1 = float(input("What's the firts number?: "))


for keys in operators:
  print(keys)

operation = input("Pick an operation from the line abover: ")
continuar = True
while continuar:
  num2 = float(input("What's the next number?: "))
  firts_answer = operators[operation](num1,num2)
  print(f"{num1} {operation} {num2} = {firts_answer}")
  pregunta = input(f"Type 'y' to continue calculating with {firts_answer},or type 'n'")
  if pregunta == 'n':
    print("Godbye!!!")
    continuar = False
  num1 = firts_answer
  
    

  