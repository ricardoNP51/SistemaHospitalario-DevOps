# SistemaHospitalario-DevOps

Proyecto académico mínimo para demostrar control de versiones e integración continua.
Modela una agenda de citas hospitalarias con datos ficticios. No utiliza datos de pacientes
reales ni pretende ser una aplicación clínica lista para producción.

## Objetivo
Aplicar ramas, commits descriptivos, Pull Requests y pruebas automáticas con GitHub Actions.

## Requisitos y ejecución
Python 3.12, sin dependencias externas.

```sh
python -m unittest discover -s tests -v
python -m compileall -q hospital tests
```

## Estructura
- `hospital/agenda.py`: registro de citas y prevención de duplicados.
- `tests/`: pruebas de los requisitos funcionales.
- `.github/workflows/ci.yml`: validación automática en cada push y Pull Request.

## Alcance
Prototipo en memoria, sin interfaz web, persistencia ni despliegue.
El resumen académico y las capturas personales se entregan en un PDF separado.

## Funcionalidad de acceso
`hospital/login.py` valida que usuario y clave no estén vacíos. No comprueba
identidades, almacena contraseñas ni otorga acceso; solo demuestra una rama de funcionalidad.
