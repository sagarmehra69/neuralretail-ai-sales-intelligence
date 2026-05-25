import pandas as pd


def load_all_data(file1, file2):

    # ====================================
    # LOAD SHEETS FROM FILE 1
    # ====================================

    sheet1 = pd.read_excel(
        file1,
        sheet_name=0
    )

    sheet2 = pd.read_excel(
        file1,
        sheet_name=1
    )

    # ====================================
    # LOAD FILE 2
    # ====================================

    df3 = pd.read_excel(file2)

    # ====================================
    # STANDARDIZE COLUMN NAMES
    # ====================================

    datasets = [sheet1, sheet2, df3]

    for df in datasets:

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

    # ====================================
    # FIX SCHEMA DIFFERENCES
    # ====================================

    for df in datasets:

        df.rename(columns={

            'invoice': 'invoiceno',

            'invoice date': 'invoicedate',

            'price': 'unitprice',

            'customer id': 'customerid',

            'customer_id': 'customerid'

        }, inplace=True)

    # ====================================
    # KEEP COMMON COLUMNS
    # ====================================

    common_cols = [

        'invoiceno',

        'stockcode',

        'description',

        'quantity',

        'invoicedate',

        'unitprice',

        'customerid',

        'country'

    ]

    sheet1 = sheet1[common_cols]

    sheet2 = sheet2[common_cols]

    df3 = df3[common_cols]

    # ====================================
    # MERGE EVERYTHING
    # ====================================

    df = pd.concat(
        [sheet1, sheet2, df3],
        ignore_index=True
    )

    # ====================================
    # REMOVE DUPLICATES
    # ====================================

    df = df.drop_duplicates()

    # ====================================
    # REMOVE NULL CUSTOMER IDs
    # ====================================

    df = df.dropna(
        subset=['customerid']
    )

    # ====================================
    # REMOVE CANCELLED INVOICES
    # ====================================

    df = df[
        ~df['invoiceno']
        .astype(str)
        .str.startswith('C')
    ]

    # ====================================
    # REMOVE INVALID VALUES
    # ====================================

    df = df[df['quantity'] > 0]

    df = df[df['unitprice'] > 0]

    # ====================================
    # CONVERT DATETIME
    # ====================================

    df['invoicedate'] = pd.to_datetime(
        df['invoicedate']
    )

    # ====================================
    # CREATE TOTAL SALES FEATURE
    # ====================================

    df['totalprice'] = (
        df['quantity']
        * df['unitprice']
    )

    return df