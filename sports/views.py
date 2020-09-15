from django.shortcuts import render
from datetime import datetime, timedelta
from sports.models import LeftPost, RightPost, CenterPost, MiniCenterPost, AsiaPost, AfricaPost, EuropePost, NorthAmericaPost

def home(request):
	northAmerica = NorthAmericaPost.objects.all().order_by('-id')[:3]
	europe = EuropePost.objects.all().order_by('-id')[:3]
	africa = AfricaPost.objects.all().order_by('-id')[:3]
	asia = AsiaPost.objects.all().order_by('-id')[:3]
	right_single = RightPost.objects.all().order_by('-id')[:1]
	double_rightpost = RightPost.objects.all().order_by('-id')[1:3]
	left_single = LeftPost.objects.all().order_by('-id')[:1]
	left_doublepost = LeftPost.objects.all().order_by('-id')[1:3]
	center_single = CenterPost.objects.all().order_by('-id')[:1]
	center_doublepost = CenterPost.objects.all()[1:3]
	minipost = MiniCenterPost.objects.all()
	template = 'sports/index.html'
	context = {
		'northAmerica': northAmerica,
		'europe': europe,
		'africa': africa,
		'dobuleposts': center_doublepost,
		'miniposts': minipost,
		'double_rightposts': double_rightpost,
		'cposts': center_single,
		'rightposts': right_single,
		'left_doublesports': left_doublepost,
		'leftposts': left_single,
		'asia': asia
	}
	response =  render(request, template, context)
	response.set_signed_cookie('name', 'User', salt='ab' , expires=datetime.utcnow()+timedelta(days=2))
	return response

def single(request, slug):
	left = LeftPost.objects.get(slug=slug)
	left.views = left.views + 1
	left.save()

	template = 'sports/slug.html'
	context = {
		'one': left
	}
	return render(request, template, context)


def news(request):
	europeone = EuropePost.objects.all().order_by('-id')[:1]
	europetwo = EuropePost.objects.all().order_by('-id')[1:3]
	leftone = LeftPost.objects.all().order_by('-id')[:1]
	rightone = MiniCenterPost.objects.all().order_by('-id')[:1]
	centerone = CenterPost.objects.all().order_by('-id')[:1]
	asiaone = AsiaPost.objects.all().order_by('-id')[:1]
	africaone = AfricaPost.objects.all().order_by('-id')[:1]
	northoneamerica = NorthAmericaPost.objects.all().order_by('-id')[:1]
	template = 'sports/single.html'
	context = {
		'europeone': europeone,
		'europetwo': europetwo,
		'leftow': leftone,
		'rightone': rightone,
		'centerone': centerone,
		'asiaone': asiaone,
		'africaone': africaone,
		'northoneamerica': northoneamerica
	}
	return render(request, template, context)

