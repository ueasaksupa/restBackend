from django.db import models

# Create your models here.

class Portfolios(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='your port.')
    pro_loss = models.FloatField(default=0)
    owner = models.ForeignKey('auth.User', related_name='portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)