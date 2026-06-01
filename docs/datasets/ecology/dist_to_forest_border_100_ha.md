# Distancia a formaciones forestales de más de 100 hectáreas

**Categoría:** distancia

**Descripción:** Esta capa representa la distancia al borde del bosque, en donde se calcula la distancia del píxel a píxel del borde más cercano de los fragmentos o parches boscosos de más de 100 ha. Para su elaboración, se consideró una unidad mínima de áreas no boscosas de 5 píxeles, esto a fin de evitar que pequeños grupos de píxeles (menores a 0.45 ha) influencien el cómputo de distancia al borde de los píxeles de cada parche de bosque. La distancia de los píxeles fue calculada utilizando la proyección UTM correspondiente, es decir UTM21S O 20S. 

**Resolución Espacial:** 30 metros

**Fuente Original:** Generado a partir de Mapbiomas Paraguay colección 2

**Fecha de Publicación:** 2023

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
      // 1. Cargar el conjunto de datos de distancia a bosque (> 100 ha)
    var dataset = ee.Image("projects/arapy-487423/assets/distance_forest_100ha");

    // 2. Definir los parámetros de visualización
    // Nota: El valor 'max' está fijado en 30000 metros (30 km). 
    // Si notas que el mapa se ve muy rojo, aumenta este valor (ej. a 50000 o 60000).
    var visParams = {
    min: 0,
    max: 20000, 
    palette: [
        '#004d1a', // Verde oscuro: Distancia 0 (Borde o dentro del bosque)
        '#4da6ff', // Azul claro: Distancias cortas
        '#ffffcc', // Amarillo: Distancias intermedias
        '#ff9933', // Naranja: Distancias largas
        '#cc0000'  // Rojo: Áreas más alejadas del bosque
    ]
    };

    // Opción alternativa de paleta (Estilo semáforo: Verde -> Amarillo -> Rojo)
    var visParamsSemaforo = {
    min: 0,
    max: 40000,
    palette: ['#1a9850', '#91cf60', '#d9ef8b', '#fee08b', '#fc8d59', '#d73027']
    };

    // 3. Centrar la vista del mapa en el área de estudio (Paraguay)
    Map.setCenter(-58.4438, -23.4425, 6);

    // 4. Añadir la capa al mapa aplicando la visualización
    Map.addLayer(dataset, visParams, 'Dist. bosque 100 ha (Gradiente)');

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *MapBiomas Paraguay. (2024). MapBiomas Paraguay collección 2. Disponible en: https://paraguay.mapbiomas.org/*


Datos procesados:
> *Giménez, C. (2026). Capa raster binaria de Formaciones forestales mayores o iguales a 1ha - Año 2023 (Versión 1.0)[Dataset de Google Earth Engine]. Tekoharenda: Catálogo Nacional de Datos Espaciales. https://carlosgl91.github.io/tekoharenda/*