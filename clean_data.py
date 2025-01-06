import pandas as pd
import re

import pandas as pd

df = pd.read_csv('data_group.csv', encoding='latin1', on_bad_lines='skip')

print(df.head())

print(df.columns)

print(df.head())

print(df.head())

print(df.columns)


df = df.drop(columns=['raw_column', 'other_column'], errors='ignore')

print(df.columns)

df = pd.read_csv('data_group.csv', encoding='utf-8-sig', on_bad_lines='skip')
print(df.columns)

print(df.iloc[:, 0].head())


df[['date_time', 'message']] = df.iloc[:, 0].str.split(' - ', expand=True, n=1)

print(df[['date_time', 'message']].head())


df[['date', 'time']] = df['date_time'].str.split(' ', n=1, expand=True)

print(df[['date', 'time']].head())


df[['sender', 'message']] = df['message'].str.split(': ', n=1, expand=True)

print(df[['date', 'time', 'sender', 'message']].head())


df.fillna({'date': '', 'time': '', 'sender': '', 'message': ''}, inplace=True)

print(df[['date', 'time', 'sender', 'message']].head())


df['message'] = df['message'].str.replace(';;', '').str.strip()
print(df[['date', 'time', 'sender', 'message']].head())


df['message'] = df['message'].str.replace('â€™', "'", regex=False)
df['message'] = df['message'].str.replace('â€œ', '"', regex=False)
df['message'] = df['message'].str.replace('â€', '"', regex=False)
print(df[['date', 'time', 'sender', 'message']].head())


df['message'] = df['message'].apply(lambda x: re.sub(r'[\x80-\x9f]', '', x) if isinstance(x, str) else x)

print(df[['date', 'time', 'sender', 'message']].head())


df['message'] = df['message'].apply(lambda x: x.encode('utf-8', errors='replace').decode('utf-8', errors='ignore') if isinstance(x, str) else x)

print(df[['date', 'time', 'sender', 'message']].head())


df = df[df['message'].str.strip().notna()]  
df = df[~df['message'].str.contains("Anda ditambahkan", case=False)]  
print(df.head())


df['message'] = df['message'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s\.,?!]', '', x) if isinstance(x, str) else x)

print(df[['date', 'time', 'sender', 'message']].head())


df = df[~df['date'].str.contains(';;', na=False)]
df = df[~df['time'].str.contains(';;', na=False)]

df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], errors='coerce', format='%d/%m/%y %H.%M')

print(df[['datetime', 'sender', 'message']].head())


df['sender'] = df['sender'].apply(lambda x: re.sub(r'^\+62', 'ID ', x) if isinstance(x, str) else x)

print(df[['datetime', 'sender', 'message']].head())


df = df.drop_duplicates(subset=['datetime', 'sender', 'message'])

print(df[['datetime', 'sender', 'message']].head())

 
df['message'] = df['message'].fillna('No message')

print(df[['datetime', 'sender', 'message']].head())


df['message'] = df['message'].str.replace(';;', '', regex=False)

print(df[['datetime', 'sender', 'message']].head())


df['message'] = df['message'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s.,;!?()-]', '', str(x)))

print(df[['datetime', 'sender', 'message']].head())

df['message'] = df['message'].str.lower()

print(df[['datetime', 'sender', 'message']].head())


df['message'] = df['message'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s.,;!?()-]', '', str(x)))

print(df[['datetime', 'sender', 'message']].head())


df['message'] = df['message'].apply(lambda x: re.sub(r'\s+', ' ', str(x).strip()))

print(df[['datetime', 'sender', 'message']].head())


df.to_csv('data_cleaned.csv', index=False)


