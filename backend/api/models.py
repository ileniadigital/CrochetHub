from django.db import models

class Colour(models.TextChoices):
    '''Colour Enum to store colour choices'''
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    PURPLE = "Purple"
    PINK = "Pink"
    BROWN = "Brown"
    BLACK = "Black"
    WHITE = "White"
    GREY = "Grey"


class Material(models.TextChoices):
    '''Material Enum to store material choices'''
    WOOL = "Wool"
    COTTON = "Cotton"
    ACRYLIC = "Acrylic"
    POLYESTER = "Polyester"


class Yarn(models.Model):
    '''Yarn Model to store yarn information'''
    brand = models.CharField(max_length=255)
    weight = models.IntegerField()
    colour = models.CharField(max_length=50, choices=Colour.choices)
    material = models.CharField(max_length=50, choices=Material.choices)
    price = models.FloatField()
    yardage = models.IntegerField()
    hook_size = models.FloatField()

    def __str__(self): 
        return f"{self.brand} {self.colour} {self.material}"


class Pattern(models.Model):
    '''Pattern Model to store pattern information'''
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.DateField()
    link = models.URLField()
    transcript = models.TextField()
    yarns = models.ManyToManyField(Yarn, through='PatternYarn')

    def __str__(self): 
        return f"{self.title}"


class User(models.Model):
    '''User Model to store user information'''
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self): 
        return f"{self.username}"


class PatternYarn(models.Model):
    '''PatternYarn Model to store yarn needed for a pattern'''
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Project(models.Model):
    '''Project Model to store project with materials and pattern'''
    title = models.CharField(max_length=255)
    description = models.TextField()
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateField()
    finished = models.BooleanField(default=False)
    date_finished = models.DateField()
    notes = models.TextField()
