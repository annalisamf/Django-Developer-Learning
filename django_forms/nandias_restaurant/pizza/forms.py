from django import forms


class PizzaForm(forms.Form):
    # fields we want on the form
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')])
