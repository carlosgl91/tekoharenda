# El SRTM Digital Elevation Data Version 4 (SRTM v4)

**Tipo de Dato:** Topográficos

**Descripción:** El conjunto de datos digitales de elevación de la Misión Topográfica de Radar del Transbordador (SRTM) se creó originalmente para proporcionar datos de elevación consistentes y de alta calidad a escala casi global. Esta versión de los datos digitales de elevación de la SRTM se ha procesado para completar la información faltante y facilitar su uso.


**Resolución Espacial:** 90 metros

**Fuente Original:** Google earth engine

**Fecha de Publicación:** 2000

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript

var elevVis = {
  min: 0,
  max: 900, 
  palette: [
    '006600', '002200', 'fff5d7', 'ab6b28', 'b30303', 'ffffff'
  ]
};

var dataset = ee.Image("projects/arapy-487423/assets/topography/dem_PY_srtm_v4"); 

Map.addLayer(dataset, elevVis, 'SRTM DEM');

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Jarvis, A., H.I. Reuter, A. Nelson, E. Guevara. 2008. Hole-filled SRTM for the globe Version 4, available from the CGIAR-CSI SRTM 90m Database: https://srtm.csi.cgiar.org.*
