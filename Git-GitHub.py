from time import sleep


#爬取前提示
print("本程序用于练习爬虫\n将会爬取“https://raw.hellogithub.com/hosts”\n这可以获取GitHub的可用IP\n随后可以选择是否写入hosts和刷新域名服务器\n继续吗？")
sleep(1)
a=input("\n按 Enter 键开始爬取...\n关键字‘q’退出\n")
if a == "q":
    exit()
#注意：a的作用只是临时判定用的


#爬取内容
from requests import get,exceptions #在这里引入是为了避免误运行此脚本时而造成白引入

print("尝试爬取……")
for i in range(5):
    try:
        h=get("https://raw.hellogithub.com/hosts",timeout=9)
    
        if h.status_code == 200:
             print(f"成功！状态：{h.status_code}\n")
             h.encoding = 'utf-8'
             sleep(2)
             print(h.text)    #可加可不加
             break             
        else:
             print(f"请求失败,状态：{h.status_code}\n正在重试。")
    except exceptions.Timeout:    #处理超时
        print("超时！\n正在重试。")
        sleep(3)
    except Exception as e:    #处理未知错误
        print(f"出错：{e}\n正在重试。")
        sleep(3)
    if i ==4:
        print ("尝试5次均失败，请检查错误提示后手动重试。")
        exit()

#请求把爬取内容写入剪切板
a=input("是否要写入剪切板？\n默认“y”\ny/n\n")
if a == "y" or a == '':
    from pyperclip import copy
    copy(h.text)

#请求打开hosts
a=input("\n是否要打开hosts？\n这将会尝试用管理员身份打开'C:\\Windows\\System32\\drivers\\etc\\hosts'\n默认“y”\ny/n\n")
if a == "y" or a == '':
    from subprocess import run
    hosts = r'C:\Windows\System32\drivers\etc\hosts'
    run(f'runas /user:Administrator "notepad.exe {hosts}"', shell=True)

#请求刷新DNS
a=input("\n是否要刷新域名服务器？\n默认“y”\ny/n\n")
if a == "y" or a == '':
    run(f'runas /user:Administrator "ipconfig /flushdns"', shell=True)
    print("成功刷新DNS。")

print("正在退出……")
sleep(3)
