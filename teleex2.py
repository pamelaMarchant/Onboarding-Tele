class Unidade(object):
    STATUS = ['ativo', 'inativo']

    def __init__(self, id, cnes,
                 nome, municipio, uf,
                 telefone, tipo, status):
        self.id = id
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
