# -*- coding: utf-8 -*-
import math
import Extract

def CollideType(Track1CPA, Track2CPA):
    Heading1 = Track1CPA[4]
    Heading2 = Track2CPA[4]
    interval =  abs(Heading2 -  Heading1)
    if  175 <= interval and interval <= 185:    # Head-On Coflict
        return 1
    if (67.5 <= interval and interval < 175) or (185 < interval and interval <= 292.5):    # Crossing Coflict
        return 2
    if interval < 67.5 or (292.5 < interval and interval < 360):    # Overtaking Coflict
        return 3

def CollideRSpeed(Track1CPA, Track2CPA):
    sog1 = Track1CPA[3]
    sog2 = Track2CPA[3]
    cog1 = Track1CPA[2]
    cog2 = Track2CPA[2]
    Bearing = cog1 - cog2
    # 两船航向 夹角
    if Bearing < 0:
        Bearing = ((Bearing + 360) * math.pi) / 360
    else:
        Bearing = (Bearing * math.pi) / 360
    RV = math.sqrt( pow( sog1, 2 ) + pow( sog2, 2 ) - 2 * sog1 * sog2 * (math.cos( Bearing )) ) # 余弦定理 两边夹角求第三边 c^2=a^2+b^2-2abcosC
    return RV

def CollideWatchStage(Track1CPA):
    UTC = Track1CPA[7]
    Ltm = Extract.timestamp_to_date(UTC)
    Hour = float(Ltm[11:13])
    if (0 <= Hour and Hour < 4) or (12 <= Hour and Hour < 16):     # First officer
        return 1
    if (4 <= Hour and Hour < 8) or (16 <= Hour and Hour < 20):     # Second officer
        return 2
    if (8 <= Hour and Hour < 12) or (20 <= Hour and Hour < 24):    # Third officer
        return 3