#coding:utf-8
import subprocess

from baseClass import suijishu


class Screenshot():  # 截取手机屏幕并保存到电脑
    def __init__(self):
        # 查看连接的手机
        connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = connect.communicate()  # 获取返回命令
        # 输出执行命令结果
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        print(stdout)
        print(stderr)

    def screen(self, cmd):  # 在手机上截图
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        # 输出执行命令结果结果
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        print(stdout)
        print(stderr)

    def saveComputer(self, cmd):  # 将截图保存到电脑
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        # 输出执行命令结果结果
        print(stdout)
        print(stderr)

i=0
cmd1 = r"adb shell /system/bin/screencap -p /sdcard/{i}.png"  # 命令1：在手机上截图3.png为图片名
cmd2 = r"adb pull /sdcard/{i}.png d:/123/{i}.png"  # 命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
screen = Screenshot()
screen.screen(cmd1)
screen.saveComputer(cmd2)