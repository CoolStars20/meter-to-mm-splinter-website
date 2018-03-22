#! /usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

from glob import glob
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import shutil


outpath = 'site'
verbatim_dirs = 'css fonts icons js'.split()
env = Environment(
    loader = FileSystemLoader(['.']),
    autoescape = select_autoescape(['html'])
)
template_data = {}


os.makedirs(outpath, exist_ok=True)


for page in glob('pages/*.html'):
    template = env.get_template(page)

    with open(os.path.join(outpath, os.path.basename(page)), 'wt') as html_out:
        html_out.write(template.render(**template_data))


for d in verbatim_dirs:
    outdir = os.path.join(outpath, d)
    os.makedirs(outdir, exist_ok=True)

    for f in os.listdir(d):
        shutil.copy(os.path.join(d, f), outdir)


# favicons should live in root directory
for f in os.listdir('favicon'):
    shutil.copy(os.path.join('favicon', f), outpath)
