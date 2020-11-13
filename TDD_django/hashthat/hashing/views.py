from django.shortcuts import render
from .forms import HashForm
from .models import Hash
import hashlib


def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST) # create new form with the post request
        if filled_form.is_valid():
            input_text = filled_form.cleaned_data('text')
            input_text_hash = hashlib.sha256(input_text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=input_text_hash) # check if the has is already present
            except Hash.DoesNotExist:
                new_hash = Hash() # create new hash object
                new_hash.text = input_text
                new_hash.hash = input_text_hash
                new_hash.save()

    form = HashForm()
    return render(request, 'hashing/home.html', {'form': form})

