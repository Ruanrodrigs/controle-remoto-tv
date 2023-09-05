from funcionalidades import *
from controleRemoto import *

# Crie uma instância de Televisor
tv = Televisor('SONY', 'SONY-123')

# Crie uma instância de ControleRemoto passando a instância da TV
controle = ControleRemoto(tv)

# Use o controle remoto para trocar de canal e sintonizar canal
controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

# Imprima o canal atual da TV
print(tv.canal_atual)
