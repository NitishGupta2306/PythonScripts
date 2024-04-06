import pandas as pd
def getTableData(url: str):
   return pd.read_html(url)

# Set the URL to the website you want to scrape table data from.
url = ''

# Get the table data from the website.
res_table = getTableData(url)

print(res_table[1])

for table in res_table:
  print(table)

