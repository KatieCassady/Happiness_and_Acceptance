import pandas as pd 

file_path = r'C:\Users\Einstein\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python312\CodeLouisvilleWork\Capstone\Happiness_and_Acceptance\World_Happiness_Index\2015.csv'
df_2015 = pd.read_csv(file_path)
print(df_2015)