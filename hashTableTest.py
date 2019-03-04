from hashTable import *

def hashFunTest():
    print("hashFun Test")
    count = 0
    ht = HashTable(4, 3)
    a = ht.put("1")

    if a == 1:
        count += 1

    a = ht.put("11")
    if a == 2:
        count += 1

    a = ht.put("111")
    if a == 3:
        count += 1

    a = ht.put("1111")
    if a == 0:
        count += 1

    a = ht.put("1")
    if a == None:
        count += 1

    if count == 5:
        print("OK")
    else:
        print("ERROR")

hashFunTest()

def putTest():
    print("put Test")
    count = 0
    ht = HashTable(4, 3)
    a = ht.put("1")

    if a == 1:
        count += 1

    a = ht.put("1")
    if a == 0:
        count += 1

    a = ht.put("1")
    if a == 3:
        count += 1

    a = ht.put("1")
    if a == 2:
        count += 1

    a = ht.put("1")
    if a == None:
        count += 1

    if count == 5:
        print("OK")
    else:
        print("ERROR")

putTest()

def seekSlotTest():
    print("seekSlot Test")
    count = 0
    ht = HashTable(4, 3)

    a = ht.seek_slot("1")
    if a == 1:
        count += 1

    ht.put("1")
    a = ht.seek_slot("1")
    if a == 0:
        count += 1

    ht.put("1")
    a = ht.seek_slot("1")
    if a == 3:
        count += 1

    ht.put("1")
    a = ht.seek_slot("1")
    if a == 2:
        count += 1

    ht.put("1")
    a = ht.seek_slot("1")
    if a == None:
        count += 1

    if count == 5:
        print("OK")
    else:
        print("ERROR")

seekSlotTest()

def findTest():
    print("find Test")
    count = 0
    ht = HashTable(4, 3)

    a = ht.find("1")

    if a == None:
        count += 1

    ht.put("1")
    a = ht.find("1")
    if a == 1:
        count += 1

    if count == 2:
        print("OK")
    else:
        print("ERROR")

findTest()