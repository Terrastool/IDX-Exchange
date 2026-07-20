#Four sold CSVs had the last 2 columns deleted if they ended in '_filled'
import pandas as pd
sold2401 = pd.read_csv("Sold Raw/CRMLSSOLD202401.csv")
print(len(sold2401))
#17976 rows in 2024 January
sold2402 = pd.read_csv("Sold Raw/CRMLSSOLD202402.csv")
print(len(sold2402))
#19925 rows in 2024 February
sold2403 = pd.read_csv("Sold Raw/CRMLSSOLD202403.csv")
print(len(sold2403))
#23276 rows in 2024 March
sold2404 = pd.read_csv("Sold Raw/CRMLSSOLD202404.csv")
print(len(sold2404))
#24640 rows in 2024 April
sold2405 = pd.read_csv("Sold Raw/CRMLSSOLD202405.csv")
print(len(sold2405))
#26487 rows in 2024 May
sold2406 = pd.read_csv("Sold Raw/CRMLSSOLD202406.csv")
print(len(sold2406))
#24328 rows in 2024 June
sold2407 = pd.read_csv("Sold Raw/CRMLSSOLD202407.csv")
print(len(sold2407))
#26240 rows in 2024 July
sold2408 = pd.read_csv("Sold Raw/CRMLSSOLD202408.csv")
print(len(sold2408))
#24558 rows in 2024 August
sold2409 = pd.read_csv("Sold Raw/CRMLSSOLD202409.csv")
print(len(sold2409))
#21267 rows in 2024 September
sold2410 = pd.read_csv("Sold Raw/CRMLSSOLD202410.csv")
print(len(sold2410))
#23274 rows in 2024 October
sold2411 = pd.read_csv("Sold Raw/CRMLSSOLD202411.csv")
print(len(sold2411))
#20279 rows in 2024 November 
sold2412 = pd.read_csv("Sold Raw/CRMLSSOLD202412.csv")
print(len(sold2412))
#20241 rows in 2024 December
sold2501 = pd.read_csv("Sold Raw/CRMLSSOLD202501.csv")
print(len(sold2501))
#18738 rows in 2025 January
sold2502 = pd.read_csv("Sold Raw/CRMLSSOLD202502.csv")
print(len(sold2502))
#18702 rows in 2025 February
sold2503 = pd.read_csv("Sold Raw/CRMLSSOLD202503.csv")
print(len(sold2503))
#21445 rows in 2025 March
sold2504 = pd.read_csv("Sold Raw/CRMLSSOLD202504.csv")
print(len(sold2504))
#23262 rows in 2025 April
sold2505 = pd.read_csv("Sold Raw/CRMLSSOLD202505.csv")
print(len(sold2505))
#23154 rows in 2025 May
sold2506 = pd.read_csv("Sold Raw/CRMLSSOLD202506.csv")
print(len(sold2506))
#22883 rows in 2025 June   
sold2507 = pd.read_csv("Sold Raw/CRMLSSOLD202507.csv")
print(len(sold2507))
#22646 rows in 2025 July
sold2508 = pd.read_csv("Sold Raw/CRMLSSOLD202508.csv")
print(len(sold2508))
#22972 rows in 2025 August
sold2509 = pd.read_csv("Sold Raw/CRMLSSOLD202509.csv")
print(len(sold2509))
#22443 rows in 2025 September
sold2510 = pd.read_csv("Sold Raw/CRMLSSOLD202510.csv")
print(len(sold2510))
#23233 rows in 2025 October
sold2511 = pd.read_csv("Sold Raw/CRMLSSOLD202511.csv")
print(len(sold2511))
#19088 rows in 2025 November
sold2512 = pd.read_csv("Sold Raw/CRMLSSOLD202512.csv")
print(len(sold2512))
#20538 rows in 2025 December
sold2601 = pd.read_csv("Sold Raw/CRMLSSOLD202601.csv")
print(len(sold2601))
#16487 rows in 2026 January
sold2602 = pd.read_csv("Sold Raw/CRMLSSOLD202602.csv")
print(len(sold2602))
#19010 rows in 2026 February    
sold2603 = pd.read_csv("Sold Raw/CRMLSSOLD202603.csv")
print(len(sold2603))
#23372 rows in 2026 March
sold2604 = pd.read_csv("Sold Raw/CRMLSSOLD202604.csv")
print(len(sold2604))
#24261 rows in 2026 April 
sold2605 = pd.read_csv("Sold Raw/CRMLSSOLD202605.csv")
print(len(sold2605))
#24194 rows in 2026 May
sold2606 = pd.read_csv("Sold Raw/CRMLSSOLD202606.csv")
print(len(sold2606))
#25521 rows in 2026 June
sold = pd.concat([sold2401, sold2402, sold2403, sold2404, sold2405, sold2406, sold2407, sold2408, sold2409, sold2410, sold2411, sold2412,sold2501, sold2502, sold2503, sold2504, sold2505, sold2506, sold2507, sold2508, sold2509, sold2510, sold2511, sold2512,sold2601,sold2602,sold2603,sold2604,sold2605,sold2606], ignore_index=True)  
print(len(sold))
#665440 rows in new dataset
# Inspect structure
sold.columns
sold.head()
# Check property categories
sold['PropertyType'].unique()
#To standardize our analysis across property types we will filter to Residential only. 
#Some interesting lot types included "land" and "BusinessOpportunity".
residentialsold = sold.loc[sold["PropertyType"] == 'Residential'].copy()
print(len(residentialsold))
#447987 rows in residential dataset
# Validate completeness
residentialsold.isnull().sum()
#Dividing these values by the row count shows that values above 90% null include:
#Middle or Junior School District, and Water Front YN. 
#Some came close to 90%, such as Buyer Agency Compensation Type and Buyer Agency Compensation.
residentialsold = residentialsold.drop(columns=['MiddleOrJuniorSchoolDistrict', 'WaterfrontYN'])
#Analyzing ClosePrice:
import matplotlib.pyplot as plt
residentialsold['ClosePrice'] = pd.to_numeric(residentialsold['ClosePrice'], errors='coerce')
close = residentialsold['ClosePrice'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(close.values, vert=True, showfliers=False)
plt.title('Residential Sold Close Price Distribution')
plt.ylabel('Close Price in Millions')
plt.xticks([1], ['ClosePrice'])
plt.show()
#No outliers illustrated
mean_close = residentialsold['ClosePrice'].mean()
print(mean_close)
#Sold Close Price mean is approximately 1.2 million dollars
#Analyzing Living Area:
residentialsold['LivingArea'] = pd.to_numeric(residentialsold['LivingArea'], errors='coerce')
living_area = residentialsold['LivingArea'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(living_area.values, vert=True, showfliers=False)
plt.title('Residential Sold Living Area Distribution')
plt.ylabel('Living Area in Square Feet')
plt.xticks([1], ['LivingArea'])
plt.show()
#No outliers illustrated
mean_living_area = residentialsold['LivingArea'].mean()
print(mean_living_area)
#Sold Living Area mean is approximately 1,904 square feet
#Analyzing DaysOnMarket:
residentialsold['DaysOnMarket'] = pd.to_numeric(residentialsold['DaysOnMarket'], errors='coerce')
days_on_market = residentialsold['DaysOnMarket'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(days_on_market.values, vert=True, showfliers=False)
plt.title('Residential Sold Days on Market Distribution')
plt.ylabel('Days on Market')
plt.xticks([1], ['DaysOnMarket'])
plt.show()
#No outliers illustrated
mean_days_on_market = residentialsold['DaysOnMarket'].mean()
print(mean_days_on_market)
#Sold Days on Market mean is approximately 37 days
#Fetch the mortgage rate data from FRED
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
#Resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
mortgage.groupby('year_month')['rate_30yr_fixed']
.mean()
.reset_index()
)
#Create a matching year_month key on the MLS datasets
residentialsold['year_month'] = pd.to_datetime(
    residentialsold['CloseDate'].astype(str).str.replace('/', '-', regex=False),
    errors='coerce'
).dt.to_period('M')
#Merge
sold_with_rates = residentialsold.merge(mortgage_monthly, on='year_month', how='left')
#Validate
print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(
sold_with_rates[
['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
].head()
)
#Convert date columns to datetime format
sold_with_rates['CloseDate'] = pd.to_datetime(
    sold_with_rates['CloseDate'],
    errors='coerce'
)
sold_with_rates['PurchaseContractDate'] = pd.to_datetime(
    sold_with_rates['PurchaseContractDate'],
    errors='coerce'
)
sold_with_rates['ListingContractDate'] = pd.to_datetime(
    sold_with_rates['ListingContractDate'],
    errors='coerce'
)
sold_with_rates['ContractStatusChangeDate'] = pd.to_datetime(
    sold_with_rates['ContractStatusChangeDate'],
    errors='coerce'
)
#Boolean flags for incorrect timelines
sold_with_rates['listing_after_close_flag'] = (
    sold_with_rates['ListingContractDate'] > sold_with_rates['CloseDate']
)

sold_with_rates['purchase_after_close_flag'] = (
    sold_with_rates['PurchaseContractDate'] > sold_with_rates['CloseDate']
)

sold_with_rates['negative_timeline_flag'] = (
    (sold_with_rates['ListingContractDate'] > sold_with_rates['PurchaseContractDate']) |
    (sold_with_rates['PurchaseContractDate'] > sold_with_rates['CloseDate'])
)
sold_with_rates['negative_timeline_flag'] = (
    sold_with_rates['ListingContractDate'].notna() &
    sold_with_rates['PurchaseContractDate'].notna() &
    sold_with_rates['CloseDate'].notna() &
    (
        (sold_with_rates['ListingContractDate'] > sold_with_rates['PurchaseContractDate']) |
        (sold_with_rates['PurchaseContractDate'] > sold_with_rates['CloseDate'])
    )
)
#Ensure numeric values aren't written as string values
sold_with_rates['ClosePrice'] = pd.to_numeric(sold_with_rates['ClosePrice'], errors='coerce')
sold_with_rates['LivingArea'] = pd.to_numeric(sold_with_rates['LivingArea'], errors='coerce')
sold_with_rates['DaysOnMarket'] = pd.to_numeric(sold_with_rates['DaysOnMarket'], errors='coerce')
#Exclude infeasible values
sold_with_rates = sold_with_rates[sold_with_rates['ClosePrice'] > 0]
sold_with_rates = sold_with_rates[sold_with_rates['LivingArea'] > 0]
sold_with_rates = sold_with_rates[sold_with_rates['DaysOnMarket'] >= 0]
sold_with_rates = sold_with_rates[sold_with_rates['BathroomsTotalInteger'] >= 0]
sold_with_rates = sold_with_rates[sold_with_rates['BedroomsTotal'] >= 0]
sold_with_rates.to_csv(r"C:\Users\madig\OneDrive\Desktop\IDX Exchange\Week 1\ResidentialSold.csv", index=False)

# Begin Listing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

listing2401 = pd.read_csv("Listing Raw/CRMLSListing202401.csv")
print(len(listing2401))
#27454 rows in 2024 January
listing2402 = pd.read_csv("Listing Raw/CRMLSListing202402.csv")
print(len(listing2402))
#27447 rows in 2024 February
listing2403 = pd.read_csv("Listing Raw/CRMLSListing202403.csv")
print(len(listing2403))
#32282 rows in 2024 March
listing2404 = pd.read_csv("Listing Raw/CRMLSListing202404.csv")
print(len(listing2404))
#36503 rows in 2024 April
listing2405 = pd.read_csv("Listing Raw/CRMLSListing202405.csv")
print(len(listing2405))
#38796 rows in 2024 May
listing2406 = pd.read_csv("Listing Raw/CRMLSListing202406.csv")
print(len(listing2406))
#35893 rows in 2024 June
listing2407 = pd.read_csv("Listing Raw/CRMLSListing202407.csv")
print(len(listing2407))
#36340 rows in 2024 July
listing2408 = pd.read_csv("Listing Raw/CRMLSListing202408.csv")
print(len(listing2408))
#35305 rows in 2024 August
listing2409 = pd.read_csv("Listing Raw/CRMLSListing202409.csv")
print(len(listing2409))
#34625 rows in 2024 September
listing2410 = pd.read_csv("Listing Raw/CRMLSListing202410.csv")
print(len(listing2410))
#34730 rows in 2024 October
listing2411 = pd.read_csv("Listing Raw/CRMLSListing202411.csv")
print(len(listing2411))
#25128 rows in 2024 November
listing2412 = pd.read_csv("Listing Raw/CRMLSListing202412.csv")
print(len(listing2412))
#19417 rows in 2024 December
listing2501 = pd.read_csv("Listing Raw/CRMLSListing202501.csv")
print(len(listing2501))
#37469 rows in 2025 January
listing2502 = pd.read_csv("Listing Raw/CRMLSListing202502.csv")
print(len(listing2502))
#33983 rows in 2025 February
listing2503 = pd.read_csv("Listing Raw/CRMLSListing202503.csv")
print(len(listing2503))
#38492 rows in 2025 March
listing2504 = pd.read_csv("Listing Raw/CRMLSListing202504.csv")
print(len(listing2504))
#40187 rows in 2025 April
listing2505 = pd.read_csv("Listing Raw/CRMLSListing202505.csv")
print(len(listing2505))
#40271 rows in 2025 May
listing2506 = pd.read_csv("Listing Raw/CRMLSListing202506.csv")
print(len(listing2506))
#26399 rows in 2025 June
listing2507 = pd.read_csv("Listing Raw/CRMLSListing202507.csv")
print(len(listing2507))
#27345 rows in 2025 July
listing2508 = pd.read_csv("Listing Raw/CRMLSListing202508.csv")
print(len(listing2508))
#25210 rows in 2025 August
listing2509 = pd.read_csv("Listing Raw/CRMLSListing202509.csv")
print(len(listing2509))
#26923 rows in 2025 September
listing2510 = pd.read_csv("Listing Raw/CRMLSListing202510.csv")
print(len(listing2510))
#27586 rows in 2025 October
listing2511 = pd.read_csv("Listing Raw/CRMLSListing202511.csv")
print(len(listing2511))
#20677 rows in 2025 November
listing2512 = pd.read_csv("Listing Raw/CRMLSListing202512.csv")
print(len(listing2512))
#18773 rows in 2025 December
listing2601 = pd.read_csv("Listing Raw/CRMLSListing202601.csv")
print(len(listing2601))
#35302 rows in 2026 January
listing2602 = pd.read_csv("Listing Raw/CRMLSListing202602.csv")
print(len(listing2602))
#32884 rows in 2026 February
listing2603 = pd.read_csv("Listing Raw/CRMLSListing202603.csv")
print(len(listing2603))
#39153 rows in 2026 March
listing2604 = pd.read_csv("Listing Raw/CRMLSListing202604.csv")
print(len(listing2604))
#39020 rows in 2026 April
listing2605 = pd.read_csv("Listing Raw/CRMLSListing202605.csv")
print(len(listing2605))
#36115 rows in 2026 May
listing2606 = pd.read_csv("Listing Raw/CRMLSListing202606.csv")
print(len(listing2606))
#37455 rows in 2026 June
listing = pd.concat([listing2401, listing2402, listing2403, listing2404, listing2405, listing2406, listing2407, listing2408, listing2409, listing2410, listing2411, listing2412,listing2501, listing2502, listing2503, listing2504, listing2505, listing2506, listing2507, listing2508, listing2509, listing2510, listing2511, listing2512,listing2601,listing2602,listing2603,listing2604,listing2605,listing2606], ignore_index=True)
print(len(listing))
#967164 rows in new dataset
# Inspect structure
listing.columns
listing.head()
# Check property categories
listing['PropertyType'].unique()
#To standardize our analysis across property types we will filter to Residential only. 
#Some interesting lot types included "land" and "BusinessOpportunity".
residentiallisting = listing[listing["PropertyType"] == 'Residential']
print(len(residentiallisting))
#615646 rows in residential dataset
# Validate completeness
residentiallisting.isnull().sum()
#Dividing these values by the row count shows that values above 90% null include:
#Middle or Junior School District
residentiallisting = residentiallisting.drop(columns=['MiddleOrJuniorSchoolDistrict'])
#Analyzing ClosePrice:
import matplotlib.pyplot as plt
residentiallisting['ClosePrice'] = pd.to_numeric(residentiallisting['ClosePrice'], errors='coerce')
close = residentiallisting['ClosePrice'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(close.values, vert=True, showfliers=False)
plt.title('Residential Sold Close Price Distribution')
plt.ylabel('Close Price in Millions')
plt.xticks([1], ['ClosePrice'])
plt.show()
#No outliers illustrated
mean_close = residentiallisting['ClosePrice'].mean()
print(mean_close)
#Sold Close Price mean is approximately 1.21 million dollars
#Analyzing Living Area:
residentiallisting['LivingArea'] = pd.to_numeric(residentiallisting['LivingArea'], errors='coerce')
living_area = residentiallisting['LivingArea'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(living_area.values, vert=True, showfliers=False)
plt.title('Residential Sold Living Area Distribution')
plt.ylabel('Living Area in Square Feet')
plt.xticks([1], ['LivingArea'])
plt.show()
#No outliers illustrated
mean_living_area = residentiallisting['LivingArea'].mean()
print(mean_living_area)
#Sold Living Area mean is approximately 1,980 square feet
#Analyzing DaysOnMarket:
residentiallisting['DaysOnMarket'] = pd.to_numeric(residentiallisting['DaysOnMarket'], errors='coerce')
days_on_market = residentiallisting['DaysOnMarket'].dropna()
plt.figure(figsize=(10, 6))
plt.boxplot(days_on_market.values, vert=True, showfliers=False)
plt.title('Residential Sold Days on Market Distribution')
plt.ylabel('Days on Market')
plt.xticks([1], ['DaysOnMarket'])
plt.show()
#No outliers illustrated
mean_days_on_market = residentiallisting['DaysOnMarket'].mean()
print(mean_days_on_market)
#Sold Days on Market mean is approximately 18.6 days
#Fetch the mortgage rate data from FRED
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
#Resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
mortgage.groupby('year_month')['rate_30yr_fixed']
.mean()
.reset_index()
)
#Create a matching year_month key on the MLS datasets
residentiallisting['year_month'] = pd.to_datetime(
residentiallisting['ListingContractDate']
).dt.to_period('M')
#Merge
listings_with_rates = residentiallisting.merge(mortgage_monthly, on='year_month', how='left')
#Validate
print(listings_with_rates['rate_30yr_fixed'].isnull().sum())
print(
listings_with_rates[
['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
].head()
)
#Convert date columns to datetime format
listings_with_rates['CloseDate'] = pd.to_datetime(
    listings_with_rates['CloseDate'],
    errors='coerce'
)
listings_with_rates['PurchaseContractDate'] = pd.to_datetime(
    listings_with_rates['PurchaseContractDate'],
    errors='coerce'
)
listings_with_rates['ListingContractDate'] = pd.to_datetime(
    listings_with_rates['ListingContractDate'],
    errors='coerce'
)
listings_with_rates['ContractStatusChangeDate'] = pd.to_datetime(
    listings_with_rates['ContractStatusChangeDate'],
    errors='coerce'
)
#Boolean flags for incorrect timelines
listings_with_rates['listing_after_close_flag'] = (
    listings_with_rates['ListingContractDate'] > listings_with_rates['CloseDate']
)

listings_with_rates['purchase_after_close_flag'] = (
    listings_with_rates['PurchaseContractDate'] > listings_with_rates['CloseDate']
)

listings_with_rates['negative_timeline_flag'] = (
    (listings_with_rates['ListingContractDate'] > listings_with_rates['PurchaseContractDate']) |
    (listings_with_rates['PurchaseContractDate'] > listings_with_rates['CloseDate'])
)
listings_with_rates['negative_timeline_flag'] = (
    listings_with_rates['ListingContractDate'].notna() &
    listings_with_rates['PurchaseContractDate'].notna() &
    listings_with_rates['CloseDate'].notna() &
    (
        (listings_with_rates['ListingContractDate'] > listings_with_rates['PurchaseContractDate']) |
        (listings_with_rates['PurchaseContractDate'] > listings_with_rates['CloseDate'])
    )
)
#Ensure numeric values aren't written as string values
listings_with_rates['ClosePrice'] = pd.to_numeric(listings_with_rates['ClosePrice'], errors='coerce')
listings_with_rates['LivingArea'] = pd.to_numeric(listings_with_rates['LivingArea'], errors='coerce')
listings_with_rates['DaysOnMarket'] = pd.to_numeric(listings_with_rates['DaysOnMarket'], errors='coerce')
#Exclude infeasible values
listings_with_rates = listings_with_rates[listings_with_rates['ClosePrice'] > 0]
listings_with_rates = listings_with_rates[listings_with_rates['LivingArea'] > 0]
listings_with_rates = listings_with_rates[listings_with_rates['DaysOnMarket'] >= 0]
listings_with_rates = listings_with_rates[listings_with_rates['BathroomsTotalInteger'] >= 0]
listings_with_rates = listings_with_rates[listings_with_rates['BedroomsTotal'] >= 0]
listings_with_rates.to_csv(r"C:\Users\madig\OneDrive\Desktop\IDX Exchange\Week 1\ResidentialListing.csv", index=False)