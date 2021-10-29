from django.shortcuts import render

# Create your views here.
def str_gl(request, *args, **kwargs):
	return render(request, 'glowna.html', {})