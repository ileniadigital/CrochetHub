from django.db import models

# Yarn Model
class Yarn(models.Model):
    '''Yarn Model to store yarn information'''
    brand= models.CharField(max_length=255)
    weight= models.IntegerField
    # NEED TO MAKE THESE INTO ENUMS
    colour = models.TextChoices("Colour", "RED ORANGE YELLOW GREEN BLUE PURPLE PINK BROWN BLACK WHITE GREY")
    material = models.TextChoices("Material", "WOOL COTTON ACRYLIC POLYESTER")
    price = models.FloatField()
    yardage = models.IntegerField()
    hook_size = models.FloatField()
    available= models.BooleanField()


class Pattern(models.Model):
    '''Pattern Model to store pattern information'''
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.DateField()
    link = models.URLField()
    transcript = models.TextField()


class User(models.Model):
    '''User Model to store user information'''
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)


class ProjectYarn(models.Model):
    '''ProjectYarn Model to store yarn needed for a project'''
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Project(models.Model):
    '''Project Model to store project with materials and pattern'''
    title = models.CharField(max_length=255)
    description = models.TextField()
    yarn = models.ManyToManyField(Yarn, through=ProjectYarn)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField()
    notes = models.TextField()