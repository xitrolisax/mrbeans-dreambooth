import os

folderPath = "datacat/instance" 

files = sorted(os.listdir(folderPath))

for i, filename in enumerate(files):
    fileExtension = os.path.splitext(filename)[1]
    if fileExtension.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
        newFileName = f"instance_{i:03}{fileExtension}"
        oldPath = os.path.join(folderPath, filename)
        newPath = os.path.join(folderPath, newFileName)
        os.rename(oldPath, newPath)

# Utility script for renaming images for DreamBooth training.
# Both class and instance images should follow a consistent naming pattern.
# Format for instance images: <subject> <class> <index>, e.g., "Mr Beans cat 001.jpg"
# Format for class images: <class> <index>, e.g., "cat 001.jpg"
