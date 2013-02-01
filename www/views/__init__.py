from django.shortcuts import render_to_response
# Create your views here.


def home(request):
    return render_to_response('index.html')


def template(request, template_name):
    return render_to_response('{0}.html'.format(template_name))
