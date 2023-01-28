import sys

info = []  # 定义全局列表，保存学员信息 data


def user_input():  # 输入什么，返回什么
    user_me = input()
    return user_me


def start():  # 开始菜单
    a_ = "---"
    print(f"""
    {a_ * 10}
    学员管理系统
    1.添加学员信息
    2.删除学员信息
    3.修改学员信息
    4.查询学员信息
    5.遍历所有学员信息
    6.退出系统
    {a_ * 10}
    """)


def input_():  # 功能序号
    user_1 = input('请选择您需要的功能序号：')
    user_2 = int(user_1)
    if 0 > user_2 > 7:
        return user_2

    else:
        print("输入1-6以外的数字!!!,请重新输入,按1")
        print("请输入“exit”主动退出系统")
        user_input()
        if user_input() == "exit":
            sys.exit()
        elif user_input() == 1:
            input_()


def add_info():  # 添加学员信息
    # 接收用户输入学员信息，并保存
    name = input("你的名字是：")
    age = input("你的年龄是：")
    mobile = input("你的手机号码：")
    global info
    # 判断是否添加学员信息
    for i in info:
        if name == i[name]:
            # 学员姓名已经存在，则报错提示
            print("报错提示!,姓名已经存在")
    info_dict = {"name": name, "age": age, "mobile": mobile}
    info.append(info_dict)


def modify_info():  # 修改学员信息
    print("请输入你要修改的学员信息名字")
    modify_name = user_input()
    global info
    # 判断是否修改学员信息
    for i in info:
        if modify_name == i["name"]:
            print("""
            1.名字信息
            2.手机号信息
            3.年龄信息
            """)
            i = user_input
            if i == 1:
                i[name] = user_input
                break
            elif i == 2:
                i[mobile] = user_input
                break
            elif i == 2:
                i[age] = user_input
                break
            else:
                print("学员不存在")
            print(info)


def del_info():  # 删除学员信息
    print("请输入你要删除的学员信息名字")
    del_name = user_input()
    global info
    # 判断是否删除学员信息
    for i in info:
        if del_name == i[del_name]:
            info.remove(i)
            break
        else:
            print("学员不存在")
        print(info)


def search_info():  # 查询的学员信息
    print("请输入你要查询的学员信息名字")
    search_name = user_input()
    global info
    for i in info:
        if search_name == i["name"]:
            print(f"查找到的学员信息如下：----------\n该学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['mobile']}")
            break
        else:
            print("该学员不存在")


def print_all():  # 打印所有学员信息
    global info
    for i in info:
        print(f"姓名：{i['name']}，年龄：{i['age']}，电话：{i['mobile']}")


def exit_info():
    for i in range(1):
        print("确认退出么? 确认请输入【yes】：")
        flag = user_input()
        if flag == "yes":
            break


def if_(user_num=input()):  # if学员
    if user_num == 1:
        print('添加学员信息')
        add_info()
    elif user_num == 2:
        print('删除学员信息')
        del_info()
    elif user_num == 3:
        print('修改学员信息')
        modify_info()
    elif user_num == 4:
        print('查询学员信息')
        search_info()
    elif user_num == 5:
        print('打印所有学员信息')
        print_all()
    elif user_num == 6:
        print('退出系统')
        exit_info()
    else:
        print('信息输入错误')


# 用户选择系统功能的代码需要循环使用，直到用户主动退出系统。
# 如果用户输入1-6以外的数字，需要提示用户。
for i in range(1):
    start()  # 显示功能界面
    input_()  # 用户输入功能序号
    if_(user_num=input())  # 获取用户输入序号 运行

