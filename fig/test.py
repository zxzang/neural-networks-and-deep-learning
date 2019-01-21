#/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding： utf8


# python2.7 test.py


import matplotlib
# Force matplotlib to not use any Xwindows backend. 
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(60)
y = np.random.randn(60)

plt.scatter(x, y, s=20)

#out_png = 'path/to/store/out_file.png'
out_png = 'out_figure1.png'
plt.savefig(out_png, dpi=150)

'''
支持的格式（注意不支持jpg格式）： 
eps, pdf, pgf, png, ps, raw, rgba, svg, svgz
'''