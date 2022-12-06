def 初值(st):
    name=None
    eng=None
    math=None
    st.append(name)
    st.append(eng)
    st.append(math)

def 修改值(st,name=None,eng=None,math=None):
    st[0]=name
    st[1]=eng
    st[2]=math

def 總分(st):
    name=st[0]
    eng=st[1]
    math=st[2]
    tot=None
    if eng is not None and math is not None:
        tot=eng+math
    return tot
#顯示
def 顯示(st):
    name=st[0]
    eng=st[1]
    math=st[2]
    tot= 總分(st)
    print(name,eng,math,tot)

#主程式
st1 =list()
初值(st1)
顯示(st1)
修改值(st1,name="Wendy",eng=80,math=90)
顯示(st1)

st2 =list()
初值(st2)
顯示(st2)
修改值(st2,name="Vivi",eng=85,math=85)
顯示(st2)


