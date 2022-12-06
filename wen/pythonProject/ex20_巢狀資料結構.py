v1={"name":"Emil","year":2004
}

v2={"name":"Tobias","year":2007
}

v3={"name":"Linus","year":2011
}


k1=1
k2=2
k3=3

#dict巢狀資料結構
d={
    k1:v1,
    k2: v2,
    k3: v3,

}

for v in d.values():
    print(v)

print(f"查詢v1=:{d[k1]}")
print("----------------")


#list巢狀資料結構
l=[v1,v2,v3]
for v in l:
    print(v)
print(f"查詢v1=:{l[0]}")