from django.db import models
from django.db.models.signals import pre_save
from player.models import Player
from competition.models import Matches, Competitions

# Create your models here.

def TotalScore(s1, s2):
	r=s1 + s2
	print(r)
	return r


class Result(models.Model):
	competition_id = models.ForeignKey(Competitions, on_delete=models.SET_NULL, null=True, related_name='tournament')
	match_id	=	models.ForeignKey(Matches, on_delete=models.SET_NULL, null = True, related_name = 'matches')
	shooter_id 	= 	models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
	s1			=	models.IntegerField(default=0)
	s2			=	models.IntegerField(default=0)
	s3			=	models.IntegerField(default=0)
	s4			=	models.IntegerField(default=0)
	s5			=	models.IntegerField(default=0)
	s6			=	models.IntegerField(default=0)
	s7			=	models.IntegerField(default=0)
	s8			=	models.IntegerField(default=0)
	s9			=	models.IntegerField(default=0)
	s10			=	models.IntegerField(default=0)
	s11			=	models.IntegerField(default=0)
	s12			=	models.IntegerField(default=0)
	s13			=	models.IntegerField(default=0)
	s14			=	models.IntegerField(default=0)
	s15			=	models.IntegerField(default=0)
	s16			=	models.IntegerField(default=0)
	s17			=	models.IntegerField(default=0)
	s18			=	models.IntegerField(default=0)
	s19			=	models.IntegerField(default=0)
	s20			=	models.IntegerField(default=0)
	s21			=	models.IntegerField(default=0)
	s22			=	models.IntegerField(default=0)
	s23			=	models.IntegerField(default=0)
	s24			=	models.IntegerField(default=0)
	s25			=	models.IntegerField(default=0)
	s26			=	models.IntegerField(default=0)
	s27			=	models.IntegerField(default=0)
	s28			=	models.IntegerField(default=0)
	s29			=	models.IntegerField(default=0)
	s30			=	models.IntegerField(default=0)
	s31			=	models.IntegerField(default=0)
	s32			=	models.IntegerField(default=0)
	s33			=	models.IntegerField(default=0)
	s34			=	models.IntegerField(default=0)
	s35			=	models.IntegerField(default=0)
	s36			=	models.IntegerField(default=0)
	s37			=	models.IntegerField(default=0)
	s38			=	models.IntegerField(default=0)
	s39			=	models.IntegerField(default=0)
	s40			=	models.IntegerField(default=0)
	total		=	models.IntegerField(default=0, editable = True)
	rank		= 	models.IntegerField(default=0)

	


	def __str__(self):
		return '{} {} {} {}'.format(self.shooter_id, self.match_id, self.total, self.rank)


def pre_save_result_receiver(sender, instance , *args, **kwargs):
	total1 = instance.s1 + instance.s2 + instance.s3+ instance.s4+ instance.s5+ instance.s6+ instance.s7+ instance.s8
	total2 = instance.s9 + instance.s10 + instance.s11+ instance.s12+ instance.s13+ instance.s14+ instance.s15+ instance.s16
	total3 = instance.s17 + instance.s18 + instance.s19+ instance.s20+ instance.s21+ instance.s22+ instance.s23+ instance.s24
	total4 = instance.s25 + instance.s26 + instance.s27+ instance.s28+ instance.s29+ instance.s30+ instance.s31+ instance.s32
	total5 = instance.s33 + instance.s34 + instance.s35+ instance.s36+ instance.s37+ instance.s38+ instance.s39+ instance.s40
	total = total1 + total2 + total3 + total4 + total5
	instance.total = total



pre_save.connect(pre_save_result_receiver, sender=Result)
