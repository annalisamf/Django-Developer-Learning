import hashlib

from django.shortcuts import render, redirect

from .forms import HashForm
from .models import Hash


def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)  # create new form with the post request
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)  # check if the has is already present
            except Hash.DoesNotExist:
                hash = Hash()  # create new hash object
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash=text_hash)  # redirect the user to the hash function

    form = HashForm()
    return render(request, 'hashing/home.html', {'form': form})


def hash(request, hash):
    hash = Hash.objects.get(hash=hash)  # hash that we have passed
    return render(request, 'hashing/hash.html', {'hash': hash})  # passing the hash object
