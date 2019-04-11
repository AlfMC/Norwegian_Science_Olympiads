import pandas as pd
import gender_guesser_mod.detector as gg
import math

_detector = gg.Detector(case_sensitive=False)

# It is assumed that the columns "first_name", "last_name", "full_name" exist.
def fix_names(df):
    """
    :param df: DataFrame
    :return: DaraFrame
    """
    has_first_name = "first_name" in df
    has_last_name = "last_name" in df

    for i in df.index:
        first_name_unchanged = df.loc[i, "first_name"].strip()
        first_name = df.loc[i, "first_name"].strip().split()[0]
        df.loc[i, "first_name"] = first_name
        df.loc[i, "school"] = df.loc[i, "school"].strip()
        if "last_name" in df:
            last_name = df.loc[i, "last_name"].strip()
            df.loc[i, "last_name"] = last_name
            df.loc[i, "full_name"] = first_name + " " + last_name
            df.loc[i, "full_name"] = df.loc[i, "full_name"].strip()  # Necessary for some cases
        else:
            df.loc[i, "full_name"] = first_name_unchanged
    if "last_name" in df:
        del df["last_name"]

    return df

# Assumes that the columns "gender" and "first_name" exist.
def fix_gender(df):
    """
    :param df: DataFrame
    :return: DataFrame
    """
    for i in df.index:
        first_name = df.loc[i, "first_name"]
        df.loc[i, "gender"] = _detector.get_gender(first_name, country="norway")
    return df

def get_unknown_names(df):
    """
    :param df: DataFrame
    :return: List
    """
    # Removing duplicates
    unknown_names = df[(df.gender != "male") & (df.gender != "female")].first_name

    unknown_names.drop_duplicates()

    return list(set(unknown_names))
