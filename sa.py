import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='/Insta_Data.xlsx'
xl = pd.ExcelFile(file)   #read Excel File
dfs= xl.parse(xl.sheet_names[0])    #Parsing the excel sheet to dataframe
dfs = list(dfs['Posts']) #Removes the blank rows from the dataframe
print(dfs)
sid = SentimentIntensityAnalyzer()
str1 = "UTC+05:30"
for data in dfs:
    data=str(data)
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
          print(k,ss[k])