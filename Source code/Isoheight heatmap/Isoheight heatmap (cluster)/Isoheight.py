import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
import pandas as pd
import io
from PIL import Image
import csv
from matplotlib import ticker, cm


def Isoheight(file,dpi,datasize,metric,method,y_font,x_font,data,cmap,vmin,vmax,vinterval,clable,cbars,cbarscale,clocation,cbarnum,cbarsize,Clablesize,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,yaxis,xaxis):

    if metric == 'None' :
      metrics = None
    else:
      metrics = metric


    fig = plt.figure(figsize=(9, 9))
    fig.subplots_adjust(top=0.91, bottom=0.199, left=0.005, right=0.95)

    ax = plt.subplot2grid((1, 4), (0, 0), colspan=1, rowspan=1)
    df = pd.read_csv(file,encoding="gbk")
    df = df.fillna(0)
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        x = next(plots)
    while "ID" in x:
        x.remove("ID")

    dend = shc.dendrogram(shc.linkage(df[x], metric = metrics,method = method ), labels=df.ID.values, color_threshold=10,
                          orientation='left')
    plt.xticks(fontsize=12)
    hs = [item.get_text() for item in ax.get_yticklabels(which='both')]
    dfs = pd.read_csv(file, index_col=0,encoding="gbk")
    dfs = dfs.fillna(0)
    dfsn = dfs.reindex(index=hs)

    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    # deng
    plt.subplot2grid((1, 4), (0, 1), colspan=3, rowspan=1)

    if vmin == 'None':
        vmins = None
    else:
        vmins = float(vmin)

    if vmax == 'None':
        vmaxs = None
    else:
        vmaxs = float(vmax)
    if vinterval == 'None':
        vintervals = None
    else:
        vintervals = float(vinterval)

    if clable == 'None' :
      clables = None
    else:
      clables = clable

    if cbarnum == 'None':
        cbarnums = None
    else:
        cbarnums = float(cbarnum)

    if xaxis == 'True':
      xaxi = True
    else:
      xaxi = False
    print(x)
    if yaxis == 'True':
        yaxi = True
    else:
        yaxi = False

    # ylable
    y = hs
    ycount = len(y)
    # xlable
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)

        header_row = next(plots)
        while "ID" in header_row:
            header_row.remove("ID")
        xcount = len(header_row)
        levels = np.arange(vmins, vmaxs, vintervals)
        h1 = plt.contourf(dfsn, levels, cmap=cmap)
        cbar = plt.colorbar(h1, fraction=clocation, anchor=(0.0, 0.3), orientation= cbars,shrink=cbarscale)

        tick_locator = ticker.MaxNLocator(nbins=cbarnums)
        cbar.locator = tick_locator
        cbar.ax.tick_params(labelsize=cbarsize)
        # 设置颜色条的title
        cbar.ax.set_title(clables, fontsize=Clablesize)
        cbar.update_ticks()

        ## 可以设置y坐标字
        scale_ls = range(ycount)
        index_ls = y
        print(y)

        plt.yticks(scale_ls, index_ls,rotation=y_rotation,color =ycolor,font=y_font,size =ylabelsize)
        scale_ls = range(xcount)
        index_ls = header_row
        print(header_row)
        plt.xticks(scale_ls, index_ls,rotation=x_rotation,color =xcolor,font=x_font,size =xlabelsize)

        plt.tick_params(labelleft=yaxi, left=yaxi, labelbottom=xaxi, bottom=xaxi)
        # 显示数据
        if data == "Yes":
            C = plt.contour(dfsn)
            plt.clabel(C, inline=False, fontsize=datasize)
        else:
            pass

        dpi = dpi.split(" ", 1)[0]
        dpi = float(dpi)
        plt.subplots_adjust(wspace=0.65)


if __name__ == "__main__":
    Isoheight()