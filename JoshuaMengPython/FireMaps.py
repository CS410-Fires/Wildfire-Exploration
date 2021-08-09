import geopandas
import geoplot
import sqlite3
import pandas as pd
from shapely import geometry
import matplotlib.pyplot as plt


def create_oregon_map_with_10_fires_2015():
    con = sqlite3.connect('FPA_FOD_20170508.sqlite')
    df = pd.read_sql_query('SELECT LATITUDE, LONGITUDE FROM Fires WHERE STATE=\'OR\' AND FIRE_YEAR=2015 LIMIT 10', con)

    # df = pd.read_sql_query('SELECT * FROM Fires WHERE STATE=\'OR\' AND FIRE_YEAR=2015 LIMIT 10', con)

    print(df.head)

    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.LONGITUDE, df.LATITUDE))
    print(gdf.head())

    usa = geopandas.read_file('./states_21basic/states.shp')
    print(usa.head())

    ax = usa[usa.STATE_ABBR == 'OR'].plot()
    gdf.plot(ax=ax, color='red')
    plt.show()

    # usa[usa.STATE_ABBR == 'OR'].plot()

    # oregon = usa[usa.__setstate__ == 'Oregon'].plot(color='white', edgecolor='black')

    # gdf.plot(oregon=oregon, color='red')

    # geoplot.show()

def create_oregon_map_with_all_fires_2015():
    con = sqlite3.connect('FPA_FOD_20170508.sqlite')
    df = pd.read_sql_query('SELECT LATITUDE, LONGITUDE FROM Fires WHERE STATE=\'OR\' AND FIRE_YEAR=2015', con)

    print(df.head())
    print(df.tail())

    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.LONGITUDE, df.LATITUDE))
    print(gdf.head())

    usa = geopandas.read_file('./states_21basic/states.shp')
    ax = usa[usa.STATE_ABBR == 'OR'].plot()
    gdf.plot(ax=ax, color='red', markersize=1)
    plt.show()

def create_oregon_map_with_all_fires_1992():
    con = sqlite3.connect('FPA_FOD_20170508.sqlite')
    df = pd.read_sql_query('SELECT LATITUDE, LONGITUDE FROM Fires WHERE STATE=\'OR\' AND FIRE_YEAR=1992', con)


    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.LONGITUDE, df.LATITUDE))

    usa = geopandas.read_file('./states_21basic/states.shp')
    ax = usa[usa.STATE_ABBR == 'OR'].plot()
    gdf.plot(ax=ax, color='red')
    plt.show()

def create_western_us_map():
    con = sqlite3.connect('FPA_FOD_20170508.sqlite')
    #df = pd.read_sql_query('SELECT FIRE_NAME, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE FROM Fires WHERE STATE=\'OR\' OR STATE=\'CA\' OR STATE=\'WA\' AND FIRE_YEAR=2015 AND FIRE_SIZE_CLASS=\'G\'', con)
    #df = pd.read_sql_query('SELECT FIRE_NAME, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE FROM Fires WHERE (STATE=\'OR\' OR STATE=\'CA\' OR STATE=\'WA\') AND FIRE_YEAR=2008 AND FIRE_SIZE_CLASS=\'G\'', con)
    df = pd.read_sql_query('SELECT FIRE_NAME, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE FROM Fires WHERE (STATE=\'OR\' OR STATE=\'CA\' OR STATE=\'WA\') AND FIRE_YEAR=2015', con)

    print(df.head())
    print(df.tail())

    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.LONGITUDE, df.LATITUDE))

    usa = geopandas.read_file('./states_21basic/states.shp')
    ax = usa[usa.SUB_REGION == 'Pacific'].plot()
 
    gdf.plot(ax=ax, color='red', markersize=1)
    plt.show()
    

create_western_us_map()
create_oregon_map_with_all_fires_2015()