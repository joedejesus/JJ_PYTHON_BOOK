# Enunciado:
"""El método ".splitlines()" en Python se utiliza para dividir una  cadena  de  texto  que  contiene
varias líneas, separadas por saltos de línea como (\n) o retornos de carro (\r), en  una  lista  que
incluye cada una de esas líneas como elemento. Esto significa que, dado un texto que contiene varias
líneas, obtendremos una lista en la que cada línea será  un  elemento.  Este  método  es  útil  para
procesar texto que contiene múltiples líneas, como archivos de texto o cadenas con saltos  de  línea
incrustados.

El método toma una cadena de texto que contiene múltiples líneas y devuelve una lista de subcadenas,
donde cada subcadena corresponde a una línea del texto original.  Por  defecto,  los  caracteres  de
salto de línea utilizados en la cadena original no se incluyen en las subcadenas  resultantes,  pero
esto puede cambiar si se pasa el argumento opcional "keepends" con el valor "True", de  esta  forma:
".splitlines(keepends=True)".

El método ".splitlines()" no requiere argumentos obligatorios para funcionar, pero  puede  tomar  un
argumento opcional llamado "keepends", que es un valor  booleano.  Si  "keepends"  se  establece  en
"True", los caracteres de salto de línea se incluirán en las subcadenas resultantes. Si se  omite  o
se establece en "False", los caracteres de salto de línea se eliminan de las subcadenas resultantes.
Esto permite que los caracteres de salto de línea se mantengan, o no, al final de cada línea en  las
subcadenas generadas, proporcionando mayor flexibilidad en el procesamiento del texto.

Por último, el método ".splitlines()" es útil para dividir cadenas de texto en líneas  individuales,
facilitando el procesamiento de texto multilínea. Su flexibilidad y facilidad de uso  lo  convierten
en una herramienta esencial para trabajar con datos textuales que contienen múltiples  líneas,  como
"logs", archivos de configuración o cualquier texto estructurado en líneas."""

# Ejemplo_3_metodo_splitlines.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene  múltiples
líneas separadas por saltos de línea (\n). Utilizamos tres comillas dobles para indicar que se trata
de un texto multilínea. Esta cadena de texto se  utilizará  para  demostrar  el  funcionamiento  del
método ".splitlines()".

A continuación, definimos una nueva variable llamada "lista_lineas" y le asignamos el  resultado  de
aplicar el método ".splitlines()" a la variable "texto" sin ningún argumento. Para ello,  escribimos
el nombre de la variable, seguido del nombre del método ".splitlines()".

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar cómo se dividió el texto contenido en  la
variable "texto".

De esta forma, hemos dividido la cadena de texto multilínea en subcadenas basadas en los  saltos  de
línea, obteniendo  una  lista  que  contiene  las  líneas  de  la  cadena  original  como  elementos
individuales."""

# Código:
texto = """Línea 1\nLínea 2\nLínea 3\nLínea 4\nLínea 5"""
lista_lineas = texto.splitlines()
print(f"Cada línea del texto: \n{texto}\nSe ha dividido y convertido en un elemento de la lista: {lista_lineas}\n")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".splitlines()" no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa  que  siempre  se  genera  una
nueva lista como resultado de su aplicación, dejando intacta la cadena original. Este comportamiento
garantiza que el texto original permanezca sin modificaciones, lo cual es crucial en contextos donde
se requiere mantener la integridad de los datos originales.

Además, si se desea almacenar el resultado del método ".splitlines()", es necesario asignarlo a  una
nueva variable o usar directamente el resultado en una operación  posterior.  De  lo  contrario,  el
resultado se perderá. Por ejemplo, si no se asigna a una variable o no se utiliza inmediatamente, la
lista generada por ".splitlines()" no será accesible posteriormente.

Este método es especialmente útil para procesar texto multilínea, como el contenido de  archivos  de
texto o cadenas generadas dinámicamente que contienen saltos de línea. Además, el argumento opcional
"keepends" proporciona flexibilidad adicional al permitir incluir o excluir los caracteres de  salto
de línea en las subcadenas resultantes. Esto puede ser particularmente valioso en situaciones  donde
el formato del texto,  incluidos  los  saltos  de  línea,  sea  relevante  para  el  análisis  o  el
procesamiento posterior.

Por último, el método ".splitlines()" es una herramienta poderosa y versátil para dividir cadenas de
texto en líneas individuales,  permitiendo  un  manejo  eficiente  y  flexible  de  datos  textuales
estructurados en múltiples líneas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
