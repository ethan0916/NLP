import numpy as np

#numpy基本操作
x = np.array([[1,2,3],
              [4,5,6]])

print('\n秩：', x.ndim)
print('\n形状：', x.shape)
print('\n大小：', x.size)
print('\n求和', np.sum(x))
print('\n按列求和', np.sum(x, axis=0))
print('\n按行求和', np.sum(x, axis=1))
print('\n改变形状', np.reshape(x, (3,2)))
print('\n平方差', np.sqrt(x))
print('\n指数', np.exp(x))
print('\n转置', x.transpose())
print('\n展开', x.flatten())


print('\n零', np.zeros((3,4,5)))
print('\n随机', np.random.rand(3,4,5))

# x = np.random.rand(3,4,5)

"""
秩： 2

形状： (2, 3)

大小： 6

求和 21

按列求和 [5 7 9]

按行求和 [ 6 15]

改变形状 [[1 2]
 [3 4]
 [5 6]]

平方差 [[1.         1.41421356 1.73205081]
 [2.         2.23606798 2.44948974]]

指数 [[  2.71828183   7.3890561   20.08553692]
 [ 54.59815003 148.4131591  403.42879349]]

转置 [[1 4]
 [2 5]
 [3 6]]

展开 [1 2 3 4 5 6]

零 [[[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]]

随机 [[[0.79528596 0.92024825 0.43159403 0.69398891 0.35498764]
  [0.95470053 0.3704821  0.20528511 0.46689444 0.44552822]
  [0.42907517 0.81455137 0.77568943 0.59369384 0.74767827]
  [0.05896781 0.19909276 0.99388907 0.81541277 0.85276701]]

 [[0.51452179 0.13119197 0.41163198 0.86862643 0.78952258]
  [0.67576637 0.67061099 0.74573763 0.74906596 0.60384812]
  [0.26119712 0.71904425 0.06833163 0.6372204  0.79862384]
  [0.75174262 0.68198278 0.59489622 0.06141429 0.31443819]]

 [[0.47825778 0.14365585 0.07579279 0.65223763 0.53422814]
  [0.92758016 0.99510613 0.86194096 0.30543281 0.81605636]
  [0.03054412 0.97412832 0.20541167 0.41455182 0.6625306 ]
  [0.07857382 0.52317382 0.29972826 0.41464152 0.62836718]]]
"""