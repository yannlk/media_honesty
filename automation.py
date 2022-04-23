import csv


def append_db(file, domain):
    f = open(file, "r")

    in_db = False

    for l in csv.reader(f):
        if domain == l[0]:
            l[1] = int(l[1]) + 1
            in_db = True

    f.close()

    if not in_db:
        f = open(file, "a")
        csv.writer(f).writerow([domain, 1])

    f.close()
