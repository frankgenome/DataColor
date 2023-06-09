import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas
import pyanatomogram
import pandas as pd
import matplotlib as mpl
from os import path
import io
from PIL import Image,ImageSequence

def anatomogram(file,dpi,type,color,cbars,clable,cbarscale,clocation,titlem,titlesize):

    if clable == 'None' :
      clables = None
    else:
      clables = clable

    df = pd.read_excel(file)
    df = df.fillna(0)
    Organs = list(df['Organs'])
    values = list(df['Values'])
    dictionary = dict(zip(Organs, values))
    print(dictionary)
    data = pandas.Series(dictionary)
    fig, axes = matplotlib.pyplot.subplots(nrows=1, ncols=1)
    norm = matplotlib.colors.Normalize()
    norm.autoscale(data)
    types = type.split(" ", 1)[0]
    anatomogram = pyanatomogram.Anatomogram(types)
    anatomogram.highlight_tissues(data.to_dict(), cmap=mpl.cm.get_cmap(color), norm=norm)
    anatomogram.to_matplotlib()

    matplotlib.pyplot.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=mpl.cm.get_cmap(color)), ax=axes,
                               orientation=cbars, label=clables,fraction=clocation, shrink=cbarscale)
    plt.title(titlem, fontdict={'fontsize': titlesize})
    dpi = dpi.split(" ", 1)[0]
    dpi = float(dpi)


if __name__=='__main__':
    anatomogram()