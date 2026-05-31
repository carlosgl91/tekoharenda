# Formaciones forestales mayores o iguales a 1ha - Año 2023

**Categoría:** Uso y cobertura del suelo

**Descripción:** Esta capa consiste en los parches de formaciones forestales correspondientes a “Leñosas cerradas” y “leñosas inundables” de la capa de MapBiomas Paraguay colección 2 correspondiente al año 2023, cuyo tamaño es mayor o igual a 1 ha.

**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a partir de Mapbiomas Paraguay colección 2

**Fecha de Publicación:** 2023

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/forest_1ha_col"); 
Map.addLayer(dataset, {}, 'Formaciones forestal...');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *MapBiomas Paraguay. (2024). MapBiomas Paraguay collección 2. Disponible en: https://paraguay.mapbiomas.org/*
