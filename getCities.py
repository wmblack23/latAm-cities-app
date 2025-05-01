import pandas as pd

# List of Latin American ISO country codes
latin_america_codes = {
    "MX", "GT", "BZ", "SV", "HN", "NI", "CR", "PA",
    "CO", "VE", "EC", "PE", "BO", "PY", "CL", "AR", "UY",
    "CU", "DO", "HT", "PR"
}

# GeoNames column headers (based on documentation)
columns = [
    "geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude",
    "feature_class", "feature_code", "country_code", "cc2", "admin1_code",
    "admin2_code", "admin3_code", "admin4_code", "population", "elevation",
    "dem", "timezone", "modification_date"
]

# Read the file and parse into DataFrame
with open("cities5000.txt", encoding="utf-8") as f:
    data = [line.strip().split("\t") for line in f if line.strip().split("\t")[8] in latin_america_codes]

cities = pd.DataFrame(data, columns=columns)

# Optional: convert some columns to numeric
cities["population"] = pd.to_numeric(cities["population"], errors="coerce")
cities["latitude"] = pd.to_numeric(cities["latitude"], errors="coerce")
cities["longitude"] = pd.to_numeric(cities["longitude"], errors="coerce")
cities["elevation"] = pd.to_numeric(cities["elevation"], errors="coerce")
cities["dem"] = pd.to_numeric(cities["dem"], errors="coerce")

cities = cities.drop(columns=['geonameid', 'alternatenames', 'feature_class', 'feature_code', 'cc2', 'admin1_code',
                      'admin2_code', 'admin3_code', 'admin4_code', 'modification_date'])
