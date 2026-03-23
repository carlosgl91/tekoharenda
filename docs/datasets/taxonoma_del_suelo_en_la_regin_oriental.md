# Taxonomía del suelo en la Región Oriental

**Tipo de Dato:** categorico
**Descripción:** El proyecto Racionalización de Uso de la Tierra PRUT (1995) Banco Mundial  Ministerio de Agricultura
y Ganadería MAG / Subsecretaria de Estado de Recursos Naturales y Medio Ambiente (SEERNMA)  Dirección de Ordenamiento Ambiental (DOA), utiliza el sistema de clasificación jerárquica USDA Soil
Taxonomy, que busca agrupar suelos similares en categorías cada vez más generales. Fue diseñada para
apoyar los levantamientos de suelos en EE. UU., específicamente la correlación de series de suelos y la
provisión de nombres de unidades cartográficas con diversos niveles de detalle cartográfico (FAOa, 2025).
Los datos fueron curados en su formato vectorial y posteriormente rasterizados al nivel de subgrupos,
utilizando como grilla de referencia el dataset de MapBiomas Paraguay colección 2. Se generó así mismo
un diccionario de datos el cual incluye los códigos raster y descripción de acuerdo con la legenda FAO 1990
(Figura 20, Anexo A1)

**Resolución Espacial:** 30m metros
**Fuente Original:** 
**Fecha de Publicación:** 1995

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/soil_type_usda_soil_taxonomy"); 
Map.addLayer(dataset, {}, 'Taxonomía del suelo ...');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *López, O.; González, E.; Llamas, P.; Molinas, A.; Franco, E.; García. S.; Ríos, E. 1995. Estudio de
reconocimiento de suelos, capacidad de uso de la tierra y propuesta de ordenamiento territorial preliminar
de la Región Oriental del Paraguay (PRUT). Asunción, PY: MAG/SRNMA/BM/PRUT. v.1, 197 p*
