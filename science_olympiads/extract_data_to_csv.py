import pandas as pd
import operations as op
import re


CHEMISTRY_YEARS = [2012,2013,2015,2017,2018,2019]
MATH_YEARS = [2016,2017,2018]
PHYSICS_YEARS = [2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
INFORMATICS_YEARS = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def extract_math(year, in_folder="raw_data/mathematics"):
    """A messy method to extracy messy data."""

    in_filename = f"{in_folder}/raw_data_{year}.txt"
    with open(in_filename, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read().strip().replace("\n", " ")

    splitted = re.split(r"\d{0,3}.-plass..\d{0,3} poeng ", data)
    splitted.pop(0)  # Need to do this for some reason.

    bracket = re.findall(r"\d{0,3}.-plass..\d{0,3} poeng ", data)

    namelist = []

    for line, ps in zip(splitted, bracket):
        # The data for each person is separated by a semicolon
        person_data = line.split(";")

        # Extracts the number of points only. Removing surrounding text.
        points = re.findall(r"\d{1,3} poeng", ps)[0].split()[0]
        for p in person_data:
            # The person's name and school is separated by a comma.
            properties = p.split(",")
            name = properties[0]
            firstname = name.split()[0]
            school = properties[1]
            person = [points, firstname, name, school]
            namelist.append(person)

    df = pd.DataFrame(namelist)
    df.columns = ["points", "first_name", "full_name", "school"]
    print(df.head())
    df.insert(1, "gender", "")
    #df.reindex(["points", "gender", "first_name", "full_name", "school"], axis=1)
    print(df.head())
    df = op.fix_names(df)
    df = op.fix_gender(df)
    print(df.head())
    return df

def write_math(years=MATH_YEARS, print_unknown_names=False):
    unknown_names = []
    for year in years:
        df = extract_informatics(year)
        df.to_csv(f"csv/mathematics_{year}.csv", index="False", encoding="utf-8")
        unknown_names.extend(op.get_unknown_names(df))
        print(f"Wrote year {year} in mathematics.")
    if print_unknown_names:
        print("Names with unknown gender:")
        for name in set(unknown_names):
            print(name)

def extract_chemistry(year, in_folder="raw_data/chemistry"):
    df = pd.read_csv(f"{in_folder}/raw_data_{year}.csv")

    columns = ["last_name", "first_name", "school", "points"]

    # Fixing columns
    df.columns = columns
    df.insert(1, "gender", "")
    df.insert(1, "full_name", "")
    df = df.reindex(["points", "gender", "first_name", "full_name", "last_name", "school"], axis=1)

    # Removing superflous whitespaces and filling full_name column
    op.fix_names(df)
    op.fix_gender(df)

    return df

def write_chemistry(years=CHEMISTRY_YEARS, print_unknown_names=False):
    unknown_names = []
    for year in years:
        print(f"Wrote year {year} in chemistry.")
        df = extract_chemistry(year)
        df.to_csv(f"csv/chemistry_{year}.csv", index="False", encoding="utf-8")
        unknown_names.extend(op.get_unknown_names(df))
    if print_unknown_names:
        for name in set(unknown_names):
            print(name)

def extract_physics(year, in_folder="raw_data/physics"):

    in_filename = f"{in_folder}/raw_data_{year}.csv"
    df = pd.read_csv(in_filename, encoding="utf-8")

    df.columns = ["first_name", "last_name", "points", "school"]

    df.insert(0, "gender", "")
    df.insert(0, "full_name", "")

    # Changing the ordering of the columns
    df = df[["points", "gender", "first_name","full_name", "last_name", "school"]]

    df = op.fix_names(df)
    df = op.fix_gender(df)
    return df

def write_physics(years=PHYSICS_YEARS, print_unknown_names=False):
    unknown_names = []
    for year in years:
        print(f"Wrote year {year} in physics.")
        df = extract_physics(year)
        df.to_csv(f"csv/physics_{year}.csv", index="False", encoding="utf-8")
        unknown_names.extend(op.get_unknown_names(df))
    if print_unknown_names:
        print("Names with unknown gender:")
        for name in set(unknown_names):
            print(name)

def extract_informatics(year, in_folder="raw_data/informatics"):

    in_filename = f"{in_folder}/raw_data_{year}.csv"
    df = pd.read_csv(in_filename, encoding="utf-8", sep=",", delimiter=",")

    df.columns = ["first_name", "school", "points"]

    # Adding gender column, and first_name column.
    df.insert(0, "gender", "")
    df.insert(0, "full_name", "")

    # Changing the ordering of the columns
    df = df[["points", "gender", "first_name", "full_name", "school"]]

    df = op.fix_names(df)
    df = op.fix_gender(df)

    return df

def write_informatics(years=INFORMATICS_YEARS, print_unknown_names=False):
    unknown_names = []
    for year in years:
        df = extract_informatics(year)
        df.to_csv(f"csv/informatics_{year}.csv", index="False", encoding="utf-8")
        unknown_names.extend(op.get_unknown_names(df))
        print(f"Wrote year {year} in informatics.")
    if print_unknown_names:
        print("Names with unknown gender:")
        for name in set(unknown_names):
            print(name)


""" Math section"""
write_math(print_unknown_names=False)

"""Chemistry section"""
write_chemistry(print_unknown_names=False)

"""Informatics section"""
write_informatics(print_unknown_names=False)

"""Physics section"""
write_physics(print_unknown_names=False)



#