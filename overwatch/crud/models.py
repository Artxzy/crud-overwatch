from django.db import models

# Create your models here.

class Heroi(models.Model):
    imagem = models.ImageField(blank=True)
    apelido = models.CharField(verbose_name="Apelido", max_length=40)
    dificuldade = models.PositiveIntegerField(verbose_name="Dificuldade")
    descricao = models.TextField(verbose_name="Descrição do herói", max_length=800)
    nome_verdadeiro = models.CharField(verbose_name="Nome verdadeiro; idade", max_length=100)
    ocupacao = models.CharField(verbose_name="Ocupação", max_length=100)
    base_operacoes = models.CharField(verbose_name="Base de operações", max_length=100)
    afiliacao = models.CharField(verbose_name="Afiliação", max_length=100)
    historia = models.TextField(verbose_name="História", max_length=10000)
    qtd_habilidades = models.PositiveIntegerField(verbose_name="Quantidade de habilidades")
    fk_funcao = models.ForeignKey('Funcao', on_delete=models.PROTECT, verbose_name="Função")
    habilidade_1 = models.TextField(verbose_name="Habilidade um: ", max_length=500, blank=True)
    habilidade_2 = models.TextField(verbose_name="Habilidade dois ", max_length=500, blank=True)
    habilidade_3 = models.TextField(verbose_name="Habilidade três: ", max_length=500, blank=True)
    habilidade_4 = models.TextField(verbose_name="Habilidade quatro: ", max_length=500, blank=True)
    habilidade_5 = models.TextField(verbose_name="Habilidade cinco : ", max_length=500, blank=True)
    habilidade_6 = models.TextField(verbose_name="Habilidade seis: ", max_length=500, blank=True)
    habilidade_7 = models.TextField(verbose_name="Habilidade sete: ", max_length=500, blank=True)

    def __str__(self):
        return self.apelido


class Funcao(models.Model):
    imagem = models.ImageField()
    nome = models.CharField(verbose_name="Nome da função", max_length=40)
    definiçao = models.TextField(verbose_name="Definição", max_length=300)

    def __str__(self):
        return self.nome
