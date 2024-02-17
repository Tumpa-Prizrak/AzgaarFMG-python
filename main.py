import os
import json

file = "Morgisnoy GridCells 2024-02-17-10-25.json"

with open(f"data/{file}", "r") as f:
    d = json.load(f)
with open(f"data/{file}", "w") as f:
    json.dump(d, f, indent=2)
