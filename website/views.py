from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from website.models import Contact
from website.forms import NameForm
def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    
    return render(request, 'website/about.html')


def contact_view(request):
    
    return render(request, 'website/contact.html')


def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            subject= form.cleaned_data['subject']
            mail= form.cleaned_data['mail']
            message= form.cleaned_data['message']
            print(name,subject,mail,message)
            return HttpResponse('done')
        else:
            return HttpResponse('not_valid')

    form = NameForm()
    return render(request,'test.html',{'form':form})
 