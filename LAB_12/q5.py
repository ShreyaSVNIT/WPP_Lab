import pandas as pd

concerts = pd.DataFrame({
    'artist': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'venue': ['X', 'Y', 'X', 'Z', 'Y', 'X', 'Z'],
    'date': pd.to_datetime(['2024-01-15', '2024-01-20', '2024-02-15',
                            '2024-01-18', '2024-02-25', '2024-01-05', '2024-02-01'])
})

concerts['year_month'] = concerts['date'].dt.to_period('M')

grouped = concerts.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

grouped.columns = [f'{a}_{v}' for a, v in grouped.columns]

print(grouped)
