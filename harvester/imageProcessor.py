from PIL import Image
from PIL.ExifTags import TAGS

def convertValue(value):
    try:
        # Convert IFDRational to float
        if hasattr(value, 'numerator') and hasattr(value, 'denominator'):
            return float(value)
        # Convert tuple of rationals (e.g., GPS)
        if isinstance(value, tuple):
            return tuple(convertValue(v) for v in value)
        # Convert bytes to hex or base64 string
        if isinstance(value, bytes):
            return value.hex()  # or use base64.b64encode(value).decode()
        return value
    except Exception:
        return str(value)


def extractMetadata(imagePath):
    try:
        image = Image.open(imagePath)
        info = image._getexif()
        if info is None:
            return {"file": imagePath, "error": "No EXIF data found"}
        metadata = {"file": imagePath}
        for tag, value in info.items():
            tagName = TAGS.get(tag, tag)
            metadata[tagName] = convertValue(value)
        return metadata
    except Exception as e:
        return {"file": imagePath, "error": str(e)}
