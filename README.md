# JPMChase-Prj.
updating and saving a processed CSV file in a location
Task
Create a lambda function that connects and processes the financial data flat file for JPMorgan Chase company. The file has 7 original columns for; Date, Open, High, Low, Close, Adj Close, and Volume. 
Your function should add two new columns to the table.
I. Daily range - Which is the difference between the open and close columns for every row.
Ii. Daily span - The difference between the high and low values for every row.

After processing, the function should save your new file to another folder within your S3 location.
# Expected Output
●	Your lambda python file that was run using AWS Lambda
●	The processed CSV file.
●	A ReadMe.MD explaining and sharing details about your project work. 
