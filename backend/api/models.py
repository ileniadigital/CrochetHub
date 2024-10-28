from django.db import models

# Yarn Model
class Yarn(models.Model):
    brand= models.CharField(max_length=255)
    weight= models.IntegerField
    colour = models.TextChoices("Colour", "RED ORANGE YELLOW GREEN BLUE PURPLE PINK BROWN BLACK WHITE GREY")
    material = models.TextChoices("Material", "WOOL COTTON ACRYLIC POLYESTER")
    price = models.FloatField()
    yardage = models.IntegerField()
    hook_size = models.FloatField()
    available= models.BooleanField()

# Tutorials Model

# User Model