import numpy as np
import logging
logger = logging.getLogger(__name__)

class MNEError(Exception):
    pass


def computeLeadFieldMatrix(sourcePositions:np.ndarray,
                           sourceOrientations:np.ndarray,
                           sensorPositions:np.ndarray,
                           sensourOrientations:np.ndarray):
    '''此函数用于构建前向模型矩阵。
    sourcePositions: (m,3) 数组，表示
    '''
    pass