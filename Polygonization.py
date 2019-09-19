# -*- coding: utf-8 -*-
import numpy as np
import geopy.distance
from matplotlib import pyplot as plt

def get_distance_point(lat, lon, distance, direction):
    """
    根据经纬度，距离，方向获得一个地点
    :param lat: 纬度
    :param lon: 经度
    :param distance: 距离（千米）
    :param direction: 方向（北：0，东：90，南：180，西：360）
    :return:
    """
    start = geopy.Point(lat, lon)
    d = geopy.distance.VincentyDistance(kilometers=distance)
    return d.destination(point=start, bearing=direction)

# 1. Square Ship Domain
def Square(Track1CPA,Track2CPA):
    Center1Lon = Track1CPA[0]
    Center1Lat = Track1CPA[1]

    cog1 = Track1CPA[4]
    Head1Bearing = cog1
    Studboard1Bearing = cog1 + 90
    Aft1Bearing = cog1 + 180
    Port1Bearing = cog1 + 270
    if Studboard1Bearing > 360:
        Studboard1Bearing = Studboard1Bearing - 360
    if Aft1Bearing > 360:
        Aft1Bearing = Aft1Bearing - 360
    if Port1Bearing > 360:
        Port1Bearing = Port1Bearing - 360
    Loa1 = Track1CPA[4]/(1000)
    Head1Ridus = 3*Loa1
    Studboard1Ridus = 0.8*Loa1
    Aft1Ridus = 3*Loa1
    Port1Ridus = 0.8*Loa1

    Pos1Head = get_distance_point( Center1Lat,  Center1Lon, Head1Ridus,Head1Bearing )
    Pos1Studboard = get_distance_point( Center1Lat,  Center1Lon, Studboard1Ridus,Studboard1Bearing )
    Pos1Aft = get_distance_point( Center1Lat,  Center1Lon, Aft1Ridus, Aft1Bearing )
    Pos1Port = get_distance_point( Center1Lat,  Center1Lon, Port1Ridus , Port1Bearing)

    Square1 = [(Pos1Head.longitude,Pos1Head.latitude),(Pos1Studboard.longitude,Pos1Studboard.latitude),(Pos1Aft.longitude,Pos1Aft.latitude),(Pos1Port.longitude,Pos1Port.latitude)]
    Center2Lon = Track2CPA[0]
    Center2Lat = Track2CPA[1]
    Center2Lon = Track2CPA[0]
    Center2Lat = Track2CPA[1]

    cog2 = Track2CPA[4]
    Head2Bearing = cog2
    Studboard2Bearing = cog2 + 90
    Aft2Bearing = cog2 + 180
    Port2Bearing = cog2 + 270
    if Studboard2Bearing > 360:
        Studboard2Bearing = Studboard2Bearing - 360
    if Aft2Bearing > 360:
        Aft2Bearing = Aft2Bearing - 360
    if Port1Bearing > 360:
        Port2Bearing = Port2Bearing - 360

    Loa2 = Track2CPA[4]/(1000)
    Head2Ridus = 3*Loa2
    Studboard2Ridus = 0.8*Loa2
    Aft2Ridus = 3*Loa2
    Port2Ridus = 0.8*Loa2

    Pos2Head = get_distance_point( Center2Lat, Center2Lon, Head2Ridus , Head2Bearing)
    Pos2Studboard = get_distance_point( Center2Lat, Center2Lon, Studboard2Ridus, Studboard2Bearing )
    Pos2Aft = get_distance_point( Center2Lat, Center2Lon, Aft2Ridus, Aft2Bearing )
    Pos2Port = get_distance_point(  Center2Lat, Center2Lon,Port2Ridus, Port2Bearing )

    Square2 = [(Pos2Head.longitude, Pos2Head.latitude), (Pos2Studboard.longitude, Pos2Studboard.latitude),
               (Pos2Aft.longitude, Pos2Aft.latitude), (Pos2Port.longitude, Pos2Port.latitude)]

    return Square1,Square2

# 2. Circle Ship Domain
def Circle(Track1CPA,Track2CPA):

    Center1Lon = Track1CPA[0]
    Center1Lat = Track1CPA[1]
    Loa1 = Track1CPA[4]
    Ridus1 = Loa1
    Circle1 = [(Center1Lon,Center1Lat,Ridus1)]

    Center2Lon = Track2CPA[0]
    Center2Lat = Track2CPA[1]
    Loa2 = Track2CPA[4]
    Ridus2 = Loa2
    Circle2 = [(Center2Lon,Center2Lat,Ridus2)]

    return Circle1, Circle2

# 3. Circle Ship Domain
# def Circle(Track1CPA,Track2CPA):
#     return