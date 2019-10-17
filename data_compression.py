def compress(data):
    if data == []:
        return ((), [])

    keys = [key for key in data[0] if data[0] != {}]
    keys.sort()

    libs = [tuple([dat[key] for key in keys]) if dat != {} else ()
            for dat in data]
    result = (tuple(keys), libs)

    return result
