# **Desarrollo de software en Python**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow)

Este proyecto organiza ejercicios y utilidades en Python con un enfoque modular, escalable y orientado a buenas prácticas de desarrollo. Está diseñado para exploración de estructuras de datos, análisis de información y visualización, incluyendo procesamiento de grandes volúmenes de datos y desarrollo de aplicaciones web interactivas.

## 📊 Antes de comenzar: *¿Por que elegir Python?*
Python se destaca como lenguaje de referencia para análisis de datos y visualización por varias razones técnicas:

### Ecosistema optimizado de librerías:
`numpy` y `pandas` gestionan datos tabulares y arreglos multidimensionales con eficiencia de memoria y velocidad cercana a C.

`matplotlib`, `seaborn` y `plotly` soportan visualización estática y dinámica de grandes datasets.

`networkx` permite procesamiento de grafos complejos y operaciones sobre conjuntos de datos interrelacionados.

### Ejecución y máquina virtual:
`CPython` interpreta bytecode ejecutado sobre la Python Virtual Machine, gestionando memoria mediante recolección automática de basura. 

La VM permite aislamiento, robustez y compatibilidad multiplataforma.

### Gestión eficiente de recursos:
Operaciones en **numpy y pandas son vectorizadas**, evitando bucles explícitos en Python y optimizando el uso de CPU. Con posibilidad de **procesamiento en chunks**, para datasets que superan la capacidad de RAM.

Soporte para paralelización (`threading`, `multiprocessing`, `dask`) y ejecución en GPU (con librerías externas como cuDF).

### Flexibilidad para integración:
Conexión directa con bases de datos **SQL/NoSQL**. Integración con APIs de Big Data y frameworks de computación distribuida como `PySpark` y `Ray`. Ejecución interactiva en notebooks o entornos web (Jupyter, Streamlit, Dash).

### Robustez y mantenibilidad:
Manejo de excepciones, tipado dinámico y estructuras de control claras. Extensibilidad mediante carga dinámica de módulos (`importlib`) y ejecución concurrente.

Arquitectura modular y empaquetamiento mediante __init__.py.

<br>

# 🗂️ Arquitectura del proyecto
Aquí encontrarás ejercicios, scripts y utilidades que exploran tanto lo básico como aspectos más avanzados del lenguaje.
Este proyecto tiene como objetivo **reforzar y organizar mi aprendizaje** en programación con Python, usando una estructura 
modular que facilita la escalabilidad, la reutilización de código y el uso de buenas prácticas.

## Breve resumen de la aplicación

Cada subdirectorio de ***project/script/*** representa un módulo temático y contiene lo siguiente.

Dentro del package **scripts** vamos a tener cada módulo que contendrá:
  - `exerciseN.py:` Ejercicios específicos de ese módulo.
  - `__main__.py:` Punto de entrada principal del módulo.
  - `__menu__.py:` Menú con un breve enunciado sobre qué hace cada ejercicio.
  - `__init__.py:` Necesario para que el directorio sea tratado como un paquete.


Dentro de **web_app** se encuentra una aplicación web desarrollada con **Flask y SocketIO**, 
que permite ejecutar y visualizar ejercicios desde el navegador con una terminal 
interactiva integrada (basada en **xterm.js**). Está diseñada para facilitar pruebas, 
depuración y ejecución dinámica de código Python.

``` bash
.Python-practices-llcejas
├── .venv/
├── lib/                     
├── data/                      
├── outputs/                    
├── project/                       
│   ├── data/
│   ├── documents/
│   ├── outputs/
│   ├── scripts/
│   │   ├── python_basic/
│   │   │   ├── conditionals/
│   │   │   ├── cycle_for/
│   │   │   ├── cycle_while/
│   │   │   ├── dictionaries/
│   │   │   ├── lists/
│   │   │   ├── sets/
│   │   │   ├── tuples/
│   │   │   └── __init__.py
│   │   ├── python_expert/
│   │   │   ├── matplotlib/
│   │   │   ├── networkx/
│   │   │   ├── numpy/
│   │   │   ├── pandas/
│   │   │   ├── venn_diagrams/
│   │   │   └── __init__.py
│   │   ├── utils/
│   │   ├── __runtime__.py
│   │   └── __init__.py
│   │
│   ├── web_app/            
│   │   ├── static/  
│   │   │    ├── img/
│   │   │    ├── javascript/
│   │   │    ├── style/
│   │   │    └── xterm/   
│   │   ├── templates/    
│   │   ├── modules.py
│   │   ├── routes.py             
│   │   ├── socketio_handlers.py     
│   │   ├── __main__.py     
│   │   └── __init__.py 
│   │        
│   └── test/                      
│       ├── test.py
│       └── __init__.py
├── .gitignore
├── requirements.txt                 
└── README.md                  
```

<br>

# ⚙️ Configuración del Entorno de Desarrollo
Para evitar conflictos entre dependencias y mantener el proyecto aislado del sistema, se recomienda usar un entorno virtual.  Una vez activado, todos los paquetes que instales con `pip` quedarán guardados dentro de **.venv/**. 

El directorio **.venv/** no debe subirse al repositorio, por eso se incluye en `.gitignore`.

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

#Guardar dependencias (opcional)
pip freeze > requirements.txt

```




### `__init__.py`: Estructura y organización de paquetes

Este archivo convierte una carpeta en un **paquete de Python**. Aunque en versiones recientes no es obligatorio, se recomienda incluirlo por:
- Organización del código

- Compatibilidad retroactiva 

- Importaciones controladas

- Permite ejecutar con **'python -m'** sin errores

Incluso si el archivo está vacío, su presencia mejora la claridad y el mantenimiento del proyecto.

### `python3 -m`: Lanzamiento de módulos desde la terminal

Desde la raíz del proyecto donde se encuentran: 
**( README.md | .gitignore | .venv | project )**, podés ejecutar cualquier módulo usando:
```bash
# Ejemplo teórico
python3 -m project.scripts.python_expert.nombre_modulo

# Ejemplo práctico
python3 -m project.scripts.python_expert.pandas
```

<br>

# 🌐 WebApp desde la terminal

La aplicación web se encuentra en el módulo WebApp y está construida con Flask y Flask-SocketIO. Esta app permite ejecutar ejercicios desde el navegador mediante una terminal interactiva basada en xterm.js. 

###  ¿Qué vas a ver en el navegador? 
- Un menú de ejercicios disponibles. 
- Una terminal interactiva (basada en xterm.js).
- La posibilidad de ejecutar código en vivo desde el navegador.

Para levantar la WebApp, desde la raíz del proyecto, ejecutá:
```bash
   python3 -m project.web_app
```

Esto iniciará el servidor Flask, que por defecto corre en:
> Running on http://localhost:5000 \
> Press CTRL+C to quit



# 🤝 Contribuciones
El repositorio está abierto a mejoras, sugerencias o análisis de implementación. Se aceptan issues y pull requests orientados a extender, mejorar o refactorizar los módulos existentes.