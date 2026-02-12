# 📘 Assignment: Data Visualization

## 🎯 Objective

Learn to create informative and visually appealing charts and graphs using Python's matplotlib and plotly libraries to communicate data insights effectively.

## 📝 Tasks

### 🛠️ Create Basic Charts with Matplotlib

#### Description
Use matplotlib to create fundamental chart types including line plots, bar charts, and scatter plots. Practice customizing colors, labels, and titles to make your visualizations clear and professional.

#### Requirements
Completed program should:

- Create at least three different chart types (line plot, bar chart, scatter plot)
- Add appropriate titles, axis labels, and legends to each chart
- Customize colors and styles for better visual appeal
- Save the charts as image files

#### Example Input
```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [15000, 18000, 22000, 19000, 25000]

# Create bar chart
plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.savefig('sales_chart.png')
```

#### Example Output
```
Chart saved: sales_chart.png

The bar chart displays:
- Title: "Monthly Sales"
- X-axis: Months (Jan through May)
- Y-axis: Sales in dollars
- Blue bars showing increasing trend with May having highest sales
```


### 🛠️ Build Interactive Visualizations with Plotly

#### Description
Create interactive charts using plotly that allow users to hover, zoom, and explore data dynamically. Build at least one interactive dashboard-style visualization.

#### Requirements
Completed program should:

- Create at least two interactive plotly charts
- Include hover information showing data details
- Use plotly's interactive features (zoom, pan, hover tooltips)
- Export one visualization as an HTML file for web viewing

#### Example Input
```python
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'population': [8.3, 3.9, 2.7, 2.3],
    'gdp': [1700, 1000, 670, 500]
})

# Create interactive scatter plot
fig = px.scatter(df, x='population', y='gdp', 
                 text='city', size='population',
                 title='City Population vs GDP')
fig.write_html('city_analysis.html')
```

#### Example Output
```
Interactive chart saved: city_analysis.html

Features:
- Scatter plot with city names as labels
- Bubble size represents population
- Hover tooltips show exact values
- Zoom and pan capabilities enabled
- Can be opened in any web browser
```
