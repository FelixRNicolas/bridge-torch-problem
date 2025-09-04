# Bridge and Torch Problem 
Una solución simple para el acertijo lógico "El Puente y la Antorcha" usando Python (enfoque matemático) y C++ (fuerza bruta).

# Acerca del problema
*"Cuatro personas llegan a un río en la noche. Hay un puente angosto, y solo puede soportar a dos personas a la vez. Tienen una antorcha y, como es de noche, la antorcha debe usarse al cruzar el puente. Cuando dos personas cruzan el puente juntas, deben avanzar al ritmo de la persona más lenta. Una persona tiene que regresar con la antorcha."* [- Fuente](https://en.wikipedia.org/wiki/Bridge_and_torch_problem)

El tiempo de cruce para cada individuo **puede variar**, pero en general buscamos el tiempo de cruce óptimo para un conjunto determinado de personas.

# Acerca del programa en Python
Este enfoque utiliza la siguiente implementación matemática para determinar el tiempo de cruce óptimo, así como la combinación de *"cruces"* o *"pasos"* a seguir para lograr el tiempo final:

$Cuando: A<B<C<D:$
<p align="center"> $min(2A + B + C + D, A + 3B + D)$ </p>

En resumen, esta ecuación representa las dos ***"estrategias de cruce"*** (canónicas) más eficientes. Dado que hay varias formas de enviar y traer de vuelta la antorcha, se comparan las posibles mejores rutas, y se elige la de menor tiempo, evitando así revisar todas las combinaciones y resultados posibles, ya que la mayoría, si no todas, producirán tiempos más altos.

**TL;DR:** Este programa revisa todas las estrategias conocidas más eficientes y se queda con la más óptima.
