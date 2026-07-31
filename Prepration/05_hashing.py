import time
def hashing(list1, list2):
    start = time.time()
    for i in list2:
        count = 0
        for j in list1:
            if(j == i):
                count += 1
        print(f"{i} : {count}")
    print(time.time() - start)

def hashing2(list1, list2):                  # optimal
    start = time.time()
    hash_dict = {}
    for i in list1:
        if(i in hash_dict):
            hash_dict[i] += 1
        else:
            hash_dict[i] = 1

    for j in list2:
        if(j in hash_dict):
            print(f"{j} : {hash_dict[j]}")
    print(time.time() - start)

list1 = [1,2,3,4,5,6,7,8,9,2,4,5,7,8,1,5,4,8,0,1,5,18]
list2 = [1,2,3,4,5,6,7,8,9]
hashing(list1, list2)
print("-"*10)
hashing2(list1, list2)