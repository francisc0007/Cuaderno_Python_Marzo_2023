# Practica While

while True:
    x=input("Enter a number to count to: ")# voy a ingresar un numero
    if x == 'q' or x== 'quit': # si digiro q o quit se terminara el while
        break
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
    
    # el programa no funciona por la identacion , esta mal identado desde la x=int(x)