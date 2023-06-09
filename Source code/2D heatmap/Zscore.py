import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import io
from PIL import Image
import csv
import numpy as np

def Zscore(file,Cbarsize,clable,Clablesize,dpi,cblock,y_font,x_font,Class,z_score,data,datasize,cmap,vmin,vmax,y,x,cbar,cbarscale,linewidths,linecolor,square,row_cluster,col_cluster,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,metric,method,treestyle,treecolor,treewidths,robust):

    df = pd.read_csv(file,index_col=0,encoding="gbk")
    df = df.fillna(0)
    df.head()
    yz = []
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile)
        # 读取第一行表头
        header_row = next(plots)
        for row in plots:
            yz.append(row[0])
            # print("y:",y)
            ycount = len(yz)
        print(ycount)
        while "" in header_row:
            header_row.remove("")

    #data,datasize
    if data == 'Yes':
      datas = True
    else:
      datas = False
    datasizes = datasize
    #vmin,vmax
    if vmin == 'None':
      vmins = None
    else:
      vmins = vmin

    if vmax == 'None' :
      vmaxs = None
    else:
      vmaxs = vmax
    #x,y
    if x == 'True':
      xs = True
    else:
      xs = False
    if y == 'True':
        ys = True
    else:
        ys = False
    #Square
    if square == 'True':
      squares = True
    else:
      squares = False
    #有问题
    cbars = cbar
    cbarscales = cbarscale

    if row_cluster == 'True':
      row_clusters = True
    else:
      row_clusters = False
    if col_cluster == 'True':
      col_clusters = True
    else:
      col_clusters = False

    methods = method
    metrics = metric



    if z_score == "None":
        z_scores = None
    elif z_score == "Column":
        z_scores = 1
    else:
        z_scores = 0

    if robust == 'True':
        robusts = True
    else:
        robusts = False

    if Class in df.columns:
        Class = df.pop(Class)
        row_c = dict(zip(Class.unique(), plt.get_cmap('Pastel1')(np.linspace(0, 3, ycount))))
        row_colors = Class.map(row_c)

    if cblock == "None" :
        row_colors = None

    g = sns.clustermap(df,robust=robusts,
                   row_cluster=row_clusters,
                   col_cluster=col_clusters,
                   metric = metrics,
                   method = methods,
                   z_score=z_scores,
                   row_colors=row_colors,
                   annot=datas,
                   annot_kws={"size": datasizes},
                   cmap=cmap,
                   vmin=vmins,
                   vmax =vmaxs,
                   yticklabels=ys,
                   xticklabels=xs,
                   cbar_kws={"orientation":cbars,"shrink": cbarscales},
                   linewidths=linewidths,
                   linecolor=linecolor,
                   square=squares,
                   tree_kws={'linestyles': treestyle,  # 线型
                                 'colors': treecolor,  # 线色
                                 'linewidths': treewidths},  # 线宽
                   cbar_pos=(0.01, 0.78, 0.05, 0.18),
                    figsize=(10, 9),
                    dendrogram_ratio=(.15, .1),
                   )

    #字体
    g.ax_cbar.tick_params(labelsize=Cbarsize)
    g.ax_cbar.set_title(clable, size=Clablesize)


    plt.setp(g.ax_heatmap.get_yticklabels(), rotation = y_rotation, color = ycolor, font=y_font, size = ylabelsize)  # For y axis
    plt.setp(g.ax_heatmap.get_xticklabels(), rotation = x_rotation, color = xcolor, font=x_font, size = xlabelsize)  # For x axis
    dpi = dpi.split(" ", 1)[0]
    dpi = float(dpi)
    #g.fig.subplots_adjust(left=0.01, bottom=0.045)


if __name__ == "__main__":
    Zscore()