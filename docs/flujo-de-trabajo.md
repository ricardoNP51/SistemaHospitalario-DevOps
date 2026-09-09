# Flujo de trabajo y criterios de aceptación

1. Definir la tarea y el resultado esperado.
2. Crear una rama de funcionalidad desde `develop`.
3. Hacer cambios pequeños y commits con mensajes descriptivos.
4. Ejecutar pruebas locales y publicar la rama.
5. Abrir un Pull Request hacia `develop`, inspeccionar el diff y comprobar CI.
6. Fusionar la funcionalidad cuando las comprobaciones sean exitosas.

Se usa `develop` porque la actividad lo solicita. Es una adaptación académica:
GitHub Flow normalmente integra ramas cortas directamente en la rama principal.

## Requisitos de la agenda
- Registrar una cita con paciente, médico y fecha.
- Rechazar identificadores vacíos y fechas de tipo incorrecto.
- Impedir que un médico o paciente tenga dos citas en el mismo instante.

## Pipeline
Cada push dispara GitHub Actions. El runner Ubuntu obtiene el repositorio,
prepara Python 3.12, compila los módulos y ejecuta unittest. Cualquier fallo
produce un resultado fallido. El pipeline demuestra CI; no despliega a producción.

## Planificación sugerida en GitHub Projects
Columnas: Pendiente, En curso, En revisión y Terminado. Tareas: agenda, pruebas,
automatización y formulario de acceso. Esta descripción no afirma que exista un tablero.
