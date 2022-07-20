# Project name

Pokemon api.

# Version 

Versión en desarrollo v.0.1

## Description

Desarrollo de endpoints para la pokemon api.

## Requirements and Installation

Se pueden ver en el archivo requirements.txt.

## Ejecutar la app

```bash
docker-compose build
```

luego

```bash
docker-compose up
```

## Ejecutar las pruebas unitarias

```bash
docker exec -it poke-app sh

```

luego

```bash
python manage.py test
```

## Ejecutar el comando para la cadena de evolución

```bash
docker exec -it poke-app sh

```

luego

```bash
python manage.py evolution_chain --id {id_evolution_chain}
```

ejemplo 

```bash
python manage.py evolution_chain --id 1
```

## Consultar el pokemon deseado


http://localhost:8000/api/pokemon/bulbasaur/
