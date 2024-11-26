from django import forms 
from AppV.models import Expreso, Vendedor

class ExpresoForm(forms.ModelForm):
    class Meta:
        model = Expreso
        fields = ['nombre', 'codigo', 'direccion_entrega']  # Campos que se mostrarán en el formulario
        labels = {
            'nombre': 'Nombre del Expreso',
            'codigo': 'Código',
            'direccion_entrega': 'Dirección de Entrega',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_entrega': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'codigo']  # Campos que se mostrarán en el formulario
        labels = {
            'nombre': 'Nombre del Vendedor',
            'apellido': 'Apellido del Vendedor',
            'codigo': 'Código',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
}

class clienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))    
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ClienteBusquedaFormulario(forms.Form):
    codigo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por código'}))    

class proveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))    
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))