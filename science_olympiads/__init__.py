import pandas as pd
import os

CHEMISTRY_YEARS = [2012,2013,2015,2017,2018,2019]
MATH_YEARS = [2016,2017,2018]
PHYSICS_YEARS = [2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
INFORMATICS_YEARS = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def get_dataframe(subject, year):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), f"csv/{subject}_{year}.csv"))


def get_all_data():
    df = pd.DataFrame(columns=["competition", "year", "points", "gender"])
    frames = []
    for year in PHYSICS_YEARS:
        df1 = get_dataframe("physics", year)
        df1 = df1[["points", "gender"]]
        df1.insert(0, "competition", "physics")
        df1.insert(1, "year", year)
        frames.append(df1)
    for year in CHEMISTRY_YEARS:
        df1 = get_dataframe("chemistry", year)
        df1 = df1[["points", "gender"]]
        df1.insert(0, "competition", "chemistry")
        df1.insert(1, "year", year)
        frames.append(df1)
    for year in INFORMATICS_YEARS:
        df1 = get_dataframe("informatics", year)
        df1 = df1[["points", "gender"]]
        df1.insert(0, "competition", "informatics")
        df1.insert(1, "year", year)
        frames.append(df1)
    for year in MATH_YEARS:
        df1 = get_dataframe("mathematics", year)
        df1 = df1[["points", "gender"]]
        df1.insert(0, "competition", "mathematics")
        df1.insert(1, "year", year)
        frames.append(df1)

    return df


def get_filenames():
    columns = ["competition", "year", "file_path"]
    rows = []
    for year in CHEMISTRY_YEARS:
        rows.append(["chemistry", year, f"science_olympiads/csv/chemistry_{year}.csv"])
    for year in MATH_YEARS:
        rows.append(["mathematics", year, f"science_olympiads/csv/mathematics_{year}.csv"])
    for year in PHYSICS_YEARS:
        rows.append(["physics", year, f"science_olympiads/csv/physics_{year}.csv"])
    for year in INFORMATICS_YEARS:
        rows.append(["informatics", year, f"science_olympiads/csv/informatics_{year}.csv"])
    df = pd.DataFrame(rows, columns=columns)

    return df

