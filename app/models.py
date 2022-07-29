from django.db import models

# Create your models her

class Cadastro(models.Model):
    produto = models.CharField(max_length=50, verbose_name='Produto')

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.produto
