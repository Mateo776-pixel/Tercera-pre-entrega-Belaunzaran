from django.shortcuts import render, redirect
from AppV.models import Vendedor, Expreso, Cliente, Proveedor
from AppV.forms import VendedorForm, ExpresoForm, clienteFormulario, proveedorFormulario

def inicio(request):
    return render(request, 'appv/index.html')


def expresos(req):
    if req.method == 'POST':
        miFormulario = ExpresoForm(req.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            expreso_obj = Expreso(nombre=informacion["nombre"], 
            codigo=informacion["codigo"], 
            direccion_entrega=informacion["direccion_entrega"])
            expreso_obj.save()
            return render(req, "appv/index.html")  # Redirigir a la página de inicio o donde desees
    else:
        miFormulario = ExpresoForm()

    return render(req, 'appv/expresos.html', {"miFormulario": miFormulario})


def vendedores(req):
    if req.method == 'POST':
        miFormulario = VendedorForm(req.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vendedor_obj = Vendedor(nombre=informacion["nombre"], 
                                    apellido=informacion["apellido"], 
                                    codigo=informacion["codigo"]) 
            vendedor_obj.save()
            return render(req, "appv/index.html")  # Redirigir a la página de inicio o donde desees
    else:
        miFormulario = VendedorForm()

    return render(req, 'appv/vendedores.html', {"miFormulario": miFormulario})


def clientes(req):
    if req.method == 'POST':
        miFormulario = clienteFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Cliente(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html")
    else:
        miFormulario = clienteFormulario()
    return render(req, 'appv/clientes.html', {"miFormulario": miFormulario})

def buscar_cliente(request):
    nombre = request.GET.get('nombre', '')  # Recupera el parámetro 'nombre' de la URL
    clientes = Cliente.objects.filter(nombre__icontains=nombre)  # Filtra los clientes por nombre (insensible a mayúsculas y minúsculas)
    
    return render(request, 'appv/index.html', {'clientes': clientes, 'nombre': nombre})



def proveedores(req):
    if req.method == 'POST':
        miFormulario = proveedorFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Proveedor(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html") 
    else:
        miFormulario = proveedorFormulario()
    return render(req, 'appv/proveedores.html', {"miFormulario": miFormulario})






