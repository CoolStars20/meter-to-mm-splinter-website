import csv


def data(**kwargs):
    with open('data/splinters.csv') as f:
        r = csv.DictReader(f, delimiter=";")
        splin = [row for row in r]

    return {'splinters': splin}
