import sys
from pathlib import Path

JPEG_IMEGES = []
JPG_IMEGES = []
PNG_IMEGES = []
SVG_IMEGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_FILE = []
DOCX_FILE = []
PDF_FILE = []
TXT_FILE = []
XLSX_FILE = []
PPTX_FILE = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ARCHIVES = []
OTHERS = []


REGISTER_EXTENSION = {
    'JPEG' : JPEG_IMEGES,
    'JPG' : JPG_IMEGES,
    'PNG' : PNG_IMEGES,
    'SVG' : SVG_IMEGES,
    'AVI' : AVI_VIDEO,
    'MP4' : MP4_VIDEO,
    'MOV' : MOV_VIDEO,
    'MKV' : MKV_VIDEO,
    'DOC' : DOC_FILE,
    'DOCX' : DOCX_FILE,
    'PDF' : PDF_FILE,
    'TXT' : TXT_FILE,
    'XLSX' : XLSX_FILE,
    'PPTX' : PPTX_FILE,
    'MP3' : MP3_AUDIO,
    'OGG' : OGG_AUDIO,
    'WAV' : WAV_AUDIO,
    'AMR' : AMR_AUDIO,
    'ZIP' : ARCHIVES

}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            # cheked if folder not the same as output folder
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)
            
            continue
        
        ext = get_extensions(item.name)
        full_name = folder / item.name
        if not ext:
            OTHERS.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                OTHERS.append(full_name)


if __name__ == '__main__':
    scan_folder = sys.argv[1]
    print(f'start in folder to scan {scan_folder}')

    scan(Path(scan_folder))
    print("*" * 25)
    print(f'Types of files {EXTENSION}')
    print(f'UKNOWN: {UNKNOWN}')
        
        



