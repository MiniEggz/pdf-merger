# pdf-merger
Merge multiple PDFs into a single PDF.

## Setup

### Clone the repo
```
git clone git@github.com:MiniEggz/pdf-merger.git
```

### cd into the repo
```
cd pdf-merger
```

### Pip install
```
pip install .
```

## Usage

For this basic merger to work, all pdf names must be ordered. Note that 12 would be sorted before 2 using this basic implementation - this will be changed at a later date. After sorting names of files to be merged in an order:
```
pdfmerger {path_to_output}.pdf
```