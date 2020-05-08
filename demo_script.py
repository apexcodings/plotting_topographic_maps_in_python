from plotting_topo import plot_topo
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
africa_plot = 0
world_plot = 1

if africa_plot:
    ## Map1
    lonmin, lonmax = -30,70
    latmin, latmax = -40,40

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    map = Basemap(projection='merc',resolution = 'l', area_thresh = 10000., llcrnrlon=lonmin, llcrnrlat=latmin,urcrnrlon=lonmax, urcrnrlat=latmax)
    cs = plot_topo(map,cmap='terrain',lonextent=(lonmin, lonmax),latextent=(latmin, latmax),zorder=2)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    map.drawcoastlines(color='k',linewidth=0.5)
    map.drawcountries(color='k',linewidth=0.1)
    map.drawstates(color='gray',linewidth=0.05)
    map.drawrivers(color='blue',linewidth=0.05)
    parallelmin = int(latmin)
    parallelmax = int(latmax)+1
    if np.abs(parallelmax - parallelmin)<5:
        parallelmax += 2
        parallelmin -= 2
        map.drawparallels(np.arange(parallelmin, parallelmax,dtype='int16').tolist(),labels=[1,0,0,0],linewidth=0)
    else:
        map.drawparallels(np.arange(parallelmin, parallelmax,10,dtype='int16').tolist(),labels=[1,0,0,0],linewidth=0)

    meridianmin = int(lonmin)
    meridianmax = int(lonmax)+1
    if np.abs(meridianmax - meridianmin)<5:
        meridianmax += 2
        meridianmin -= 2
        map.drawmeridians(np.arange(meridianmin, meridianmax,dtype='int16').tolist(),labels=[0,0,0,1],linewidth=0)
    else:
        map.drawmeridians(np.arange(meridianmin, meridianmax,20,dtype='int16').tolist(),labels=[0,0,0,1],linewidth=0)

    map.drawmapboundary(color='k', linewidth=2, zorder=1)

    plt.savefig('africa.png',bbox_inches='tight',dpi=300)
    plt.close('all')


if world_plot:
    ## World map
    lonmin, lonmax = -180,180
    latmin, latmax = -50,50

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    map = Basemap(projection='merc',resolution = 'l', area_thresh = 10000., llcrnrlon=lonmin, llcrnrlat=latmin,urcrnrlon=lonmax, urcrnrlat=latmax)
    cs = plot_topo(map,cmap='terrain',lonextent=(lonmin, lonmax),latextent=(latmin, latmax),zorder=2)
    fig.colorbar(cs, ax=ax, shrink=0.4)
    map.drawcoastlines(color='k',linewidth=0.5)
    map.drawcountries(color='k',linewidth=0.1)
    # map.drawstates(color='gray',linewidth=0.05)
    # map.drawrivers(color='blue',linewidth=0.05)
    parallelmin = int(latmin)
    parallelmax = int(latmax)+1
    if np.abs(parallelmax - parallelmin)<5:
        parallelmax += 2
        parallelmin -= 2
        map.drawparallels(np.arange(parallelmin, parallelmax,dtype='int16').tolist(),labels=[1,0,0,0],linewidth=0,fontsize=6)
    else:
        map.drawparallels(np.arange(parallelmin, parallelmax,10,dtype='int16').tolist(),labels=[1,0,0,0],linewidth=0,fontsize=6)

    meridianmin = int(lonmin)
    meridianmax = int(lonmax)+1
    if np.abs(meridianmax - meridianmin)<5:
        meridianmax += 2
        meridianmin -= 2
        map.drawmeridians(np.arange(meridianmin, meridianmax,dtype='int16').tolist(),labels=[0,0,0,1],linewidth=0,fontsize=6)
    else:
        map.drawmeridians(np.arange(meridianmin, meridianmax,20,dtype='int16').tolist(),labels=[0,0,0,1],linewidth=0,fontsize=6)

    map.drawmapboundary(color='k', linewidth=2, zorder=1)

    plt.savefig('world_map.png',bbox_inches='tight',dpi=300)
    plt.close('all')