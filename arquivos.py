import os

# Verifica se um arquivo ou diretório existe
print(os.path.exists('dunder.py'))

print(os.path.exists('pacote'))

print(os.path.exists('principal.py'))

# Exemplos de caminhos
print(os.path.exists('subpacote/outros.py'))

# Criando arquivos
#os.mknod('arquivonovo.py')

# Criando diretório
os.mkdir('pastanova')
