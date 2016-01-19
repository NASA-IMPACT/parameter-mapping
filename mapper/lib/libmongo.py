#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-22 12:06:24
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-22 14:19:17

""" Mongodb
    Database    :       mapper
    Collections :
            keywords    :   ks
            variables   :   vs
            maps        :   ms
"""

from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost', 27017)
    db = client.mapper      # mapper collection
    return db


def insert_test_keywords(db):
    k1 = {"keyword_list": ["ATMOSPHERE->AEROSOLS->AEROSOLPARTICLEPROPERTIES", "ATMOSPHERE->AEROSOLS->CLOUDCONDENSATIONNUCLEI", "ATMOSPHERE->AEROSOLS->AEROSOLEXTINCTION", "ATMOSPHERE->AEROSOLS->AEROSOLSOPTICALDEPTH/THICKNESS", "ATMOSPHERE->AEROSOLS->AEROSOLRADIANCE", "ATMOSPHERE->AEROSOLS->CARBONACEOUSAEROSOLS", "ATMOSPHERE->AEROSOLS->DUST/ASH/SMOKE", "ATMOSPHERE->AEROSOLS->NITRATEPARTICLES", "ATMOSPHERE->AEROSOLS->ORGANICPARTICLES", "ATMOSPHERE->AEROSOLS->PARTICULATEMATTER", "ATMOSPHERE->AEROSOLS->SULFATEPARTICLES", "ATMOSPHERE->ATMOSPHERICRADIATION->RADIATIVEFLUX", "ATMOSPHERE->ATMOSPHERICRADIATION->REFLECTANCE", "ATMOSPHERE->ATMOSPHERICRADIATION->OPTICALDEPTH/THICKNESS"], "long_name": "MODIS/Terra Aerosol 5-Min L2 Swath 10km", "dataset_id": "MODIS/Terra Aerosol 5-Min L2 Swath 10km V005 NRT", "version": "5", "short_name": "MOD04_L2"}
    k2 = {"keyword_list": ["OCEANS->OCEANOPTICS->OCEANCOLOR", "OCEANS->OCEANTEMPERATURE->SEASURFACETEMPERATURE"], "long_name": "GHRSST L2P Skin Sea Surface Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite", "dataset_id": "GHRSST Level 2P USA NASA MODIS Aqua SST:1", "version": "1", "short_name": "GHRSST LEVEL 2P USA NASA MODIS AQUA SST"}
    k3 = {"keyword_list": ["ATMOSPHERE->CLOUDS->CLOUDAMOUNT/FREQUENCY", "ATMOSPHERE->CLOUDS->CLOUDHEIGHT", "ATMOSPHERE->CLOUDS->CLOUDVERTICALDISTRIBUTION"], "long_name": "SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native)", "dataset_id": "SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native) V003", "version": "3", "short_name": "g3acldb"}
    k4 = {"keyword_list": ["LANDSURFACE->TOPOGRAPHY->TERRAINELEVATION", "HYDROSPHERE->GLACIERS/ICESHEETS->GLACIERELEVATION/ICESHEETELEVATION", "CRYOSPHERE->GLACIERS/ICESHEETS->GLACIERELEVATION/ICESHEETELEVATION"], "long_name": "GLAS/ICESat L1B Global Waveform-based Range Corrections Data", "dataset_id": "GLAS/ICESat L1B Global Waveform-based Range Corrections Data V034", "version": "34", "short_name": "GLA05"}
    k5 = {"keyword_list": ["ATMOSPHERE->AEROSOLS->AEROSOLEXTINCTION", "ATMOSPHERE->AEROSOLS->AEROSOLEXTINCTION", "ATMOSPHERE->AEROSOLS->AEROSOLRADIANCE", "ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE", "ATMOSPHERE->AIRQUALITY->NITROGENOXIDES", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->TRACEGASES/TRACESPECIES", "ATMOSPHERE->ATMOSPHERICTEMPERATURE->AIRTEMPERATURE", "ATMOSPHERE->ATMOSPHERICWATERVAPOR->HUMIDITY", "ATMOSPHERE->ATMOSPHERICWATERVAPOR->WATERVAPOR", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONANDHYDROCARBONCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONDIOXIDE", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONANDHYDROCARBONCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONMONOXIDE", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONANDHYDROCARBONCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->METHANE", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROGENCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROGENDIOXIDE", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROGENCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROGENOXIDES", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROGENCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->NITROUSOXIDE", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->OXYGENCOMPOUNDS", "ATMOSPHERE->ATMOSPHERICCHEMISTRY->OZONE"], "long_name": "UARS Improved Stratospheric and Mesospheric Sounder (ISAMS) Level 3AL", "dataset_id": "UARS Improved Stratospheric and Mesospheric Sounder (ISAMS) Level 3AL V001", "version": "001", "short_name": "UARIS3AL"}

    airs = {"keyword_list": ["ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE",
    "ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE",
    "ATMOSPHERE->ALTITUDE->GEOPOTENTIALHEIGHT",
    "ATMOSPHERE->ALTITUDE->TROPOPAUSE",], "long_name": "Very SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native)", "dataset_id": "Rp SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native) V003", "version": "33", "short_name": "ritesh"}

    # db.ks.insert_one(k1)
    db.ks.insert_one(k2)
    db.ks.insert_one(airs)


def insert_test_variables(db):
    al = ["latAIRS",
    "lonAIRS",
    "TAirStd",
    "TAirStd_QC",
    "TAirStdErr",

    "latAIRS",
    "lonAIRS",
    "TAirStd",
    "TAirStd_QC",
    "TAirStdErr",
    "TSurfAir",
    "TSurfAir_QC",
    "TSurfAirErr",

    "GP_Height",
    "GP_Height_QC",

    "PTropopause",
    "PTropopause_QC",

    "latAIRS",
    "lonAIRS",
    "TAirStd",
    "TAirStd_QC",
    "TAirStdErr",
    "TSurfAir",
    "TSurfAir_QC"]

    vl = ["lonAIRS",
    "TAirStd",
    "TAirStd_QC",
    "TAirStdErr",
    "TSurfAir",
    "TSurfAir_QC",
    "TSurfAirErr",
    ]

    airs = {"name": "Very SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native)", "variable_list": al}
    v1 = {"name": "GHRSST L2P Skin Sea Surface Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite", "variable_list": vl}

    db.vs.insert_one(airs)
    db.vs.insert_one(v1)

def insert_test_maps(db):
    kva = {"ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE": ["latAIRS",
    "lonAIRS",
    "TAirStd",
    "TAirStd_QC"],

    "ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE": ["TAirStd_QC",
    "TAirStdErr",
    "TSurfAir"],

    "ATMOSPHERE->ALTITUDE->GEOPOTENTIALHEIGHT" : ["PTropopause",
    "PTropopause_QC"],
    }

    vka = {
        "latAIRS": ["ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE"],
        "TAirStd_QC": ["ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE", "ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE"]
    }


    kv1 = {
    "OCEANS->OCEANOPTICS->OCEANCOLOR": ["TAirStd_QC",
    "TAirStdErr",
    "TSurfAir"],
    "OCEANS->OCEANTEMPERATURE->SEASURFACETEMPERATURE": ["TAirStd",
    "TAirStd_QC",
    "TAirStdErr"]
    }
    vk1 ={
        "TAirStdErr": ["OCEANS->OCEANOPTICS->OCEANCOLOR", "OCEANS->OCEANTEMPERATURE->SEASURFACETEMPERATURE"]
    }

    airs_map = {
        "name": "Very SAGE III Meteor-3M L2 Monthly Cloud Presence Data (Native)",
        "kv": kva,
        "vk": vka
    }
    m1 = {
        "name": "GHRSST L2P Skin Sea Surface Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite",
        "kv": kv1,
        "vk": vk1
    }

    db.ms.insert_one(airs_map)
    db.ms.insert_one(m1)

def main():
    db = get_db()

    insert_test_keywords(db)
    # insert_test_variables(db)
    # insert_test_maps(db)

if __name__ == '__main__':
    main()

# db.keywords.insert_one(name_keywords_dict)