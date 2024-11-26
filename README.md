Tercera Preentrega Proyecto Django Este proyecto de Django tiene como objetivo la gestión de expresos, vendedores, clientes y proveedores. Además, permite realizar búsquedas de clientes por nombre desde la página principal.

Pasos para ejecutar el proyecto Clona el repositorio en tu máquina local:

bash Copiar código git clone https://github.com/Mateo776-pixel/Tercera-pre-entrega-Belaunzaran.git

bash Copiar código pip install -r requirements.txt Activa el entorno virtual:

bash Copiar código source venv1/Scripts/activate Inicia el servidor de desarrollo:

bash Copiar código python manage.py runserver Accede al proyecto desde tu navegador:

Abre la URL: http://localhost:8000/inicio/ Funcionalidades

Página de inicio / Búsqueda de clientes por nombre URL: /inicio/ (o haciendo clic en "Inicio" en la barra de navegación) 
Descripción: En la página de inicio, los usuarios pueden buscar clientes por su nombre. Si no se encuentran resultados, se muestra un mensaje indicando que no se han encontrado clientes. Para poder realizar una búsqueda, primero debes registrar un cliente. Por ejemplo, si registras un cliente con el nombre "Mateo", podrás buscarlo en la página de inicio y ver sus detalles (nombre, email, teléfono y dirección).

Registro de Expresos URL: /expresos/ (o haciendo clic en "Expresos" en la barra de navegación) 
Descripción: Esta página permite registrar un nuevo expreso. Para ello, debes ingresar un nombre, un código y la dirección de entrega. Todos los campos son obligatorios y debes presionar el botón "Enviar" para completar el registro.

Registro de Vendedores URL: /vendedores/ (o haciendo clic en "Vendedores" en la barra de navegación) 
Descripción: En esta página, puedes registrar un vendedor. Los datos requeridos son el nombre, apellido y código del vendedor. Al igual que en otras secciones, todos los campos son obligatorios y se debe presionar el botón "Enviar" para completar el registro.

Registro de Clientes URL: /clientes/ (o haciendo clic en "Clientes" en la barra de navegación)
Descripción: Esta página permite registrar nuevos clientes ingresando su nombre, email, teléfono y dirección. Al igual que en los registros anteriores, todos los campos son obligatorios y debes presionar el botón "Enviar" para completar el registro. Este registro es importante, ya que se utilizará para realizar las búsquedas de clientes desde la página de inicio.

Registro de Proveedores URL: /proveedores/ (o haciendo clic en "Proveedores" en la barra de navegación) 
Descripción: En esta página, puedes registrar un proveedor ingresando su nombre, email, teléfono y dirección. Todos los campos son obligatorios y el registro se completa al presionar el botón "Enviar". 

Acceso al panel de administración de Django Para gestionar la base de datos a través de la interfaz de administración de Django, inicia sesión en el siguiente enlace:
URL del panel de administración: http://localhost:8000/admin/ 

Nombre de usuario: CoderUsu Contraseña: Coder123
