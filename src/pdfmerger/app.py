import argparse
from pdfmerger.pdfmerger import PdfMerger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="File path of the output file.")
    args = parser.parse_args()
    merger = PdfMerger()
    merger.merge(args.file_path)