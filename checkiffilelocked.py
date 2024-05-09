geoip_db_path = '/path/to/GeoLiteCity.dat' #change to your own path to the file

try:
    with open(geoip_db_path, 'rb') as f:
        # Read data from the file
        pass  # Replace 'pass' with your file processing logic
except IOError as e:
    print(f"Error opening or reading file: {e}")