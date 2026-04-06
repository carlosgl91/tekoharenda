# Taxonomía del suelo en la Región Oriental

**Tipo de Dato:** Taxonomía del suelo

**Descripción:** El proyecto Racionalización de Uso de la Tierra PRUT (1995) Banco Mundial  Ministerio de Agricultura y Ganadería MAG / Subsecretaria de Estado de Recursos Naturales y Medio Ambiente (SEERNMA)  Dirección de Ordenamiento Ambiental (DOA), utiliza el sistema de clasificación jerárquica USDA Soil Taxonomy, que busca agrupar suelos similares en categorías cada vez más generales. Fue diseñada para apoyar los levantamientos de suelos en EE. UU., específicamente la correlación de series de suelos y la provisión de nombres de unidades cartográficas con diversos niveles de detalle cartográfico.

Los datos fueron curados en su formato vectorial y posteriormente rasterizados al nivel de subgrupos, utilizando como grilla de referencia el dataset de MapBiomas Paraguay colección 2. Se generó así mismo un diccionario de datos el cual incluye los códigos raster y descripción de acuerdo con la legenda FAO 1990

**Resolución Espacial:** 30m metros

**Fuente Original:** 

**Fecha de Publicación:** 1995

## Acceso en Google Earth Engine

Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:

```javascript
var dataset = ee.Image("projects/arapy-487423/assets/soil_type_usda_soil_taxonomy"); 

Map.addLayer(dataset, {}, 'Taxonomía del suelo ...');
```

| Orden | Grupo | Subgrupo | Cantidad de Polígonos | Código |
| :--- | :--- | :--- | :--- | :--- |
| Agua | Agua | Agua | 2027 | 1 |
| Alfisol | Albaqualf | Typic Albaqualf | 12 | 2 |
| Alfisol | Hapludalf | Aquic Lithic Hapludalf | 2 | 3 |
| Alfisol | Hapludalf | Oxyaquic Hapludalf | 2 | 4 |
| Alfisol | Hapludalf | Typic Hapludalf | 3 | 5 |
| Alfisol | Kandiudalf | Mollic Kandiudalf | 2 | 6 |
| Alfisol | Kandiudalf | Rhodic Kandiudalf | 12 | 7 |
| Alfisol | Natrudalf | Mollic Natrudalf | 2 | 8 |
| Alfisol | Natrudalf | Typic Natrudalf | 23 | 9 |
| Alfisol | Paleudalf | Albaquic Paleudalf | 21 | 10 |
| Alfisol | Paleudalf | Aquic Paleudalf | 81 | 11 |
| Alfisol | Paleudalf | Arenic Paleudalf | 30 | 12 |
| Alfisol | Paleudalf | Grossarenic Paleudalf | 2 | 13 |
| Alfisol | Paleudalf | Mollic Paleudalf | 118 | 14 |
| Alfisol | Paleudalf | Oxyaquic Paleudalf | 1 | 15 |
| Alfisol | Paleudalf | Rhodic Paleudalf | 77 | 16 |
| Alfisol | Paleudalf | Typic Paleudalf | 22 | 17 |
| Alfisol | Rhodudalf | Typic Rhodudalf | 14 | 18 |
| Ciudad | Ciudad | Ciudad | 236 | 19 |
| Entisol | Psammaquent | Typic Psammaquent | 19 | 20 |
| Entisol | Quartzipsamment | Typic Quartzipsamment | 76 | 21 |
| Entisol | Udifluvent | Aquic Udifluvent | 189 | 22 |
| Entisol | Udipsamment | Lithic Udipsamment | 31 | 23 |
| Entisol | Udipsamment | Oxyaquic Udipsamment | 7 | 24 |
| Entisol | Udipsamment | Typic Udipsamment | 1 | 25 |
| Entisol | Udorthent | Lithic Udorthent | 309 | 26 |
| Inceptisol | Dystrochrept | Oxyaquic Dystrochrept | 4 | 27 |
| Inceptisol | Dystrochrept | Ruptic Alfic Dystrochrept | 34 | 28 |
| Inceptisol | Dystrochrept | Typic Dystrochrept | 20 | 29 |
| Inceptisol | Dystrochrept | Umbric Dystrochrept | 54 | 30 |
| Inceptisol | Eutrochrept | Aquic Eutrochrept | 2 | 31 |
| Isla | Isla | Isla | 51 | 32 |
| Mollisol | Argiudoll | Calcic Argiudoll | 2 | 33 |
| Mollisol | Hapludoll | Lithic Hapludoll | 37 | 34 |
| Mollisol | Paleudoll | Vertic Paleudoll | 5 | 35 |
| Oxisol | Acrudox | Rhodic Acrudox | 7 | 36 |
| Oxisol | Eutrudox | Kandiudalfic Eutrudox | 8 | 37 |
| Oxisol | Eutrudox | Lithic Eutrudox | 2 | 38 |
| Oxisol | Haplaquox | Typic Haplaquox | 45 | 39 |
| Oxisol | Kandiudox | Rhodic Kandiudox | 29 | 40 |
| Oxisol | Kandiudox | Typic Kandiudox | 2 | 41 |
| Tierras Miscelaneas | Miscelaneas | Tierras Miscelaneas | 90 | 42 |
| Ultisol | Albaquult | Typic Albaquult | 13 | 43 |
| Ultisol | Epiaquult | Typic Epiaquult | 2 | 44 |
| Ultisol | Kandiudult | Arenic Kandiudult | 3 | 45 |
| Ultisol | Paleaquult | Typic Paleaquult | 16 | 46 |
| Ultisol | Paleudult | Aquic Paleudult | 7 | 47 |
| Ultisol | Paleudult | Arenic Rhodic Paleudult | 19 | 48 |
| Ultisol | Paleudult | Fragiaquic Paleudult | 2 | 49 |
| Ultisol | Paleudult | Grossarenic Paleudult | 4 | 50 |
| Ultisol | Paleudult | Rhodic Paleudult | 230 | 51 |
| Ultisol | Paleudult | Typic Paleudult | 82 | 52 |
| Ultisol | Rhodudult | Psammentic Rhodudult | 1 | 53 |
| Ultisol | Rhodudult | Typic Rhodudult | 32 | 54 |
| Ultisol | hapludult | Aquic hapludult | 1 | 55 |
| Ultisol | hapludult | Humic hapludult | 27 | 56 |
| Ultisol | hapludult | Ochreptic hapludult | 3 | 57 |
| Ultisol | hapludult | Typic hapludult | 10 | 58 |
| Vertisol | Hapludert | Typic Hapludert | 4 | 59 |

## Cita
Si utilizas estos datos, por favor cita la fuente original:
> *López, O.; González, E.; Llamas, P.; Molinas, A.; Franco, E.; García. S.; Ríos, E. 1995. Estudio de
reconocimiento de suelos, capacidad de uso de la tierra y propuesta de ordenamiento territorial preliminar
de la Región Oriental del Paraguay (PRUT). Asunción, PY: MAG/SRNMA/BM/PRUT. v.1, 197 p*
