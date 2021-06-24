# coding=utf8
import requests
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillUnivList(text, num):
    response = requests.get(url, timeout=40)
    text = response.text
    data = json.loads(text)
    content = data['data']['rankings']
    ulist = []
    for i in range(num):
        index = content[i]['rankOverall']
        name = content[i]['univNameCn']
        score = content[i]['score']
        category = content[i]['univCategory']
        tags = content[i]['univTags']
        ulist.append([index, name, score, category, tags])
    return ulist


def printUnivList(ulist):
    tplt = "{0:^10}\t{1:^10}\t{3:^10}\t{4:^10}\t{5:^10}"
    print(tplt.format("排名", "学校名称", chr(12288), "总分", "类型", "标签"))
    for i in range(200):
        u = ulist[i]
        if u[4] in [[]]:
            print(tplt.format(u[0], u[1], chr(12288), u[2], u[3], ''))
        else:
            print(tplt.format(u[0], u[1], chr(12288), u[2], u[3], u[4][0]))


def draw():
    name_list = []
    score_list = []
    for i in range(10):
        u = ulist[i]
        name_list.append(u[1])
        score_list.append(u[2])
    plt.bar(name_list, score_list, fc='r')
    plt.show()


def main():
    global url, ulist
    url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021'
    text = getHTMLText(url)
    ulist = fillUnivList(text, 200)
    printUnivList(ulist)
    draw()


if __name__ == '__main__':
    main()
    #if __name__ == '__main__':,素数,and和or的短路特性
