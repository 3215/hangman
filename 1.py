import easygui as g
import sys

while 1:
    g.msgbox('嘿，草泥马')

    msg = '操你大爷'
    title = '游戏互动'
    choices = ['打飞机','看片','叫鸡']
    
    choice = g.choicebox(msg, title, choices)
    
    g.msgbox('你的选择是：' + str(choice), '结果')

    msg = '你希望重新开始打飞机吗？'
    title = '请选择'

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
