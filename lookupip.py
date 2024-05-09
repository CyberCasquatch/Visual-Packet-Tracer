import pygeoip

# Initialize GeoIP database
gi = pygeoip.GeoIP('/Users/vonatron/PycharmProjects/VisualPacketTracker/.venv/GeoLiteCity.dat')

# Specify IP addresses to query
ip_addresses = ['8.8.8.8', '127.0.0.1']  # Example IP addresses - use your own IP

# Query the GeoIP database for each IP address
for ip in ip_addresses:
    record = gi.record_by_name(ip)
    if record:
        print(f"Information for IP address {ip}:")
        print(f"Country: {record['country_name']}")
        print(f"City: {record['city']}")
        print(f"Latitude: {record['latitude']}")
        print(f"Longitude: {record['longitude']}")
        print()
    else:
        print(f"No information available for IP address {ip}")