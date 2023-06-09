import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import csv
import pandas as pd
import io
from PIL import Image
from pylab import *



def dot(file,marker,Transparency,magnification,dpi,y_font,x_font,x,y,cmap,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,clable,cbars,cbarscale,clocation,cbarsize,Clablesize):
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

    marker = marker.split(" ", 1)[0]
    fig, ax = plt.subplots(figsize=(5.5,4.9))
    fig.subplots_adjust(bottom=0.214, left=0.185, right=0.935, top=0.915)
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
            # print("y:",y)
            ycount = len(y)
        print(ycount)
        ## 可以设置y坐标字

        scale_ls = range(xcount)
        index_ls = x
        ax.set_xticks(scale_ls, index_ls,rotation=x_rotation,color =xcolor,font = x_font,size =xlabelsize)

        # print(ycount)
        ## 可以设置y坐标字
        scale_ls = range(ycount)
        index_ls = y
        ax.set_yticks(scale_ls, index_ls, rotation=y_rotation,color =ycolor,font = y_font,size =ylabelsize)

        plt.tick_params(labelleft=ys, left=None, labelbottom=xs, bottom=None)

        X = np.arange(0, xcount, 1)
        Y = np.arange(0, ycount, 1)
        X, Y = np.meshgrid(X, Y)

        plt.grid(alpha=0.4,zorder=0)
        df = pd.read_csv(file,encoding="gbk")
        df = df.fillna(0)
        dat = df.drop(columns=['ID'])  # 去除‘id’列
        data = np.array(dat.loc[:, :])  # 去除第一行
        colo = data

        # setting color bar

        color_map = cm.ScalarMappable(cmap=cmap)

        color_map.set_array(colo)
        colors = np.array(colo)

        # creating the heatmap

        img = ax.scatter(X, Y, marker=marker,

                         s=colo * magnification, cmap=cmap, c=colors,alpha = Transparency,zorder=30)

        cbar=plt.colorbar(color_map,fraction=clocation, anchor=(0.0, 0.3), orientation= cbars,shrink=cbarscale)
        cbar.ax.tick_params(labelsize=cbarsize)
        cbar.ax.set_title(clables, fontsize=Clablesize)
        # adding title and labels
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)




        dpi = dpi.split(" ", 1)[0]
        dpi = float(dpi)




if __name__ == "__main__":
    dot()