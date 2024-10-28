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

# Pattern Model
class Pattern(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.DateField()
    link = models.URLField()

# User Model
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

# ProjectYarn Model to store yarn needed for a project
class ProjectYarn(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    yarn = models.ManyToManyField(Yarn, through=ProjectYarn)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField()
    notes = models.TextField()