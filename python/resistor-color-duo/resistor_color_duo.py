def value(colors):
    coldict = {
            "black":0,
            "brown":1,
            "red":2,
            "orange":3,
            "yellow":4,
            "green":5,
            "blue":6,
            "violet":7,
            "grey":8,
            "white":9,
    }
    return int(''.join([str(coldict[colors[i]]) for i in range(0,2)]))

value(["white", "red"])