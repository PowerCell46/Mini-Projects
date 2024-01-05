from django.db import models

# Create your models here.


class SatelliteImage(models.Model):
    territory = models.CharField(max_length=25)
    sourceUrl = models.URLField()
    dataSource = models.CharField(
        choices=(('S-2', 'Sentinel-2'), ('L-8', 'Landsat 8-9'), ('Copernicus', 'Copernicus Services')))
    trueColourImage = models.ImageField()
    falseColourImage = models.ImageField()
    NDVIimage = models.ImageField()
    imageDate = models.DateField()
    publicationDate = models.DateField(auto_now_add=True)
