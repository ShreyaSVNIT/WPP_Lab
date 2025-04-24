import pandas as pd

df = pd.DataFrame({
    'John': [True, False, True, True, False, False, True, False, False, True],
    'Judy': [True, False, True, False, False, True, True, False, True, True]
})

party_days = (df['John'] & df['Judy']).values

days_til_party = [None] * len(df)
for i in range(len(df)):
    for j in range(i, len(df)):
        if party_days[j]:
            days_til_party[i] = j - i
            break
    if days_til_party[i] is None:
        days_til_party[i] = -1

df['days_til_party'] = days_til_party
print(df)
