import pandas as pd
from IPython.display import display

my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
df = pd.DataFrame(my_dict)
print(df)
display(df.index)
display(df.values)

print("==================")
my_list = df.values
df = pd.DataFrame(my_list, columns=['학번', '이름', '점수'])
print(df)

print("===================")
print(df['학번'])
print("===================")
print(df['학번'][0])