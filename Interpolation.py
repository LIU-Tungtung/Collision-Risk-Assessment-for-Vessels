# -*- coding: utf-8 -*-
import AIS
import math
import Extract
import numpy as np

def Interpolation():
    WATERID = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    TRACK_WATER = []
    for id in WATERID:
        db = AIS.Ais( host="localhost", user="root", password="123456", db="aisdb", port=3306, charset='gbk' )
        sql_MMSI = "select distinct SHIPID from ningbo_id where WATERID = " + str(id)
        MMSI = db.Query( sql_MMSI )
        TRACKS = []
        for mmsi in MMSI:
            sql_MMSI = "select LON,LAT,COG,SOG,TRUEHEADING,LOA,BM,LTM from ningbo_id where SHIPID = " + str( mmsi[0] ) +" and WATERID = " + str(id) + " order by LTM"
            track = db.Query( sql_MMSI )
            if len( track ) <= 10:
                continue
            TS = []
            time = np.array(track)[:, 7]
            for ltm in time:
                t = Extract.date_to_timestamp( ltm, format_string="%Y%m%d%H%M%S" )
                TS.append( t )

            if mmsi[0] == 412205101:
                test = 0

            TT = []
            temp = []
            ii = 0 
            for ii in range(1,len(TS),1):
                temp.append( TS[ii - 1] )
                inter = float(TS[ii]) - float(TS[ii - 1])
                if inter >= 600.0:
                    TT.append(temp)
                    temp = []
            if ii <= 0 or ii >= len(TS): 
                break
            temp.append( TS[ii] )
            TT.append( temp )

            for T in TT:
                n = len( T )
                if n <= 5:
                    continue
                TRACK = []
                UTCleft = T[0]
                lv = math.ceil( UTCleft / 5.0 )
                UTCleft = int( lv * 5 )

                for i in range( 1, n, 1 ):
                    if T[i] <= UTCleft:  
                        continue
                    Ta = T[i - 1]
                    Tb = UTCleft
                    Tc = T[i]
                    lon = track[i - 1][0] / 600000.0 + (track[i][0] / 600000.0 - track[i - 1][0] / 600000.0) * (
                            Tb - Ta) / (
                                  Tc - Ta)
                    lat = track[i - 1][1] / 600000.0 + (track[i][1] / 600000.0 - track[i - 1][1] / 600000.0) * (
                            Tb - Ta) / (
                                  Tc - Ta)
                    cog = (track[i - 1][2] / 10.0) + (track[i][2] / 10.0 - track[i - 1][2] / 10.0) * (
                            Tb - Ta) / (
                                  Tc - Ta)
                    sog = (track[i - 1][3] / 10.0) + (track[i][3] / 10.0 - track[i - 1][3] / 10.0) * (
                            Tb - Ta) / (
                                  Tc - Ta)
                    heading = (track[i - 1][4]) + (track[i][4] - track[i - 1][4]) * (
                            Tb - Ta) / (
                                      Tc - Ta)
                    temp = []
                    temp.append( lon )
                    temp.append( lat )
                    temp.append( cog )
                    temp.append( sog )
                    temp.append( heading )
                    temp.append( track[0][5] )
                    temp.append( track[i][6] )
                    temp.append( UTCleft )  
                    temp.append( id )  
                    temp.append( int(mmsi[0]) ) 

                    TRACK.append( temp )
                    break

                for i in range( 1, n, 1 ):
                    if T[i] <= UTCleft:  
                        continue
                    m = int( math.floor( (T[i] - UTCleft) / 5.0 ) )
                    for j in range( 0, m, 1 ):
                        # deltatime = int( (j+1) * 5 )
                        UTCleft = 5 + UTCleft
                        Ta = T[i - 1]
                        Tb = UTCleft
                        Tc = T[i]

                        lon = track[i - 1][0] / 600000.0 + (track[i][0] / 600000.0 - track[i - 1][0] / 600000.0) * (
                                Tb - Ta) / (
                                      Tc - Ta)
                        lat = track[i - 1][1] / 600000.0 + (track[i][1] / 600000.0 - track[i - 1][1] / 600000.0) * (
                                Tb - Ta) / (
                                      Tc - Ta)
                        cog = (track[i - 1][2] / 10.0) + (track[i][2] / 10.0 - track[i - 1][2] / 10.0) * (
                                Tb - Ta) / (
                                      Tc - Ta)
                        sog = (track[i - 1][3] / 10.0) + (track[i][3] / 10.0 - track[i - 1][3] / 10.0) * (
                                Tb - Ta) / (
                                      Tc - Ta)
                        heading = (track[i - 1][4]) + (track[i][4] - track[i - 1][4]) * (
                                Tb - Ta) / (
                                          Tc - Ta)
                        temp = []
                        temp.append( lon )
                        temp.append( lat )
                        temp.append( cog )
                        temp.append( sog )
                        temp.append( heading )
                        temp.append( track[0][5] )
                        temp.append( track[i][6] )
                        temp.append( UTCleft ) 
                        temp.append( id )
                        temp.append( int( mmsi[0] ) )  

                        TRACK.append( temp )
                TRACKS.append( TRACK )

        TRACK_WATER.append( TRACKS )
    return TRACK_WATER