from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from matplotlib import font_manager, rc
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

from lib.DataCollector import DataCollector


def cur_annotations(cur):
    cur.annotation.set_text(
        'Cursor One:\nRange {:.2f}\nHeight {:.2f} m\nindex: {}'.format(cur.target[0], cur.target[1], cur.target.index))
    cur.annotation.get_bbox_patch().set(fc="powderblue", alpha=0.9)
    # for s in crs2.selections:
    #     crs2.remove_selection(s)

dc = DataCollector()

# print(dc.get_timeseries())

data = dc.get_timeseries().get("Korea, South")

# dateL = []
# confirmedL = []
# deathsL = []
# recoveredL = []
#
# for i in data :
#     dateL.append(i.get('date'))
#     confirmedL.append(i.get('confirmed'))
#     deathsL.append(i.get('deaths'))
#     recoveredL.append(i.get('recovered'))

# print(dc.cut_timeseries(data, 'date'))
# fig, ax =plt.subplots(1,1)
fig=plt.figure()
dateL = dc.cut_timeseries(data, 'date')
plt.bar(dc.cut_timeseries(data, 'date'), dc.cut_timeseries(data, 'confirmed'), label='confirmed')
plt.bar(dc.cut_timeseries(data, 'date'), dc.cut_timeseries(data, 'deaths'), label='deaths')
r = plt.plot(dc.cut_timeseries(data, 'date'), dc.cut_timeseries(data, 'recovered'),'g-', label='recovered')
plt.xticks([dateL[0],'2020-2-1','2020-3-1','2020-4-1'], [dateL[0],'2020-2-1','2020-3-1','2020-4-1'])
# plt.set_xlabel('date')

locs, labels = plt.xticks()
plt.setp(labels, rotation=-12)
# plt.setp(r, linewidth=3.0)
plt.legend()
cur = mplcursors.cursor(hover=True)
cur.connect("add", cur_annotations)

# plt.bar([1,2,3],[5,5,5])
# plt.bar([1,2,3],[1,2,3])
plt.show()
