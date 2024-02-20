

class Funcionario:

    pass


class FrontEnd(Funcionario):
    def FrontEnd(self):
        super().trabalhar()


class BackEnd(Funcionario):
    def Backend(self):
        super().trabalhar()


class FullStack(BackEnd, FrontEnd):
    pass

ana = FullStack()
ana.FrontEnd()
ana.Backend()

# algoritmo mmro