# Task 01: Reproject a layer
Prompt: "Using PyQGIS, reproject the shapefile D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp to EPSG:32643 and save it as D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/countries_utm43.gpkg."
Input data: Natural Earth 110m countries (naturalearthdata.com)
Expected result: countries_utm43.gpkg exists, CRS is EPSG:32643, feature count equals the input
Check: script reads the output and compares CRS and count
QGIS versions: 3.40