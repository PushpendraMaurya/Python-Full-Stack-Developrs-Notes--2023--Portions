import pandas as pd


data = {"name":["pushpendra","ritesh","suraj","ravi","gaurab"],
        "gender":["male","male","male","male","male"],
        "location":["thane","thane","manpada","dombivali","nitin"],
        "contact":[7388006830,78965412,7896547895,3214567895,789654125]}


df = pd.DataFrame(data)

df.to_excel("new_file.xlsx",index = False)

print(df)