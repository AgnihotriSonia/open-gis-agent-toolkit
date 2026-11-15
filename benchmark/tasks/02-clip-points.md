# Task 02: Clip points to a polygon
Prompt: "Using PyQGIS, keep only the points from D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/ne_110m_populated_places/ne_110m_populated_places.shp that fall inside India (the feature with NAME = 'India' in D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp) and save them as D:/GIS_AI_Toolkit/open-gis-agent-toolkit/benchmark/data/india_places.gpkg."
Input data: Natural Earth 110m populated places and countries (naturalearthdata.com)
Expected result: 4 points
Check: feature count of india_places.gpkg equals 4
QGIS versions: 3.40.14
Answer key: made by hand in the QGIS interface on 2026-11-15 with Extract by location (are within)