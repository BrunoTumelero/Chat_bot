import pandas as pd
import xlrd

padaria = pd.read_excel('pao-pra-ja.xlsx') 
print(padaria)

produtos = ['Leite', 'Café',  'Pão', 'Mortadela', 'Suco', 'Manteiga']
leite, cafe, pao, mortadela, suco, manteiga = 0, 0, 0, 0, 0, 0

print('\n')

vendas = []
for cliente in padaria.index:
  consumo = []
  for produto in produtos:
      if padaria[produto][cliente] == 'sim':
        consumo.append(produto)

        if produto == 'Leite':
          leite += 1
        elif produto == 'Café':
          cafe += 1
        elif produto == 'Pão':
          pao += 1
        elif produto == 'Mortadela':
          mortadela += 1
        elif produto == 'Suco':
          suco += 1
        elif produto == 'Manteiga':
          manteiga += 1
  vendas += [consumo] 
# Análise por linha (quais produtos cada cliente consumiu)
  print('Consumidor: {} → Produtos: {}'.format(padaria['N'][cliente], consumo))
print('\n')
# Análise por coluna (quantos clientes consumiram determinado produto)
print('Total de compras do produto:\nLeite: {}\nCafé: {}\nPão: {}\nMortadela: {}\nSuco: {}\nManteiga: {}\n'
  .format(leite, cafe, pao, mortadela, suco, manteiga))

print('Vendas por cliente: {}'.format(vendas))

# Frequência de compra de cada ítem: Análise de coluna(ordem dos clientes que compraram o produto)

# Leite: 0,1,0,1,0,0,0,0,1,0
# Café: 0,0,1,0,1,0,0,0,0,1
# Pão: 0,1,1,0,1,1,0,0,1,1
# Mortadela: 0,1,1,0,0,1,1,0,0,0
# Suco: 1,1,0,1,0,0,0,1,0,0
# Manteiga: 0,0,0,0,1,0,0,1,1,1

# Produtos que podem ser comprados juntos: Análise de frequência de combinação entre produtos

# Leite, Pão, Mortadela, Suco →[ Leite e Pão¹ ], [ Pão e Mortadela¹ ]
# Café, Pão, Mortadela → [ Café e Pão¹ ], [ Pão e Mortadela² ]
# Leite, Suco
# Café, Pão, Manteiga → [ Café e Pão² ], [ Pão e Manteiga¹ ] 
# Pão, Mortadela → [ Pão e Mortadela³ ]
# Suco, Manteiga
# Leite, Pão, Manteiga → [ Leite e Pão² ], [ Pão e Manteiga² ]
# Café, Pão, Manteiga → [ Café e Pão³ ], [ Pão e Manteiga³ ]

# Ocorrências das combinações:
# Leite e Pão: 2
# Café e Pão: 3
# Pão e Mortadela: 3
# Pão e Manteiga: 3

# Produtos que SEMPRE são comprados juntos: Análise de frequência de combinação entre produtos (produtos com 100% de combinações entre si)

# Leite e Pão
# Café e Pão

# Produtos que NUNCA são comprados juntos: Análise de frequência de combinação entre produtos (produtos com 0% combinações entre si)

# Suco e Café
# Mortadela e Manteiga