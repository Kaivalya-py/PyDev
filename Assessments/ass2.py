def revenue_for_category(data, category):
    revenue = 0.0
    i = 0
    while True:
        j = data.find(';', i)
        if j == -1:
            info = data[i:]
            if category == info.split(',')[1]:
                revenue += float(info.split(',')[2])
            break
        info = data[i:j]
        if category == info.split(',')[1]:
            revenue += float(info.split(',')[2])
        i = j + 1
    return revenue

# Example usage:
data = "Product1,Electronics,50;Product2,Clothing,30;Product3,Electronics,70;Product4,Clothing,20"
category = "Electronics"
print(revenue_for_category(data, category))  

# Output: 120.0
