# linear search (doğrusal arama)

meyveler = ["elma","muz","kiraz"]
yeri=-1
aranan = "muz"
for abc in range(len(meyveler)):
    if meyveler[abc] == aranan : yeri=abc
print(aranan,"ifadesinin yeri:",yeri)

##########################################################
#iterative method

def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
k = 5
result = binarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

##########################################################
#recursive method

def BinarySearch(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return BinarySearch(arr, k, low, mid-1)
        else:
            return BinarySearch(arr, k, mid + 1, high)
    else:
        return -1
arr = [1, 3, 5, 7, 9]
k = 5
result = BinarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

##########################################################
#jump search method

import math

def AtlayarakAra (ArananilacakYer, aranan):
    elemansayisi = len(ArananilacakYer)
    atlamamiktari = int(math.sqrt(elemansayisi))
    basi, sonu = 0, 0
    while basi < elemansayisi and ArananilacakYer[basi] <= aranan:
        sonu = min(elemansayisi - 1, basi + atlamamiktari)
        if ArananilacakYer[basi] <= aranan and ArananilacakYer[sonu] >= aranan:
            break
        basi += atlamamiktari;
    if basi >= elemansayisi or ArananilacakYer[basi] > aranan:
        return -1
    sonu = min(elemansayisi - 1, sonu)
    i = basi
    while i <= sonu and ArananilacakYer[i] <= aranan:
        if ArananilacakYer[i] == aranan:
            return i
        i += 1
    return -1
print(AtlayarakAra([1,2,3,4,5,6,7,8,9], 4))

##########################################################
# Fibonacci search

def FibonacciileAra(AranacakYer, aranan):
    fibS_onceki_2 = 0
    fibS_onceki_1 = 1
    fibS = fibS_onceki_1 + fibS_onceki_2
    while (fibS < len(AranacakYer)):
        fibS_onceki_2 = fibS_onceki_1
        fibS_onceki_1 = fibS
        fibS = fibS_onceki_1 + fibS_onceki_2
    yer = -1;
    while (fibS > 1):
        i = min(yer + fibS_onceki_2, (len(AranacakYer)-1))
        if (AranacakYer[i] < aranan):
            fibS = fibS_onceki_1
            fibS_onceki_1 = fibS_onceki_2
            fibS_onceki_2 = fibS - fibS_onceki_1
            yer = i
        elif (AranacakYer[i] > aranan):
            fibS = fibS_onceki_2
            fibS_onceki_1 = fibS_onceki_1 - fibS_onceki_2
            fibS_onceki_2 = fibS - fibS_onceki_1
        else :
            return i
    if(fibS_onceki_1 and yer < (len(AranacakYer)-1) and AranacakYer[yer+1] == aranan):
        return yer+1;
    return -1
print(FibonacciileAra([1,2,3,4,5,6,7,8,9,10,11], 1))

##########################################################
# exponential search

def bolerekAra( aranacakYer, basi, sonu, aranan):
    if sonu >= basi:
        orta = basi + ( sonu-basi ) // 2
        if aranacakYer[orta] == aranan: # If the element is present at
            return orta # the middle itself
        if aranacakYer[orta] > aranan:# If the element is smaller than orta,
            return bolerekAra(aranacakYer, basi, orta - 1, aranan)# then it can only in left part
        return bolerekAra(aranacakYer, orta + 1, sonu, aranan)# Else it can only be in the right
    return -1 # We reach here if the element is not present
# Returns the position of first occurrence of aranan in aranacakYeray
def ustalarakAra(aranacakYer, elemanSayisi, aranan):
    if aranacakYer[0] == aranan: # IF aranan is present at first
        return 0 # location itself
    i = 1
    while i < elemanSayisi and aranacakYer[i] <= aranan: # Find range for binary search
        i = i * 2 # j by repeated doubling    
    return bolerekAra( aranacakYer, i // 2, min(i, elemanSayisi-1), aranan)# Call binary search for the found range
aranacakYer = [2, 3, 4, 10, 40] # Array
elemanSayisi = len(aranacakYer)
aranan = 22
yeri = ustalarakAra(aranacakYer, elemanSayisi, aranan)
if yeri == -1: print (aranan,"elemanı",aranacakYer,"dizisinde bulunamadı") 
else: print ("Aradığınız elemanın yeri %d" %(yeri))

##########################################################
# interpolation search

def InterpolationSearch(arananYer, aranan):
    basi = 0
    sonu = (len(arananYer) - 1)
    while basi <= sonu and aranan >= arananYer[basi] and aranan <= arananYer[sonu]:
        yeri = basi + int(((float(sonu - basi) / ( arananYer[sonu] - arananYer[basi])) * ( aranan - arananYer[basi])))
        if arananYer[yeri] == aranan:
            return yeri
        if arananYer[yeri] < aranan:
            basi = yeri + 1;
        else:
            sonu = yeri - 1;
    return -1
print(InterpolationSearch([1,2,3,4,5,6,7,8], 8))

##########################################################
# https://www.geeksforgeeks.org/searching-algorithms/ 
# https://stackabuse.com/search-algorithms-in-python/#membershipoperators 
# https://www.geeksforgeeks.org/searching-algorithms/
# https://www.tutorialspoint.com/python_data_structure/python_searching_algorithms.htm
# https://www.educative.io/edpresso/how-to-search-in-python
# https://favtutor.com/blogs/searching-algorithms


