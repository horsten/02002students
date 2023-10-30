import xml.etree.ElementTree as ET

def update_styleUrl(placemark):
    description_elem = placemark.find("{http://earth.google.com/kml/2.1}description")
    style_url_elem = placemark.find("{http://earth.google.com/kml/2.1}styleUrl")

    if description_elem is not None and style_url_elem is not None:
        description_text = description_elem.text

        if "Band:\n                160" in description_text:
            style_url_elem.text = "#160mStyle"
        elif "Band:\n                80" in description_text:
            style_url_elem.text = "#80mStyle"
        elif "Band:\n                40" in description_text:
            style_url_elem.text = "#40mStyle"
        elif "Band:\n                20" in description_text:
            style_url_elem.text = "#20mStyle"
        elif "Band:\n                15" in description_text:
            style_url_elem.text = "#15mStyle"
        elif "Band:\n                10" in description_text:
            style_url_elem.text = "#10mStyle"

if __name__ == "__main__":
    tree = ET.parse('cp/th/kmlstyles/input.kml')
    root = tree.getroot()
    ns = {'kml': 'http://earth.google.com/kml/2.1'}

    for placemark in root.findall(".//kml:Placemark", namespaces=ns):
        update_styleUrl(placemark)

    # Serialize to string and remove the namespace prefixes
    xml_str = ET.tostring(root).decode()
    xml_str = xml_str.replace('ns0:', '').replace(':ns0', '')

    # Write to output file
    with open('cp/th/kmlstyles/output.kml', 'w') as f:
        f.write(xml_str)
