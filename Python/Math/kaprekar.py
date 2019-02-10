def isKaprekar(num):
    numSqr = num*num
    lenNum = len(str(num))
    lenNumSqr = len(str(numSqr))
    r=int(str(numSqr)[lenNumSqr-lenNum:])
    if lenNumSqr>lenNum:
        l =  int(str(numSqr)[:lenNumSqr-lenNum])
    else:
        l =0
    if l+r==num and r!=0:
        return True
    else:
        return False