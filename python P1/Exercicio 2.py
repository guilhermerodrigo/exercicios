produto = float(input("Digite o valor do seu produto R$: "))

if produto<=50:
    produtocomreajuste = produto + (produto * 0.40)
    print("Seu produto com aumento R$ ",produtocomreajuste)

if produto>50 and produto<=100:
    produtocomreajuste = produto + (produto * 0.10)
    print("Seu produto com aumento R$ ",produtocomreajuste)

if produto>100:
    produtocomreajuste = produto + (produto * 0.15)
    print("Seu produto com aumento R$ ",produtocomreajuste)

if produtocomreajuste<=80:
    print("Produto barato")

if produtocomreajuste>80 and produtocomreajuste<=120:
    print("Produto normal")
    
if produtocomreajuste>120 and produtocomreajuste<=200:
    print("Produto caro")

if produtocomreajuste>200:
    print("Muito caro")




