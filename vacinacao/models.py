from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(choices=(('M', 'Masculino'), ('F', 'Feminino')), max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        abstract = True


    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    cnes = models.CharField(max_length=6)


class Paciente(Pessoa):
    sus = models.CharField(max_length=15)


class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Vacina(models.Model):
    tipo = models.CharField(max_length=20)
    lote = models.CharField(max_length=20)
    validade = models.DateField()
    quantidade = models.IntegerField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo