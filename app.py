import  numpy as np


print("A")

print("B")

def clean_df(df):
    df = df.dropna()

    return df

def remove_dub(df):
    df = df.drop_duplicates(subset=['id'])
    print("drop by duplicates id")
    return df

#checking out git branch

def plot_this(x_data, y_data):
        try:
             plt.plot(x_data, y_data)
             print("success rendering plot")
        except Exception as e:
             print(e)

#no way this will work. SIKE