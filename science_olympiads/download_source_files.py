import requests
import shutil
import os

#Year 2011 is missing
PHYSICS_ROUND1 = [
    [2018, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/resultat-r1-1718-diplom-rettet.pdf"],
    [2017, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/resultat11617(1).pdf"],
    [2016, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/resultat11516.pdf"],
    [2015, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/resultat11415b(1).pdf"],
    [2014, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/resultat_1314.pdf"],
    [2013, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/res_1R_1213.pdf"],
    [2012, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/Res_1R_1112.pdf"],
    [2010, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/res_1R_0910.pdf"],
    [2009, "https://www.mn.uio.no/fysikk/forskning/grupper/skolelab/fysikk-ol/res_1R_0809.pdf"]
    ]
INFORMATICS_ROUND1 = [
    [2018, "http://nio.no/resultater-1-runde-nio-2017-2018/"],
    [2017, "http://nio.no/resultater-1-runde-nio-2016-2017/"],
    [2016, "http://nio.no/resultater-fra-1-runde-i-nio-20152016/"],
    [2015, "http://nio.no/resultater-fra-1-runde-i-nio-2014-2015/"],
    [2014, "http://nio.no/resultater-fra-1-runde-2013-2014/"],
    [2013, "http://nio.no/resultater-fra-1-runde-2012-2013/"]
    ]

CHEM_ROUND1 = [
    [2019, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2019.pdf"],
    [2018, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2018.pdf"],
    [2017, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2017.pdf"],
    [2016, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2016.pdf"],
    [2015, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2015.pdf"],

    [2013, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2013.pdf"],
    [2012, "https://foreninger.uio.no/kjemiolympiaden/resultater/Runde1-2012.pdf"],
    ]

MATH_ROUND1 = [
    [2019, "https://abelkonkurransen.no/files/runde1-2018.pdf"],
    [2018, "https://abelkonkurransen.no/files/runde1-2017.pdf"],
    [2017, "https://abelkonkurransen.no/files/runde1-2016.pdf"]
    ]


def get_physics_files(folder="raw_data/physics/pdf"):
    urls = PHYSICS_ROUND1
    if not os.path.exists(folder):
        os.makedirs(folder)
    for u in urls:
        year = u[0]
        url = u[1]
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(f"{folder}/round1_{year}.pdf", 'wb') as f:
            shutil.copyfileobj(r.raw, f)


def get_math_files(folder="raw_data/mathematics/pdf"):
    urls = MATH_ROUND1
    if not os.path.exists(folder):
        os.makedirs(folder)
    for u in urls:
        year = u[0]
        url = u[1]
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(f"{folder}/round1_{year}.pdf", 'wb') as f:
            shutil.copyfileobj(r.raw, f)


def get_chemistry_files(folder="raw_data/chemistry/pdf"):
    urls = CHEM_ROUND1
    if not os.path.exists(folder):
        os.makedirs(folder)
    for u in urls:
        year = u[0]
        url = u[1]
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(f"{folder}/round1_{year}.pdf", 'wb') as f:
            shutil.copyfileobj(r.raw, f)


def get_informatics_files(folder="raw_data/informatics/pdf"):
    urls = INFORMATICS_ROUND1
    if not os.path.exists(folder):
        os.makedirs(folder)
    for u in urls:
        year = u[0]
        url = u[1]
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(f"{folder}/round1_{year}.pdf", 'wb') as f:
            shutil.copyfileobj(r.raw, f)


get_math_files()
get_physics_files()
get_chemistry_files()
get_informatics_files()
