class Cliente:
    def __init__(self, n, t):

        self._nome = n
        self._telefone = t

    def get_nome(self):
        return self._nome
    
    def get_telefone(self):
        return self._telefone
    
    def set_nome(self,nome):
        self._nome=nome

    def set_telefone(self,telefone):
        self._telefone=telefone