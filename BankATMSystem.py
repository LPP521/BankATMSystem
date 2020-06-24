'''
人
类名：Person
属性：
行为：

卡
类名：Card
属性：卡号   密码  余额
行为：

提款机
类名：ATM
属性：用户字典
行为：开户   查询  取款  存储  转账  改密  锁定  解锁  补卡  销户

管理员
类名：Admin
属性：
行为：管理员界面    管理员登录    系统功能界面     退出
'''

from admin75 import Admin
from ATM75 import ATM
import pickle
import time
import os

def main():
    # 管理员对象
    admin = Admin()

    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    #提款机对象
    filePath = os.path.join(os.getcwd(), "allUsers.txt")
    f = open(filePath, "rb")
    allUsers = pickle.load(f)
    atm = ATM(allUsers)

    while True:
        admin.printSysFunctionView()
        #等待用户操作
        option = input("请输入您的操作：")
        if option == "1":
            #开户
            atm.createUser()
        elif option == "2":
            #查询
            atm.searchUserInfo()
        elif option == "3":
            #取款
            atm.getMoney()
        elif option == "4":
            #存储
            pass
        elif option == "5":
            #转账
            pass
        elif option == "6":
            #改密
            pass
        elif option == "7":
            #锁定
            atm.lockUser()
        elif option == "8":
            #解锁
            atm.unlockUser()
        elif option == "9":
            #补卡
            pass
        elif option == "0":
            #销户
            pass
        elif option == "q":
            #退出
            if not admin.adminOption():
                #将当前系统中的所有用户信息保存到文件中
                f = open(filePath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()

                return -1
        time.sleep(1)

if __name__ == "__main__":
    main()
