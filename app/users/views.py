#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 20/08/2020 11:03.
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})
