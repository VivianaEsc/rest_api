# Proyecto API Rest con Django y Django Rest Framework

## Descripción del Proyecto
Este proyecto implementa una API Rest utilizando Django y la librería Django Rest Framework (DRF). Está estructurado en varios módulos que gestionan diferentes aspectos de la aplicación, como usuarios y productos. A continuación se detallan las configuraciones y los módulos incluidos.

## Contenidos
1. [Configuraciones del Proyecto] 
   - [Conexión a base de datos MySQL]
   - [Configuración de Endpoints (Rutas)]
2. [Módulos](#2-módulos)
   - [Módulo Base] 
   - [Módulo Usuarios] 
   - [Módulo Productos] 

### 1. Configuraciones del Proyecto

#### 1.1 Conexión a base de datos MySQL
**Herramientas:**
- Django
- MySQL
- Conector MySQL para Python (por ejemplo, MySQLclient)

**Proceso:**
1. Instalar el conector MySQL.
2. Configurar la base de datos en Django actualizando el archivo `settings.py`.
3. Ejecutar migraciones para sincronizar los modelos de datos con la base de datos MySQL.

#### 1.2 Configuración de Endpoints (Rutas)
**Herramientas:**
- Django Rest Framework

**Proceso:**
1. Definir las rutas de la API en los archivos de configuración de URLs para cada módulo.
2. Registrar vistas para manejar las solicitudes de la API.

### 2. Módulos

#### 2.1 Módulo Base
**Propósito:**
- Proveer funcionalidades y modelos comunes para otros módulos.

**Modelo de datos:**
- **id**: Identificador único del registro.
- **estado**: Estado actual del registro (activo, inactivo, etc.).
- **fecha creación**: Fecha y hora de creación del registro.
- **fecha modificación**: Fecha y hora de última modificación del registro.
- **fecha borrado**: Fecha y hora de eliminación del registro (si aplica).

**Proceso:**
1. Definir el modelo base.
2. Implementar el serializer para el modelo base.
3. Crear vistas para operar con los datos del modelo base.

#### 2.2 Módulo Usuarios
**Propósito:**
- Gestionar la información y operaciones relacionadas con los usuarios.

**Modelo de datos:**
- **nombre**: Nombre completo del usuario.
- **correo electrónico**: Dirección de correo electrónico del usuario.
- **contraseña**: Contraseña del usuario.
- **nombre de usuario**: Identificador único del usuario en el sistema.
- **fecha de registro**: Fecha de registro del usuario.
- **último inicio de sesión**: Fecha y hora del último inicio de sesión del usuario.
- **roles**: Roles o permisos asociados al usuario.

**Proceso:**
1. Extender el modelo de usuario base de Django con campos adicionales.
2. Actualizar el serializer del usuario.
3. Modificar las vistas de usuario para gestionar la creación, actualización y consulta de usuarios.

#### 2.3 Módulo Productos
**Propósito:**
- Manejar el registro e información de productos.

**Modelo de datos:**
- **nombre**: Nombre del producto.
- **descripción**: Descripción del producto.
- **categoría**: Categoría del producto.
- **unidad de medida**: Unidad de medida del producto (por ejemplo, kg, litros).
- **imagen**: Imagen del producto.

**Proceso:**
1. Definir el modelo de producto.
2. Crear el serializer de producto.
3. Desarrollar vistas para la creación, actualización y consulta de productos.

---

 
