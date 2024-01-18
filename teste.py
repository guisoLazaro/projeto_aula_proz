nome = input("Digite o nome: ")
preco = float(input("Digite o preco: "))
if(preco < 50.00):
    print("Preço baixo")
elif((preco >= 50.00) and (preco <= 100.00)):
    print("Preço médio")
else:
    print("Preço alto")