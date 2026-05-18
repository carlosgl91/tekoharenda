# Promedio anual de precipitación acumulada periodo 01-01-1994 a 01-01-2024

**Tipo de Dato:** climáticos

**Descripción:** Los datos de precipitación fueron calculados utilizando la base de datos CHIRPS Pentad: Climate Hazards Center InfraRed Precipitation With Station Data dentro de la plataforma Google Earth Engine abarcando el periodo 01-01-1994 a 01-01-2024. Los datos resultantes corresponden al promedio anual de precipitación acumulada en milímetros.

**Resolución Espacial:** 5566  metros

**Fuente Original:** CHIRPS pentad

**Fecha de Publicación:** 2015

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
    var paletteVibrant = [
    '#ffffff', // Blanco (0 mm)
    '#00ffff', // Cian (lluvia ligera)
    '#00bfff', // Azul claro (lluvia moderada)
    '#0000ff', // Azul (lluvia fuerte)
    '#800080'  // Púrpura (lluvia extrema)
    ];

    var paletteYlGnBu = [
    '#ffffcc', // Amarillo muy claro (poca/nula precipitación)
    '#c7e9b4', // Verde claro
    '#7fcdbb', // Turquesa
    '#41b6c4', // Azul medio
    '#2c7fb8', // Azul oscuro
    '#253494'  // Azul marino (alta precipitación)
    ];

    var precipVis = {
    min: 0,
    max: 2000, // Ajusta este valor al máximo de tus datos en mm
    palette:paletteYlGnBu
    
    };

    var dataset = ee.Image("projects/arapy-487423/assets/precipitation"); 

    Map.addLayer(dataset, precipVis, 'Promedio anual de precipitación');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Funk, Chris, Pete Peterson, Martin Landsfeld, Diego Pedreros, James Verdin, Shraddhanand Shukla, Gregory Husak, James Rowland, Laura Harrison, Andrew Hoell & Joel Michaelsen. "The climate hazards infrared precipitation with stations-a new environmental record for monitoring extremes". Scientific Data 2, 150066. doi:10.1038/sdata.2015.66 2015.*
