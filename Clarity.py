# Librerías a usar
import os
import glob
import shutil

# Carpeta donde va a funcionar el script
os.chdir("/Users/yosoy/Downloads")

# Creamos un bucle, que va a investigar, si la carpeta ya existe, 
# Si no es así la crea (Todo esto lo estará haciendo en la carpeta "Descargas")
while(True):
        if os.path.exists("Audio") == True:
            pass
        else:
            os.makedirs("Audio")
            continue
        if os.path.exists("Imagenes") == True:
            pass
        else:
            os.makedirs("Imagenes")
            continue
        if os.path.exists("Videos") == True:
            pass
        else:
            os.makedirs("Videos")
            continue
        if os.path.exists("Documentos") == True:
            pass
        else:
            os.makedirs("Documentos")
            continue
        if os.path.exists("Otros") == True:
            pass
        else:
            os.makedirs("Otros")
            break

# Extensiones de imagenes:
BMP = glob.glob("*.bmp")
TIFF = glob.glob("*.tiff")
JPEG = glob.glob("*jpeg")
JPG = glob.glob("*.jpg")
GIF = glob.glob("*.gif")
PNG = glob.glob("*.png")

# Extensiones de videos:
MP4 = glob.glob("*.mp4")
MKV = glob.glob("*.mkv")
AVI = glob.glob("*.avi")
MOV = glob.glob("*.mov")
DIVX = glob.glob("*.divx")

# Extensiones de audio:
MP3 = glob.glob("*.mp3")
WAV = glob.glob("*.wav")
AAC = glob.glob("*.acc")
AIFF = glob.glob("*.aiff")
WMA = glob.glob("*.wma")
FLV = glob.glob("*.flv")

# Extensiones de documentos:
PDF = glob.glob("*.pdf")
DOC = glob.glob("*.doc")
DOCX = glob.glob("*.docx")
ODT = glob.glob("*.odt")
TXT = glob.glob("*.txt")

# Extensiones de otros
PY = glob.glob("*.py")
RAR= glob.glob("*.rar")
ZIP = glob.glob("*.zip")
EXE = glob.glob("*.exe")

# Mover archivos (Imagenes)
for i in (BMP):
    shutil.move(i, "Imagenes")
for i in (TIFF):
    shutil.move(i, "Imagenes")
for i in (JPEG):
    shutil.move(i, "Imagenes")     
for i in (JPG):
    shutil.move(i, "Imagenes")
for i in (GIF):
    shutil.move(i, "Imagenes")
for i in (PNG):
    shutil.move(i, "Imagenes")   

# Mover archivos (Videos)
for i in (MP4):
    shutil.move(i, "Videos")
for i in (MKV):
    shutil.move(i, "Videos")
for i in (AVI):
    shutil.move(i, "Videos")     
for i in (MOV):
    shutil.move(i, "Videos")
for i in (DIVX):
    shutil.move(i, "Videos")

# Mover archivos (Audio)
for i in (BMP):
    shutil.move(i, "Audio")
for i in (MP3):
    shutil.move(i, "Audio")
for i in (WAV):
    shutil.move(i, "Audio")     
for i in (AAC):
    shutil.move(i, "Audio")
for i in (AIFF):
    shutil.move(i, "Audio")
for i in (WMA):
    shutil.move(i, "Audio")   
for i in (FLV):
    shutil.move(i, "Audio") 

# Mover archivos (Documentos)
for i in (PDF):
    shutil.move(i, "Documentos")
for i in (DOC):
    shutil.move(i, "Documentos")
for i in (DOCX):
    shutil.move(i, "Documentos")     
for i in (ODT):
    shutil.move(i, "Documentos")
for i in (TXT):
    shutil.move(i, "Documentos")

# Mover archivos (Otros)
for i in (PY):
    shutil.move(i, "Otros")
for i in (RAR):
    shutil.move(i, "Otros")
for i in (ZIP):
    shutil.move(i, "Otros")     
for i in (EXE):
    shutil.move(i, "Otros")
