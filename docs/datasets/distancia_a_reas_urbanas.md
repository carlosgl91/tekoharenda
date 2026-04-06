# Distancia a áreas urbanas

**Tipo de Dato:** distancia

**Descripción:** Esta capa representa las áreas urbanas de Paraguay concebidas cómo el área cubierta por la capa de manzanas de Paraguay generadas por el INE (2022).

La capa de manzanas fue editada a fin de eliminar geometrías inválidas, posteriormente se aplicó un buffer de 200 m y se eliminaron los huecos residuales, finalmente se aplicó un buffer negativo de 200m

Los datos fueron procesados a fin de obtener una capa raster en donde el valor “1” corresponde a píxeles cubiertos por áreas urbanas y “no data” a áreas no cubiertas por áreas urbanas.


**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a partir de manzanas del INE 2022

**Fecha de Publicación:** 2022


```javascript
 
var dataset = ee.Image("projects/arapy-487423/assets/areas_urbanas_ine_manz_2022"); 

Map.addLayer(dataset, {}, 'Paraguay urban areas 2022');

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Instituto Nacional de Estadística. (2022). Cartografía Digital 2022. Disponible en: https://www.ine.gov.py/microdatos/cartografia-digital-2022.php*
