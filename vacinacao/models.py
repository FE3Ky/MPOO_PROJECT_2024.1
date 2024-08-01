from django.db import models


class Endereco(models.Model):
    rua = models.CharField()
    bairro = models.CharField()
    numero = models.CharField()
    cidade = models.CharField()
    estado = models.CharField()
    cep = models.CharField(max_length=9)


class Pessoa(models.Model):
    nome = models.CharField()
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(choices=(('M', 'Masculine'), ('F', 'Feminino')),)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Funcionario(Pessoa):
    ...

