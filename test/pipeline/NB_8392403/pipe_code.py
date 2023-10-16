import pickle
import pandas as pd
df0 = pickle.load(open("data_0.pickle",'rb'))
df0.columns = [str(c) for c in df0.columns]
df0["index"] = df0.index
df1 = df0[((df0['date'].isnull()) == False)]
df2 = pickle.load(open("data_7.pickle",'rb'))
df2.columns = [str(c) for c in df2.columns]
df2["index"] = df2.index
df3 = df2[((df2['date'].isnull()) == False)]
df4 = pickle.load(open("data_14.pickle",'rb'))
df4.columns = [str(c) for c in df4.columns]
df4["index"] = df4.index
df5 = df4[((df4['date'].isnull()) == False)]
df6 = pickle.load(open("data_21.pickle",'rb'))
df6.columns = [str(c) for c in df6.columns]
df6["index"] = df6.index
df7 = df6[((df6['date'].isnull()) == False)]
df8 = pd.concat([df1,df3], axis=0)
df9 = pd.concat([df8,df5], axis=0)
df10 = pd.concat([df9,df7], axis=0)
df11 = df10.sort_values(by=["date"])
df12 = df11.groupby(["date"]).agg({ "SearchFrequency":"sum" }).reset_index().rename(columns={ "SearchFrequency":"SearchFrequency" })
pickle.dump(df12, open('./temp/result_original.p', 'wb'))