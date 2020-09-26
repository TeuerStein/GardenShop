from django.db import models

class Seed(models.Model):
    ''' Seed model '''

    name = models.CharField(max_length=25, unique=True, verbose_name='Name')
    picture = models.ImageField(verbose_name='Picture')
    title = models.CharField(max_length=50, verbose_name='Title')
    short_description = models.TextField(verbose_name='Short Description')
    long_description = models.TextField(verbose_name='Long Description')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, verbose_name='Rubric')

    class Meta:
    	verbose_name = 'Seed'
    	verbose_name_plural = 'Seeds'


class Rubric(models.Model):
    ''' Rubric for Seed model '''

    rubric_name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Rubric Name'
    )

    def __str__(self):
    	return self.rubric_name

    class Meta:
    	verbose_name_plural = "Rubrics"
    	verbose_name = "Rubric"
    	ordering = ["rubric_name"]
