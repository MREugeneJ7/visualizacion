import geopandas
import geodatasets
import contextily as cx
from matplotlib import pyplot as plt
df = geopandas.read_file(geodatasets.get_path("nybb"))
df_wm = df.to_crs(epsg=3857)
ax = df_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
cx.add_basemap(ax)
plt.show()