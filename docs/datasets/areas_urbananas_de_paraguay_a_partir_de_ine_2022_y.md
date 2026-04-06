# Areas urbananas de Paraguay a partir de INE 2022 Y OSM 2025

**Tipo de Dato:** Uso y cobertura del suelo

**Descripción:** Áreas urbanas de Paraguay concebidas cómo el área cubierta por la capa de manzanas de Paraguay generadas por el INE (2022) y áreas urbanas, industriales y comerciales extraídas de Open Street Map a junio de 2025. La capa de manzanas fue editada a fin de eliminar geometrías inválidas, posteriormente se aplicó un buffer de 200 m y se eliminaron los huecos residuales, finalmente se aplicó un buffer negativo de 150m

En relación con los datos de OSM, los polígonos obtenidos fueron verificados, se corrigieron geometrías inválidas y se calculó el área de cada polígono. Al analizar el área de los polígonos, se observó que el 25 % de los datos se encuentra por debajo de 0.63 ha, el 50 % de los datos 3.14 ha y el 75 % de los datos por debajo 16.3 ha. Este alto número de polígonos de menor tamaño se debe en gran medida a la granulación de los datos de OSM, y debe ser tomada en cuenta dependiendo de las aplicaciones

Los datos fueron procesados a fin de obtener una capa raster en donde el valor “1” corresponde a píxeles cubiertos por áreas urbanas y “no data” a áreas no cubiertas por áreas urbanas.


**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a partir de manzanas del INE 2022 y OSM 2025

**Fecha de Publicación:** 2022 y 2025

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
 
var dataset = ee.Image("projects/arapy-487423/assets/areas_urbanas_manzanas_osm_ine_2022"); 

Map.addLayer(dataset, {}, 'Paraguay urban areas 2022');

```


## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Instituto Nacional de Estadística. (2022). Cartografía Digital 2022. Disponible en: https://www.ine.gov.py/microdatos/cartografia-digital-2022.php*
