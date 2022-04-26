# Programa de leitura e manipulação de dados de um arquivo csv.

dataset = open('salarios.csv', 'r')
dataframe = dataset.read()
lines = dataframe.split('\n')

columns = []

for item in lines:
    lines_split = item.split(',')
    columns.append(lines_split)

dataset.close()

print(columns[:10])

# fim do programa