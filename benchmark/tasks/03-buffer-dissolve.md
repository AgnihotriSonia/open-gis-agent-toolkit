# Task 03: Buffer and dissolve
Prompt: "Using PyQGIS, keep only the points from D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/ne_110m_populated_places/ne_110m_populated_places.shp that fall inside India (the feature with NAME = 'India' in D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp) and save them as D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/india_places.gpkg."
Input data: Natural Earth 110m rivers and countries (naturalearthdata.com)
Expected result: one feature with an ellipsoidal area of about 2,479 km² (tolerance 5%), with the buffer distance applied in metres, not degrees
Check: ellipsoidal area (WGS 84, EPSG:7030) of the output within 5% of 2,478.6 km²
Answer key: made by hand on 2026-11-15 in QGIS 3.40.14 (Extract by location, Reproject to EPSG:32643, Buffer 500 m with Dissolve, then $area / 1000000 with project ellipsoid EPSG:7030); reference saved as benchmark/data/rivers_buffer_reference.gpkg
QGIS versions: 3.40.14