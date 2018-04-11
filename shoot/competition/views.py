from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompetitionForm, MatchForm
from .models import Matches, Competitions

# Create your views here.



def CompetitionCreate(request):
	form = CompetitionForm(request.POST or None)
	message = 'Create NEW Competition entry or Update / Delete previous competition from list'
	competition_list = Competitions.objects.all().order_by('competition_id')

	if form.is_valid():
		form.save()
		message = 'Competition Successfully Stored..'
	else:
		form = CompetitionForm()

	context = {
		'form':form,
		'competition_list': competition_list,
		'message': message,
	}

	return render(request, 'competition_form.html', context)



def CompetitionUpdate(request, pk=1):
	instance = get_object_or_404(Competitions, pk=pk)
	message = ' Please make changes in selected Competition Record..'
	competition_list = Competitions.objects.all().order_by('competition_id')

	form = CompetitionForm(request.POST or None, instance = instance)

	if request.method =='POST':
		if form.is_valid():
			form.save()
			message = 'Record Successfully updated..'
			return redirect('competition-create')
		else:
			print ('form invalid')

	context = {
		'form':form,
		'competition_list': competition_list,
		'message': message,
	}

	return render(request, 'competition_form.html', context)



def CompetitionDelete(request, pk):
	instance = Competitions.objects.get(pk=pk)
	instance.delete()
	return redirect('competition-create')




def MatchCreate(request):

	match_list = Matches.objects.all()

	form = MatchForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = MatchForm()

	context = {
		'form':form,
		'match_list': match_list,
	}

	return render(request, 'match_form.html', context)

def MatchUpdate(request, pk=1):
	match_list = Matches.objects.all()

	instance = get_object_or_404(Matches, pk=pk)
	form = MatchForm(request.POST or None, instance = instance)

	if form.is_valid():
		form.save()
		return redirect('match-create')

	context = {
		'form': form,
		'match_list': match_list,
	}

	return render(request, 'match_form.html', context)

def MatchDelete(reuqest, pk=1):
	instance = get_object_or_404(Matches, pk=pk)
	instance.delete()
	return redirect('match-create')
