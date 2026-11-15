# Task 03: Buffer and dissolve
Prompt: "Using PyQGIS, buffer ne_110m_rivers_lake_centerlines.shp by 500 metres, dissolve the result into one feature and save it as rivers_buffer.gpkg."
Input data: Natural Earth rivers (naturalearthdata.com)
Expected result: a single feature whose area matches a reference within a small tolerance, with distances in metres, not degrees
Check: compare area with a reference made once in the QGIS interface
QGIS versions: 3.40