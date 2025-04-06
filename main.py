import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from harvester.imageProcessor import extractMetadata
from harvester.jsonlWriter import appendToJsonl

def getImagePaths(rootDir):
    supportedExtensions = {".jpg", ".jpeg", ".png"}
    for dirpath, _, filenames in os.walk(rootDir):
        for file in filenames:
            if os.path.splitext(file)[1].lower() in supportedExtensions:
                yield os.path.join(dirpath, file)

def processAndWrite(imagePath):
    from harvester.imageProcessor import extractMetadata
    from harvester.jsonlWriter import appendToJsonl
    metadata = extractMetadata(imagePath)
    appendToJsonl(metadata)
    return imagePath

if __name__ == "__main__":
    imagePaths = list(getImagePaths("inputImages"))
    print(f"Found {len(imagePaths)} images. Starting metadata extraction...")

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(processAndWrite, path) for path in imagePaths]
        for future in as_completed(futures):
            try:
                completedPath = future.result()
                print(f"✔ Processed: {completedPath}")
            except Exception as e:
                print(f"✖ Error: {e}")
