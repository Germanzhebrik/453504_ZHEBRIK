import json
from geometric_lib.circle import area

with open("config.json") as f:
    cfg = json.load(f)

r = cfg["radius"]
print("Area:", area(r))
