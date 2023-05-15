import matplotlib.pyplot as plt

# Data
sectors = ['Energy Industry', 'Transport', 'Other industrial Combustion', 'Buildings', 'Other Sectors']
values = [37.66, 20.19, 21.44, 9.01, 11.69]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=sectors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal') 

# Title
plt.title('CO2 emissions worldwide by sector in 2021', pad=20)

# set transparency
# rgba color scheme layout
fig.patch.set_facecolor((0.3, 0.3, 0.3, 0.3))

plt.subplots_adjust(top = 0.85)

# plt.savefig("plot.png", transparent=True)

# Show the plot
plt.show()
