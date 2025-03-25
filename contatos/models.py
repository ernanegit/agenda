from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    class Meta:
        ordering = ['-id']  # Ordenar por ID de forma decrescente