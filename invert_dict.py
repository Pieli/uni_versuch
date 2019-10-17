def invert(d):
    werte = set(d.values())
    new_d = {}

    for wert in werte:
        new_d[wert] = []

    for key, value in d.items():
        alt = new_d.get(value)
        alt.append(key)
        alt.sort()
        new_d[value] = alt
    return new_d
