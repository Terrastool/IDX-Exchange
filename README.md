To begin CSVs lebeled with '_filled' should have their last two columns deleted, at the time of my completion there are 4 of such CSVs.
Written 1 loads all the data and prints their row count, then concatenates the two datasets (sold and listing) and lists their row counts.
Further, the two data sets are filtered to only Residential Property Types then row counted once more.
Then both are saved as CSVs for use in future weeks.

Week 2/Written2.py
Columns Values are analyzed and values with over 90% null rows are flagged.
ClosePrice, DaysOnMarket, and Living Area are boxplotted and analyzed for means.

Week 3/Written3.py
Adds June values for listing and sold data sets.
Dropped null columns from week 3.
Pulled data from FRED to create a new variable then validated.

Week 4/Written4.py
Runs a variety of checks including event time order, numeric values not as strings, 
and deleting illogical numeric entries for values like Bedrooms or Days on the Market.

Week 5/Written5.py
Creates a variable called District Name which uses school district regions to place homes in groupings using geo data.

Week 6/Written6.py
Makes sure that flags are in place for Coordinate Issues rather than dropping rows.
Creates new values (Price Ratio, Price Per Sqr Feet, Close to Original List Ratio, Listing to Contract Days, and Contract to Close Days) 
using formulas and generates summary statistics tables for 6 groupings (Property Type, Property Sub Type, County or Parish, MLS Area Major, List Office Name, and Buyer Office Name).
