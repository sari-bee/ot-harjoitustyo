import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

POS_ABO_CELL_REACTIONS = os.getenv("POSITIVE_ABO_CELL_REACTIONS") or "34"
POS_ABO_PLASMA_REACTIONS = os.getenv(
    "POSITIVE_ABO_PLASMA_REACTIONS") or "234"
POS_D_CELL_REACTIONS = os.getenv("POSITIVE_D_CELL_REACTIONS") or "34"

ABO_UNCLEAR = os.getenv(
    "ABO_UNCLEAR") or "Punasolut O, trombosyytit mitä vain ABO-ryhmää, jääplasma AB."
ABO_CLEAR = os.getenv("ABO_CLEAR") or "Verivalmisteet ABO-ryhmän mukaisesti."
RHD_UNCLEAR = os.getenv("RHD_UNCLEAR") or "Punasolut ja trombosyytit RhD neg."
RHD_NEGATIVE = os.getenv(
    "RHD_NEGATIVE") or "Punasolut ja trombosyytit RhD neg."
RHD_POSITIVE = os.getenv(
    "RHD_POSITIVE") or "Punasolut ja trombosyytit RhD pos."

SAMPLES_FILENAME = os.getenv("SAMPLES_FILENAME") or "samples.csv"
SAMPLES_FILEPATH = os.path.join(dirname, "..", "data", SAMPLES_FILENAME)

USERS_FILENAME = os.getenv("USERS_FILENAME") or "users.csv"
USERS_FILEPATH = os.path.join(dirname, "..", "data", USERS_FILENAME)
