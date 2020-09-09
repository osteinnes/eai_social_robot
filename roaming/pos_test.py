f = open('heavy_lab_positions.json')
    data = json.load(f)

    for i in data:
        print(i)

    f.close()