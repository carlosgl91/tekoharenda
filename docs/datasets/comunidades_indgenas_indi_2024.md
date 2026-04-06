# Comunidades indígenas INDI 2024

**Tipo de Dato:** Estatus de protección

**Descripción:** Los datos fueron procesados a fin de obtener una capa raster binaria, donde el valor “1” corresponde a píxeles cubiertos por comunidades indígenas y 0 a áreas no cubiertas por dichas áreas de acuerdo con ambas bases de datos.

**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a patir de INDI 2017

**Fecha de Publicación:** 2017

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/com_ind_INDI_raster_2017"); 

Map.addLayer(dataset, {}, 'Comunidades indígena FAPI 2024');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Instituto nacional del indígena  Paraguay (INDI). 2017. Base de datos de comunidades indígenas del Paraguay.  Disponible en https://informacionpublica.paraguay.gov.py/#!/ciudadano/solicitud/63421*
