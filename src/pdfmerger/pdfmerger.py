from PyPDF4 import PdfFileMerger
import os
from pathlib import Path


class PdfMerger:

    def __init__(self):
        self.pdfs = [file for file in os.listdir() if ".pdf" in file]
        self.pdfs.sort()

    def merge(self, output_path):
        output_path = Path(output_path)
        merger = PdfFileMerger()
        for pdf in self.pdfs:
            merger.append(pdf)
        merger.write(str(output_path))
        merger.close()
