from django.db import models
from vacinacao.choices import STATUS_CHOICES


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    data_nascimento = models.DateField()
    sexo = models.CharField(choices=(('M', 'Masculino'), ('F', 'Feminino')), max_length=11, verbose_name='Sexo')
    rua = models.CharField(max_length=50, verbose_name='Rua')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    numero = models.CharField(max_length=5, verbose_name='Numero')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    cep = models.CharField(max_length=9, verbose_name='CEP')

    class Meta:
        abstract = True


class Funcionario(Pessoa):
    cnes = models.CharField(max_length=6, verbose_name='Cnes')


class Paciente(Pessoa):
    sus = models.CharField(max_length=15, unique=True, verbose_name='Sus')

    def __str__(self):
        return f'{self.nome} | SUS: {self.sus} | CPF: {self.cpf}'


class Fabricante(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')

    def __str__(self):
        return self.nome


class Vacina(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='Tipo')
    lote = models.CharField(max_length=20, verbose_name='Lote')
    validade = models.DateField()
    quantidade = models.IntegerField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.tipo} {self.fabricante}'


class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)
    data = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return f'{self.paciente} | {self.vacina} | {self.data} | {self.status}'
