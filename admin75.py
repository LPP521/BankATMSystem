import time

class Admin(object):
    admin = "123"
    passwd = "123"

    def printAdminView(self):
        print("*********************************************")
        print("*                                           *")
        print("*             欢迎登录嘉鯂银行              *")
        print("*                                           *")
        print("*********************************************")

    def printSysFunctionView(self):
        print("*********************************************")
        print("*     开户(1)               查询(2)         *")
        print("*     取款(3)               存款(4)         *")
        print("*     转账(5)               改密(6)         *")
        print("*     锁定(7)               解锁(8)         *")
        print("*     补卡(9)               销户(0)         *")
        print("*                 退出(q)                   *")
        print("*********************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员帐号：")
        if inputAdmin != self.admin:
            print("账号输入有误！！！")
            return -1
        inputPasswd = input("请输入管理员密码：")
        if inputPasswd != self.passwd:
            print("密码输入有误！！！")
            return -1

        # 能执行到这里说明账号密码正确
        print("操作成功！请稍后……")
        time.sleep(1)
        return 0








