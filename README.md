# Visualization Application
This Visualization Application is designed to provide a dynamic and intuitive platform for exploring and analyzing the Cities and Municipalities Competitiveness Index (CMCI) data at both the provincial and Local Government Unit (LGU) levels. Leveraging interactive maps, various charts, and dropdown menus, this application offers a comprehensive visual representation of CMCI scores in the Philippines, fostering data-driven insights and informed decision-making.

# How to Run the Application 

To run the application, ensure you have python and the following libraries installed: dash, plotly.express, dash_bootstrap_components, openpyxl, pathlib, pandas, geopandas, plotly.graph_objects and numpy

If any of these libraries are missing, you can install them using pip:
```python
pip install dash plotly-express dash-bootstrap-components openpyxl pandas geopandas plotly numpy
```

Once you have all the required libraries, follow these steps to run the application:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the CMCI_Hub.py file.
3. Type the following command and press Enter:
```python
python CMCI_Hub.py
```

This command will start the application, and you should see output in the terminal indicating that the Dash app is running. Once the app is running, you can access it by opening a web browser and navigating to the specified URL. From there, each main page of the application may be viewed, including the homepage, visualization dashboard and interactive map, from the navigation bar. 

## Province Dashboard

### Features 
- Province Charts: Includes 3 charts - line chart, bar chart, and choropleth map
- Dropdown Menus: Utilizes dropdown menus for province selection with 84 provinces available
- Nominal Variables: The province dataset is represented by nominal variables and uses a categorical color scheme in charts
- Line Chart: Shows selected pillar indicator scores for each province at the specified year range
- Bar Chart: Displays distances of each province from the center of Manila in miles
- Choropleth Map: Illustrates overall scores of all provinces

### Usage
1. Use the dropdown menus to select provinces and specify the year range for analysis.
2. View the line chart to observe selected pillar indicator scores for each province over time.
3. Interpret the bar chart to understand distances of provinces from the center of Manila.
4. Explore the choropleth map to see overall scores of provinces and observe changes based on proximity to Manila.

## LGU Dashboard

### Features 
- LGU Charts: Includes a bar chart displaying changes over time for the selected pillar and a grouped bar chart showing the composition of overall scores for chosen LGUs
- Sidebar Selection: Users can choose LGUs conveniently from the sidebar
- Dynamic Search Bar: With 1,613 LGUs available, a search bar dynamically updates to ease selection
- Clear Selection Option: Added for user convenience to clear selections easily
- Qualitative Representation: LGUs are treated as nominal variables and use a categorical colormap in charts
- Pillar Description: Provides a description of the chosen pillar and its indicators for context
- Trends: Enables comparison of trends (line chart) and discovery of distribution (grouped bar chart) for in-depth analysis

### Usage 
1. Select LGUs from the sidebar or use the dynamic search bar for easier selection.
2. Choose a pillar and time interval to update the line chart and compare trends in pillar scores over time.
3. Explore the grouped bar chart to discover the composition of overall scores for selected LGUs. Use the year dropdown for specific yearly data.
4. Utilize the clear selection option for a clean slate and access additional information about pillars and indicators for better understanding throughout the dashboard page. 

## Interactive Map Page

### Features 
- Interactive Elements: Dropdown menus for selecting provinces, years, and LGUs enable seamless navigation and exploration of data
- Choropleth Map: Utilizes the Viridis color palette for clear and detailed representation of CMCI scores, with colors changing based on the selected year
- Reference Points: Includes a fixed reference point for Manila on the map, while the point representing the selected province dynamically adjusts for spatial context
- Province Profile: Displays detailed statistics such as overall CMCI score, ranking, highest score rank, population, and revenue for selected provinces
- LGU Profile: Provides insights into LGU-specific statistics within the selected province
- Color-Coded Bar Chart: Showcases scores across the five pillars of competitivenes for the selected province under the LGU Profile

### Usage
1. Select a province and year from the dropdown menus to view CMCI statistics for the chosen province in the Choropleth Map, witnessing the color-coded scores across the Philippines and the distance from the selected province to Manila.
2. Explore LGU-specific data by selecting an LGU from the dropdown menu in the LGU profile section.
3. Interact with the bar chart to compare scores across the five pillars of competitiveness for the selected LGU. Hover over elements in the visualization for detailed information and insights.
4. Check the additional information and definition of each pillar through the dropdown menu.

# Contributors
- Cansana, Ma. Katrina Isabela M.
- Dee, Ethan S.
- Del Rosario, Cara Isabel P.
- Fabro, Kate Alexandra R. 
- Que, Michael Dave A.


   
