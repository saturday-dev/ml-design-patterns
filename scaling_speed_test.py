from sklearn import datasets, linear_model
import timeit
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
raw = diabetes_X[:, None, 2]
max_raw = max(raw)
min_raw = min(raw)

scaled = ( 2 * raw - max_raw - min_raw) / (max_raw - min_raw)

def train_raw():
    linear_model.LinearRegression().fit(raw, diabetes_y)

def train_scaled():
    linear_model.LinearRegression().fit(scaled, diabetes_y)
    
raw_time = timeit.timeit(train_raw, number=1000)
scaled_time = timeit.timeit(train_scaled, number=1000)


print('raw time : ', raw_time)
print('scaled time : ', scaled_time)
ratio = 100 * (raw_time - scaled_time) / raw_time
# print((raw_time - scaled_time))
print('ratio :', ratio, '%' )