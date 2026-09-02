import pandas as pd

data = {
    'transazione_id': [101, 102, 103, 104, 105],
    'prodotto': ['Corsa Standard', 'Corsa Premium', 'Van', 'Corsa Standard', 'Van'],
    'citta': ['Milano', 'Roma', 'Milano', 'Milano', 'Roma'],
    'prezzo': [45.0, 90.0, 120.0, 45.0, 110.0]
}
df = pd.DataFrame(data)

report = df.groupby('citta').agg(
    totale_ricavi=('prezzo', 'sum'),
    numero_prenotazioni=('transazione_id', 'count'),
    prezzo_medio=('prezzo', 'mean')
).reset_index()

report.to_csv('report_riepilogo.csv', index=False)

print("Generated Summary Report:")
print(report)
