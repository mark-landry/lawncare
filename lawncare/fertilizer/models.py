from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=200)
    bag_weight = models.IntegerField(default=0)
    bag_coverage =  models.IntegerField(default=0)
    percent_N = models.DecimalField(max_digits=4, decimal_places=2)
    percent_P = models.DecimalField(max_digits=4, decimal_places=2)
    percent_X = models.DecimalField(max_digits=4, decimal_places=2)

class Application(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE) 
    bags_applied = models.DecimalField(max_digits=4, decimal_places=2)
    date_applied = models.DateField()