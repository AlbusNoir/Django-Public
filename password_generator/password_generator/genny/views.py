from django.shortcuts import render
import random

# Create your views here.

# option vals
range(8, 31)


def home(request):
    return render(request, 'genny/index.html', {'pass_length': range(8, 31)})


def password(request):
    # password options
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    if request.GET.get('special'):
        chars.extend(list("!\"#$%&'()*+,-./:;<=>?@\\[]^_`|{}~"))

    length = int(request.GET.get('length', 10))  # 10 is default

    pword = ''
    for x in range(length):
        pword += random.choice(chars)

    return render(request, 'genny/password.html', {'password': pword})
