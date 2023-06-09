import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import io
from PIL import Image
import csv
import numpy as np
import squarify
import xlrd
import matplotlib as mpl

def Treemap(file,dpi,data,datasize,cmap,linewidths,linecolor,transparency,titlem,titlemsize):


        df = pd.read_excel(file)
        df = df.fillna(0)
        df.head()
        fig = plt.figure(figsize=(19, 10))
        fig.subplots_adjust(bottom=0.005, left=0.005, right=0.995, top=0.955)
        name = list(df['Description'])
        new_list = []
        for phrase in name:
            words = phrase.split()
            new_phrase = ''
            for i, word in enumerate(words):
                new_phrase += word + ' '
                if (i+1) % 2 == 0:
                    new_phrase += '\n'
            new_list.append(new_phrase.strip())

        income = list(df['PValue'])

        Count = list(df['Count'])
        min_diff = min(income)
        max_diff = max(income)
        cmap = mpl.cm.get_cmap(cmap)
        norm = mpl.colors.Normalize(vmin=min_diff, vmax=max_diff)
        colors = [cmap(norm(value)) for value in income]


        if data == 'No':
            new_list = False
        else:
            new_list = new_list
        plot = squarify.plot(sizes = Count,
                             label = new_list,
                             color = colors,
                             alpha = transparency,

                             edgecolor = linecolor,
                             linewidth =linewidths,
                             text_kwargs={'fontsize':datasize}
                            )

        plt.rc('font', size=5)

        plot.set_title(titlem,fontdict = {'fontsize':titlemsize})

        plt.axis('off')

        plt.tick_params(top = 'off', right = 'off')

        dpi = dpi.split(" ", 1)[0]
        dpi = float(dpi)

        buffer = io.BytesIO()
        plt.savefig(buffer, format='JPEG',dpi = dpi)
        img = Image.open(io.BytesIO(buffer.getvalue()))
        plt.close()
        buffer.close()
        return img

if __name__ == "__main__":
    Treemap()