from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    Equipo = forms.CharField(max_length=30)
    Numero = forms.CharField(max_length=30)


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    legajo= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)