# Python_Linear_Regression
Ordinary least squares Linear Regression

## 目標
    使用scikit learn對糖尿病資料集做線性迴歸分析

## 普通最小平方線性迴歸Ordinary least squares Linear Regression
    假設獨立變數X與依變數Y存在線性關係，建立一個線性模型，並最小化目標值Y與在迴歸線上的預測值Y之間的差距（垂直距離，殘差residual）
[wiki](https://zh.wikipedia.org/wiki/%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8)
[程式網址](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py)

## 公式
![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/495382d7c370d1ba0c0fa3d2f9dff042eb45b45d)


## 糖尿病資料
sklearn.datasets.load_diabetes <br>
[參考網址](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)

## 虛擬碼
    1.下載糖尿病資料集
    2.切分訓練集與數據集
    3.建立線性迴歸物件
    4.輸入訓練集訓練模型
    5.使用測試集進行預測
    6.衡量線性迴歸的預測能力與解釋能力
    7.繪圖

## 預測結果衡量
![image](https://github.com/leodflag/Python_Linear_Regression/blob/master/diabetes_predict_result.png)

## 線性迴歸結果圖
![image](https://github.com/leodflag/Python_Linear_Regression/blob/master/diabetes_linear_regression.png)
