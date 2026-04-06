# Áreas certificadas bajo el régimen de servicios ambientales

**Tipo de Dato:** Estatus de protección

**Descripción:** áreas certificadas bajo el régimen de servicios ambientales (ACSA) presentan un estatus distinto de restricción de uso. Los datos utilizados corresponden a la base de datos espacial de áreas certificadas del MADES (MADES, 2022b).

Los datos fueron procesados a fin de obtener una capa raster binaria, donde el valor “1” corresponde a píxeles cubiertos por ACSAs.
Rasterizado en base a Mapbiomas Paraguay Colección II. 

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

Datos procesados:
> *Giménez, C. (2026). Capa raster binaria de Áreas Certificadas bajo el Régimen de Servicios Ambientales (ACSA) de Paraguay (Versión 1.0) [Dataset de Google Earth Engine]. Tekoharenda: Catálogo Nacional de Datos Espaciales. https://carlosgl91.github.io/tekoharenda/*
