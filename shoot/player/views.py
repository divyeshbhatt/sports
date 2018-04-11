from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PlayerForm
from .models import Player
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

# ----------------Player CREATE-----------------------
@login_required
def PlayerCreate(request):

	
	form = PlayerForm(request.POST or None)		# Can use if request.method =='POST':
	message = 'Create NEW Entry of Players or Update / Delete any players from list'
	player_list = Player.objects.all().order_by('-pk')

	pages = pagination(request, player_list, num=6)


	if form.is_valid():
		form.save()
		message = 'Record Successfully stored..'
		# return redirect('home')

	
	form = PlayerForm()

	context = {
	'form': form,
	'player_list': player_list,
	'message':message,
	}	
	
	return render(request, 'player_form.html', context)

# ----------Player UPDATE----------------------------
@login_required
def PlayerUpdate(request, pk=1):
	instance =get_object_or_404(Player, pk=pk)
	message = 'Please update current record and submit for changes..'
	player_list = Player.objects.all().order_by('-pk') 
	
	form = PlayerForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		message = 'Record updated...'
		return redirect('player-create')  
	context = {
		'form': form,
		'message': message,
		'player_list': player_list,
	}
	return render(request, 'player_form.html',context)


# ---------------------Player LIST----------------------

# def PlayerList(request):
# 	player_list = Player.objects.all().order_by('-pk') 
# 	context = {
# 		'player_list': player_list,
# 	}
# 	return render(request, 'player_list.html', context)

@login_required
def PlayerDelete(request, pk=1):
	instance =get_object_or_404(Player, pk=pk)
	instance.delete()
	
	return redirect('player-create')


def pagination(request, data, num=4):
	
	page = request.GET.get('page')
	
	paginator = Paginator(data, num)

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	index = items.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 5 if index >= 5 else 0
	end_index = index + 5 if index <= max_index - 5 else max_index
	page_range = paginator.page_range[start_index:end_index]

	return items, page_range