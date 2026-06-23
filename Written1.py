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
sold = pd.concat([sold2401, sold2402, sold2403, sold2404, sold2405, sold2406, sold2407, sold2408, sold2409, sold2410, sold2411, sold2412,sold2501, sold2502, sold2503, sold2504, sold2505, sold2506, sold2507, sold2508, sold2509, sold2510, sold2511, sold2512,sold2601,sold2602,sold2603,sold2604], ignore_index=True)  
print(len(sold))
#615725 rows in new dataset
residentialsold = sold[sold["PropertyType"] == 'Residential']
print(len(residentialsold))
#414063 rows in residential dataset
residentialsold.to_csv(r"C:\Users\madig\OneDrive\Desktop\IDX Exchange\Week 1\ResidentialSold.csv", index=False)
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
listing = pd.concat([listing2401, listing2402, listing2403, listing2404, listing2405, listing2406, listing2407, listing2408, listing2409, listing2410, listing2411, listing2412,listing2501, listing2502, listing2503, listing2504, listing2505, listing2506, listing2507, listing2508, listing2509, listing2510, listing2511, listing2512,listing2601,listing2602,listing2603,listing2604], ignore_index=True)
print(len(listing))
#893594 rows in new dataset
residentiallisting = listing[listing["PropertyType"] == 'Residential']
print(len(residentiallisting))
#567549 rows in residential dataset
residentiallisting.to_csv(r"C:\Users\madig\OneDrive\Desktop\IDX Exchange\Week 1\ResidentialListing.csv", index=False)