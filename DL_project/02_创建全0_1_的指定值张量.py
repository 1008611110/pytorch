""""
案例：
    演示如何创建全0_1_的,指定值的张量
涉及到的函数如下：
    torch.ones 和torch.ones_like
    torch.zeros 和torch.zeros_like
    torch.full 和torch.full_like
"""

#导包
import torch


def dm01():
    #场景1：torch.ones 和torch.ones_like 创建全1张量
    t1=torch.ones(2,3)  #创建2行3列的全1张量
    print(f't1:{t1},type:{type(t1)}')
    print('_'*30)

    t2 = torch.tensor([[2, 3], [3, 4], [4, 5]])  # 创建2行3列的张量
    print(f't2:{t2},type:{type(t2)}')
    print('_' * 30)
    
    t3 = torch.ones_like(t2)  # 基于t2的形状 创建2行3列的全1张量
    print(f't3:{t3},type:{type(t3)}')
    print('_' * 30)

    #场景2：torch.zeros 和torch.zeros_like 创建全0张量
    t1 = torch.zeros(2, 3)  # 创建2行3列的全0张量
    print(f't1:{t1},type:{type(t1)}')
    print('_' * 30)

    t2 = torch.tensor([[2, 3], [3, 4], [4, 5]])  # 创建2行3列的张量
    print(f't2:{t2},type:{type(t2)}')
    print('_' * 30)

    t3 = torch.zeros_like(t2)  # 基于t2的形状 创建2行3列的全0张量
    print(f't3:{t3},type:{type(t3)}')
    print('_' * 30)

    #场景3：torch.full 和torch.full_like 创建全1张量

if __name__ == '__main__':
     dm01()
