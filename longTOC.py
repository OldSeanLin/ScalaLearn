'''本脚本用来解决vscodeTOC插件不能对很长的markdown生成目录的问题
目前是直接输出目录，通过复制粘贴的方式放入源文件，不会有写操作，避免失误将心血破坏
'''

'''脚本逻辑，按行读取，如果行包含“#”则提取该行
根据“#”确定tab的个数。
为了显示你的工作量，顺便会统计字数。
[显示的内容](#标题标号-标题文本)
注意要点:
1. []中括号填写需要在页面上显示的内容；
2. ()小括号内部声明跳转目标标题，以#开头，标题题号如果包含.、下划线直接忽略掉，标题文本中如果有空格，使用-横杠符号替代，标题文本中的大写字母转换成小写。
'''

#TODO:添加序号功能，以后有空做。把打印到屏幕上的内容写入文本文件

def readTile(path):
    file = open(path,encoding="utf-8") 
    titles=[]
    count=0
    for line in file:
        if "#" in line and "目录" not in line:
            titles.append(line.replace("\n",""))
        line.replace(" ","")
        count+=len(line)
    print(count)
    print(titles)
    return titles

def convertTOC(titles):
    begin="<!-- TOC -->"
    print(begin)
    for t in  titles:
        sharp=t.lstrip().split(" ")[0]
        tabNum=len(sharp)
        t2=t[tabNum+1:].replace(" ","-").replace("_","").replace(".","").replace("*","").lower()
        t1=" "*tabNum
        toc = "%s- [%s](#%s)"%(t1,t[tabNum+1:],t2)
        print(toc)
    end="<!-- /TOC -->"
    print(end)



   


if __name__ == "__main__":
    path='scalaBOOK_copy.md'
    titles =  readTile(path)
    convertTOC(titles)



