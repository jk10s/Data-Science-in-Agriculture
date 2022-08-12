import json
import csv

with open ("archivo.json", "r") as f:
    data = json.load(f)
    print(data)