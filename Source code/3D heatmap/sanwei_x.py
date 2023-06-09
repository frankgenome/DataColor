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


def sanwei_x(file,dpi,metric,method,y_font,x_font,cmap,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,zlabelsize,z_rotation,zcolor,clable,cbars,cbarscale,clocation,cbarsize,Clablesize,titlem,xlable,ylable,zlable,yaxis,xaxis):

    fig = plt.figure(figsize=(5, 8), dpi=80)
    ax1 = fig.add_subplot(111)
    # file = 'C:\\Users\\11231\\Desktop\\Heatmap\\hm1.csv'
    df = pd.read_csv(file)
    df = df.fillna(0)
    data = df.values  # data是数组，直接从文件读出来的数据格式是数组
    index1 = list(df.keys())  # 获取原有csv文件的标题，并形成列表
    data = list(map(list, zip(*data)))  # map()可以单独列出列表，将数组转换成列表
    data = pd.DataFrame(data, index=index1)  # 将data的行列转换
    data.to_csv(file, header=0)
    df = pd.read_csv(file, encoding="gbk")
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        x = next(plots)
        while "ID" in x:
            x.remove("ID")
        # Plot
        # plt.title("USArrests Dendograms", fontsize=22)
    dend = shc.dendrogram(shc.linkage(df[x],metric = metric,method = method), labels=df.ID.values,
                          color_threshold=10,
                          orientation='left')
    plt.xticks(fontsize=1)
    hs = [item.get_text() for item in ax1.get_yticklabels(which='both')]
    dfs = pd.read_csv(file, index_col=0, encoding="gbk")
    dfs = dfs.fillna(0)
    dfsn = dfs.reindex(index=hs)

    # plt.savefig('USArrests_Dendograms.png')
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    plt.axis('off')  # 去掉坐标轴
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
    y =[]
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
            while "ID" in x:
                y.remove("ID")
            ycount = len(y)
        # ylable

        ## 可以设置y坐标字
        scale_ls = range(ycount)
        index_ls = y
        ax.set_xticks(scale_ls, index_ls, rotation=x_rotation,color =xcolor,font = x_font,size =xlabelsize)

        # print(ycount)
        ## 可以设置y坐标字
        scale_ls = range(xcount)
        index_ls = x
        ax.set_yticks(scale_ls, index_ls, rotation=y_rotation,color =ycolor,font = y_font,size =ylabelsize)
        ax.tick_params(axis='z', rotation=z_rotation,color =zcolor,labelsize =zlabelsize)
        plt.tick_params( labelleft=ys, left=ys, labelbottom=xs, bottom=xs)

        X = np.arange(0, ycount, 1)
        Y = np.arange(0, xcount, 1)
        X, Y = np.meshgrid(X, Y)

        dfsn = dfsn.T
        dat = dfsn.reset_index(drop=True)  # 去除‘id’列
        data = np.array(dat.loc[:, :])  # 去除第一行
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

        df = pd.read_csv(file)
        data = df.values
        index1 = list(df.keys())
        data = list(map(list, zip(*data)))
        data = pd.DataFrame(data, index=index1)
        data.to_csv(file, header=0)



if __name__ == "__main__":
    sanwei_x()