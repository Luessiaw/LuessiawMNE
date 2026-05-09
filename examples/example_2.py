from MEGssiaw import *
from MEGssiaw.visualise import *

'''固定位置的源，在探头球面上产生的测量值分布，并绘制散点图'''

# 源通道, 用于产生信号
rp = np.array([0,0,0.08])
rps = rp[None,:] # 只考虑一个方向
nps = unit_y[None,:]
# 源强度
Q = np.array([10e-9,]) # 单位:Am

# 探头通道。
N = 10000
# 1. 测量方向沿 x 轴
rs = np.array([0,0,0.11])
rss_v = np.array([rs,]*3)
# 2. 标量磁力仪, 测量方向沿特定方向。
rss_s = rs[None,:]

# 探头通道的方向
# 矢量磁力仪
nss_v = np.array([unit_x,unit_y,unit_z])
# 标量磁力仪
theta = np.deg2rad(30)
unit = unit_x*np.cos(theta) + unit_y*np.sin(theta)
nss_s = unit[None,:]


# 导联场, 用于产生信号
# 矢量磁力仪
L0_v = computeLeadFieldMatrix(rps,nps,rss_v,nss_v)
# 标量磁力仪
L0_s = computeLeadFieldMatrix(rps,nps,rss_s,nss_s)

# 信号
B_v = L0_v @ Q
B_s = L0_s @ Q

