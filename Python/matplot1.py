import matplotlib.pyplot as plt
   
Country = ['China','Canada','India','UK','France']
GDP_Per_Capita = [60000,42000,52000,49000,47000]

plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()