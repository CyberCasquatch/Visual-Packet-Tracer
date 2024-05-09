def retKML(dstip, srcip):
    print(f"Destination IP: {dstip}")
    print(f"Source IP: {srcip}")

    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('YOUR_PUBLIC_IP')  # Make sure to put in own IP
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
            '<LineString>\n'  # Added missing opening tag
            '<coordinates>%f,%f\n%f,%f</coordinates>\n'  # Corrected formatting
            '</LineString>\n'  # Corrected closing tag
            '</Placemark>\n'  # Corrected closing tag
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)  # Corrected formatting
        return kml
    except Exception as e:  # Added more specific exception handling
        print(f"Error generating KML for IPs {srcip} and {dstip}: {e}")
        return ''