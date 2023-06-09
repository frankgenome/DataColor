import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image

def bubble(file,dpi,legend,Transparency,magnification,clable2,Clablesize2,y_font,x_font,cmap,clable,cbarscale,clocation,Clablesize,ylabelsize,xlabelsize,y_rotation,x_rotation,ycolor,xcolor,yaxis,xaxis):#气泡图
    if xaxis == 'True':
      xaxi = True
    else:
      xaxi = False

    if yaxis == 'True':
        yaxi = True
    else:
        yaxi = False
    dpi = dpi.split(" ", 1)[0]
    dpi = float(dpi)

    df = pd.read_excel(file)
    df = df.fillna(0)
    df.head()
    fig, ax = plt.subplots(figsize=(15, 10))
    fig.subplots_adjust(bottom=0.154, left=0.350, right=0.98)
    sns.set(style = "whitegrid")
    ax.grid(zorder=0)
    x = df['PValue']
    xs = - np.log10(x)
    y = df['Description']
    z = df['Count']
    cm = plt.cm.get_cmap(cmap)
    bubble = ax.scatter(xs, y , s = z * magnification, c = xs, cmap = cm, linewidth = 0.5, alpha = Transparency,zorder=30)

    cbar = fig.colorbar(bubble,shrink =cbarscale,fraction=clocation, anchor=(0.2, 0.7),aspect=7)
    cbar.ax.set_title(clable, fontsize=Clablesize)
    plt.yticks(font=y_font)
    plt.xticks(font=x_font)
    plt.tick_params(axis='y',
                         labelsize=ylabelsize,
                         color='black',
                         labelcolor=ycolor,
                         rotation=y_rotation
                         )
    #x轴参数
    plt .tick_params(axis='x',
                         labelsize=xlabelsize,
                         color='black',
                         labelcolor=xcolor,
                         rotation=x_rotation
                         )

    plt.tick_params(labelleft=yaxi, left=yaxi, labelbottom=xaxi, bottom=xaxi)
    step =math.ceil((max(z) - min(z))/5)
    sizes =list(range(min(z), max(z),step))
    labels = [str(s) for s in sizes]
    handles = [plt.scatter([], [], s=s*magnification,c = "black", alpha=0.8) for s in sizes]

    ax.legend(handles, labels,bbox_to_anchor=(1.17,0.5), title=clable2,fontsize=Clablesize2, frameon=False,labelspacing =legend )
    ax.set_xlabel('', fontsize = 15)#X轴标签
    ax.set_ylabel('', fontsize = 15)#Y轴标签

if __name__=='__main__':
    bubble()#气泡图