# -*- coding: utf-8 -*-
import math
import numpy as np

def dis(coor1,coor2):
    lon1 = coor1[0]
    lat1 = coor1[1]
    lon2 = coor2[0]
    lat2 = coor2[1]

    dist = math.sqrt( pow( (lon2 - lon1), 2 ) + pow( (lat2 - lat1), 2 ) )
    return dist

def CPA(Track1,Track2):
    LLtm1 = Track1[0][7]
    RLtm1 = Track1[-1][7]
    LLtm2 = Track2[0][7]
    RLtm2 = Track2[-1][7]

    label1 = 0
    label2 = 0

    # error back
    t1 = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
    t2 = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]

    # 0. not time series
    if LLtm2 > RLtm2 or LLtm1 > RLtm1:
        return t1, t2

    # 1/6. LLtm2......RLtm2......LLtm1......RLtm1 or LLtm1......RLtm1......LLtm2......RLtm2
    if RLtm2 < LLtm1 or RLtm1 < LLtm2:
        return t1, t2 

    # 2. LLtm2......LLtm1......RLtm2......RLtm1
    if  LLtm2 <= LLtm1 and  LLtm1 <= RLtm2 and RLtm2 <= RLtm1 :
        if (RLtm2 - LLtm1)%5 != 0: 
            return t1, t2  # 返回
        interval = int( (RLtm2 - LLtm1) / 5 )

        a = np.array( Track1 )[:, 7]
        a = a.tolist()
        Lindex1 = a.index( LLtm1 )
        Rindex1 = a.index( RLtm2 )
        b = np.array( Track2 )[:, 7]
        b = b.tolist()
        Lindex2 = b.index( LLtm1 )
        Rindex2 = b.index( RLtm2 )

        if (Rindex1 - Lindex1) != (Rindex2 - Lindex2): 
            return t1, t2 

        mindist = 10000
        lenTime = int(Rindex1 - Lindex1)
        for i in range( 0, lenTime, 1 ):
            coor1 = []
            coor2 = []
            coor1.append( Track1[Lindex1+i][0] )
            coor1.append( Track1[Lindex1+i][1] )
            coor2.append( Track2[Lindex2+i][0] )
            coor2.append( Track2[Lindex2+i][1] )

            dist = dis( coor1, coor2 )
            if dist <= mindist:
                mindist = dist
                label1 = Lindex1 + i
                label2 = Lindex2 + i

    # 3. LLtm2......LLtm1......RLtm1......RLtm2
    if  LLtm2 <= LLtm1 and  RLtm1 <= RLtm2:
        if (RLtm1 - LLtm1)%5 != 0: 
            return t1, t2  
        interval = int( (RLtm1 - LLtm1) / 5 )
        a = np.array( Track1 )[:, 7]
        a = a.tolist()
        Lindex1 = a.index( LLtm1 )
        Rindex1 = a.index( RLtm1 )
        b = np.array( Track2 )[:, 7]
        b = b.tolist()
        Lindex2 = b.index( LLtm1 )
        Rindex2 = b.index( RLtm1 )

        if (Rindex1 - Lindex1) != (Rindex2 - Lindex2): 
            return t1, t2 

        mindist = 10000
        lenTime = int(Rindex1 - Lindex1)
        for i in range( 0, lenTime, 1 ):
            coor1 = []
            coor2 = []
            coor1.append( Track1[Lindex1+i][0] )
            coor1.append( Track1[Lindex1+i][1] )
            coor2.append( Track2[Lindex2+i][0] )
            coor2.append( Track2[Lindex2+i][1] )

            dist = dis( coor1, coor2 )
            if dist <= mindist:
                mindist = dist
                label1 = Lindex1 + i
                label2 = Lindex2 + i

    # 4. LLtm1......LLtm2......RLtm2......RLtm1
    if LLtm1 <= LLtm2 and RLtm2 <= RLtm1:
        if (RLtm2 - LLtm2) % 5 != 0: 
            return t1, t2 
        interval = int( (RLtm2 - LLtm2) / 5 )
        a = np.array( Track1 )[:, 7]
        a = a.tolist()
        Lindex1 = a.index( LLtm2 )
        Rindex1 = a.index( RLtm2 )
        b = np.array( Track2 )[:, 7]
        b = b.tolist()
        Lindex2 = b.index( LLtm2 )
        Rindex2 = b.index( RLtm2 )

        if (Rindex1 - Lindex1) != (Rindex2 - Lindex2): 
            return t1, t2 

        mindist = 10000
        lenTime = int( Rindex1 - Lindex1 )
        for i in range( 0, lenTime, 1 ):
            coor1 = []
            coor2 = []
            coor1.append( Track1[Lindex1 + i][0] )
            coor1.append( Track1[Lindex1 + i][1] )
            coor2.append( Track2[Lindex2 + i][0] )
            coor2.append( Track2[Lindex2 + i][1] )

            dist = dis( coor1, coor2 )
            if dist <= mindist:
                mindist = dist
                label1 = Lindex1 + i
                label2 = Lindex2 + i

    # 5. LLtm1......LLtm2......RLtm1......RLtm2
    if LLtm1 <= LLtm2 and LLtm2 <= RLtm1 and RLtm1 <= RLtm2:
        if (RLtm1 - LLtm2) % 5 != 0:
            return t1, t2 
        interval = int( (RLtm1 - LLtm2) / 5 )
        a = np.array( Track1 )[:, 7]
        a = a.tolist()
        Lindex1 = a.index( LLtm2 )
        Rindex1 = a.index( RLtm1 )
        b = np.array( Track2 )[:, 7]
        b = b.tolist()
        Lindex2 = b.index( LLtm2 )
        Rindex2 = b.index( RLtm1 )

        if (Rindex1 - Lindex1) != (Rindex2 - Lindex2): 
            return t1, t2 

        mindist = 10000
        lenTime = int( Rindex1 - Lindex1 )
        for i in range( 0, lenTime, 1 ):
            coor1 = []
            coor2 = []
            coor1.append( Track1[Lindex1 + i][0] )
            coor1.append( Track1[Lindex1 + i][1] )
            coor2.append( Track2[Lindex2 + i][0] )
            coor2.append( Track2[Lindex2 + i][1] )

            dist = dis( coor1, coor2 )
            if dist <= mindist:
                mindist = dist
                label1 = Lindex1 + i
                label2 = Lindex2 + i

    return Track1[label1], Track2[label2]