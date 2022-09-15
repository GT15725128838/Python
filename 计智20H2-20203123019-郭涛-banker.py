import numpy as np


class Banker():
    def __init__(self, available, max, allocation, need):
        """
        初始化参数
        :param available: 系统可用资源数
        :param max: M个进程对N类资源最大资源需求量
        :param allocation: M个进程已经得到N类资源的资源量
        :param need: M个进程还需要N类资源的资源量
        """
        self.available = available
        self.max = max
        self.allocation = allocation
        self.need = need

    def Request(self, P, request):
        """
        请求资源
        :param P: 进程号
        :param request: 请求资源个数

        """
        # 判断请求个数是否小于需求个数
        length = len(request)
        for i in range(length):
            if request[i] > self.need[P][i]:
                break
        if i != len(request) - 1:
            print("进程{0}所需资源超过它的最大值".format(P))
            return

        # 判断请求个数是否小于可用资源个数
        for j in range(length):
            if request[i] > self.available[i]:
                break
        if j != length - 1:
            print("尚未足够的资源供进程{0}使用".format(P))
            return
        # 逻辑分配
        avi_temp = self.available
        all_temp = self.allocation
        need_temp = self.need

        for k in range(length):
            avi_temp[k] = avi_temp[k] - request[k]
            all_temp[P][k] = all_temp[P][k] + request[k]
            need_temp[P][k] = need_temp[P][k] - request[k]

        # 执行安全性算法，若存在安全序列，执行分配
        if self.Security():
            self.need = need_temp
            self.allocation = all_temp
            self.available = avi_temp
            print("请求成功！各数据结构修改为:")
            print("Need=\n{0}\nAllocation=\n{1}\nAvailable=\n{2}\n".format(self.need, self.allocation, self.available))

        else:
            print("如此分配会导致系统处于不安全状态，拒绝本次分配")
            return

    def Security(self):
        """
        安全性算法，检验逻辑分配后系统是否处于安全状态。
        """
        work = self.available
        finish = [False for i in range(self.need.shape[0])]
        pro_number = self.need.shape[0]
        pro_list = [i for i in range(pro_number)]
        length = self.need.shape[1]
        secureSeq = ""

        # 寻找安全序列
        for k in range(pro_number):
            for i in pro_list:
                flag = 1
                for j in range(length):
                    if self.need[i][j] > work[j]:
                        flag = 0
                        break

                if flag and finish[i] is False:
                    work += self.allocation[i]
                    finish[i] = True
                    secureSeq += str(i) + "->"
                    pro_list.remove(i)
                    break

        for i in range(len(finish)):
            if finish[i] is not True:
                return False
        print("存在安全序列为{0}".format(secureSeq.strip("->")))
        return True


if __name__ == "__main__":
    avi = np.array([3, 3, 2])

    need = np.array([[7, 4, 3],
                     [1, 2, 2],
                     [6, 0, 0],
                     [0, 1, 1],
                     [4, 3, 1]])
    all = np.array([[0, 1, 0],
                     [2, 0, 0],
                     [3, 0, 2],
                     [2, 1, 1],
                     [0, 0, 2]])
    max = np.array([[7, 5, 3],
                    [3, 2, 2],
                    [9, 0, 2],
                    [2, 2, 2],
                    [4, 3, 3]])
    Test = Banker(avi, max, all, need)
    Test.Request(1, np.array([1, 0, 2]))
