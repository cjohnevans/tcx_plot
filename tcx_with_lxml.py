# tcx_with_lxml
# testing with lxml
# https://lxml.de/tutorial.html#the-parse-function

from lxml import etree

tree = etree.parse('/home/john/code/tcx_plot/activity_8120026129.tcx')

root = tree.getroot()
print(root.tag)
etree.tostring(root)
print(root.iter)

level1 = list(root)

for item1 in level1:
    print(item1.tag)

