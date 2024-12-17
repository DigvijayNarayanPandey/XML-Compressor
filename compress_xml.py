import xml.etree.ElementTree as ET
from collections import defaultdict

tree = ET.parse('music.xml')
root = tree.getroot()

index_map = defaultdict(lambda: len(index_map))

def compress_xml(node):
    tag_index = index_map[node.tag]
    compressed_content = f"<{tag_index}>"

    if node.text is not None and node.text.strip():
        compressed_content += node.text.strip()

    for child in node:
        compressed_content += compress_xml(child)

    compressed_content += f"</{tag_index}>"
    return compressed_content

compressed_xml = compress_xml(root)

print("Index Map (Tag Name -> Index):")
for tag, idx in index_map.items():
    print(f"{tag} -> {idx}")

print("\nCompressed XML:")
print(compressed_xml)