import re
def analyze(posts):
    line = ' '.join(posts)
    analyse = {}

    expressions = re.findall(r'#([a-z,A-Z][A-Z,a-z,0-9]*)', line)
    keys = set(expressions)

    for key in keys:
        analyse.update({key: line.count(key)})

    return analyse
