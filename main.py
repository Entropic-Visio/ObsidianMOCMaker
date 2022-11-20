import os
import markdown
from pathlib import Path


# Obsidian Vault
basepath = Path('C:\\Users\\entro\\OneDrive\\Documents\\Kaiser')

# MOC Path
indexPath = 'C:\\Users\\entro\\OneDrive\\Documents\\Kaiser\\SETTINGS\\_INDEX\\INDEX.md'
    
pathlist = Path(basepath).rglob('*.md')

# REMOVES ALL CONTENT IN INDEX.md
with open(indexPath, "r+") as file:
    file.truncate(0)

# APPENDS ALL MD Files into INDEX
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     baseFilename = os.path.splitext(os.path.basename(path))[0]
     with open(indexPath, 'a+') as f:
        f.write(f"[[{baseFilename}]]\n")
