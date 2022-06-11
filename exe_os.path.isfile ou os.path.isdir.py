# Exercício que retona se um objeto dentro do diretorio atual é um arquivo ou uma pasta.

import os
import os.path

for item in os.listdir('.'):
	if os.path.isfile(item):
		print(f'{item} é um arquivo.')
	elif os.path.isdir(item):
		print(f'{item} é uma pasta')

# fim do programa