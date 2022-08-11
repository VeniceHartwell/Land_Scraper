# Land Scraper – Parcel Estimator Tool

## Purpose
This Parcel Estimator Tool returns the following parcel data based on zip code:
- Average price per acre.
- Average price.
- average acreage.
- Most popular seller.
- listing popularity for the area.


## How to Use the "scrape" file
- Input your given zip code. 
- A new csv, with today's date, and charts will be exported to the "output" folder containing information on all LandModo results for your given zip code.
- Use this csv in the "visualize" file to further analyze your data.


## How to Use the "Visualize" file
- Input the date of the csv you would like to see visualized. 
- All images shown in the Visualization tool will be found in the "output>images" folder, saved with the date of the input csv.
- The visualization tool can be used repeatedly to visualize any csv made by the EDA file.


## Tool Functionality
1. Import: Import previous tool data. 
2. Scrape: Scrape Landmodo for parcel data into dataframe.
3. Clean: Clean dataframe's new rows.
4. Visualize: Plot charts, identifying the differences in key metrics.
5. Export: Export dataframe as CSV and charts as PNG files.


## Resources
- Test Zip Code Dataset (33k < 42k): https://github.com/scpike/us-state-county-zip
- Paid dataset (42k): https://www.uszipcodeslist.net/csv#download
- Scrapable list of zip codes (not guaranteed to be all 42k): https://namecensus.com/zip-codes/alabama/ 
- Libraries: Pandas, Numpy, BeautifulSoup, Matplotlib, Seaborn, Plotly
