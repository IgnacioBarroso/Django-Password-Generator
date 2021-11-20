from django.shortcuts import render
from random import choice

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    length = int(request.GET.get('length'))
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('-_+¿¡!?\@#$%^&*(){}[]/'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for i in range(length):
        generated_password += choice(characters)
    
    return render(request, 'password.html', {'password': generated_password})