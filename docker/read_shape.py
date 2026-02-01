from osgeo import ogr

shapefile_path = "example_points.shp"

# Open shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")
datasource = driver.Open(shapefile_path, 0)  # 0 = read-only

if datasource is None:
    raise RuntimeError("Could not open shapefile")

# Get first layer
layer = datasource.GetLayer(0)

print("Number of features:", layer.GetFeatureCount())

# Loop through features
for feature in layer:
    # Read attributes
    fid = feature.GetFID()
    field_id = feature.GetField("id")
    name = feature.GetField("name")

    # Read geometry
    geom = feature.GetGeometryRef()
    geom_type = geom.GetGeometryName()

    # For point geometry
    x = geom.GetX()
    y = geom.GetY()

    print(f"FID={fid}, id={field_id}, name={name}")
    print(f"Geometry type: {geom_type}, X={x}, Y={y}")
    print("-" * 40)

# Cleanup
datasource = None
