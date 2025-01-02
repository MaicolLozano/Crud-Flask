# Aplicación CRUD con Flask

Una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) simple construida con Flask y MySQL.

## Estructura del Proyecto
```
CRUD/
├── app.py              # Archivo principal de la aplicación
├── db.sql             # Esquema de la base de datos
├── templates/         # Plantillas HTML
│   ├── index.html    # Página principal
│   └── actualizar.html # Formulario de actualización
```

## Requisitos Previos
- Python 3.x
- MySQL
- pip (Instalador de paquetes de Python)

## Instrucciones de Configuración
1. Instalar script `db.sql` en la base de datos MySQL.

## Ejecutar la Aplicación
1. Ejecutar la aplicación Flask:
```bash
python app.py
```
2. Abrir el navegador web y navegar a `http://localhost:5000`

## Características
- Crear nuevos registros
- Ver todos los registros
- Actualizar registros existentes
- Eliminar registros

