# Enriching and Cleaning File for Scraper Tool

# Import general libraries
import pandas as pd
import numpy as np

# import libraries necessary for web scraping
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def missing_vals(df):
    """ RETURN THE MISSING VALUES OF A DATAFRAME """
    print('Missing values:\n')
    print(df.isnull().sum())
    print('\nTotal values:\n')
    print(df.count())
    return 


def empty_page(url):
    """ CHECK IF PAGE HAS ZERO RESULTS BY SEARCHING FOR THE 'SORRY, PAGE IS EMPTY' LABEL """
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    warning = soup.select('div.alert.alert-warning')
    if warning == []:
        return False # page is not empty
    else:
        return True # page is empty


def new_search(url):
    """ SEARCH FOR ALL LISTING RESULTS ON A PAGE """
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    # check for response
    #if html:
    #    Break

    # Return location data of all results on current page to new lists.
    location_raw = soup.select('div.post-location-snippet.bmargin.font-sm')

    # Clean location data.
    location_list = [i.get_text().strip() for i in location_raw]

    # Split location data into separate lists.
    list_of_lists = [elem.split(",") for elem in location_list]
    locations = []
    zip_codes_states = []
    countries = []
    try:
        for list_ in list_of_lists:
            location, location_list, country = list_[0], list_[1], list_[2]
            locations.append(location)
            zip_codes_states.append(location_list)
            countries.append(country)
    except:
        for list_ in list_of_lists:
            location, location_list, country = np.nan, np.nan, np.nan
            locations.append(location)
            zip_codes_states.append(location_list)
            countries.append(country)

    # split further
    try:
        list_of_lists = [elem.strip().split(" ") for elem in zip_codes_states]
        states = []
        zip_codes = []
        for list_ in list_of_lists:
            state, zip_code = list_[0], list_[1]
            states.append(state)
            zip_codes.append(str(zip_code))
    except:
        states = []
        zip_codes = []
        for list_ in list_of_lists:
            state, zip_code = np.nan, np.nan
            states.append(state)
            zip_codes.append(str(zip_code))
        
    # Return all parcel size, price, name data to new list.
    parcel_size = soup.select('div.post-location-snippet.tmargin span.inline-block')
    parcel_price = soup.select('div.bg-secondary.hpad.font-lg.text-center.line-height-xl')
    listing_name = soup.select('a.h3.bold.bmargin.center-block')

    # clean parcel data.
    size = [i.get_text().strip() for i in parcel_size]
    size = [i.lstrip("Acres:\n") for i in size]
    price = [i.get_text().lstrip('\n$').replace(",","") for i in parcel_price]
    listing = [i.get_text().strip() for i in listing_name]

    # Return author and date data of all results on page 1 to new lists.
    author_and_date = soup.select('div.col-xs-8.col-sm-10.nolpad.font-sm.bmargin.posted_meta_data')

    # Clean author and date data.
    auth_and_date = [author_and_date[i].get_text().strip() for i in range(len(author_and_date))] # send to cleaning function later

    # Split author and date data into separate lists.
    # Every string has the same format, ie: 'Posted\n04/14/2022 \n\nby\n\nLandJakes'
    date = []
    author = []
    for elem in auth_and_date:
        date.append(elem.replace("\n", "")[6:].replace("by", "").split(" ")[0]) 
        author.append(elem.replace("\n", "")[6:].replace("by", "").split(" ")[1])

    # Add all lists to a new (temp) dataframe.
    dict_to_merge = {'Zip Code':zip_codes, 'Location':locations, 'State':states, 'Country':countries, 
                    'Parcel Size (acres)':size, 'Parcel Price':price, 'Listing Name':listing, 
                    'Listing Author':author, 'Post Date':date}
    new_search_df = pd.DataFrame(dict_to_merge)
    
    return new_search_df


def input_date():
    """ RETURN A DATE VIA USER INPUT """
    return input("Enter a date in the \"YYYY-MM-DD\" format to import a CSV from: ")


def avg_df(df):
    """ ??? """
    prev_zip = df["Zip Code"][0]
    price_sum = 0
    acre_sum = 0
    avg_dict = {"Zip Code":[],"Avg Acre Price":[]}
    for i in range(len(df)):
        current_zip = df["Zip Code"][i]
        if current_zip != prev_zip:
            avg_dict["Zip Code"].append(prev_zip)
            avg_dict["Avg Acre Price"].append(price_sum/acre_sum)
            price_sum=0
            acre_sum=0
        prev_zip = current_zip
        price_sum += df["Parcel Price"][i]
        acre_sum += df["Parcel Size (acres)"][i]
    avg_dict["Zip Code"].append(prev_zip)
    avg_dict["Avg Acre Price"].append(price_sum/acre_sum)
    avg_df = pd.DataFrame.from_dict(avg_dict)
    return avg_df
