# import numpy as np
# from mindspore import Tensor
# import mindspore.ops as ops
# import mindspore.context as context
# import matplotlib.pyplot as plt
# import mindspore.dataset as ds
#
#
# context.set_context(device_target="Ascend")
# x = Tensor(np.ones([1, 3, 3, 4]).astype(np.float32))
# y = Tensor(np.ones([1, 3, 3, 4]).astype(np.float32))
# print(ops.add(x, y))
#
#
# def f(xline):
#     return np.power(xline, 2)
#
#
# def secondFunction(xline):
#     return 2.0 * xline
#
#
# def firstFunction(function, xline, delta=1e-4):
#     return (function(xline + delta) - function(xline - delta)) / (2 * delta)
#
#
# # plot the function
# xs = np.arange(-10, 11)
# plt.plot(xs, f(xs))
# plt.show()
#
# learning_rate = 0.1
# max_loop = 30
#
# x_init = 10.0
# x = x_init
# lr = 0.1
# for i in range(max_loop):
#     d_f_x = firstFunction(f, x)
#     x = x - learning_rate * d_f_x
#     print(x)
#
# print('initial x =', x_init)
# print('arg min f(x) of x =', x)
# print('f(x) =', f(x))
#
# # Size of the points dataset.
# m = 20
#
# # Points x-coordinate and dummy value (x0, x1).
# X0 = np.ones((m, 1))
# X1 = np.arange(1, m + 1).reshape(m, 1)
# X = np.hstack((X0, X1))
#
# # Points y-coordinate
# y = np.array([
#     3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
#     11, 13, 13, 16, 17, 18, 17, 19, 21
# ]).reshape(m, 1)
#
# # The Learning Rate alpha.
# alpha = 0.01
#
#
# def error_function(theta, X, y):
#     '''Error function J definition.'''
#     diff = np.dot(X, theta) - y
#     return (1. / 2 * m) * np.dot(np.transpose(diff), diff)
#
#
# def gradient_function(theta, X, y):
#     """Gradient of the function J definition."""
#     diff = np.dot(X, theta) - y
#     return (1. / m) * np.dot(np.transpose(X), diff)
#
#
# def gradient_descent(X, y, alpha):
#     """Perform gradient descent."""
#     theta = np.array([1, 1]).reshape(2, 1)
#     gradient = gradient_function(theta, X, y)
#     while not np.all(np.absolute(gradient) <= 1e-5):
#         theta = theta - alpha * gradient
#         gradient = gradient_function(theta, X, y)
#     return theta
#
#
# optimal = gradient_descent(X, y, alpha)
# print('optimal:', optimal)
# print('error function:', error_function(optimal, X, y)[0, 0])
#
#
# data = ds.NumpySlicesDataset([1, 2, 3], column_names=["col_1"])
# for x in data.create_dict_iterator():
#     print(x)
