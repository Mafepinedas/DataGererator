#  -*- coding: utf-8 -*-
"""
This module defines the template to generate random data for each document type.
"""

import random
from datetime import datetime
from typing import Dict

from dateutil.relativedelta import relativedelta

import generators


def document_formulario_conocimiento_empleados(seed=None) -> Dict:
    """
    This method create a sample for a Document of "Formulario de conocimiento de empleados"
    :param int seed: Seed to initialize the random functions.
    :return Dict:
    """
    data_entry = {
        'sg_document_type': 'formulario_conocimiento_empleados',
        'sg_create_at': datetime.now().date(),
        'sg_update_at': datetime.now().date(),
        'sg_additional_info': None,
        'form_date': datetime.now().date() - relativedelta(days=random.randint(1, 60)),
        }

    # Create basic information data
    basic_info = dict()
    basic_info['id_type'] = generators.id_types_generator(seed=seed)
    basic_info['id_number'] = generators.id_generator(id_type=basic_info['id_type'], seed=seed)
    basic_info['address'] = generators.address_generator(seed=seed)
    basic_info['birthdate'] = generators.birthdate_generator(seed=seed)
    basic_info['city'] = generators.city_generator(seed=seed)
    basic_info['id_expedition_date'] = generators.id_expedition_date_generator(birthdate=basic_info['birthdate'],
                                                                               seed=seed)
    basic_info['marital_status'] = generators.marital_status_generator(seed=seed)
    basic_info['nationality'] = generators.nationality_generator(seed=seed)
    basic_info['phone'] = generators.phone_generator(colombian=True, seed=seed)
    basic_info['id_expedition_place'] = generators.city_generator(seed=seed)
    basic_info['blood_type'] = generators.blood_type_generator(seed=seed)
    basic_info['name'] = generators.name_generator(seed=seed)
    basic_info['genre'] = generators.genre_generator(seed=seed)
    basic_info['position'] = generators.job_generator(seed=seed)
    basic_info['email'] = generators.email_generator(seed=seed)

    data_entry['basic_info'] = basic_info

    # Create basic information group
    social_security = dict()
    social_security['eps'] = {
        'name': generators.eps_generator(seed=seed),
        'isActive': random.choice([True, False]),
        'isContributor': random.choice([True, False])
        }
    social_security['arl'] = {
        'name': generators.arl_generator(seed=seed),
        'isActive': random.choice([True, False]),
        }
    social_security['health_insurance'] = {
        'name': generators.health_insurance_generator(seed=seed),
        'isActive': random.choice([True, False]),
        }

    data_entry['social_security'] = social_security

    # Create laboral information group
    laboral_information = dict()

    laboral_information['leader_information'] = {
        'name': generators.name_generator(),
        'cellphone': generators.phone_generator(),
        'position': generators.job_generator()
        }
    laboral_information['contract_start_date'] = generators.contract_start_date_generator(basic_info['birthdate'],
                                                                                          seed=seed)
    laboral_information['contract_end_date'] = generators.contract_end_date_generator(
        laboral_information['contract_start_date'], seed=seed)
    laboral_information['address'] = generators.address_generator()
    laboral_information['city'] = generators.city_generator()
    laboral_information['phone'] = generators.phone_generator(colombian=True)
    laboral_information['contractType'] = generators.contract_type_generator(seed=seed)
    laboral_information['company'] = generators.company_generator(seed=seed)
    laboral_information['position'] = generators.job_generator()

    data_entry['laboral_information'] = [laboral_information]

    # Create academic information group
    academic_information = dict()

    academic_information['date'] = generators.contract_start_date_generator(basic_info['birthdate'],
                                                                            seed=seed)
    academic_information['city'] = generators.city_generator(seed=seed)
    academic_information['phone'] = generators.phone_generator(colombian=True)
    academic_information['institution'] = generators.institution_generator(seed=seed)
    academic_information['degree'] = generators.degree_generator(seed=seed)
    academic_information['contact_info'] = generators.name_generator(seed=seed)
    academic_information['register'] = generators.id_generator(id_type='CC', seed=seed)

    data_entry['academic_information'] = [academic_information]

    return data_entry


def document_formulario_conocimiento(seed=None) -> Dict:
    """
    This method create a sample for a Document of "Formulario de conocimiento"
    :param int seed: Seed to initialize the random functions.
    :return Dict:
    """
    data_entry = {
        'sg_document_type': 'formulario_conocimiento',
        'sg_create_at': datetime.now().date(),
        'sg_update_at': datetime.now().date(),
        'sg_additional_info': None,
        'form_date': datetime.now().date() - relativedelta(days=random.randint(1, 60)),
        'user_type': random.choice(['cliente', 'proveedor']),
        'format_action': 'vincular',
        'format_info': {'code': 'Sagrilaft', 'version': '1'},
        }

    # Create basic information data
    basic_info = dict()
    basic_info['type'] = random.choice(['natural', 'juridica'])
    basic_info['entity'] = {
        'name': generators.company_generator(seed=seed) if basic_info['type'] == 'juridica'
        else generators.name_generator(seed=seed),
        'id_type': 'NIT' if basic_info['type'] == 'juridica' else 'CC',
        'id': generators.id_generator(id_type='CC', seed=seed)
        }
    legal_representative_id = random.choice(['NIT', 'CC', 'CE'])
    if basic_info['type'] == 'juridica':
        basic_info['legal_representative'] = {
            'name': generators.company_generator() if legal_representative_id == 'NIT'
            else generators.name_generator(),
            'id_type': legal_representative_id,
            'id': generators.id_generator(id_type=legal_representative_id, seed=seed)
            }
    else:
        basic_info['legal_representative'] = {
            'name': None,
            'id_type': None,
            'id': None
            }
    basic_info['address'] = generators.address_generator(seed=seed)
    basic_info['city'] = generators.city_generator(seed=seed)
    basic_info['phone'] = generators.phone_generator(colombian=True, seed=seed)

    basic_info['contact_info'] = {
                                     'name': generators.name_generator() if basic_info['type'] == 'juridica' else
                                     basic_info['entity']['name'],
                                     "position": generators.job_generator(seed=seed),
                                     "email": generators.email_generator(seed=seed),
                                     "phone": [generators.phone_generator(colombian=True, seed=seed)]
                                     },
    basic_info['isPEP'] = random.choice([True, False])
    basic_info['last_position'] = generators.job_generator(seed=seed)

    data_entry['basic_info'] = basic_info

    # Create basic information data
    activity, ciiu = generators.ciiud_generator(seed=seed)

    business_info = {
        "statutory_activity": activity,
        "ciiu": ciiu,
        "joint-document": random.randint(0, 9999),  # TODO: Validate code for juridicas
        "commercial_registration": generators.fake_ES.sha1(raw_output=False) if basic_info[
                                                                                    'type'] == 'juridica' else None,
        "registered_shared_capital": generators.fake_ES.sha1(raw_output=False) if basic_info[
                                                                                      'type'] == 'juridica' else None,
        "constitution_date": generators.birthdate_generator(seed=seed),
        "good_or_service": activity if basic_info['type'] == 'juridica' else None,
        "company_type": random.choice(["Sociedad Anónima", "Sociedad Limitada", "Sociedad en comandita", "Otras"]) if
        basic_info['type'] == 'juridica' else None,
        "sector": random.choice(['Publico', 'Privado', 'Mixto']) if basic_info['type'] == 'juridica' else None,
        }

    data_entry['business_info'] = business_info

    # Create certificates data
    certificates = {
                       "list_of_certificates": random.choice(
                           ['9001', '14001', '18001', ' 27001', 'OEA', 'BASC', 'Otra'])
                       if basic_info['type'] == 'juridica' else None,
                       "in_progress": {
                           "process": None,
                           "percentage_progress": None,
                           "init_date": None
                           }
                       },

    data_entry['certificates'] = certificates

    data_entry['business_type'] = random.choice(['Microempresa', 'Pequeña', 'Mediana', 'Grande']) \
                                      if basic_info['type'] == 'juridica' else None,

    # Create accounting and taxes group
    accounting_and_taxes = dict()
    accounting_and_taxes['isRegimenComun'] = True if basic_info['type'] == 'juridica' else False
    accounting_and_taxes['isRegimenSimplificado'] = False if basic_info['type'] == 'juridica' else random.choice(
        [True, False])
    accounting_and_taxes['isDeclaraRenta'] = True if basic_info['type'] == 'juridica' else random.choice([True, False])
    accounting_and_taxes['isAutoRetenedor'] = random.choice([True, False]) if basic_info[
                                                                                  'type'] == 'juridica' else False
    accounting_and_taxes['isAutoRetenedor'] = random.choice([True, False]) if basic_info[
                                                                                  'type'] == 'juridica' else False
    accounting_and_taxes['payment_terms'] = random.choice(['Contado', '30d0', '60d'])
    accounting_and_taxes['payment_terms_other'] = None

    data_entry['accounting_and_taxes'] = accounting_and_taxes

    # Create legal representatives group
    legal_representatives = []
    if basic_info['type'] == 'juridica':
        for i in range(random.randint(1, 4)):
            id_type = generators.id_types_generator()
            legal_representatives.append({
                'name': generators.name_generator(),
                'id_type': id_type,
                'id_number': generators.id_generator(id_type=id_type),
                'nationality': generators.nationality_generator(),
                })

    data_entry['legal_representatives'] = legal_representatives

    # Create directives group
    directives = []
    if basic_info['type'] == 'juridica':
        for i in range(random.randint(1, 4)):
            id_type = generators.id_types_generator()
            directives.append({
                'name': generators.name_generator(),
                'id_type': id_type,
                'id_number': generators.id_generator(id_type=id_type),
                'nationality': generators.nationality_generator(),
                })
        # Add a legal representative as directive
        if random.random() < 0.6:
            directives.append(random.choice(legal_representatives))

    data_entry['directives'] = directives

    # Create shareholders group
    shareholders = []
    if basic_info['type'] == 'juridica':
        for i in range(random.randint(1, 4)):
            id_type = generators.id_types_generator()
            shareholders.append({
                'name': generators.name_generator(),
                'id_type': id_type,
                'id_number': generators.id_generator(id_type=id_type),
                'nationality': generators.nationality_generator(),
                'isPEP': random.choice([True, False]),
                'share_percentage': 1,
                })

    data_entry['shareholders'] = shareholders

    # Create bank referrals group
    bank_referrals = []
    for i in range(random.randint(0, 4)):
        bank_referrals.append({
            'name': random.choice(['Bancolombia', 'AVillas', 'Finandina']),
            'address': generators.address_generator(),
            'phone': generators.phone_generator(),
            })

    data_entry['bank_referrals'] = bank_referrals

    # Create bank referrals group
    commercial_referrals = []
    if basic_info['type'] == 'juridica':
        for i in range(random.randint(0, 4)):
            commercial_referrals.append({
                'name': generators.company_generator(),
                'address': generators.address_generator(),
                'phone': generators.phone_generator(),
                })

    data_entry['commercial_referrals'] = commercial_referrals

    return data_entry
