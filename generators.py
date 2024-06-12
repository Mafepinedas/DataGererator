#  -*- coding: utf-8 -*-
"""
This module defines the template to generate random data for each document type.
"""

import random
from datetime import datetime
from typing import Tuple

import numpy as np
from dateutil.relativedelta import relativedelta
from faker import Faker
from faker.providers import internet

from base_data import *

fake_ES = Faker('es_ES')
fake_CO = Faker(['es_CO'])
fake_ES.add_provider(internet)


def id_generator(id_type='CC', seed: int = None) -> str:
    """
    This method creates random ID numbers based on the id_type.

    # TODO: Implemente Passport generators

    :param str id_type: ID Type. Currently supported: CC, CE, and NIT.
    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    id_generators = {
        'CC': f"{random.randint(10000000, 9999999999)}",
        'CE': f"{random.randint(1000, 9999999999)}",
        'NIT': f"{random.randint(1000, 9999999999)}-{random.randint(0, 9)}",
        }

    if seed:
        random.seed(seed)
    if id_type in id_generators.keys():
        x = id_generators[id_type]
    else:
        print(f'The id type: {id_type} is not supported yet.')
        x = f"{np.NAN}"
    return x


def id_types_generator(seed: int = None) -> str:
    """
    This method select an id type based on the static definitions.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(id_types)


def birthdate_generator(min_age: int = 18, max_age: int = 50, seed: int = None) -> datetime.date:
    """
    This method create random a birthdate between an interval of ages.

    # TODO: Implement a birthdate generator for dates before 1970

    :param int min_age: Lower bound used in the birthdate generator.
    :param int max_age: Higher bound used in the birthdate generator
    :param int seed: Seed to initialize the random functions.
    :return datetime.date:
    """
    if seed:
        random.seed(seed)
    timestamp_min = (datetime.now() - relativedelta(years=max_age)).timestamp()
    timestamp_max = (datetime.now() - relativedelta(years=min_age)).timestamp()
    x = random.uniform(timestamp_min, timestamp_max)
    return datetime.fromtimestamp(x).date()


def city_generator(seed: int = None) -> str:
    """
    This method select a Colombian city based on the static definitions.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(colombian_cities)


def id_expedition_date_generator(birthdate: datetime.date, seed: int = None) -> datetime.date:
    """
    This method create a random ID expedition date, based on the birthdate.

    :param datetime.date birthdate: Base date to calculate ID expedition date.
    :param int seed: Seed to initialize the random functions.
    :return datetime.date:
    """
    if seed:
        random.seed(seed)
    return birthdate + relativedelta(years=18, days=random.randint(0, 60))


def nationality_generator(seed: int = None) -> str:
    """
    This method select a country from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(countries_phone_codes)['name']


def phone_generator(colombian=True, seed: int = None) -> str:
    """
    This method generates random telephone numbers. If colombian=True then the dial code is +57. Otherwise, a random
    dial code is selected from the static data.

    :param bool colombian: Select if the number is a Colombian number.
    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    if not colombian:
        phone_code = random.choice(countries_phone_codes)['dial_code']
    else:
        phone_code = '+ 57'
    return f"{phone_code} {random.randint(0000000000, 9999999999)}"


def blood_type_generator(seed: int = None) -> str:
    """
    This method select a blood type from static data.

    # TODO: Implement a weighted selection based on  the probability of each blood type.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(blood_types)


def genre_generator(seed: int = None) -> str:
    """
    This method select a genre from the static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(genres)


def email_generator(seed: int = None) -> str:
    """
    This method create random fake emails.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        Faker.seed(seed)
    return fake_ES.ascii_free_email()


def name_generator(seed: int = None) -> str:
    """
    This method create random Spanish names.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        Faker.seed(seed)
    return fake_CO.name()


def job_generator(seed: int = None) -> str:
    """
    This method select a Colombian job define in CIUO-88 from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(jobs_colombia)


def address_generator(seed: int = None) -> str:
    """
    This method generate random street addresses.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        Faker.seed(seed)
    return fake_CO.street.address()


def marital_status_generator(seed: int = None) -> str:
    """
    This method select a marital status from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(marital_status)


def eps_generator(seed: int = None) -> str:
    """
    This method select an EPS from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(colombian_eps)


def arl_generator(seed: int = None) -> str:
    """
    This method select an ARL from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(colombian_arl)


def health_insurance_generator(seed: int = None) -> str:
    """
    This method select a Health Insurance from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(colombian_health_insurances)


def company_generator(seed: int = None) -> str:
    """
    This method generate fake Companies in Spanish.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        Faker.seed(seed)
    return fake_CO.company()


def contract_start_date_generator(birthdate: datetime.date, seed: int = None) -> datetime.date:
    """
    This method generate random contract start dates based on the birthdate, creating contracts dates for only legal
    ages dates.

    :param datetime.date birthdate: Base date to calculate ID expedition date.
    :param int seed: Seed to initialize the random functions.
    :return datetime.date:
    """
    if seed:
        random.seed(seed)
    start_date = birthdate
    start_date += relativedelta(
        years=(18 + random.randint(0, 8)),
        months=random.randint(0, 12),
        days=random.randint(0, 30))
    # Validate if start_date is in the future
    if start_date >= datetime.now().date():
        start_date = datetime.now().date() - relativedelta(months=random.randint(0, 6), days=random.randint(0, 30))
    return start_date


def contract_end_date_generator(start_date: datetime.date, seed: int = None) -> datetime.date:
    """
    This method generate contract end dates based on start date of the contract.

    :param datetime.date start_date:  Base date to calculate contract end date.
    :param int seed: Seed to initialize the random functions.
    :return datetime.date:
    """
    if seed:
        random.seed(seed)
    end_date = start_date
    end_date += relativedelta(
        years=(random.randint(0, 8)),
        months=random.randint(0, 12),
        days=random.randint(0, 30))
    # Validate if end_date is more than 1 year in the future
    diff = end_date - start_date
    if diff.days <= 0 and abs(diff.days) > 365:
        end_date = start_date + relativedelta(months=random.randint(0, 4), days=random.randint(0, 30))
    return end_date


def contract_type_generator(seed: int = None) -> str:
    """
    This method select a contract type from the static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(contract_types)


def institution_generator(seed: int = None) -> str:
    """
    This method select an institution from the static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(institutions_study)


def degree_generator(seed: int = None) -> str:
    """
    This method select a degree from static data.

    :param int seed: Seed to initialize the random functions.
    :return str:
    """
    if seed:
        random.seed(seed)
    return random.choice(degrees_study)


def ciiud_generator(seed: int = None) -> Tuple[str, str]:
    """
    This method select a CIIUD code, with the respective activity description.

    :param int seed: Seed to initialize the random functions.
    :return Tuple[str, str]:
    """
    if seed:
        random.seed(seed)
    return random.choice(ciiud)
