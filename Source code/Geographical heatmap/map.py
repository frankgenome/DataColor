from pyecharts.charts import Map
from pyecharts import options as opts
import csv
import pandas as pd
import io
from PIL import Image
from pylab import *

def map(file,color,width,height,vmin,vmax,titlem,lable,clable,cbars,type):

    if color == 'True':
        colors = True
    else:
        colors = False
    print(file)
    if type == 'America':
        type = "美国"
    else:
        type = type
    df = pd.read_excel(file)
    df.head()
    provice = list(df['Location'])
    values = list(df['Values'])
    sequence = list(zip(provice, values))
    width = str(width) + 'px'
    height = str(height) + 'px'
    print(vmin)
    vmins = int(vmin)
    vmaxs = int(vmax)


    def map_visualmap(sequence, year) -> Map:
        c = (
            Map(opts.InitOpts(width=width, height=height,
                              page_title="DataColor-Map"))
            .add(series_name=year, data_pair=sequence, maptype=type)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=titlem),
                visualmap_opts=opts.VisualMapOpts(max_=vmaxs, min_=vmins, is_piecewise=True, orient=cbars,
                                                  range_text=[clable, ''],
                                                  pos_top="middle",
                                                  pos_left="left",
                                                  split_number=5,
                                                  ),
            )
        )
        return c


    map = map_visualmap(sequence, lable)

    map.render(path="map.html")
    os.system("map.html")
    path = os.path.abspath("map.html")

if __name__ == "__main__":
    map()