# Lista de vendas brutas dos vendedores
vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]

# Lista para armazenar o contagem de vendedores em cada faixa salarial
contadores = [0] * 10

# Calcula o salário de cada vendedor e atualiza os contadores
for venda in vendas:
    salario = 200 + 0.9 * venda
    indice = int((salario - 200) // 100)
    if indice >= 0 and indice <= 9:
        contadores[indice] += 1
    else:
        contadores[-1] += 1
        
# Imprime os resultados
print("$200 - $299:", contadores[0])
print("$300 - $399:", contadores[1])
print("$400 - $499:", contadores[2])
print("$500 - $599:", contadores[3])
print("$600 - $699:", contadores[4])
print("$700 - $799:", contadores[5])
print("$800 - $899:", contadores[6])
print("$900 - $999:", contadores[7])
print("$1000 em diante:", contadores[8])    
