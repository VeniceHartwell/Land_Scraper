# Project II: Pipelines – Parcel Estimator Tool

## Purpose
The Parcel Estimator tool returns the following parcel data based on zip code:
- Average price per acre.
- Average price.
- average acreage.
- Most popular seller.
- listing popularity for the area.


## How to Use the "EDA" file
- Input your given zip code. 
- A new csv, with today's date, and charts will be exported to the "output" folder containing information on all LandModo results for your given zip code.
- Use this csv in the "visualization" file to further analyze your data.


## How to Use the "Visualization" file
- Input the date of the csv you would like to see visualized. 
- All images shown in the Visualization tool will be found in the "output>images" folder, saved with the date of the input csv.
- The visualization tool can be used repeatedly to visualize any csv made by the EDA file.


## Functionality
1. Import: Import previous tool data. 
2. Scrape: Scrape Landmodo for parcel data into dataframe.
3. Clean: Clean dataframe's new rows.
4. Visualize: Plot charts, identifying the differences in key metrics.
5. Export: Export dataframe as CSV and charts as PNG files.


## Resources
- Dataset: import previous csv's to compare.
- Landmodo: landmodo.com
- Libraries: Pandas, Numpy, BeautifulSoup, Matplotlib, Seaborn, Plotly


## Results
- Average price and acreage vary unpredictably by zip code.
- Price per acre is very high in California.
- Land investors make lump purchases, and resell proerties by the dozen or, more commonly, half-dozen.