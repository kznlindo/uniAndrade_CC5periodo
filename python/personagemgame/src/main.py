import sys
import os

# Adiciona a pasta pai (raiz do projeto) ao caminho
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.personagem import PersonagemGame

# Criando personagens
personagem1 = PersonagemGame("Shelly", 3600, 500, 2.5)
personagem1.inventario.append("Poção de Vida")

personagem2 = PersonagemGame("Colt", 2800, 600, 3.2)
personagem2.inventario.extend(["Revólver", "Coletor de Energia"])

# Exibindo dados e ações
print(personagem1.mostrar_dados())
print(personagem1.atacar())
print(personagem1.usar_super())

print("\n--------------------------\n")

print(personagem2.mostrar_dados())
print(personagem2.atacar())
print(personagem2.usar_super())
