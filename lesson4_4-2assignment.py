import csv

data = []
tdata = []
cnt = 0
temp = []
months = {"Jan":0, "Feb":1, "Mar":2, "Apr":3, "May":4, "Jun":5, "Jul":6, "Aug":7, "Sep":8, "Oct":9, "Nov":10, "Dec":11 }
def Read(filename):
    global cnt
    global rdr
    f = open(filename, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        #print(line)
        #print(parser.split('/')[1])
        cnt = cnt + 1
        if(cnt != 1):
            #print(line)
            t = tuple(line)
            data.append(t)
    #print(data)
    #print(cnt)
    #print(data[0])
    f.close()

def Sort(index):
    data.sort(key = lambda element:element[index])

def tSort(index):
    global months
    global tdata
    #배열 새로 만들고, 새로 정렬
    #print(data)
    for i in data:
        #print(i)
        ci = list(i)
    # 일단 월->숫자 로 바꿔주기
    # 중간 날짜 part를 이제 분리해주기
        #print(ci[1]) 시간문장단위
        #print((ci[1].split(':')[0]).split('[')[1])
        #front.append(ci[1][13:])
        #print(ci[1][13:])
        shi = ci[1][13:].split(':')[0]
        fen = ci[1][13:].split(':')[1]
        xiao = ci[1][13:].split(':')[2]
        new_front = xiao + ":" + fen + ":" + shi
        #print(new_front)
        back = (ci[1].split(':')[0]).split('[')[1]
        ri = back.split('/')[0]
        yue = back.split('/')[1]
        nian = back.split('/')[2]
        new_back = ri + "/" + yue + "/" + nian
        #print(new_back)
        #newci1 = (xiao,fen,shi,ri,yue,nian)
        #print(newci1)
        #tdata.append([ci[0],xiao+":"+fen+ ":" +shi + ":" +ri+ "/" + yue + "/"+ nian,ci[2]])
        tdata.append([ci[0], nian + "/" + str(months[yue]) + "/" + ri + "," + shi + ":" + fen + "/" + xiao, ci[2]])
    tdata.sort( key=lambda element: element[index])

    #for i in data:
    #    print(i)
    for i in tdata:
        for yue,num in months.items():
            if (int(i[1].split('/')[1])) == num:
                print( i[0] + ' , '+ i[1][:5] + yue + i[1][6:] + ' , ' +i[2] )

if __name__=="__main__":

    while True:
        commend = input("$ ")

        if len(commend.split()) == 2:
            second = commend.split()[1]

        first = commend.split()[0]

        if first == "read":
            Read(second)

        if first == "sort":
            if second == "-t":
                tSort(1)



            if second == "-ip":
                Sort(0)

        # if first == "print":
        #     for i in range(len(data)):
                # print("IP : ",data[i][0])
                # print("TIME : ",data[i][1].split("[")[1])
                # print("URL : ",data[i][2])
                # print("Staus : ", data[i][3])
                # print("---------------------")
                #print(data[i])

        if first == "exit":
            break