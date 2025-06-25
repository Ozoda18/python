import numpy as np
lst=[12.23, 13.32, 100, 36.32]
numPy=np.array(lst)
print(numPy);

matrix=np.arange(2,11).reshape(3,3)
print(matrix);

zeros=np.zeros(10)
zeros[6]=11
print(zeros);

my_arr=np.arange(12,38)
print(my_arr);

array=[1,2,3,4]
datas=np.array(array)
print(datas)
print(datas.astype(np.float));

centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = centigrade * 9 / 5 + 32
print("Centigrade degrees:", centigrade)
print("Fahrenheit degrees:", fahrenheit)
fahrenheit_input = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Original Fahrenheit input array:", fahrenheit_input);

numbers=np.array([10,20,30])
new_values=[40,50,60,70,80,90]
appended=np.append(numbers,new_values)
print(appended);

arr=np.random.randint(0,100,size=10)
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)
print(arr)
print(mean_val)
print(median_val)
print(std_dev);

arr=np.random.rand(10,10)
min_val=np.min(arr)
max_val=np.max(arr)
print(arr)
print(min_val)
print(max_val);

arr=np.random.rand(3,3,3)
print(arr)

