from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you can save the email to your database or send confirmation email
        # For now, just redirect to thank you page
        return HttpResponseRedirect(reverse('newsletter_thanks'))
    
    return render(request, 'element/newsletter.html')


def newsletter_thanks(request):
    return render(request, 'element/newsletter_thanks.html')
