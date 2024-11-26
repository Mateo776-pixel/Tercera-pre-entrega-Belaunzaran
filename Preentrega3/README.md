# Tercera preentrega Proyecto Django - Web intemedia

El proyecto de web intermedia incluye las funcionalidades para registrar expresos, vendedores, clientes y proveedores asi como realizar la busqueda de un cliente por el nombre del cliente en la pantalla principal.

# Pasos para ejecutar:
1. Clona el repositorio en la terminal de tu maquina local: 
git clone 

2. Instala las dependencias del proyecto: 
pip install –r requirements.txt 

3. Activa el entorno virtual: 
source venv1/Scripts/activate

4. Inicia el servidor:
python manage.py runserver

5. Accede desde el navegador al inicio del proyecto:
http://localhost:8000/inicio/

# Funcionalidades:

1. Pagina de inicio / Buscar clientes por nombre del cliente:
- URL /inicio/ O haciendo click en "inicio" en la barra de navegacion
- Descripcion: Es la pagina principal del proyecto donde se visualiza un titulo y debajo se puede buscar clientes por nombre del cliente (hay un pequeño mensaje abajo del buscador informando que no hay ningun cliente para buscar) Primero debemos ir a clientes y guardar algun cliente. Luego al ir a inicio podremos buscarlo, por ejemplo si cargamos el un cliente con nombre 'Mateo' al ponerlo en la busqueda, debajo nos aparecera toda la info respecto de ese cliente, en este caso: Nombre - Email - Telefono - Direccion 

2. Registro de Expresos:
- URL /expresos/ O haciendo click en "Expresos" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de expresos, ingresando un nombre, codigo y direccion de entrega. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del expreso.

3. Registro de Vendedores:
- URL /vendedores/ O haciendo click en "Vendedores" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de un vendedor, ingresando nombre, apellido y codigo Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del vendedor.

4. Registro de clientes:
- URL /cli/ O haciendo click en "Clientes" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de clientes, ingresando el nombre, email, telefono y direccion. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del cleinte. Este registro se podra usar para la busqueda de clientes en la pantalla Inicio.

5. Registro de proveedores:
- URL /prov/ O haciendo click en "Proveedores" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de proveedores, ingresando el nombre, email, telefono y direccion. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del proveedor.

# Acceso al panel de administracion:
Inicia sesion con tu usuario para acceder al panel de administracion de Django y ver la base de datos:
Accede desde el navegador al login de administracion: http://localhost:8000/admin/
- Nombre de usuario: CoderUsu
- Contraseña: Coder123


