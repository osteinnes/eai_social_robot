#!/usr/bin/env python
import json

f = open('heavy_lab_positions.json')
data = json.load(f)

for pos in data:
    position = pos["pose"]["position"]
    orientation = pos["pose"]["orientation"]

    


f.close()