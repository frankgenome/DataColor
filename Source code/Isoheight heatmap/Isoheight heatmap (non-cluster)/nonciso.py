import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
import pandas as pd
import io
from PIL import Image
import csv
from matplotlib import ticker, cm


def nonciso(file,dpi,datasize,y_font,x_font,data,cmap,vmin,vmax,vinterval,clable,cbars,cbarscale,clocation,cbarnum,cbarsize,Clablesize,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,yaxis,xaxis):



    fig = plt.figure(figsize=(7,8))
    fig.subplots_adjust(bottom=0.220, left=0.159, right=0.985,top=0.915)

    dfs = pd.read_csv(file, index_col=0,encoding="gbk")
    dfs = dfs.fillna(0)


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

    if yaxis == 'True':
        yaxi = True
    else:
        yaxi = False

    # ylable
    y = []
    # xlable
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        # 读取第一行表头
        header_row = next(plots)
        while "ID" in header_row:
            header_row.remove("ID")
        xcount = len(header_row)
        for row in plots:
            y.append(row[0])

            ycount = len(y)
        print(y)
        levels = np.arange(vmins, vmaxs, vintervals)
        h1 = plt.contourf(dfs, levels, cmap=cmap)
        cbar = plt.colorbar(h1, fraction=clocation, anchor=(0.0, 0.3), orientation= cbars,shrink=cbarscale)

        tick_locator = ticker.MaxNLocator(nbins=cbarnums)
        cbar.locator = tick_locator
        cbar.ax.tick_params(labelsize=cbarsize)

        cbar.ax.set_title(clables, fontsize=Clablesize)
        cbar.update_ticks()


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
            C = plt.contour(dfs)
            plt.clabel(C, inline=False, fontsize=datasize)
        else:
            pass

        dpi = dpi.split(" ", 1)[0]
        dpi = float(dpi)



if __name__ == "__main__":
    nonciso()