from django.contrib.auth.models import User
from django.db import models
from django import forms


# Cria a model de sindicatos
class Sindicato(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField('CNPJ', max_length=100)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cep = models.CharField('CEP', max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    presidente = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

# Cria a model de socios.
class Socio(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField('CPF', max_length=15)
    rg = models.CharField('RG', max_length=7)
    ssp = models.CharField('SSP', max_length=3)
    data_exp = models.DateField('Data de Expedissão')
    cnh = models.CharField('CNH', max_length=12)
    categoria = models.CharField(max_length=5)
    titulo = models.CharField(max_length=15)
    nacionalidade = models.CharField(max_length=100)
    fator_rh = models.CharField('Fator RH', max_length=50)
    naturalidade = models.CharField(max_length=100)
    uf = models.CharField('UF', max_length=3)
    SEXO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'))
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=128)
    matricula = models.CharField(max_length=50)
    data_admissao = models.DateField('Data de Ademissão')
    data_nascimento = models.DateField('Data de Nascimento')
    ESTADOSIVIL_CHOICES = (
    ('C', 'Casado(a)'), ('S', 'Solteiro(a)'), ('D', 'Divorciado(a)'), ('V', 'Viuvo(a)'), ('O', 'Outros'))
    estado_sivil = models.CharField(choices=ESTADOSIVIL_CHOICES, max_length=1)
    conjugue = models.CharField('Cônjuge', max_length=100, blank=True)
    dependentes = models.IntegerField()
    email = models.EmailField('Email de Contato')
    profissao = models.CharField('Profissão', max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField('Mãe', max_length=100)
    endereco = models.CharField('Endereço', max_length=150)
    numero = models.CharField('Nº', max_length=10)
    bairro = models.CharField(max_length=150)
    cep = models.CharField('CEP', max_length=9)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=3)
    fone_resid = models.CharField('Fone Residencial', max_length=15)
    celular = models.CharField(max_length=15)
    placa_veiculo = models.CharField('Placa do Veiculo', max_length=10)
    concessao = models.CharField('Concessão', max_length=7)
    MOTORISTA_CHOICES = (('P', 'Prop.'), ('A', 'Alx.'))
    categorias = models.CharField(choices=MOTORISTA_CHOICES, max_length=1)
    foto = models.FileField(upload_to='static/img/%d', blank=True)
    sindicato = models.ForeignKey(Sindicato, verbose_name='Sindicato')
    added_by = models.ForeignKey(User, null=True, blank=False, verbose_name='Cadastrado Por')
    updated = models.DateTimeField('Ultima Atualização', auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    class Admin:
        list_display = ['nome', 'cpf']


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Sócio'




