class Cuenta:
    
    def __init__(self,cuenta,saldo):
        self.cuenta = cuenta
        self.saldo = saldo

    def consultarSaldo(self):
        return self.saldo

    def retirar(self,monto):
        if self.saldo < monto:
            return "saldo insuficiente"
        else:
            self.saldo = self.saldo - monto
            return f"se retiro: {monto} de la cuenta"
    
    def consignar(self, monto):
        self.saldo = self.saldo + monto
        return f"se consigno: {monto} en la cuenta"


        