# Distancia a áreas urbanas, industriales y comerciales

**Categoría:** distancia

**Descripción:** Esta capa representa la distancia más cercana a áreas urbanas, comerciales e industriales calculada utilizando la proyección WGS84 UTM 21S. Para la identificación y delimitación de zonas urbanizadas, comerciales e industriales se utilizaron los datos oficiales de manzanas del año 2022 del Instituto Nacional de Estadística (INE) de Paraguay. Así como también se incluyeron las áreas comerciales, industriales, residenciales y ciudades de acuerdo con Opens Street Maps (OSM) del año 2025.

Primeramente, se realizó la preparación de la capa de manzanas, en donde se editó la capa a fin de eliminar geometrías inválidas, posteriormente se aplicó un buffer de 200 metros y se eliminaron los huecos generados, finalmente se aplicó un buffer negativo de 150m, generando así un área urbana más homogénea con un buffer de 50 metros como área de influencia directa.

Finalmente, esta capa fue fusionada con la capa de polígonos obtenida de OSM, se verificaron y corrigieron geometrías inválidas y se calculó el área de cada polígono. Al analizar el área de la capa generada, se observó que el 25 % de los datos se encuentra por debajo de 0.63 ha, el 50 % de los datos 3.14 ha y el 75 % de los datos por debajo 16.3 ha. Este alto número de polígonos de menor tamaño se debe en gran medida a la granulación de los datos de OSM, y debe ser tomada en cuenta dependiendo de las aplicaciones. Debido a lo anterior, el directorio de esta capa también contiene los archivos intermedios utilizados para su generación, estos son la capa corregida de manzanas de Paraguay al año 2022 y la capa consulta de OSM a junio de 2025. 


**Resolución Espacial:** 30 metros
**Fuente Original:** Generado a partir de manzanas del INE 2022 y OSM 2025
**Fecha de Publicación:** 2022 y 2025

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *OpenStreetMap contributors (OSM). 2015. OpenStreetMap [Datos de polígonos de áreas residenciales, comerciales e industriales]. Recuperado de https://www.openstreetmap.org/copyright*
