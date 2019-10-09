def get_average_grade(path):
    if not os.path.exists(path):
        return None
    else:
        noten = []
        with open(path, 'rt') as f:
            for line in f.readlines():
                if line.startswith('#') or line.startswith('\n'):
                    continue
                else:
                    new = line.rstrip()
                    note = float(new.split(':')[1].strip())
                    noten.append(note)
        if len(noten) == 0:
            return 0.0
        else:
            return sum(noten) / len(noten)
