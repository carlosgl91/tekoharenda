# Temperatura anual promedio en el periodo 1991-2019

**Tipo de Dato:** climáticos

**Descripción:** Para la generación de datos de temperatura se utilizó el set de datos de ERA 5 - Land1, el cual es un reanálisis
climático desarrollado por el ECMWF (Centro Europeo de Predicción Meteorológica a Medio Plazo).
Concretamente, se utilizó la banda de temperatura del aire (2m) en Kelvin, la cual fue convertida a grados
centígrados mediante la sustracción de 273,15.

**Resolución Espacial:** 11132  metros

**Fuente Original:** ERA5-Land Hourly - ECMWF Climate Reanalysis

**Fecha de Publicación:** 2019

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/temp"); 

Map.addLayer(dataset, {}, 'Temperatura anual promedio');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Muñoz Sabater, J., (2019): ERA5-Land monthly averaged data from 1981 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). (<date of access>), doi:10.24381/cds.68d2bb30*
