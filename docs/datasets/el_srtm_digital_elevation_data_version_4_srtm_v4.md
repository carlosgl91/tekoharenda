# El SRTM Digital Elevation Data Version 4 (SRTM v4)

**Descripción:** 90 m elevation DEM

**Resolución Espacial:** 90 metros
**Fuente Original:** Google earth engine
**Fecha de Publicación:** 2000

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/topography/dem_PY_srtm_v4"); 
Map.addLayer(dataset, {}, 'El SRTM Digital Elev...');
```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Jarvis, A., H.I. Reuter, A. Nelson, E. Guevara. 2008. Hole-filled SRTM for the globe Version 4, available from the CGIAR-CSI SRTM 90m Database: https://srtm.csi.cgiar.org.*
