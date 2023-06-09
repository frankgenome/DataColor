import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import csv
import pandas as pd
import io
from PIL import Image
from pylab import *
import scipy.cluster.hierarchy as shc


def sanwei_y(file,dpi,metric,method,y_font,x_font,cmap,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,zlabelsize,z_rotation,zcolor,clable,cbars,cbarscale,clocation,cbarsize,Clablesize,titlem,xlable,ylable,zlable,yaxis,xaxis):

    fig = plt.figure(figsize=(5, 8), dpi=80)
    ax1 = fig.add_subplot(111)


    df = pd.read_csv(file, encoding="gbk")
    df = df.fillna(0)
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        x = next(plots)
        while "ID" in x:
            x.remove("ID")

    dend = shc.dendrogram(shc.linkage(df[x], metric = metric,method = method), labels=df.ID.values,
                          color_threshold=10,
                          orientation='left')
    plt.xticks(fontsize=1)
    hs = [item.get_text() for item in ax1.get_yticklabels(which='both')]
    dfs = pd.read_csv(file, index_col=0, encoding="gbk")
    dfs = dfs.fillna(0)
    dfsn = dfs.reindex(index=hs)


    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.close()


    # creating figures
    if clable == 'None' :
      clables = None
    else:
      clables = clable

    if xaxis == 'True':
      xs = True
    else:
      xs = False
    if yaxis == 'True':
        ys = True
    else:
        ys = False

    if titlem == 'None':
        titlems = None
    else:
        titlems = titlem
    if xlable == 'None' :
      xlables = None
    else:
      xlables = xlable
    if ylable == 'None' :
      ylables = None
    else:
      ylables = ylable
    if zlable == 'None' :
      zlables = None
    else:
      zlables = zlable

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(111, projection='3d')
    y = hs
    print(y)
    ycount = len(y)
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        x = next(plots)
        while "ID" in x:
            x.remove("ID")
        print(x)
        xcount = len(x)
        print(xcount)
        # ylable

        ## 可以设置y坐标字
        scale_ls = range(xcount)
        index_ls = x
        ax.set_xticks(scale_ls, index_ls, rotation=x_rotation,color =xcolor,font = x_font,size =xlabelsize)

        # print(ycount)
        ## 可以设置y坐标字
        scale_ls = range(ycount)
        index_ls = y
        ax.set_yticks(scale_ls, index_ls, rotation=y_rotation,color =ycolor,font = y_font,size =ylabelsize)
        ax.tick_params(axis='z', rotation=z_rotation,color =zcolor,labelsize =zlabelsize)
        plt.tick_params( labelleft=ys, left=ys, labelbottom=xs, bottom=xs)

        X = np.arange(0, xcount, 1)
        Y = np.arange(0, ycount, 1)
        X, Y = np.meshgrid(X, Y)

        dat = dfsn.reset_index(drop=True)
        data = np.array(dat.loc[:, :])
        Z = data
        # setting color bar

        color_map = cm.ScalarMappable(cmap=cmap)

        # creating the heatmap

        img = ax.plot_surface(X, Y, Z,cmap=cmap,rstride = 1, cstride = 1)

        cbar=plt.colorbar(color_map,fraction=clocation, anchor=(0.0, 0.3), orientation= cbars,shrink=cbarscale)
        cbar.ax.tick_params(labelsize=cbarsize)
        cbar.ax.set_title(clables, fontsize=Clablesize)
        # adding title and labels

        ax.set_title(titlems)

        ax.set_xlabel(xlables)

        ax.set_ylabel(ylables)

        ax.set_zlabel(zlables)

        dpi = dpi.split(" ", 1)[0]
        dpi = float(dpi)






if __name__ == "__main__":
    sanwei_y()