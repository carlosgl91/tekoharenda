# Áreas silvestres protegidas de Paraguay actualizado a agosto de 2022

**Categoría:** Estatus de protección

**Tipología**: Raster binario

**Descripción:** Las áreas silvestres protegidas (ASPs) representan un estatus diferente de restricción de uso lo que deriva en una oferta potencial de recursos naturales y hábitat dependiendo del estado de conservación de estas. Los datos utilizados corresponden a la base de datos espacial de áreas silvestres protegidas del Ministerio del Ambiente y Desarrollo Sostenible (MADES) (MADES, 2022). Este conjunto de datos cuenta con 113 áreas protegidas y 3 áreas de reserva de biosfera distribuidas por todo el territorio de Paraguay.
Los datos fueron procesados a fin de obtener una capa raster binaria, donde el valor “1” corresponde a píxeles cubiertos por áreas protegidas y 0 a áreas no cubiertas por áreas protegidas. En la versión raster de los datos se excluyeron las reservas de biosfera

**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a partir de datos del MADES 2022

**Fecha de Publicación:** Agosto 2022

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
  
var dataset = ee.Image("projects/arapy-487423/assets/protected_areas_raster"); 
Map.addLayer(dataset, {}, 'Áreas silvestres pro...');

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Ministerio del Ambiente y Desarrollo Sostenible Paraguay (MADES). 2022. Base de datos espacial de áreas silvestres protegidas de Paraguay. Disponible en: https://informacionpublica.paraguay.gov.py/#!/ciudadano/solicitud/63421*
