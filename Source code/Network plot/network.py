import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import io
from PIL import Image

def network(file,linestyle,dpi,node,cmap,linewidths,linecolor,clable,magnification,cbars,cbarscale,clocation,cbarsize,Clablesize,ylabelsize,ycolor,Transparency):

    G = nx.Graph()
    df = pd.read_excel(file)
    df = df.fillna(0)
    df.head()
    x = df['ID1']
    set1=set(x)
    y = df['ID2']
    zipped = list(zip(x,y))

    G.add_nodes_from((set1))

    G.add_edges_from(zipped)
    average_deg = sum(d for n, d in G.degree()) / G.number_of_nodes()
    print(average_deg)
    size = [magnification *deg/average_deg for node, deg in G.degree()]
    print(size)
    z = np.array(size)


    norm = mpl.colors.Normalize(vmin=np.min(z), vmax=np.max(z))
    cmap = mpl.cm.get_cmap(cmap)
    colors = [cmap(norm(val)) for val in z]

    # グラフの出力
    fig = plt.figure(figsize=(7,5))
    fig.subplots_adjust(top =0.9 ,bottom=0.05, left=0.01, right=0.9)
    if node =="Circular layout":
        pos = nx.spring_layout(G, iterations=1000)
    elif node =="Random layout":
        pos = nx.random_layout(G)
    elif node =="Shell layout":
        pos = nx.shell_layout(G)
    elif node == "Spring layout":
        pos = nx.spring_layout(G)
    elif node == "Spectral layout":
        pos = nx.spectral_layout(G)
    else:
        pos = nx.kamada_kawai_layout(G)

    cset= nx.draw(G, with_labels=True,
                  pos=pos,
                  node_size = size,
                  font_size=ylabelsize,
                  font_color=ycolor,
                  width=linewidths,
                  node_color = colors,
                  edge_color=linecolor,
                  alpha = Transparency,
                  style =linestyle
                  )


    sm = plt.cm.ScalarMappable(cmap=cmap,
                               norm=plt.Normalize(vmin=np.min(z), vmax=np.max(z)))
    sm._A = []
    cbar = plt.colorbar(sm,aspect=15,anchor=(0, 0.5),fraction=clocation,  orientation= cbars,shrink=cbarscale)
    cbar.ax.tick_params(labelsize=cbarsize)
    cbar.ax.set_title(clable, fontsize=Clablesize)


    dpi = dpi.split(" ", 1)[0]
    dpi = float(dpi)

    plt.axis("off")

if __name__=='__main__':
    network()