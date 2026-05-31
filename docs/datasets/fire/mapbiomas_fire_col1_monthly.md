# MapBiomas Fuego colección 1  1999-2024 (mensual)

**Categoría:** Fuego

**Descripción:** El conjunto de datos de Área Quemada Mensual abarca el periodo comprendido entre 1999 y 2024; los datos de cada píxel se obtienen del mosaico anual, basándose en la fecha de la imagen satelital. Este conjunto indica el mes (del 1 al 12) en el que se produjo el incendio para cada píxel dentro de dicho periodo.

**Resolución Espacial:** 30 metros

**Fuente Original:** Mapbiomas Paraguay

**Fecha de Publicación:** 1999-2024

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:   

```javascript
    
    var mapbiomasAsset = 'projects/arapy-487423/assets/mapbiomas_fire_col1_monthly'; 
    var image = ee.ImageCollection(mapbiomasAsset);
    print(image)
        
    Map.centerObject(image.first())
    var imagemasked = image.first()
    imagemasked = imagemasked.updateMask(imagemasked) 
    Map.addLayer(imagemasked,{ palette:["red"]},"Extensión de áreas quemadas monthly" )

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *MapBiomas fuego - Paraguay. (2025). MapBiomas Paraguay Fuego collección 1. Disponible en: https://paraguay.mapbiomas.org/*
