import matplotlib.pyplot as plt

# Sample data: Product names and their corresponding sales amounts
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [3500, 4800, 6200, 3200, 7800]

''' Creating a bar chart'''

plt.bar(products,sales,color = 'skyblue')

plt.xlabel("Products")
plt.ylabel("Sales Amount (RS)")
plt.title("Sales Performance by Product")

plt.show()


