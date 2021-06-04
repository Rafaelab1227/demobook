# Add-on Nbgrader



***Nbgrader*** es una herramienta que ayuda en el proceso de creación y calificación de tareas basadas en Jupyter Notebooks.

Para su uso es necesario primeramente la creación de una versión del instructor o docente, segundo, la herramienta crea automáticamente la versión del estudiante que deberá ser distribuida o recogida por el instructor; tercero, permite la calificación automática, la calificación manual y la generación de feedback en comentarios visibles para el estudiante.

Al integrarlo con JupyterHub se puede distribuir y recoger las tareas automáticamente, el estudiante al ingresar se encontrará en su sesión con todas las tareas asignadas y podrá enviarlas directamente. Al igual, el instructor podrá recibir automáticamente las entregas y calificarlas.  

Documentación https://nbgrader.readthedocs.io/en/stable/index.html

Este add-on permite que los cuadernos puedan ser calificados automáticamente de forma masiva y al mismo tiempo que sean evaluados manualmente para ajustar puntajes, adicionar comentarios o valorar respuestas abiertas o tasks. La definición de la tarea debe considerar qué tipo de celda constituye cada entrada existiendo varias alternativas:

1) **Manually graded answer**: pregunta abierta que permite edición en la misma celda.
2) **Manually graded task**: pregunta abierta que no permite edición, esta pensada para definir enunciados de tareas que involucrarán generar más celdas.
3) **Read-only**: celdas de lectura.
4) **Autograded answer**: definición de la pregunta.
5) **Autograded test**: guarda los test tipo ***assert*** o similar para corroborar resultados, aquí se marca el puntaje que obtendrá el alumno, estas no podrán ser editadas por el rol de estudiante.

Por ejemplo:

### Celda tipo ***Read-only***

### 1) Create a function to count words in a phrase, the result should be just a number.

### Celda tipo ***Autograded answer***

# Definition of the function
def myfunction1(phrase):
    
    ### BEGIN SOLUTION
    # Remove spaces and split phrase
    return(len(phrase.strip().split(" ")))
    ### END SOLUTION

### Celda tipo ***Autograded test***

# Test the function
assert myfunction1("La vida no es esperar que pase la tormenta. Es aprender a bailar bajo la lluvia.")== 16
### BEGIN HIDDEN TESTS
assert myfunction1("Práctica demo nbgrader") == 3
assert myfunction1("Práctica demo nbgrader test") == 4
### END HIDDEN TESTS

### Celda tipo ***Manually graded task***

### 4) Create a list of Python data types

# YOUR ANSWER BELOW IN ONLY ONE CELL

=== BEGIN MARK SCHEME ===

Answer :

Numeric data types: int, float, complex
String data types: str
Sequence types: list, tuple, range
Binary types: bytes, bytearray, memoryview
Mapping data type: dict
Boolean type: bool
Set data types: set, frozenset

=== END MARK SCHEME ===

### Video de la presentación oficial de Nbgrader en la conferencia SciPy 2017

from IPython.display import HTML

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/5WUm0QuJdFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')