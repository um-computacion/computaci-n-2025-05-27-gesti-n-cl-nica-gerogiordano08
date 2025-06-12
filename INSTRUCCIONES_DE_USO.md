# INSTRUCCIONES DE USO

## USO DE INTERFAZ

Para comenzar a usar el script se debe ejecutar desde el directorio principal el siguiente comando:

```
python3 cli_interfaz/main.py
```

Así accederemos a la interfaz principal del script, que nos da las siguientes opciones: <br/> -**_Agregar paciente_**<br/> -**_Agregar médico_**<br/> -**_Agendar turno_**<br/> -**_Agregar especialidad_**<br/> -**_Emitir receta_**<br/> -**_Ver historia clínica_**<br/> -**_Ver todos los turnos_**<br/> -**_Ver todos los pacientes_**<br/> -**_Ver todos los médicos_**<br/> -**_Salir_**<br/>

- Para agregar a un paciente ingresamos **'1'**, luego ingresamos el DNI del paciente, su nombre y su fecha de nacimiento con el formato (AAAA-MM-DD)
- Para agregar un médico ingresamos **'2'**, luego ingresamos su matricula, su nombre y procedemos a ingresar sus especialidades: primero la cantidad de especialidades que posee, nombramos la primera, ingresamos la cantidad de dias en los que la atiende y por ultimo ingresamos dichos dias. Esto se repetira tantas veces como la cantidad de especialidades que hayamos ingresado.
- Para agendar un turno ingresamos **'3'**, luego ingresamos el DNI del paciente, la matricula del medico, la especialidad de la consulta, y la fecha y hora de la consulta en el formato (AAAA-MM-DD hh-mm). La fecha DEBE caer en un dia en el que el médico atienda la especialidad para poder registrar el turno.
- Para agregar una especialidad al perfil de un médico ingresamos **'4'**, luego ingresamos la matricula del médico en cuestion, el nombre de la especialidad, la cantidad de dias a la semana en los que se atendera, y nombramos cada día.
- Para emitir una receta ingresamos **'5'**, ingresamos el DNI del paciente, la matricula del médico, la cantidad de medicamentos que se recetaran, y procedemos a nombrar cada medicamento.
- Para ver una historia clínica ingresamos **'6'**, ingresamos el DNI del paciente y podremos ver la historia clínica.
- Para ver todos los turnos registrados en la clínica ingresamos **'7'**.
- Para ver todos los pacientes registrados en la clínica ingresamos **'8'**.
- Para ver todos los médicos registrados en la clínica ingresamos **'9'**.
- Si precisamos salir del sistema, ingresamos **'0'**.

## USO DE TESTS

Para usar los tests, desde el directorio principal, usamos la siguiente linea:

```
python3 -m unittest tests/(nombre)_tests.py
```

Donde nombre es uno de los siguientes:

- _rec_ para los tests de recetas, que incluyen:
  - Testear si las recetas se emiten exitosamente.
  - Testear si da error al intentar emitir una receta con un médico no existente.
  - Testear si da error al intentar emitir una receta con un paciente no existente.
  - Testear si da error al intentar emitir una receta con un medicamento vacio.
  - Testear si da error al intentar emitir una receta con la cantidad de medicamentos == 0.
- _turn_ para los tests de turnos, que incluyen:
  - Testear si los turnos se agendan exitosamente.
  - Testear si da error al intentar agendar una turno duplicado.
  - Testear si da error al intentar agendar un turno para un paciente no existente.
  - Testear si da error al intentar agendar un turno para un médico no existente.
  - Testear si da error al intentar agendar un turno para una especialidad no disponible.
- _pac_med_ para los tests de pacientes y médicos, que incluyen:
  - Testear si los registros de médicos son exitosos.
  - Testear si da error al intentar registrar un médico duplicado.
  - Testear si da error al intentar registrar un médico con la matricula vacía.
  - Testear si da error al intentar registrar un médico con el nombre vacío.
  - Testear si da error al intentar registrar un médico con datos incorrectos en las especialidades.
  - Testear si los registros de pacientes son exitosos.
  - Testear si da error al intentar registrar un paciente duplicado.
  - Testear si da error al intentar registrar un paciente con el DNI vacío.
  - Testear si da error al intentar registrar un paciente con el nombre vacío.
  - Testear si da error al intentar registrar un paciente con una fecha de nacimiento invalida.
- _hc_ para los tests de historias clínicas, que incluyen:
  - Testear que las recetas se registren correctamente en las historias clínicas.
  - Testear que los turnos se registren correctamente en las historias clínicas.
  - Testear que de error al pedir la historia clínica de un paciente que no esta registrado.
- _esp_ para los tests de especialidades, que incluyen:
  - Testear que las especialidades se agreguen correctamente.
  - Testear que de error al intentar registrar una especialidad ya registrada.
  - Testear que de error al ingresar un dia de la semana invalido.
  - Testear que de error al intentar registrar una especialidad para un médico no existente.

# GRACIAS POR UTILIZAR
