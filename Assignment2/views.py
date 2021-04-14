from django.http import HttpResponse

def home(request):
	# add your individual unique string into the response
    return HttpResponse("Hello, world. 4c72c616 is the polls index.") 