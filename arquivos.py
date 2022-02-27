import os
import pydf

# Verifica se um arquivo ou diretório existe
print(os.path.exists('dunder.py'))

print(os.path.exists('pacote'))

print(os.path.exists('principal.py'))

# Exemplos de caminhos
print(os.path.exists('subpacote/outros.py'))

# Criando arquivos
# os.mknod('arquivonovo.py')

# Criando diretório
# os.mkdir('pastanova')

# Criando arquivo pdf
pdf = pydf.generate_pdf('<h1>Meu PDF gerado com python</h1>')
with open('meu_pdf.pdf', 'wb') as f:
    f.write(pdf)
