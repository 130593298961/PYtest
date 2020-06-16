# coding=utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from baseClass import suijishu

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    # "deviceName": "Honor Play",
    "deviceName":"HRY-AL00a",
    "appPackage": "com.fgh.dnwx",
    "appActivity": ".ui.main.SplashActivity",
    # "appPackage": "com.example.myapplication",
    # "appActivity": ".MainActivity",
    "autoAcceptAlerts": "true",
    "noReset": "true",
    'automationName': 'uiautomator2'
}

#获取屏幕长宽
# def test_a_getSize(self):
#     x = self.driver.get_window_size()['width']
#     y = self.driver.get_window_size()['height']
#     return (x, y)

userName = suijishu.get_random_str(6)
password = suijishu.get_random_str(3)
search = suijishu.get_random_china(3)
print(userName)
print(password)
print(search)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print('连接成功，开始测试')
sleep(6)

# i=0
# while(i<20):
#   i=i+1
#   driver.find_element_by_android_uiautomator('new UiSelector().text("注册")').click()
#   driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
#   print(i)
#   continue
# try:
#   driver.find_element_by_id('btn_casual')
# except Exception as e:
#   print('未找到元素')
# else:
#   driver.find_element_by_id('btn_casual').click()
#

# 登陆
print('开始测试登录校验')
#向上滑动
# def test_swipeUp(self,t):   #p
#     l=self.getSize()
#     x1=int(l[0]*0.5)
#     y1=int(l[1]*0.75)
#     y2=int(l[1]*0.25)
#     self.driver.swipe(x1,y1,x1,y2,t)
try:
    driver.find_element_by_id('btn_login').click()
    toast_message = "请输入账号"
    message = '//*[@text=\'{}\']'.format(toast_message)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
    assert toast_element.text == '请输入账号'
except Exception as e:
    print('校验账号失败')
else:
    pass
sleep(2)

try:
    driver.find_element_by_id('edit_phone').send_keys(userName)
    driver.find_element_by_id('btn_login').click()
    toast_message = "请输入密码"
    message = '//*[@text=\'{}\']'.format(toast_message)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
    assert toast_element.text == '请输入密码'
except Exception as e:
    print('校验密码失败')
sleep(2)

try:
    driver.find_element_by_id('edit_phone').send_keys(userName)
    driver.find_element_by_id('edit_password').send_keys(password)
    driver.find_element_by_id('cb_login').click()
    driver.find_element_by_id('btn_login').click()
    toast_message = "请勾选同意"
    message = '//*[@text=\'{}\']'.format(toast_message)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
    assert toast_element.text == '请勾选同意'
except Exception as e:
    print('校验隐私协议失败')
else:
    pass
sleep(2)

# driver.find_element_by_id('edit_phone').send_keys(userName)
# driver.find_element_by_id('edit_password').send_keys(password)
# driver.find_element_by_id('btn_login').click()
# toast_message = "账号或密码错误"
# message = '//*[@text=\'{}\']'.format(toast_message)
# toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
# print(toast_element.text)
# assert toast_element.text=='账号或密码错误'
# sleep(2)

try:
    driver.find_element_by_id('edit_phone').send_keys('13645121332')
    driver.find_element_by_id('edit_password').send_keys('13645121332')
    driver.find_element_by_id('cb_login').click()
    driver.find_element_by_id('btn_login').click()
    sleep(2)
    my = driver.find_element_by_android_uiautomator('new UiSelector().text("首页")')
except Exception as e:
    print('登录失败，未找到首页', e)
    print('切换游客登录进行测试')
    driver.find_element_by_id('btn_casual').click()
else:
    print('登录成功')
    pass
sleep(3)

# try:
#     driver.find_element_by_id("search_ly").click()
#     print('点击搜索栏')
# except Exception as e:
#     print('打开搜索栏失败，未找到热门搜索标题', e)
# else:
#     pass
# sleep(3)
#
# try:
#     driver.find_element_by_id('edt_search').send_keys(search)
#     print('在搜索栏输入内容')
#     sleep(3)
#     driver.find_element_by_id('sta_search').click()
#     print('点击搜索按钮')
#     sleep(3)
# except Exception as e:
#     print('点击返回按钮，返回首页')
# else:
#     pass
#
# driver.find_element_by_id('btn_back').click()
#
# try:
#     driver.find_element_by_id('btn_notice').click()
#     print('点击消息图标')
# except Exception as e:
#     print('点击无反应')
# else:
#     pass
#
# try:
#     # driver.find_element_by_id('btn_more_course').click()
#     driver.find_element_by_id('titleRight').click()
#     print('点击编辑按钮')
#     driver.find_elements_by_id('checkBox')[0].click()
#     print('勾选消息列表第一条')
#     driver.find_element_by_id('tv_delete').click()
#     print('点击删除按钮')
# except Exception as e:
#     print('删除失败')
# else:
#     pass
#
# driver.find_element_by_class_name('android.widget.ImageButton').click()
#
# try:
#     driver.find_element_by_id('btn_ask').click()
#     print('点击搜索栏左侧按钮')
#     driver.find_elements_by_id('rl_course')[0].click()
#     print('选择咨询科目')
#     driver.find_element_by_id('edit_chat').send_keys('你好')
#     driver.find_element_by_id('btn_send').click()
#     driver.find_element_by_id('edit_chat').send_keys('你好')
#     driver.find_element_by_id('btn_send').click()
#     driver.find_element_by_id('edit_chat').send_keys('你好')
#     driver.find_element_by_id('btn_send').click()
#     driver.find_element_by_class_name('android.widget.ImageButton').click()
#     driver.find_element_by_class_name('android.widget.ImageButton').click()
# except Exception as e:
#     print('发送失败')
# else:
#     pass

# try:
#     driver.find_elements_by_id('rl_home_course')[0].click()
#     print('点击课程')
# #待定
# except Exception as e:
#     print('')
# else:
#     pass

# try:
#     driver.find_element_by_id('btn_more_course').click()
#     print('点击我的课程更多按钮')
# except Exception as e:
#     print()
# else:
#     pass

# try:
#     driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
#     driver.find_elements_by_id('user_img')[0].click()
#     print('点击头像进入个人中心')
#     driver.find_element_by_id('user_nickname').click()
#     driver.find_element_by_id('edit_content').send_keys('牛牛就叫牛牛')
#     driver.find_element_by_id('titleRight').click()
#     print('修改昵称并提交')
#     toast_message = "修改成功"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '修改成功'
# except Exception as e:
#     print(e)
# else:
#     pass
#
# try:
#     driver.find_element_by_id('user_sex').click()
#     # driver.find_element_by_id().send_keys()
#     driver.find_element_by_id('tv_man').click()
#     # driver.find_element_by_id('titleRight').click()
#     print('修改性别并提交')
#     toast_message = "修改成功"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '修改成功'
# except Exception as e:
#     print(e)
# else:
#     pass
#
# try:
#     driver.find_element_by_id('tv_autograph').click()
#     driver.find_element_by_id('edit_content').send_keys('牛牛就是牛牛')
#     # driver.find_element_by_id('tv_man').click()
#     driver.find_element_by_id('titleRight').click()
#     print('修改签名并提交')
#     toast_message = "修改成功"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '修改成功'
# except Exception as e:
#     print(e)
# else:
#     pass
#
# try:
#     driver.find_element_by_id('real_name_ly').click()
#     driver.find_element_by_id('edit_content').send_keys('牛牛就是牛牛')
#     # driver.find_element_by_id('tv_man').click()
#     driver.find_element_by_id('titleRight').click()
#     print('修改真实姓名并提交')
#     toast_message = "修改成功"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '修改成功'
# except Exception as e:
#     print(e)
# else:
#     pass
#
# #修改密码
# try:
#     driver.find_element_by_id('tv_change_password').click()
#     # driver.find_element_by_id('edt_old_password').send_keys('123')
#     driver.find_element_by_id('btn_define').click()
#     toast_message = "请输入原始密码"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '请输入原始密码'
#
#     driver.find_element_by_id('edt_old_password').send_keys('123')
#     driver.find_element_by_id('btn_define').click()
#     toast_message = "密码错误"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '密码错误'
#
#     driver.find_element_by_id('edt_old_password').send_keys('123456')
#     driver.find_element_by_id('btn_define').click()
#     toast_message = "请输入新密码"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '请输入新密码'
#
#     # driver.find_element_by_id('tv_man').click()
#     driver.find_element_by_id('edt_old_password').send_keys('123456')
#     driver.find_element_by_id('edt_new_password').send_keys('123456')
#     driver.find_element_by_id('titleRight').click()
#     print('修改性别并提交')
#     toast_message = "两次输入的密码不一样"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '两次输入的密码不一样'
#
#     driver.find_element_by_id('edt_old_password').send_keys('123456')
#     driver.find_element_by_id('edt_new_password').send_keys('123456')
#     driver.find_element_by_id('edt_again_password').send_keys('1234')
#     driver.find_element_by_id('titleRight').click()
#     print('修改性别并提交')
#     toast_message = "两次输入的密码不一样"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '两次输入的密码不一样'
#
#     driver.find_element_by_id('edt_old_password').send_keys('123456')
#     driver.find_element_by_id('edt_new_password').send_keys('123456')
#     driver.find_element_by_id('edt_again_password').send_keys('123456')
#     driver.find_element_by_id('titleRight').click()
#     print('修改性别并提交')
#     toast_message = "修改成功"
#     message = '//*[@text=\'{}\']'.format(toast_message)
#     toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
#     print(toast_element.text)
#     assert toast_element.text == '修改成功'
# except Exception as e:
#     print(e)
# else:
#     pass
#
#
# driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
# driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("资讯")').click()
#
# try:
#     driver.find_element_by_android_uiautomator('new UiSelector().text("成人高考")').click()
#     driver.find_element_by_android_uiautomator('new UiSelector().text("远程教育")').click()
#     driver.find_element_by_android_uiautomator('new UiSelector().text("专插本")').click()
#     driver.find_element_by_android_uiautomator('new UiSelector().text("教师资格证")').click()
#     driver.find_element_by_android_uiautomator('new UiSelector().text("远程教育")').click()
#     driver.find_element_by_android_uiautomator('new UiSelector().text("自学考试")').click()
#     # driver.find_elements_by_id('subtitle_tabLayout')[1].click()
#     # driver.find_elements_by_id('subtitle_tabLayout')[2].click()
#     # driver.find_elements_by_id('subtitle_tabLayout')[0].click()
#     driver.find_elements_by_id('rl_information')[1].click()
# except Exception as e:
#     print(e)
# else:
#     pass

try:
    for i in range(10):
        driver.find_element_by_android_uiautomator('new UiSelector().text("学习")').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("资讯")').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        print(i)
        # driver.find_elements_by_id('rl_course')[0].click()
except Exception as e:
    print(e)
else:
    pass