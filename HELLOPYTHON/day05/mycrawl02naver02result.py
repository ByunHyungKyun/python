import xml.etree.ElementTree as elemTree

tree = elemTree.parse('chicken.xml')
root = tree.getroot()

item = root.findall("item")
title = [x.findtext("title") for x in item]
description = [x.findtext("description") for x in item]
print(title)
print(description)
