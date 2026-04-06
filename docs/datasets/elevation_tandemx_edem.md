# elevation_tandem-x_edem

**Tipo de Dato:** Topográficos

**Descripción:** TanDEM-X (complemento TerraSAR-X para mediciones digitales de elevación) es una misión de radar de observación de la Tierra que consta de un interferómetro SAR integrado por dos satélites prácticamente idénticos que vuelan en formación cerrada. Con una separación típica entre los satélites de entre 120 y 500 m, se ha generado un Modelo Digital de Elevación (MDE) global.

El EDEM TanDEM-X de 30 m es una variante del Modelo Digital de Elevación (MDE) global, adquirido en el marco de la misión alemana TanDEM-X entre 2010 y 2014, y presenta una separación entre píxeles reducida de 1 segundo de arco (arsec), lo que corresponde a 30 m en el ecuador. El Instituto de Microondas y Radar del Centro Aeroespacial Alemán (DLR) desarrolló una edición automatizada para obtener una cobertura completa y nítida de todas las masas continentales de la Tierra de polo a polo (DLR, 2024).


**Resolución Espacial:** 30 metros

**Fuente Original:** Deutsche Zentrum für Luft - und Raumfahrt (DLR)

**Fecha de Publicación:** 2010-2014

```javascript

var elevVis = {
  min: 0,
  max: 900, 
  palette: [
    '006600', '002200', 'fff5d7', 'ab6b28', 'b30303', 'ffffff'
  ]
};

var dataset = ee.Image("projects/arapy-487423/assets/topography/elevation30m_tandem_x_dem"); 

Map.addLayer(dataset, elevVis, 'TANDEM-X DEM');

```

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *Deutsche Zentrum für Luft - und Raumfahrt (DLR). 2024. TanDEM-X - Edited Digital Elevation Model (EDEM) - Global, 30m. https://download.geoservice.dlr.de/TDM30_EDEM/#details*
