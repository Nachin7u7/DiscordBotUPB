# Bot UPB de Discord

Este bot de Discord permite a los usuarios consultar y modificar el saldo de monedas y diamantes asociados a un código de estudiante UPB.

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
```

2. Instala las dependencias necesarias usando pip:

```bash
pip install -r requirements.txt
```

## Configuración

1. Obtén un token de Discord para tu bot siguiendo las instrucciones en [Discord Developer Portal](https://discord.com/developers/applications).
2. Define una variable de entorno llamada `MyToken` con el token que obtuviste.
   - En sistemas Unix/Linux/macOS, puedes hacerlo ejecutando el siguiente comando en la terminal:

```bash
export MyToken=your_token_here
```

## Uso

1. Ejecuta el bot utilizando el siguiente comando:

```bash
python bot.py
```

2. Una vez que el bot esté en línea, puedes invocarlo en tu servidor de Discord prefijando los comandos con `b!`. Por ejemplo:
   - `b!ayuda`: Muestra la lista de comandos disponibles.
   - `b!saldo [código de estudiante UPB]`: Consulta el saldo de monedas y diamantes.
   - `b!coins [cantidad] [código de estudiante UPB]`: Añade monedas a la cuenta (solo para personal autorizado).
   - `b!diamonds [cantidad] [código de estudiante UPB]`: Añade diamantes a la cuenta (solo para personal autorizado).

## Pruebas

Puedes probar el bot en un servidor de Discord donde tengas permisos de administrador. Invita al bot al servidor y prueba cada comando para asegurarte de que funcione correctamente.

## Autores

Este bot fue desarrollado por el Equipo de DevOps.
