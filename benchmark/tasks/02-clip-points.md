# Task 02: Clip points to a polygon
Prompt: "Using PyQGIS, keep only the points from ne_110m_populated_places.shp that fall inside the India polygon of countries_utm43.gpkg (NAME = 'India') and save them as india_places.gpkg."
Input data: Natural Earth populated places, and the output of task 01
Expected result: only places inside India, and the count matches a reference count
Check: reference count made once with Select by Location in the QGIS interface
QGIS versions: 3.40