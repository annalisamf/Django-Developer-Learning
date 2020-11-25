from django.forms import formset_factory
from django.shortcuts import render

from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)  # take info from the post and create a new form object
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            note = f'Thanks for ordering! Your {size} {topping1} and {topping2} pizza is on its way!'
            filled_form = PizzaForm() # clear out the form
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again.'
        return render(request, 'pizza/order.html',
                          {'created_pizza_pk': created_pizza_pk, 'pizzaform': filled_form, 'note': note,
                           'multiple_form': multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form': multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)  # get the pizza from the db
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)

        if filled_form.is_valid():
            filled_form.save()  # update with the new info
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'note': note, 'pizzaform': form, 'pizza': pizza})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})
