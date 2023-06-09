import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import csv
import pandas as pd
import io
from PIL import Image
from pylab import *
import itertools


def sanbar(file,dpi,y_font,x_font,x,y,cmap,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,zlabelsize,z_rotation,zcolor,clable,cbars,cbarscale,clocation,cbarsize,Clablesize,titlem,xlable,ylable,zlable):
    # creating figures
    if clable == 'None' :
      clables = None
    else:
      clables = clable

    if x == 'True':
      xs = True
    else:
      xs = False
    if y == 'True':
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
    y = []
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        x = next(plots)
        while "ID" in x:
            x.remove("ID")
        print(x)
        xcount = len(x)
        print(xcount)
        # ylable
        for row in plots:
            y.append(row[0])  # 从csv读取的数据是str类型

            ycount = len(y)
        print(ycount)


        scale_ls = range(xcount)
        index_ls = x
        ax.set_xticks(scale_ls, index_ls, rotation=x_rotation,color =xcolor,font = x_font,size =xlabelsize)


        scale_ls = range(ycount)
        index_ls = y
        ax.set_yticks(scale_ls, index_ls, rotation=y_rotation,color =ycolor,font = y_font,size =ylabelsize,)
        ax.tick_params(axis='z', rotation=z_rotation,color =zcolor,labelsize =zlabelsize)
        plt.tick_params(labelleft=ys, left=ys, labelbottom=xs, bottom=xs)

        X = np.arange(0, xcount, 1)
        Y = np.arange(0, ycount, 1)
        xx, yy = np.meshgrid(X, Y)

        X, Y = xx.ravel(), yy.ravel()


        df = pd.read_csv(file,encoding="gbk")
        df = df.fillna(0)
        dat = df.drop(columns=['ID'])
        data = np.array(dat.loc[:, :])
        colo = data
        merge = itertools.chain.from_iterable(data)
        Z = list(merge)
        z = np.array(Z)
        # setting color bar

        color_map = cm.ScalarMappable(cmap=cmap)
        color_map.set_array(Z)

        colors = plt.cm.get_cmap(cmap)(z.flatten() / float(z.max()))
        height = np.zeros_like(Z)
        width = depth = 1

        # creating the heatmap

        img = ax.bar3d(X, Y, height, width, depth,Z,color=colors)

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
    sanbar()