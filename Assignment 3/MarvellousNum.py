def CheckPrime(TempList, Size):
    PrimeLis = []
    TempNum = 0
    Countr = 0

    for i in range (Size):
        TempNum = int(TempList[i]/2)

        while (TempNum > 1):
            if ((TempList[i] % TempNum) == 0):
                Countr = Countr + 1
            
            TempNum = TempNum - 1
            
        if (Countr == 0):
            PrimeLis.append(TempList[i])

        Countr = 0

    return PrimeLis

def AddPrime(TempList):
    
    TempAdd = 0
    Size = len(TempList)

    for i in range (Size):
        TempAdd = TempAdd + TempList[i]

    return TempAdd