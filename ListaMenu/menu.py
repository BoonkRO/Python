import xml.etree.ElementTree as ET


tree = ET.parse('menuXML.xml')
root = tree.getroot()

for element in root.iter("food"):
    nombre = element.find('name').text
    precio = element.find('price').text
    print("Nombre plato: {0}, Precio: {1}".format(nombre, precio))
