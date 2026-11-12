# Django - Laboratorio 02 (Formularios y Cálculos)

Aplicación web desarrollada en **Django** para el Laboratorio 02 del curso **Desarrollo de Aplicaciones Empresariales (DAE)**. Se enfoca en el procesamiento de peticiones HTTP (`GET`/`POST`), captura de datos mediante formularios HTML y renderizado dinámico de resultados.

## Funcionalidades y Vistas (`encuesta/`)

* **Formulario y Respuesta (`formulario.html` / `respuesta.html`):** Captura de datos del usuario y visualización procesada en pantalla.
* **Operaciones Matemáticas (`operaciones.html`):** Interfaz para realizar cálculos aritméticos desde el servidor.
* **Cálculo Geométrico (`cilindro.html`):** Formulario especializado para calcular propiedades (como área o volumen) de un cilindro.

## Estructura del Proyecto

```text
Django-Lab02-DAE/
├── lab02/
│   ├── manage.py
│   ├── lab02/                  # Configuración principal (settings.py, urls.py)
│   └── encuesta/               # Aplicación principal con vistas, URLs y templates HTML
│       └── templates/encuesta/
│           ├── cilindro.html
│           ├── formulario.html
│           ├── operaciones.html
│           └── respuesta.html
└── requirements.txt            # Dependencias del entorno (Django 6.1.2)
```

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com
   cd Django-Lab02-DAE
   ```
2. Crea un entorno virtual, actívalo e instala las dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor local desde `lab02`:
   ```bash
   cd lab02
   python manage.py runserver
   ```
