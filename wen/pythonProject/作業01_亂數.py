import random
from itertools import count


#產生亂數 x=產生多少個
def RandomList(x,f,l):
    data=list()
    for num in range(x):
        data.append(random.randint(f,l)) #自己定義亂數範圍
    return data

def verifyData(num,data):
    #奇偶數判別
    if num==1:
        奇數=0
        偶數=0
        for x in data:
            if x%2==0:
                偶數=偶數+1
            else:
                奇數 = 奇數 + 1
        print(f"list中奇數有={奇數}個")
        print(f"list中偶數有={偶數}個")
    #最大最小值判別
    elif num==2:
        # print(data)
        print(f"list中最大值={max(data)}")
        print(f"list中最小值={min(data)}")
    #加總
    elif num == 3:
        # print(data)
        print(f"list加總={sum(data)}")
    # 平均
    elif num == 4:
        # print(data)
        print(f"list平均={sum(data)/len(data)}")
    #各數出現次數
    elif num == 5:
        minNum = min(data)  # 最小
        maxNum = max(data)  # 最大
        # 取得變數中數字範圍
        for x in range(1, 6):
            print(f"list中{x}出現了={data.count(x)}")

    elif num == 6:
        pass
    #死板寫法
    # one=0
    # two=0
    # three=0
    # four=0
    # five=0
    # # print(data)
    # for x in data:
    #     if x==1:
    #         one=one+1
    #     elif x==2:
    #         two=two+1
    #     elif x==3:
    #         three=three+1
    #     elif x==4:
    #         four=four+1
    #     else:
    #         five=five+1
    # print(f"list中1出現了={one}次")
    # print(f"list中2出現了={two}次")
    # print(f"list中3出現了={three}次")
    # print(f"list中4出現了={four}次")
    # print(f"list中5出現了={five}次")
    else:
        pass



#主程式
rList=RandomList(10,1,5)
print(f"List={rList}")
verifyData(1,rList)
verifyData(2,rList)
verifyData(3,rList)
verifyData(4,rList)
verifyData(5,rList)