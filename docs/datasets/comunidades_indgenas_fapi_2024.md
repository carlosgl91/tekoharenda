# Comunidades indígenas FAPI 2024

**Tipo de Dato:** Estatus de protección

**Descripción:** Los datos fueron procesados a fin de obtener una capa raster binaria, donde el valor “1” corresponde a píxeles cubiertos por comunidades indígenas y 0 a áreas no cubiertas por dichas áreas de acuerdo con ambas bases de datos.

**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a patir de FAPI 2024

**Fecha de Publicación:** 2024

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/com_ind_fapi_raster_2024"); 

Map.addLayer(dataset, {}, 'Comunidades indígena FAPI 2024');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Federación por la autodeterminación de los Pueblo Indígenas (FAPI). 2024. Base de datos de tierras indígenas de Paraguay. Disponible en: https://tierras-indigenas-2024-fapi.hub.arcgis.com/datasets/cbce905f55af4d508f775a0ee39b9cec/about*
