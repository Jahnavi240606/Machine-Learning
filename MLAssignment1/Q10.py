import pandas as pd

df = pd.read_excel(r"C:\Users\pandu\OneDrive\Documents\MLAssignment1\MLASSIGN1.xlsx")

df['City, State'] = df['City'] + ", " + df['State']

df.to_excel(r"C:\Users\pandu\OneDrive\Documents\MLAssignment1\MLASSIGN1_UPDATED.xlsx", index=False)
