import dpkt
import socket
import pygeoip

gi = pygeoip.GeoIP('/path/to/GeoLiteCity.dat') #Use your own path to the file

def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('127.0.0.1')  # Make sure to put in own Public IP
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%f,%f\n%f,%f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except Exception as e:  # Added more specific exception handling
        print(f"Error generating KML for IPs {srcip} and {dstip}: {e}")
        return ''

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts += KML  # Changed concatenation
        except Exception as e:  # Added more specific exception handling
            print(f"Error processing packet: {e}")
    return kmlPts

def main():
    try:
        with open('WiresharkCapture.pcap', 'rb') as f:  # Use with statement for file handling MAKE SURE TO ADD YOUR WIRESHARK FILE HERE*****
            pcap = dpkt.pcap.Reader(f)
            kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                        '<Style id="transBluePoly">' \
                        '<LineStyle>' \
                        '<width>1.5</width>' \
                        '<color>501400E6</color>' \
                        '</LineStyle>' \
                        '</Style>'
            kmlfooter = '</Document>\n</kml>\n'
            kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
            print(kmldoc)
    except IOError as e:
        print(f"Error opening or reading file: {e}")

if __name__ == '__main__':
    main()