import json

def printDateTimeOriginal(fieldName, jsonlPath="output/metadata.jsonl"):
    with open(jsonlPath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                value = data.get(fieldName, "N/A")
                print(f"{data['file']} → {fieldName}: {value}")
            except Exception as e:
                print(f"Error reading line: {e}")

if __name__ == "__main__":
    # 👇 Change this to any EXIF key you want
    targetKey = "DateTimeOriginal"
    printDateTimeOriginal(targetKey)
