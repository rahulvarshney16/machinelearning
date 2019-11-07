# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:40:24 2019

@author: Rahul Varshney
"""


import xlsxwriter
import openpyxl



# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('TD_cases_aging.xlsx')
worksheet = workbook.add_worksheet('aging_graph')

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)

# Insert an image.
#worksheet.write('A2', 'Insert an image in a cell:')
#worksheet.insert_image('B2', 'ageplot.png')

# Insert an image offset in the cell.
worksheet.write('A1', 'cases aging trend line:')
worksheet.insert_image('A3', 'ageplot.png', {'x_offset': 15, 'y_offset': 10})

# Insert an image with scaling.
#worksheet.write('A23', 'Insert a scaled image:')
#worksheet.insert_image('B23', 'ageplot.png', {'x_scale': 0.5, 'y_scale': 0.5})

workbook.close()


#from pandas.io.excel import ExcelWriter
#import pandas

#csv_files = ['join.csv', 'mean.csv']

#with ExcelWriter('ageing.xlsx') as ew:
#    for csv_file in csv_files:
#        pandas.read_csv(csv_file).to_excel(ew, sheet_name=csv_file)
        
             
        
#filename='ageing.xlsx'
writer = pandas.ExcelWriter('TD_cases_aging.xlsx', engine='openpyxl')

#if os.path.exists(file_name):
book = openpyxl.load_workbook('TD_cases_aging.xlsx')
writer.book = book
df=pandas.read_csv('Old_Current_Aging.csv')
df.to_excel(writer, sheet_name='Old_Current_Aging')
df2=pandas.read_csv('aging_mean.csv')
df2.to_excel(writer, sheet_name='aging_mean')
writer.save()
writer.close()
        
        
        
