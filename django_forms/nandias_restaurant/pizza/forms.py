from django import forms

from .models import Pizza, Size


# class PizzaForm(forms.Form):
# fields we want on the form
# topping1 = forms.CharField(label='Topping 1', max_length=100)
# topping2 = forms.CharField(label='Topping 2', max_length=100)
# # toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')],
# #                                      widget=forms.CheckboxSelectMultiple)
# size = forms.ChoiceField(label='Size', choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')])

class PizzaForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Pizza
        fields = ['size', 'topping1', 'topping2']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}
        # widgets = {'size': forms.CheckboxSelectMultiple}
