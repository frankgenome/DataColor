import pandas as pd
from matplotlib import pyplot as plt
import io
from PIL import Image
import seaborn as sns

def basic(file,Clablesize,dpi,Ytick,Xtick,y_font,x_font,clable,center,data,datasize,cmap,vmin,vmax,y,x,ylabelsize,xlabelsize,y_rotation,x_rotation,scale,cbar,cbarscale,cbarsize,linewidths,linecolor,square,ycolor,xcolor):


    df = pd.read_csv(file,index_col=0,encoding="gbk")
    df = df.fillna(0)
    df.head()
    fig = plt.figure(figsize=(5.5,4.9))
    fig.subplots_adjust(bottom=0.184, left=0.185, right=0.935,top=0.915)
    #data,datasize
    if data == 'Yes':
      datas = True
    else:
      datas = False

    datasizes = datasize
    #vmin,vmax
    if vmin == 'None' :
      vmins = None
    else:
      vmins = vmin

    if vmax == 'None' :
      vmaxs = None
    else:
      vmaxs = vmax

    if center == 'None' :
      centers = None
    else:
      centers = float(center)
    #x,y
    if Xtick == 0 and x == "True":
        xs = True
    elif x =="False":
        xs = False
    else:
        xs = Xtick
    if Ytick == 0 and y == "True":
        ys = True
    elif y == "False":
        ys = False
    else:
        ys = Ytick
    #Square
    if square == 'True':
      squares = True
    else:
      squares = False

    if clable == 'None' :
      clables = None
    else:
      clables = clable

    cbars =cbar
    cbarscales = cbarscale

    dpi = dpi.split(" ", 1)[0]
    dpi =float(dpi)

    sns_plot = sns.heatmap(df,center=centers,annot=datas,annot_kws={"size": datasizes},cmap=cmap,vmin=vmins,vmax =vmaxs,yticklabels=ys,xticklabels=xs,cbar_kws={"orientation":cbars,"shrink": cbarscales},linewidths=linewidths,linecolor=linecolor,square=squares)

    #字体

    sns_plot.tick_params(axis='y',
                         labelsize=ylabelsize,
                         color='black',
                         labelcolor=ycolor,
                         rotation=y_rotation
                         )
    #x轴参数
    sns_plot.tick_params(axis='x',
                         labelsize=xlabelsize,
                         color='black',
                         labelcolor=xcolor,
                         rotation=x_rotation
                         )

    x1_label = sns_plot.get_xticklabels()
    [x1_label_temp.set_fontname(x_font) for x1_label_temp in x1_label]
    y1_label = sns_plot.get_yticklabels()
    [y1_label_temp.set_fontname(y_font) for y1_label_temp in y1_label]
    sns_plot.tick_params(direction=scale)

    cbar = sns_plot.collections[0].colorbar
    cbar.ax.tick_params(labelsize=cbarsize)
    cbar.ax.set_title(clables, font='Arial',fontsize=Clablesize)



if __name__ == "__main__":
    basic()