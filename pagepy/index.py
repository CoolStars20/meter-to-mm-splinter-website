from glob import glob
import csv

def data(**kwargs):
    with open('data/LOCmembers.csv') as f:
        r = csv.DictReader(f)
        loc = [row for row in r]

    with open('data/SOC.csv') as f:
        r = csv.DictReader(f)
        soc = [row for row in r]

    for row in soc:
        if row['Status'] == 'Chair':
            row['Full Name'] = row['Full Name'] + ' (chair)'

    images = glob('images/slide-*')
    images.sort()

    return {'loc': loc, 'soc': soc, 'images': images}
