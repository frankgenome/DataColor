import calplot
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
import pandas as pd
import matplotlib
import io
from PIL import Image
import calendar


def date_h(file,ylabelsize,ycolor,dpi,data,cmap,linewidths,linecolor,yearcolor,titlem):
# 读取数据
    if data == 'No':
         datas = None
    else:
         datas = '{:.0f}'

    df = pd.read_csv(file,encoding="gbk")
    df = df.fillna(0)
    # 数据格式转换
    df['Date'] = pd.to_datetime(df['Date'])

    # 将订单时间设置为索引
    df.set_index('Date', inplace = True)

    fig, axes= calplot.calplot(data = df['Counts'],
                          how = 'sum',
                          cmap = cmap,
                          figsize = (16, 8),
                          suptitle = titlem,
                          yearlabel_kws={'color': yearcolor,
                                         'fontname':'sans-serif'},
                          linewidth=linewidths,
                          textformat=datas,
                          edgecolor=linecolor
                          )
    for ax in axes:
        ax.set_xticklabels(calendar.month_abbr[1:], color=ycolor,size =ylabelsize)
        ax.set_yticklabels(calendar.day_abbr[:], color=ycolor,size =ylabelsize)
    dpi = dpi.split(" ", 1)[0]
    dpi =float(dpi)



if __name__ == "__main__":
    date_h()