from django.db import models
from django.utils.html import strip_tags

# Create your models here.
class PostDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=100)
    nome_disciplina = models.CharField(max_length=100)
    img_professor = models.FileField(upload_to='professores/')
    periodo = models.IntegerField()

    def __str__(self):
        return self.nome_professor + ' - ' + self.nome_disciplina

class PostMonitoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo_monitoria = models.CharField(max_length=200)
    descricao_monitoria = models.TextField()
    img_monitoria = models.FileField(upload_to='monitorias/')

    def descricao_resumida(self, num_caracteres = 50):
        descricao_sem_tags = strip_tags(self.descricao_monitoria)
        if len(descricao_sem_tags) > num_caracteres:
            return descricao_sem_tags[:num_caracteres] + '...'
        else:
            return descricao_sem_tags

    descricao_resumida.short_description = "Descrição resumida"

    def __str__(self):
        return self.titulo_monitoria

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)
    link_evento = models.URLField(max_length=300)
    data_evento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome_evento
class PostNoticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo_noticia = models.CharField(max_length=200)
    descricao_noticia = models.TextField()
    img_noticia = models.FileField(upload_to='noticias/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def descricao_resumida(self, num_caracteres=50):
        descricao_sem_tags = strip_tags(self.descricao_noticia)
        if len(descricao_sem_tags) > num_caracteres:
            return descricao_sem_tags[:num_caracteres] + '...'
        else:
            return descricao_sem_tags

    descricao_resumida.short_description = "Descrição resumida"

    def __str__(self):
        return self.titulo_noticia

class Extensao(models.Model):
    TIPO_EXTENSAO_CHOICES = (
        ('Atual', 'Atual'),
        ('Futura', 'Futura'),
    )

    nome_extensao = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    assunto = models.CharField(max_length=500)
    tipo = models.CharField(max_length=10, choices=TIPO_EXTENSAO_CHOICES, default='Atual')

    def __str__(self):
        return f"{self.nome_extensao} - {self.professor}"

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=200)
    descricao_projeto = models.TextField()

    def __str__(self):
        return self.nome_projeto

class Documentacao(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('Requerimento', 'Requerimento'),
        ('Arquivo', 'Arquivo'),
    ]

    nome_arquivo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentacao/')
    tipo = models.CharField(max_length=20, choices=TIPO_DOCUMENTO_CHOICES, default='Arquivo')

    def __str__(self):
        return self.nome_arquivo
