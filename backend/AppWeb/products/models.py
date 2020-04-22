from django.db import models

class Product(models.Model):
	name = models.CharField('nombre', max_length = 100)
	conectioner = models.CharField('confeccionista', max_length = 100)
	purchase_detail = models.CharField('detalle_compra', max_length = 100)
		
