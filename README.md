# Proyecto 1: Modelado y Programación 

## Descripción:
Programa que obtiene el clima del aereopuerto de salida y de destino según sus coordenadas, dado 
un archivo en formato `.csv` de donde obtenemos la información. 

## Ejecución:
Primero, clone el repositorio.

``` sh
git clone https://github.com/AlbertNath/Proyecto01_MyP_2022_2.git
```

### Prerrequisitos:
Es necesario usar `python3` al momento de ejecutar.

Utilizamos las siguientes librerías en este proyecto, por lo que de no estar instaladas en su 
entorno de python, recomendamos sean seguir los correspondientes manuales de instalación:
- `requests`: [manual](https://docs.python-requests.org/es/latest/user/install.html)
- `csv`: [manual](https://pypi.org/project/python-csv/)
- `tkinter`: [manual](https://www.tutorialspoint.com/how-to-install-tkinter-in-python)

Una vez comprobado que estas librearías se encuentran en su entorno, debe ir al directorio 
`main`: 

``` sh
cd Proyecto01_MyP_2022_2/src/main/
```

Ahí encontrará el archivo `constantes.py`, en el cual debe introducir su llave de 
[OpenWeatherMap](https://openweathermap.org/) en la sección del string como se indica:

``` python
LLAVES = ['AQUI_VA_SU_LLAVE']
```

De lo contrario, el programa lanzará una excepción.

Con esto, ya puede proceder a ejecutar el programa.

### Pruebas: 
Para ejecutar las pruebas debe situarse en el directorio `src/` de la siguiente forma: 

```sh
cd Proyecto01_MyP_2022_2/src/
```

Luego, ejecute: 

``` sh
python3 -m unittest discover 
```

### Programa:
Para ejecutar el proyecto debe situarse en el directorio `src/` de la siguiente forma: 

```sh
cd Proyecto01_MyP_2022_2/src/
```

Después ejecutar

``` sh
python3 main/main.py
```

**Nota:** la ejecución del programa puede tomar unos segundos en procesar todas las respuestas de 
la API. 

## Documentación: 
El `pdf` solicitado se encuentra en el directorio `docs/`, bajo el nombre de `proyecto1.pdf`.

## Integrantes: 

- Karyme Ivette Azpeitia García
- Ui Chul Shin
- Alberto Natanael Medel Piña

## Bibliografía: 

1. [Requests Docs](https://docs.python-requests.org/en/latest/user/quickstart/)
1. [Unit Testing in Python Tutorial](https://www.datacamp.com/community/tutorials/unit-testing-python)
1. [Python Tutorial: Working with CSV file for Data Science](https://discord.com/channels/800826113906835474/800826113906835476/951709877401710653)
1. [tkinter — Interface de Python para Tcl/Tk](https://docs.python.org/es/3/library/tkinter.html)
1. [Python | Accessing Key-value in Dictionary ](https://discord.com/channels/800826113906835474/800826113906835476/951709366275407922)
1. [Python regex | Check whether the input is Floating point number or not](https://www.geeksforgeeks.org/python-regex-check-whether-the-input-is-floating-point-number-or-not/)
1. [Dictionaries in Python](https://realpython.com/python-dicts/)
