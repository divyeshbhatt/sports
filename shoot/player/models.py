from django.db import models

# Create your models here.

def increment_player_code():
	
	last_code1 = Player.objects.all().order_by('id').last()
	if not last_code1:
		last_code=0
	else:
		last_code = last_code1.id

	print(last_code)
	if not last_code:
		new_id = 'GS0000'+ str(last_code + 1)
		# new_id = 'GS00001'
	elif last_code < 10:
		new_id = 'GS0000'+ str(last_code + 1)
	elif last_code < 99:
		new_id = 'GS000'+ str(last_code + 1)
	elif last_code < 999:
		new_id = 'GS00'+ str(last_code + 1)

	return new_id





class Player(models.Model):
	code 		=	models.CharField(max_length=7, default = increment_player_code, editable=True)
	name 		=	models.CharField(max_length=30)
	last_name	=	models.CharField(max_length=30)
	birth_date	=	models.DateField()
	about 		=	models.CharField(max_length=200)

	def __str__(self):
		return '{} | {} {}'.format(self.code, self.name, self.last_name)

	def codegenerator(self):
		code_generator = Player.objects.last()
		code = 'GS-'.join(str(code_generator.pk))
		return code

