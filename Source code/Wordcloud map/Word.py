import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image,ImageSequence
from wordcloud import WordCloud,ImageColorGenerator
from os import path
import io


def Word(file,dpi,image,width,height,color,min,max,margin,background_color,image_color,max_words):

    if image == "None (.jpg, .png)":
        alice_coloring = None
    else:
        d = path.dirname(__file__)
        alice_coloring = np.array(Image.open(path.join(d, image)))
        image_colors = ImageColorGenerator(alice_coloring)


    wc = WordCloud(background_color = background_color,
                   width=width,
                   height= height,
                   margin=margin,
                   max_words = max_words,
                   colormap=color,
                   mask=alice_coloring,
                   min_font_size=min,
                   max_font_size = max,
                   )
    fp = pd.read_excel(file)
    fp = fp.fillna(0)
    name = list(fp.Description)
    value = fp.Count
    for i in range(len(name)):
      name[i] = str(name[i])

    dic = dict(zip(name, value))
    wc.generate_from_frequencies(dic)

    if image_color == 'None' :
      plt.imshow(wc)
    else:
      plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    #plt.imshow(wc)
    dpi = dpi.split(" ", 1)[0]
    dpi = float(dpi)

    plt.axis("off")


if __name__=='__main__':
    Word()