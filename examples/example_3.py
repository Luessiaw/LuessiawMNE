'''固定源，由测量值进行源成像'''
from MEGssiaw import *

# 真实源, 用于产生信号
radius = 0.08
rp0 = np.array([0,0,radius])
rp0s = np.array([rp0,rp0]) # 两个方向
np0s = np.array([unit_x,unit_y])
# 源强度
Q0 = np.array([0,100e-9]) # 单位:Am

# 用于成像的格点。在半径为 8 cm 的上半球面上均匀划分。
grid_length = 0.01
grid_point_num = int(8*radius**2/grid_length**2)
print("Number of grid points: {0:d}".format(grid_point_num))

rps = np.array(fibonacci_half_sphere(grid_point_num))

print()