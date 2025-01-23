import numpy as np

#cricket runs and players program
runs = np.array([[45, 50, 30, 60, 25], [10, 15, 5, 20, 12], [80, 60, 75, 100, 90], [25, 30, 20, 35, 40], [0, 5, 10, 0, 2],
     [50, 55, 60, 65, 70], [35, 40, 45, 50, 55], [100, 110, 120, 115, 125], [10, 12, 15, 10, 8], [70, 80, 85, 90, 95],
     [40, 45, 50, 55, 60]])
index = 0
for i in runs:
    #for printing total runs of each player
    total = sum(i)
    index += 1
    print('Total runs of player {} : {}'.format(index,total))
index = 0
for i in runs:
    #for printing max runs of each player
    largest_score = max(i)
    index += 1
    print('Maximum runs of player {} : {}'.format(index,largest_score))
index = 0
for i in runs:
    #for printing total runs of each player
    total = sum(i)
    average = total / 5
    index += 1
    print('Average runs of player {} : {}'.format(index,average))


#sales data program
sales_data = np.array([[150, 200, 250, 300, 400, 350, 500],  [120, 180, 210, 240, 310, 280, 400],   [100, 130, 190, 220, 300, 270, 350],   [80,  90,  150, 180, 240, 220, 300],  [50,  60,  80,  100, 130, 120, 180] ])

#shape of the sales_data array.
shape_of_sales_data = np.shape(sales_data)
print('shape of the sales_data array : ',shape_of_sales_data)

# Identify the number of dimensions in the sales_data array
no_of_dimension = np.ndim(sales_data)
print('the number of dimensions in the sales_data array : ',no_of_dimension)

#data type of elements stored in the sales_data array
data_type_of_arr = np.dtype(sales_data)
print('data type of elements stored in the sales_data array : ',data_type_of_arr)

#the total number of elements in the sales_data array
print("the total number of elements in the sales_data array : ", np.size(sales_data))

#Transpose the array so that rows represent days and columns represent products
days = np.transpose(sales_data)
print('Days : ',days)

#Product 3 on Day 4
print('Product 3 on Day 4 : ',sales_data[2][3])

print("All sales data for Product 1 : ", days [0])

print('Sales data for the last 2 days : ',days[-1:-3:-1])

print('Sales data for the last 2 days : ',days[4])

for i in sales_data:
    j = 1
    print('Sales data for product{} : '.format(j,i))
    j += 1
    if j ==3 :
        break

