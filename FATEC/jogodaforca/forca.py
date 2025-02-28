import random
import requests

class Forca:
    "Jogo de forca feito em python"

    # Sorteia uma palavra
    def palavra(self):
        url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
        response = requests.get(url)
        palavras = response.text.splitlines()
        self.palavra = random.choice(palavras)
        
    # Define como será a string oculta no início do jogo
    def palavra_oculta(self):
        self.resposta = ""
        # O x começará do 0
        for x in range(len(self.palavra)):
            self.resposta += "_"

    # Inicio do jogo
    def inicio_jogo(self):
        self.erros = 0
        self.victory = False
        self.lista_letras = []
        self.desing = [
    """
      ------
      |    |
      |
      |
      |
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |
      |
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    -----    
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    -----    
    """
]
        self.palavra()
        self.palavra_oculta()
        print("Bem vindo ao jogo da forca!")
        print("A palavra tem ",len(self.palavra)," letras")
        
    #Roda o código
    def run(self):
        self.inicio_jogo()

        while self.erros < 7 and self.victory == False:
            self.layout()
            self.escreve_resposta()
            self.chuta_letra()
            self.escreve_erros()
            self.vitoria()

        self.final_jogo()

    
    # Código que escreve a resposta até onde o usuário acertou
    def escreve_resposta(self):
        for x in self.resposta:
            print (x,end=" ")




    # Função que detecta se uma letra existe na palavra
    def chuta_letra(self):
        letra = input("\nDigite uma letra: ")

        # Verifica se o caractere digitado tem mais de uma letra
        if len(letra) > 1:
            print("Digite apenas uma letra!")
            return  # Retorna, para que o código abaixo não seja executado se a entrada for inválida
    
        # Verifica se a letra já foi chutada
        if letra in self.lista_letras:
            print("Esta letra já foi!")
            return
    
        # Se a letra existe na palavra
        if letra in self.palavra:
            acerto = True
        else:
            acerto = False

        # O que fazer caso a letra exista na palavra
        if acerto:
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.resposta = self.resposta[:i] + letra + self.resposta[i + 1:]
        else:
            self.erros += 1

        # Adiciona a letra chutada à lista de letras já tentadas
        self.lista_letras.append(letra)

        

            
    #Função que escreve na tela a quantidade de erros do jogador
    def escreve_erros(self):
        print("Quantidade de erros: ",self.erros)

    def vitoria(self):
        if self.resposta==self.palavra:
            self.victory=True

    def final_jogo(self):
        if self.erros == 7:
            print("Você perdeu! A palavra era: ",self.palavra)
        else:
            print("Você venceu! A palavra era: ",self.palavra)
        print("Fim de jogo")

    def layout(self):
        print(self.desing[self.erros])



    


app = Forca()
app.run()


        



