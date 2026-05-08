from MEGssiaw import *
from MEGssiaw.visualise import *

'''将源放置在固定位置，产生信号并源定位。'''


# 探头通道。
# 考虑两种单轴探头阵列：
# 1. 矢量磁力仪, 测量方向沿径向 
# 2. 标量磁力仪, 测量方向沿z方向。
# 两种阵列中探头通道的位置是相同的,只是方向不同.
# 假设探头按 Fibonacci 螺旋线分布
N = 256
rss = fibonacci_sphere(2*N)[:N]
rss = np.array(rss)
# 矢量磁力仪
nss_v = []
for rs in rss:
    ns = rs/np.linalg.norm(rs)
    nss_v.append(ns)
nss_v = np.array(nss_v)
# 标量磁力仪
nss_s = np.array([unit_z,]*N)

# 源通道, 用于产生信号
rp = np.array([0,0,0.08])
rps = np.array([rp,rp]) # 两个通道，因为源有两个方向
nps = np.array([unit_x,unit_y])
# 源强度
Q = np.array([0, 100e-9]) # 单位:Am

# 导联场, 用于产生信号
# 矢量磁力仪
L0_v = computeLeadFieldMatrix(rps,nps,rss,nss_v)
# 标量磁力仪
L0_s = computeLeadFieldMatrix(rps,nps,rss,nss_s)

# 信号
B_v = L0_v @ Q
B_s = L0_s @ Q

print(B_v)
print(B_s)
