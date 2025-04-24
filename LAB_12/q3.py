import pandas as pd

asking_prices = pd.Series([10000, 12000, 8000, 7500, 9500])
fair_prices = pd.Series([10500, 11000, 8500, 7600, 9700])

good_deals = asking_prices < fair_prices
good_deal_indices = good_deals[good_deals].index.tolist()

print(good_deal_indices)
