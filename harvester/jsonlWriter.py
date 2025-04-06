import json
import threading

writeLock = threading.Lock()

def appendToJsonl(data, outputPath="output/metadata.jsonl"):
    with writeLock:
        with open(outputPath, "a", encoding="utf-8") as f:
            json.dump(data, f)
            f.write("\n")
