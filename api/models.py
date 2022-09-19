from django.db import models

# Create your models here.
# This is a copy of swapi model for planet and people
# link: https://github.com/Juriy/swapi/blob/master/resources/models.py

class DateTimeModel(models.Model):
  """ A base model with created and edited datetime fields """

  class Meta:
    abstract = True

  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)


class EditableModel(models.Model):
  """
  A model with a boolean that determins the read/write state of the model
  """

  editable = models.NullBooleanField()

class Planet(DateTimeModel):
  name = models.CharField(max_length=100)
  rotation_period = models.CharField(max_length=40)
  orbital_period = models.CharField(max_length=40)
  diameter = models.CharField(max_length=40)
  climate = models.CharField(max_length=40)
  gravity = models.CharField(max_length=40)
  terrain = models.CharField(max_length=40)
  surface_water = models.CharField(max_length=40)
  population = models.CharField(max_length=40)

  def __str__(self):
    return self.name


class People(DateTimeModel):
  name = models.CharField(max_length=100)
  height = models.CharField(max_length=10, blank=True)
  mass = models.CharField(max_length=10, blank=True)
  hair_color = models.CharField(max_length=20, blank=True)
  skin_color = models.CharField(max_length=20, blank=True)
  eye_color = models.CharField(max_length=20, blank=True)
  birth_year = models.CharField(max_length=10, blank=True)
  gender = models.CharField(max_length=40, blank=True)
  homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.CASCADE)

  def __str__(self):
    return self.name
