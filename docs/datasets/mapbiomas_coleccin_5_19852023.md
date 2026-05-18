# MapBiomas colección 5 1985-2023

**Categoría:** Uso y cobertura del suelo

**Descripción:** Se utilizó el conjunto de datos MapBiomas colección 2 (https://paraguay.mapbiomas.org/mapas-de-la-coleccion/), el cual proporciona mapas anuales de cobertura y uso del suelo a nivel nacional, con una resolución espacial de 30 metros y una cobertura temporal que abarca desde el año 1985 hasta el 2023, lo que permite analizar espacialmente y cuantificar cambios en la cobertura, tendencias de conversión de uso
y patrones de dinámica territorial a lo largo del tiempo.

**Resolución Espacial:** 30 metros

**Fuente Original:** Mapbiomas Paraguay

**Fecha de Publicación:** 1985-2023

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:   

```javascript
        // ==============================================================================
        // 1. CARGAR LOS DATOS
        var mapbiomasAsset = 'projects/arapy-487423/assets/MapbiomasPyCol2'; 
        var image = ee.ImageCollection(mapbiomasAsset);
        print(image)
        // Seleccionamos los años que queremos comparar (bandas de la imagen)
        // Ajusta los nombres de las bandas según tu catálogo (suele ser 'classification_AÑO')
        var year1 = 'projects/arapy-487423/assets/MapbiomasPyCol2/mapbiomas_paraguay_collection2_integration_v1-classification_1985';
        var year2 = 'projects/arapy-487423/assets/MapbiomasPyCol2/mapbiomas_paraguay_collection2_integration_v1-classification_2023';

        var imgLeft = ee.Image(year1);
        var imgRight = ee.Image(year2);

        // ==============================================================================
        // 2. PARÁMETROS DE VISUALIZACIÓN (Paleta Oficial de MapBiomas)
        // MapBiomas usa códigos de valores específicos (ej: 3 = Bosque, 15 = Pastura, etc.)
        // A continuación, una paleta simplificada basada en la leyenda oficial para que 
        // los colores tengan sentido geográfico (verde=bosque, amarillo=agro, azul=agua).

        var mapbiomasPalette = [
        '#ffffff', '#129912', '#1f4423', '#006400', '#00ff00', '#687537', '#76a5af',
        '#29eee4', '#77a605', '#935132', '#bbfcac', '#45c2a5', '#b8af4f', '#f1c232',
        '#ffffb2', '#ffd966', '#f6b26b', '#f99f40', '#e974ed', '#d5a6bd', '#c27ba0',
        '#fff3bf', '#ea9999', '#dd7e6b', '#aa0000', '#ff99ff', '#0000ff', '#d5d5e5',
        '#dd497f', '#b2ae7c', '#af2a2a', '#8a2be2', '#968c46', '#0000ff', '#4fd3ff',
        '#645617', '#f3b4f1', '#02106f', '#02106f', '#c59cb4', '#cc0013', '#9ca367',
        '#ffebaf', '#f4ce5a', '#d6bea2', '#d6bea2', '#f6bd3f', '#f4ce5a', '#ff99ff',
        '#ff0000'
        ];

        var visParams = {
        min: 0,
        max: 49,
        palette: mapbiomasPalette
        };

        // ==============================================================================
        // 3. CONFIGURAR LOS PANELES DEL MAPA (INTERFAZ DE USUARIO)

        // Crear el mapa izquierdo
        var leftMap = ui.Map();
        leftMap.setControlVisibility(false); // Ocultar controles para que se vea limpio
        var leftLayer = ui.Map.Layer(imgLeft, visParams, 'Año: ' + year1);
        leftMap.layers().add(leftLayer);
        leftMap.add(ui.Label('Año: 2000', {position: 'bottom-left', fontWeight: 'bold'}));

        // Crear el mapa derecho
        var rightMap = ui.Map();
        rightMap.setControlVisibility(true); // Dejar controles en un solo mapa
        var rightLayer = ui.Map.Layer(imgRight, visParams, 'Año: ' + year2);
        rightMap.layers().add(rightLayer);
        rightMap.add(ui.Label('Año: 2022', {position: 'bottom-right', fontWeight: 'bold'}));

        // ==============================================================================
        // 4. VINCULAR LOS MAPAS Y CREAR EL "SWIPE"

        // Esto vincula los movimientos (zoom, paneo) de ambos mapas
        var linker = ui.Map.Linker([leftMap, rightMap]);

        // Crear el panel divisor
        var splitPanel = ui.SplitPanel({
        firstPanel: linker.get(0),
        secondPanel: linker.get(1),
        orientation: 'horizontal',
        wipe: true, // Esto crea el efecto de deslizar (swipe)
        style: {stretch: 'both'}
        });

        // Reemplazar la interfaz estándar de GEE con nuestro panel dividido
        ui.root.widgets().reset([splitPanel]);

        // Centrar el mapa en Paraguay
        // Coordenadas: [Longitud, Latitud], Zoom
        leftMap.setCenter(-58.3, -23.5, 6);
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *MapBiomas Paraguay. (2024). MapBiomas Paraguay collección 2. Disponible en: https://paraguay.mapbiomas.org/*
