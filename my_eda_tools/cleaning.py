def missing_report(df):
    """Багана бүрийн хоосон утгын тоог буцаана."""
    return df.isna().sum()
def remove_duplicates(df):
    """Давхардсан мөрүүдийг арилгасан шинэ хүснэгт буцаана."""
    return df.drop_duplicates().reset_index(drop=True)