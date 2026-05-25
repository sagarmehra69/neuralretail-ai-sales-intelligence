import pandas as pd

def clean_data(df):

    # Remove null customer IDs
    df = df.dropna(subset=['customerid'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove cancelled invoices
    df = df[~df['invoiceno'].astype(str).str.startswith('C')]

    # Convert date column
    df['nvoicedate'] = pd.to_datetime(df['invoicedate'])

    return df

def save_clean_data(df):
    df.to_csv("data/processed/cleaned_retail.csv", index=False)
