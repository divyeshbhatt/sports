from django.db import models

# Create your models here.

class Competitions(models.Model):
	competition_id 		=	models.CharField('Id', max_length=10)
	competition_name	=	models.CharField('Competition', max_length=100)
	start_from			=	models.DateField()
	end_on				=	models.DateField()
	venue				=	models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.competition_id)

class Matches(models.Model):
	competition_id 	= 	models.ForeignKey(Competitions, on_delete=models.SET_NULL, null=True)
	match_id		= 	models.CharField(max_length=6, null=True)
	match_detail	=	models.CharField(max_length=100, null=True)
	targets			=	models.IntegerField(null=True)
	fees 			= 	models.IntegerField(null=True)

	def __str__(self):
		return '{}|{}'.format(self.competition_id, self.match_id)
