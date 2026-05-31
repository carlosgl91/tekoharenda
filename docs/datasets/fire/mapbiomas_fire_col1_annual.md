# MapBiomas Fuego colección 1  1999-2024 (anual)

**Categoría:** Fuego

**Descripción:** El conjunto de datos de Áreas Quemadas Anuales abarca el periodo comprendido entre 1999 y 2024, identificando las áreas cartografiadas como quemadas para cada año. También incluye la Cobertura Anual de Áreas Quemadas, la cual representa la superficie quemada anualmente para cada clase de uso y cobertura del suelo; cada píxel contiene el valor correspondiente de uso y cobertura del suelo —proveniente de la Colección 2— para la clase que resultó quemada.

**Resolución Espacial:** 30 metros

**Fuente Original:** Mapbiomas Paraguay

**Fecha de Publicación:** 1999-2024

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:   

```javascript
         var mapbiomasAsset = 'projects/arapy-487423/assets/mapbiomas_fire_col1_annual'; 
        var image = ee.ImageCollection(mapbiomasAsset);
        print(image)
        
  Map.centerObject(image.first())
  var imagemasked = image.first().eq(1)
  imagemasked = imagemasked.updateMask(imagemasked) 
  Map.addLayer(imagemasked,{ palette:["red"]},"Extensión de áreas quemadas" )

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *MapBiomas fuego - Paraguay. (2025). MapBiomas Paraguay Fuego collección 1. Disponible en: https://paraguay.mapbiomas.org/*
