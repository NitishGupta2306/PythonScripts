import pandas as pd
import camelot
def getTableData_URL(url: str):
   return pd.read_html(url)

def getTableData_PDF(PDF_path: str, FileName:str):
   """
   Args:
       PDF_path (str): Exact path to the PDF file.
       FileName (str): CSV file name where the table data will be stored.
   """
   table = camelot.read_pdf(PDF_path, pages='all', flavor='stream')
   table.export(FileName + '.csv', f= 'csv', compress= True)
   table.to_csv(FileName + '.csv', index=False)

#! Set the path to the PDF file you want to scrape table data from.
PDF_path = ''
#! Set the name of the CSV file where the table data will be stored.
FileName = ''
# Get the table data from the PDF file.
getTableData_PDF(PDF_path, FileName)


#! Set the URL to the website you want to scrape table data from.
url = ''
# Get the table data from the website.
res_table = getTableData_URL(url)


