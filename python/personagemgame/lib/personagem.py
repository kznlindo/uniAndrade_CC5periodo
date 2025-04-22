class PersonagemGame:
    def __init__(self, nome, vida, poder, velocidade):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.velocidade = velocidade
        self.inventario = []

    def atacar(self):
        return f"{self.nome} atacou causando {self.poder} de dano!"

    def usar_super(self):
        return f"{self.nome} usou sua Super habilidade!"

    def mostrar_dados(self):
        return (f"Nome: {self.nome}\n"
                f"Vida: {self.vida}\n"
                f"Poder: {self.poder}\n"
                f"Velocidade: {self.velocidade}\n"
                f"Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}\n")
