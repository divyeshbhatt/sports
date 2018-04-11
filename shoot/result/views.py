from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory, inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Result
from player.models import Player
from competition.models import Matches, Competitions
from .forms import Result1Form, ResultFormSet, Result2Form, ScoreForm
# Create your views here.

def Participation(request):
	
	result_list = Result.objects.all().order_by('shooter_id')
	form = Result1Form(request.POST or None)

	if form.is_valid():
		form.save()
	
	context = {
		'form': form,
		'result_list': result_list,
	}
	return render(request, 'result_form.html',context)


def ParticipationofEvents(request, id):
	instance = get_object_or_404(Result, id=id)
	shooter_id = instance.shooter_id
	competition_id = instance.competition_id
	
	result_list = Result.objects.filter(shooter_id=shooter_id, competition_id=competition_id)

	if request.method == 'POST':
		form = Result2Form(request.POST or None)
		if form.is_valid():
			match_id = form.cleaned_data['match_id']
			Result.objects.create(competition_id=competition_id, shooter_id=shooter_id, match_id=match_id)
			form = Result2Form()
	else:
		form = Result2Form()

	context = {
		'form': form,
		'result_list': result_list,
		'instance': instance,
	}
	return render(request, 'result_form.html',context)


def ParticipantsList(request):
	result_list = Result.objects.all()

	
	context = {

		'result_list': result_list,
	}

	return render(request, 'result_list.html', context)


def EventScore(request, id):
	instance = get_object_or_404(Result, id=id)
	form = ScoreForm(request.POST or None, instance = instance)
	result_list = Result.objects.all()

	if form.is_valid():
		form.save()
	context = {
		'result_list':result_list,
		'form': form,
		'instance': instance,
	}

	return render(request, 'scoring_list.html', context)




	






# def ParticipationFormset(request, id=1):

	
# 	result_list = Result.objects.all()

# 	if request.method == 'POST':
# 		form = Result1Form(request.POST or None)

# 		if form.is_valid():
# 			shooter_id=form.cleaned_data['shooter_id']
# 			competition_id = form.cleaned_data['competition_id']
# 			form.save()
# 			result_list = Result.objects.filter(shooter_id=shooter_id, competition_id = competition_id)

# 		else:
# 			print('form not valid..')
# 	else:
# 		form = Result1Form()

# 	context = {
# 		'form': form,
# 		'result_list': result_list,
# 	}
# 	return render(request, 'result_form.html', context)




# def ParticipationFormset(request, id=1):
# 	if id:
# 		competition = Competitions.objects.get(id=id)
# 		print(competition)
# 		result_list = Result.objects.filter(competition_id=competition.id)
# 	else:
# 		competition = Competition.objects.get(id=id)
# 		result_list = Result.objects.all()


# 	Result_formset = inlineformset_factory(Competitions, Result, extra=2, fields=('shooter_id', 'match_id',))
	
# 	if request.method == 'POST':
# 		formset = Result_formset(request.POST, request.FILES, instance = competition)
# 		if formset.is_valid():
# 			formset.save()
# 			print('saved.')
# 		else:
# 			print('not saved..')
# 	else:
# 		formset = Result_formset(instance = competition)

# 	context = {
# 		'formset': formset,
# 		'result_list': result_list,
# 	}
# 	return render(request, 'result_form.html', context)
