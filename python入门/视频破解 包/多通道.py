import re
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
from urllib import parse
window = tk.Tk()
window.title('哈哈哈哈哈哈')
window.geometry('300x230')
var = tk.StringVar()
zc = tk.Label(window, text='输入视频链接:（Ctrl 和 V 一块按可以粘贴哦！！！）')
zc.pack()
e = tk.Entry(window, show=None)
e.pack()
#port1 = 'http://www.wmxz.wang/video.php?url='
port2 = 'http://jx.618ge.com/?url='
port3 = 'https://www.administratorw.com/admin.php?url='
port4 = 'http://17kyun.com/api.php?url='
port1 = 'http://api.bbbbbb.me/jx/?url='
def bf1():
    if re.match(r'^https?:/{2}\w.+$', e.get()):
        ip = e.get()
        ip = parse.quote_plus(ip)
        webbrowser.open(port1 + ip)
    else:
        msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
b1 = tk.Button(window,text='播放方法1',font=('楷体', 12), fg='red',width=15,height=2,command=bf1)
b1.pack()
def bf2():
    if re.match(r'^https?:/{2}\w.+$', e.get()):
        ip = e.get()
        ip = parse.quote_plus(ip)
        webbrowser.open(port2 + ip)
    else:
        msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
b2 = tk.Button(window,text='播放方法2',font=('楷体', 12), fg='Purple',width=15,height=2,command=bf2)
b2.pack()
def bf3():
    if re.match(r'^https?:/{2}\w.+$', e.get()):
        ip = e.get()
        ip = parse.quote_plus(ip)
        webbrowser.open(port3 + ip)
    else:
        msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
b3 = tk.Button(window,text='播放方法3',font=('楷体', 12), fg='yellow',width=15,height=2,command=bf3)
b3.pack()
def bf4():
    if re.match(r'^https?:/{2}\w.+$', e.get()):
        ip = e.get()
        ip = parse.quote_plus(ip)
        webbrowser.open(port4 + ip)
    else:
        msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
b4 = tk.Button(window,text='播放方法4',font=('楷体', 12), fg='blue',width=15,height=2,command=bf4)
b4.pack()

window.mainloop()

