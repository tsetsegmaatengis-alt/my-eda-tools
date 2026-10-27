def missing_report(df):
    """Багана бүрийн хоосон утгын тоог буцаана."""
    return df.isna().sum()