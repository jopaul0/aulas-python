class Conta:
    def __init__(self,titular,numero):
        self._saldo=0
        self._numero=numero
        self._titular=titular

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,saldo):
        if saldo<0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo=saldo

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo-=valor
            print(f"Você sacou {valor} reais")
        else:
            print("Você não tem saldo suficiente para sacar esse valor")

    def deposita(self, valor):
        self._saldo+=valor

    def extrato(self):
        print("Cliente: ",self._titular," Saldo Atual: ",self._saldo)