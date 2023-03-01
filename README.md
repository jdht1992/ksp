# KSP
Crear un módulo de administración de Empleados de una empresa, que contenga su información
general, más el detalle de la información de su beneficiario.
 ### Requerimientos
 - Docker
 - Docker Compose
 

 ### Instalar Docker
 El primer paso es instalar la aplicación Docker de escritorio para su máquina local:
 - [Docker para Mac](https://docs.docker.com/docker-for-mac/install/)
 - [Docker para Windows](https://docs.docker.com/docker-for-windows/install/)
 - [Docker para Linux](https://docs.docker.com/engine/install/#server)

 Docker Compose es una herramienta adicional que se incluye automáticamente con las descargas de Docker para Mac y Windows. Sin embargo, si está en Linux, deberá agregarlo manualmente. Puede hacer esto ejecutando el comando sudo pip install docker-compose una vez completada la instalación de Docker.


### Instalacion.

Clonar el proyecto
```sh
git clone https://github.com/jdht1992/ksp.git          
```

Para crear la imagen ejecutas los siguientes comandos
```sh
cd ksp
docker-compose up --build
```

### Ejecutar proyecto.

Para ejecutar las migraciones, abrir otra terminal y entrar al contenedor y ejecutar los siguientes comandos.
```sh
docker-compose exec web bash 
python manage.py migrate
```

Usuario para ingresar 
```sh
username: usuario
password: 1234
```

## Rutas del proyecto
### Employee

Pagina principal
```sh
  localhost:8000
  http://ec2-3-136-157-156.us-east-2.compute.amazonaws.com:8000/
```

Login para acceder a las vistas
```sh

127.0.0.1:8000/accounts/login/
http://ec2-3-136-157-156.us-east-2.compute.amazonaws.com:8000/accounts/login/

```

Lista para poder ver todos los Employee
```sh
127.0.0.1:8000/employee/list
```

Crear Employee
```sh
127.0.0.1:8000/employee/create
```

Detalle del Employee
```sh
127.0.0.1:8000/employee/detail/<employee_id>/
```

Actualizar Employee
```sh
127.0.0.1:8000/employee/update/<employee_id>
```

Eliminar el Employee
```sh
127.0.0.1:8000/employee/delete/<employee_id>
```

### Beneficiary
Crear beneficiario
```sh
127.0.0.1:8000/beneficiary/create/<employee_id>
```

Detalle del beneficiario
```sh
127.0.0.1:8000/beneficiary/detail/<beneficiary_id>
```

Actualizar beneficiario
```sh
127.0.0.1:8000/beneficiary/update/<beneficiary_id>
```

Eliminar beneficiario
```sh
127.0.0.1:8000/beneficiary/delete/<beneficiary_id>
```
