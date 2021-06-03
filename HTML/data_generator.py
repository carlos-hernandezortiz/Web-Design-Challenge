import pandas as pd
df = pd.read_csv("C:/Users/empha/Desktop/Data_Analytics/Semana_11/Web-Design-Challenge/Resources/cities.csv")
df.head()
df.to_html('C:/Users/empha/Desktop/Data_Analytics/Semana_11/Web-Design-Challenge/HTML/Data_table.html',index=False)
