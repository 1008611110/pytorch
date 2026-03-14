"""
案例：
    演示张量的基本创建方式
张量：
    pytorch属于 深度学习最基本的框架，无论是后需要学的ANN还是CNN或RNN，
        底层在处理数据时，都是使用 张量 来处理的
    张量 ——> 存储同一类型元素的容器，且元素值必须是 数值 才行

    张量的基本创建方式：
        torch.tensor:指定 数据 创建张量
        torch.Tensor:根据 形状 创建张量，也可以指定 数据 创建张量
        torch.IntTensor 、torch.FolatTensor 、 torch.DoubleTensor 创建指定类型的张量

    总结：
        1.Tensor方式比较于tensor，可以基于形状创建张量
        2.重点掌握dem01   tensor
"""

# 导包
import torch
import numpy as np


def dm01():
    # 演示：torch.tensor:指定 数据 创建张量
    # 场景一：标量 张量
    t1 = torch.tensor(10)
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 场景二：二位列表 张量
    data = [[2, 2, 4], [3, 2, 1, ]]
    t2 = torch.tensor(data)
    print(f't2:{t2},type:{type(t2)}')

    # 场景三:numpy nd数组 张量
    data2 = np.random.randint(0, 10, size=(2, 3))
    t3 = torch.tensor(data2)
    print(f't3:{t3},type:{type(t3)}')

    # 场景三:尝试直接创建指定维度 张量  维度为2
    # t4=torch.tensor(3,2)  #报错
    # print(f't4:{t4},type:{type(t4)}')


def dm02():
    # 演示：torch.Tensor:根据 形状 创建张量，也可以指定 数据 创建张量
    # 场景一：标量 张量
    t1 = torch.Tensor(10)
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 场景二：二位列表 张量
    data = [[2, 2, 4], [3, 2, 1, ]]
    t2 = torch.Tensor(data)
    print(f't2:{t2},type:{type(t2)}')

    # 场景三:numpy nd数组 张量
    data2 = np.random.randint(0, 10, size=(2, 3))
    t3 = torch.Tensor(data2)
    print(f't3:{t3},type:{type(t3)}')

    # 场景三:尝试直接创建指定维度 张量  维度为2
    t4 = torch.Tensor(2, 3)  # 报错
    print(f't4:{t4},type:{type(t4)}')


def dm03():
    # 演示： torch.IntTensor 、torch.FolatTensor 、 torch.DoubleTensor 创建指定类型的张量
    # 场景一：标量 张量
    t1 = torch.IntTensor(10)
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 场景二：二位列表 张量
    data = [[2, 2, 4], [3, 2, 1, ]]
    t2 = torch.IntTensor(data)
    print(f't2:{t2},type:{type(t2)}')

    # 场景三:numpy nd数组 张量
    data2 = np.random.randint(0, 10, size=(2, 3))
    t3 = torch.IntTensor(data2)
    print(f't3:{t3},type:{type(t3)}')

    # 场景四：如果类型不匹配，会尝试自动转换类型
    data3 = np.random.randint(0, 10, size=(2, 3))
    t4 = torch.FloatTensor(data3)  #自动转换为浮点型
    print(f't4:{t4},type:{type(t4)}')

if __name__ == '__main__':
    # dm01()  常用
    # dm02()
    dm03()
