# XML Compressor

This project compresses XML data by replacing tag names with indices, reducing the overall size of the XML content. The tool uses Python's `xml.etree.ElementTree` for parsing and `collections.defaultdict` for indexing tags.

## Features

- Parse and compress XML data.
- Replace tag names with unique indices.
- Output the compressed XML and a mapping of tag names to indices.

## Requirements

- Python 3.x
- `xml.etree.ElementTree` (included with Python)
- `collections.defaultdict` (included with Python)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/xml-compressor.git
   cd xml-compressor
