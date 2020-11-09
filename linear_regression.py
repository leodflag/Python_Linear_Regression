import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 下載diabetes 資料集
data_X, data_Y = datasets.load_diabetes(return_X_y=True)

#  np.newaxis為每個元素增加一個座標軸，此取出第2直行的所有元素做成新二維矩陣
data_X = data_X[:, np.newaxis, 2]

# 切分資料的訓練集與測試集
data_X_train = data_X[:-20] # 取全部到最後20項前
data_X_test = data_X[-20:] # 後20項全部

# 切分標籤的訓練集與測試集
data_Y_train = data_Y[:-20]
data_Y_test = data_Y[-20:]

# 建立線性迴歸物件
regr = linear_model.LinearRegression()

# 使用訓練集訓練模型
regr.fit(data_X_train, data_Y_train)

# 使用測試集做預測
data_Y_pred = regr.predict(data_X_test)

# 迴歸係數
print('coefficients: \n', regr.coef_)
# mse
print('mean squared error: %.2f' %mean_squared_error(data_Y_test, data_Y_pred))
# 決定係數，判斷統計模型的解釋力，若為1為完美預測
print('coefficient of determination: %.2f' %r2_score(data_Y_test, data_Y_pred))

# 繪圖結果
plt.scatter(data_X_test, data_Y_test, color = 'black')
plt.plot(data_X_test, data_Y_pred, color = 'blue', linewidth = 3)
plt.xticks(())
plt.yticks(())
plt.show()
