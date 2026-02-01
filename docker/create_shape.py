from osgeo import ogr, osr
import os

# Output shapefile path
shapefile_path = "example_points.shp"

# Remove existing shapefile (if exists)
if os.path.exists(shapefile_path):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    driver.DeleteDataSource(shapefile_path)

# Create shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")
datasource = driver.CreateDataSource(shapefile_path)

# Define spatial reference (WGS84)
spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromEPSG(4326)

# Create layer
layer = datasource.CreateLayer(
    "points",
    spatial_ref,
    geom_type=ogr.wkbPoint
)

# Define attributes
field_id = ogr.FieldDefn("id", ogr.OFTInteger)
layer.CreateField(field_id)

field_name = ogr.FieldDefn("name", ogr.OFTString)
field_name.SetWidth(50)
layer.CreateField(field_name)

# Create a feature
feature_def = layer.GetLayerDefn()

feature = ogr.Feature(feature_def)
feature.SetField("id", 1)
feature.SetField("name", "Sample Point")

# Create geometry (longitude, latitude)
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(106.8456, -6.2088)  # Jakarta

feature.SetGeometry(point)

# Add feature to layer
layer.CreateFeature(feature)

# Cleanup
feature = None
datasource = None

print("Shapefile created successfully!")
