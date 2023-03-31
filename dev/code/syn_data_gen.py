import pandas as pd
import smogn

df = pd.read_csv("../dataset/formatted.csv")
tar_col = "LC50 [-LOG(mol/L)]"
smoted = smogn.smoter( data = df, y = tar_col)
# print(smoted)
df["isSyn"] = 0
smoted["isSyn"] = 1

# print(f"df shape: {df.shape}")
# print(f"smoted shape: {smoted.shape}")

export_df = pd.concat([df, smoted], ignore_index=True)
# print(export_df)

export_df.to_csv("../dataset/smogn_syn_data.csv",index=False)
