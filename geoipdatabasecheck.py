import os

# Specify the file path to the GeoIP database
geoip_db_path = '/path/to/GeoLiteCity.dat' #change to your own path to file

# Check if the GeoIP database file exists
if not os.path.exists(geoip_db_path):
    print(f"GeoIP database file '{geoip_db_path}' not found.")