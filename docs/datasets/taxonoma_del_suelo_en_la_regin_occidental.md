# Taxonomía del suelo en la Región Occidental

**Tipo de Dato:** categorico
**Descripción:** El proyecto Sistema Ambiental del Chaco (PSACh) BGR (Bundesanstalt für Geowissenschaften und
Rohstoffe  Hannover / Rca. Federal de Alemania Cooperación Técnica y el MAG/SSERNMA-DOA
generó datos para la región Occiental basados en el sistema del Mapa Mundial de Suelos (FAO-UNESCO,
1990) con una escala de trabajo de 1:250.000 y publicación de 1:750.000.
Los datos fueron curados en su formato vectorial y posteriormente rasterizados al nivel de subtipos,
utilizando como grilla de referencia el dataset de MapBiomas Paraguay colección 2. Se generó así mismo
un diccionario de datos el cual incluye los códigos raster y descripción de acuerdo con la legenda FAO 1990

**Resolución Espacial:** 30m metros
**Fuente Original:** 
**Fecha de Publicación:** 1990

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/soil_type_FAO_1990_paraguay_BGR"); 
Map.addLayer(dataset, {}, 'Taxonomía del suelo ...');
```

