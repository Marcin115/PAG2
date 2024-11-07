import arcpy
import os

# Define the base directory and full path to the shapefile
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shp_path = os.path.join(base_dir, "data", "jezdnie.shp")

# Check if the shapefile exists at the specified path
if not os.path.exists(shp_path):
    print(f"File not found: {shp_path}")
else:
    print(f"File found: {shp_path}")

    try:
        # Explicitly set the workspace and use the full path to the shapefile
        arcpy.env.workspace = os.path.join(base_dir, "data")
        
        # Use the full path in the SearchCursor
        fields = ["FID", "SHAPE@"]  # Add more fields as needed
        with arcpy.da.SearchCursor(shp_path, fields) as cursor:
            for row in cursor:
                # Print basic info for each row in the shapefile
                print(f"Feature ID: {row[0]}, Shape info: {row[1]}")
        
        print("Shapefile opened and read successfully.")
    
    except arcpy.ExecuteError:
        # Catch arcpy-specific errors
        print(f"ArcPy error: {arcpy.GetMessages(2)}")
    except Exception as e:
        # Catch any other general errors
        print(f"Error opening shapefile: {e}")



