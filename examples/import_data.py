# This example file demonstrates how to import data
# using the python module `pandas'
# pandas can be imported as follows (required to be able
# to use functions, classes, ...) that are defined
# in the module
import pandas as pd

# then, to import data, use the pd.read_<datatype> function
excel_data = pd.read_excel("example_data/data_file.xlsx")  # imports xlsx files
csv_data = pd.read_csv("example_data/data_file.csv")  # imports csv files

# now, one can start to work with the data stored in the
# newly created variables `excel_data' and `csv_data'
# make sure to use the correct import function for your data format, though!
print(csv_data.head(n=5))  # `head()' method prints the first `n' rows
print(excel_data.head(n=3))  # in this case, only the first 3 rows are printed
