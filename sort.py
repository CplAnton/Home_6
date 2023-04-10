from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path) -> None:
    if not filename.exists():
        print(f"File {filename} does not exist")
        return None
    
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.removesuffix(filename.suffix))
    
    print(f"Creating directory: {folder_for_file}")
    folder_for_file.mkdir(exist_ok=True, parents=True)
    
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file))
    except shutil.ReadError:
        print(f"Failed to unpack archive {filename}")
        folder_for_file.rmdir()
        return None

    


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    
    except OSError:
        print(f'Sorry, we can not delete folder {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMEGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMEGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMEGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMEGES:
        handle_media(file, folder / 'images' / 'SVG')




    # відео файли до video
    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    
    # документи переносимо до папки documents
    for file in parser.DOC_FILE:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_FILE:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.PDF_FILE:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.TXT_FILE:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.XLSX_FILE:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_FILE:
        handle_media(file, folder / 'documents' / 'PPTX')
    
    # аудіо файли переносимо до audio

    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # move to other folder with unknown ext
    for file in parser.OTHERS:
        handle_media(file, folder / 'others')
    
    # remove empty folders
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == '__main__':
    scan_folder = Path(sys.argv[1])
    main(scan_folder.resolve())