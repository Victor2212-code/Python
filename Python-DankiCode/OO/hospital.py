from datetime import date


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    @classmethod
    def idadeAnoNascimento(cls, nome,  anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return cls(nome, idade, cpf, email)


class Medico:
    pass


"""paciente = Paciente('Mono Lisa', 20, '000-000-00', 'monalise@gmail.com')
print(paciente.__dict__)
print(Paciente.idadeAnoNascimento(1926))"""
paciente = Paciente.idadeAnoNascimento('Mono Lisa', 1900, '000-000-00', 'monalise@gmail.com')
print(paciente.__dict__)
print(paciente.idade)