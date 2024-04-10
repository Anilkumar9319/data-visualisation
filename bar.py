import matplotlib.pyplot as plt

# Create a list of countries and their corresponding population values
countries = ['USA', 'Canada', 'Germany', 'France', 'India']
populations = [327.2, 38.0, 83.0, 66.9, 126.5]

# Plot a bar chart of population vs. countries
plt.bar(countries, populations)

# Label the x-axis as 'Countries' and the y-axis as 'Population (in millions)'
plt.xlabel('Countries')
plt.ylabel('Population (in millions)')

# Add a title to the plot as 'Population Bar Chart'
plt.title('Population Bar Chart')

# Show the plot
plt.show()