# Áreas certificadas bajo el régimen de servicios ambientales

**Tipo de Dato:** Estatus de protección
**Descripción:** 30m rasterized based on Mapbiomas grid

**Resolución Espacial:** 30 metros
**Fuente Original:** Ministerio del Ambiente y Desarrollo Sostenible de Paraguay
**Fecha de Publicación:** Agosto 2022

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/eca/certified_areas_dec_2022"); 
Map.addLayer(dataset, {}, 'Áreas certificadas b...');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Ministerio del Ambiente y Desarrollo Sostenible (MADES). 2022. Base de datos espacial de áreas certificadas bajo el régimen de la ley 3001/06. Paraguay*
