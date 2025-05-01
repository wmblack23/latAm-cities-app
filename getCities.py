from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
import os

load_dotenv()

# Connect to Mongo
clusterUrl = os.environ["clusterUrl"]
client = MongoClient(clusterUrl)
db = client['latAm-app']

# Latin American country codes
latin_america_codes = {
    "MX", "GT", "BZ", "SV", "HN", "NI", "CR", "PA",
    "CO", "VE", "EC", "PE", "BO", "PY", "CL", "AR", "UY",
    "CU", "DO", "HT", "PR"
}

# GeoNames column headers
columns = [
    "geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude",
    "feature_class", "feature_code", "country_code", "cc2", "admin1_code",
    "admin2_code", "admin3_code", "admin4_code", "population", "elevation",
    "dem", "timezone", "modification_date"
]

# Create DataFrame
with open("cities5000.txt", encoding="utf-8") as f:
    data = [line.strip().split("\t") for line in f if line.strip().split("\t")[8] in latin_america_codes]

cities = pd.DataFrame(data, columns=columns)

# Change certain columns to numeric
cities["population"] = pd.to_numeric(cities["population"], errors="coerce")
cities["latitude"] = pd.to_numeric(cities["latitude"], errors="coerce")
cities["longitude"] = pd.to_numeric(cities["longitude"], errors="coerce")
cities["elevation"] = pd.to_numeric(cities["elevation"], errors="coerce")
cities["dem"] = pd.to_numeric(cities["dem"], errors="coerce")

# Drop columns we don't want
cities = cities.drop(columns=['geonameid', 'alternatenames', 'feature_class', 'feature_code', 'cc2', 'admin1_code',
                      'admin2_code', 'admin3_code', 'admin4_code', 'elevation', 'modification_date'])

# Rename column
cities.rename(columns={'dem': 'elevation'}, inplace=True)

# Send aDFll to Mongo collection
db.LatinAmericanCities.insert_many(cities.to_dict('records'))