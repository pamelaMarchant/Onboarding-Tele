class Usuario(object):
    STATUS = ["ativo", "inativo"]
#    PERFIL = ["monitor", "solicitante", "teleconsultor"]

    def __init__(self, ide, nome, email, cpf, dataCriacao, status):
        self.id = ide
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.dataCriacao = dataCriacao
        self.status = status
#        self.perfil = perfil
        assert self.verificaCpf()
        assert self.verificaEmail()
        self.verificaStatus()
#        self.verificaPerfil()

    def verificaCpf(self):
        assert len(self.cpf) == 11
        return "%s.%s.%s-%s" % (self.cpf[0:3],
                                self.cpf[3:6],
                                self.cpf[6:9],
                                self.cpf[9:10])

    def verificaStatus(self):
        assert self.status in self.STATUS

#    def verificaPerfil(self):
#        assert self.perfil in self.PERFIL

    def verificaEmail(self):
        assert type(self.email) == str
        return self.email.find('@') != -1 and  \
            self.email.find('.') > self.email.find('@')

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)


u = Usuario(1, "joaozinho", "joaozinho123@telessauders.org.br", "23456789101",
            "13032020", "ativo")
u1 = Usuario(2, "fulaninho", "fulaninho123@telesauders.org.br", "98765432134",
             "16032020", "ativo")
u2 = Usuario(3, "siclano", "siclano123@telessauders.org.br", "65432178954",
             "16032020", "ativo")
print(u.__dict__)
print(u2.__dict__)

idTeleconsultoria = 0


class Teleconsultoria(object):
    STATUSTELE = ['em espera', 'em atendimento', 'finalizado', 'cancelado']

    def __init__(self, ide, teleconsultor, solicitante, dadosCaso,
                 dataInicio, dataFim, status):

        self.id = ide
        self.teleconsultor = teleconsultor
        self.solicitante = solicitante
        self.dadosCaso = dadosCaso
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.status = status

    def verificaStatus(self):
        assert self.status in self.STATUSTELE

    def contId(idteleconsultoria):
        idteleconsultoria = idteleconsultoria + 1
        return idteleconsultoria

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)


def criaTeleconsultoria(teleconsultor, solicitante):
    tele = Teleconsultoria(123, teleconsultor, solicitante, "febre",
                           "13032020", "16032020", "finalizado")
    return tele


class Unidade(object):

    STATUS = ['ativo', 'inativo']

    def __init__(self, ide, cnes,
                 nome, municipio, uf,
                 telefone, tipo, status):
        self.id = ide
        self.cnes = cnes
        self.nome = nome
        self.municipio = municipio
        self.uf = uf
        self.telefone = telefone
        self.tipo = tipo
        self.status = status
        self.verificaStatus()

    def verificaStatus(self):
        assert self.status in self.STATUS


Uni = []

Uni.append(1, "12345", "consumidora", "Porto Alegre", "RS",
              "987654321", "centro de saude/unidade basica", "ativo")
Uni.append(2, "54321", "provedora", "Porto Alegre", "RS",
           "123456789", "Telessaude", "ativo")


class UsuarioUnidade(object):
    PERFIL = ['monitor', 'teleconsultor', 'solicitante']

    def __init__(self, id, idUsuario, idUnidade, perfil):
        self.id = id
        self.idUsuario = idUsuario
        self.idUnidade = idUnidade
        self.perfil = perfil
        self.verificaPerfil()

    def verificaPerfil(self):
        assert self.perfil in self.PERFIL


def func(id, idUsuario, idUnidade, perfil):
    return UsuarioUnidade


print(func)

userUni = []
userUni.append(UsuarioUnidade(1, 1, 1, "solicitante"))
userUni.append(UsuarioUnidade(2, 2, 2, "teleconsultor"))

a = userUni[x in userUni, x.ide == ide]
tele = criaTeleconsultoria(userUni[1])
print(tele.__dict__)
