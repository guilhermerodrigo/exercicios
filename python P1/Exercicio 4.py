x = float(input("Digite o valor da medida X: "))
y = float(input("Digite o valor da medida Y: "))
z = float(input("Digite o valor da medida Z: "))


if x==y and y==z :
   print("Triangulo equilatero.")
if x!=y and  x!=z and y!=z:
   print("Triangulo escaleno.")   
elif x!=y or y==z and z==x:
    print("Triangulo isosceles.")
elif y!=z or x==y and z==x:
   print("Triangulo isosceles.")
elif z!=x or y==z and x==y: 
   print("Triangulo isosceles.")
else:
    print("Triangulo inexistente.")


 



