#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-01-21 14:24:16
# @Last Modified by:   ritesh
# @Last Modified time: 2016-01-26 14:27:48


""" Mongodb
    Database    :       mapper
    Collections :
            keywords    :   ks
            variables   :   vs
            maps        :   ms
"""

import libmongo

db = libmongo.get_db()

ks_main = {"unique_name": "LIS_OTD 2_5 DEGREE LOW RESOLUTION DIURNAL CLIMATOLOGY (LRDC) V2_3_2013", "short_name": "lolrdc", "keyword_list": ["ATMOSPHERE->ATMOSPHERIC_ELECTRICITY->LIGHTNING"], "long_name": "LIS/OTD 2.5 DEGREE LOW RESOLUTION DIURNAL CLIMATOLOGY (LRDC)", "version": "2.3.2013", "dataset_id": "LIS/OTD 2.5 DEGREE LOW RESOLUTION DIURNAL CLIMATOLOGY (LRDC) V2.3.2013"}
vs_main = ['LRDC_LIS_RF', 'DE Latitude', 'Local Hour', 'LRFC_OTD_DE', 'LRDC_OTD_RF', 'LRDC_OTD_SF', 'LRDC_LIS_SF', 'LRDC_LIS_FR', 'DE Longitude', 'LRDC_OTD_VT', 'DE Local Hour', 'Longitude', 'LRFC_LIS_DE', 'LRDC_COM_FR', 'LRDC_LIS_VT', 'Latitude', 'LRDC_OTD_FR', 'LRDC_AREA', 'DE By Threshold']

v1 = { "unique_name" : "GHRSST Level 2P USA NASA MODIS Aqua SST:1", "variable_list" : [ "latAIRS", "lonAIRS", "TAirStd", "TAirStd_QC", "TAirStdErr", "latAIRS", "lonAIRS", "TAirStd", "TAirStd_QC", "TAirStdErr", "TSurfAir", "TSurfAir_QC", "TSurfAirErr", "GP_Height", "GP_Height_QC", "PTropopause", "PTropopause_QC", "latAIRS", "lonAIRS", "TAirStd", "TAirStd_QC", "TAirStdErr", "TSurfAir", "TSurfAir_QC" ], "dataset_id": "GHRSST Level 2P USA NASA MODIS Aqua SST:1" }
v2 = { "unique_name" : "MODIS_Terra Aerosol 5-Min L2 Swath 10km V005 NRT", "variable_list" : [ "Optical_Depth_Small_Average_Ocean", "Asymmetry_Factor_Best_Ocean", "Angstrom_Exponent_1_Ocean", "Cloud_Fraction_Ocean", "Angstrom_Exponent_2_Ocean", "Effective_Optical_Depth_Best_Ocean", "Mean_Reflectance_Ocean", "Optical_Depth_Small_Best_Ocean", "Critical_Reflectance_Land", "STD_Reflectance_Land", "Solar_Zenith", "STD_Reflectance_Ocean", "Effective_Radius_Ocean", "Latitude", "Sensor_Azimuth", "Aerosol_Cldmask_Byproducts_Land", "Optical_Depth_Ratio_Small_Land_And_Ocean", "Quality_Assurance_Ocean", "Surface_Reflectance_Land", "Fitting_Error_Land", "Sensor_Zenith", "Scan_Start_Time", "Image_Optical_Depth_Land_And_Ocean", "Mean_Reflectance_Land_All", "Effective_Optical_Depth_Average_Ocean", "Optical_Depth_Large_Average_Ocean", "Mass_Concentration_Land", "Cloud_Fraction_Land", "Optical_Depth_Small_Land", "Aerosol_Cldmask_Byproducts_Ocean", "Optical_Depth_Large_Best_Ocean", "Corrected_Optical_Depth_Land_wav2p1", "Error_Path_Radiance_Land", "Quality_Assurance_Crit_Ref_Land", "Backscattering_Ratio_Average_Ocean", "Deep_Blue_Mean_Reflectance_Land", "Solution_Index_Ocean_Small", "Deep_Blue_Number_Pixels_Used_Land", "Deep_Blue_Aerosol_Optical_Depth_Land_STD", "Asymmetry_Factor_Average_Ocean", "Longitude", "Deep_Blue_Angstrom_Exponent_Land", "Angstrom_Exponent_Land", "QualityWeight_Critical_Reflectance_Land", "Solar_Azimuth", "Backscattering_Ratio_Best_Ocean", "Cloud_Mask_QA", "Corrected_Optical_Depth_Land", "Least_Squares_Error_Ocean", "Deep_Blue_Aerosol_Optical_Depth_Land", "Scattering_Angle", "Aerosol_Type_Land", "Optical_Depth_Ratio_Small_Ocean_0.55micron", "Mass_Concentration_Ocean", "Mean_Reflectance_Land", "Deep_Blue_Single_Scattering_Albedo_Land", "QualityWeight_Path_Radiance_Land", "Quality_Assurance_Land", "Deep_Blue_Surface_Reflectance_Land", "Path_Radiance_Land", "Deep_Blue_Aerosol_Optical_Depth_550_Land", "Error_Critical_Reflectance_Land", "Cloud_Condensation_Nuclei_Ocean", "Optical_Depth_Land_And_Ocean", "Number_Pixels_Used_Ocean", "Deep_Blue_Aerosol_Optical_Depth_550_Land_STD", "Standard_Deviation_Reflectance_Land_All", "Optical_Depth_Ratio_Small_Land", "Solution_Index_Ocean_Large", "Number_Pixels_Used_Land", "Optical_Depth_by_models_ocean" ], "dataset_id": "MODIS/Terra Aerosol 5-Min L2 Swath 10km V005 NRT" }
v3 = { "unique_name" : "AIRS_Aqua Level 2 Support retrieval (AIRS+AMSU) V005", "variable_list" : [ "GP_Height_QC", "HingeSurf:L2_Standard_atmospheric&surface_product", "ftptgeoqa", "O3VMRLevStdErr", "emisIRStdErr", "CH4_verticality_10func", "TSurfAirErr", "num_CH4_Func", "H2OMMRSatSurf_QC", "topog", "CH4_total_column_QC", "H2O_verticality", "CldFrcTot_QC", "totO3Std", "H2OMMRLevStdErr", "AIRSTrack:L2_Standard_atmospheric&surface_product", "num_CO_Func", "totH2OStd_QC", "totH2OStdErr", "TSurfAir_QC", "num_H2O_Func", "H2OMMRSatLevStd_liquid_QC", "GP_Tropopause_QC", "Longitude", "PBest", "H2OMMRLevStd_QC", "CldFrcStd", "PTropopause_QC", "H2OMMRLevStd", "PSurfStd_QC", "sfcTbMWStd_QC", "CH4VMRLevStdErr", "CH4_total_column", "H2OPressureLev:L2_Standard_atmospheric&surface_product", "GP_Surface_QC", "H2O_dof", "CO_total_column", "O3VMRLevStd_QC", "TSurfStd", "olr_QC", "EmisMWStd", "solzen", "latAIRS", "TAirMWOnlyStd", "MWSurfClass", "GP_Height", "olr", "H2OMMRSat", "RelHum_liquid", "Latitude", "O3VMRLevStd", "totCldH2OStd_QC", "TSurfAir", "H2OMMRSurf", "H2OMMRSatLevStd_QC", "H2OMMRStd_QC", "GP_Tropopause", "CH4_dof", "TSurfStdErr", "H2OMMRSatSurf_liquid_QC", "olr3x3_QC", "solazi", "emisIRStd_QC", "COVMRLevStd", "GP_Height_MWOnly_QC", "T_Tropopause_QC", "CldFrcStdErr", "TSurfStd_QC", "CldFrcTot", "RelHum", "clrolr_err", "H2OMMRSurfErr", "StdPressureLay:L2_Standard_atmospheric&surface_product", "H2OMMRSatSurf", "satzen", "RelHum_QC", "zengeoqa", "totH2OStd", "O3_dof", "landFrac_err", "H2OMMRSat_liquid_QC", "AIRSXTrack:L2_Standard_atmospheric&surface_product", "H2OMMRSatLevStd_liquid", "sfcTbMWStd", "PGood", "totCldH2OStdErr", "num_O3_Func", "RelHumSurf_liquid_QC", "olr_err", "PSurfStd", "EmisMWStdErr", "landFrac", "TCldTop_QC", "CO_dof", "H2OMMRSurf_QC", "TAirMWOnlyStd_QC", "PTropopause", "COVMRLevStd_QC", "CldFrcStd_QC", "SurfClass", "RelHumSurf", "totO3StdErr", "H2OPressureLay:L2_Standard_atmospheric&surface_product", "RelHum_liquid_QC", "dust_flag", "TAirStdErr", "GP_Surface", "CH4VMRLevStd", "PCldTop", "MWHingeSurf:L2_Standard_atmospheric&surface_product", "TAirStd", "PCldTop_QC", "COVMRLevStdErr", "RelHumSurf_QC", "GeoXTrack:L2_Standard_atmospheric&surface_product", "H2OMMRSat_liquid", "O3VMRStdErr", "Time", "totCldH2OStd", "Cloud:L2_Standard_atmospheric&surface_product", "nGoodStd", "nBestStd", "totO3Std_QC", "EmisMWStd_QC", "O3VMRStd_QC", "TAirStd_QC", "H2OMMRSat_QC", "H2OMMRSatSurf_liquid", "nCld", "nSurfStd", "O3VMRStd", "CH4VMRLevStd_QC", "CO_verticality", "totH2OMWOnlyStd_QC", "H2OMMRStd", "clrolr_QC", "clrolr", "totH2OMWOnlyStd", "sun_glint_distance", "H2OMMRStdErr", "olr3x3", "TCldTopErr", "H2OMMRSatLevStd", "GeoTrack:L2_Standard_atmospheric&surface_product", "CO_total_column_QC", "MW_ret_used", "RelHumSurf_liquid", "O3_verticality", "satazi", "Temp_dof", "emisIRStd", "freqEmis", "all_spots_avg", "numHingeSurf", "T_Tropopause", "PCldTopErr", "GP_Height_MWOnly", "TCldTop", "retrieval_type", "topog_err", "lonAIRS", "demgeoqa", "StdPressureLev:L2_Standard_atmospheric&surface_product" ], "dataset_id": "AIRS/Aqua Level 2 Support retrieval (AIRS+AMSU) V005" }
v4 = { "unique_name" : "MODIS_Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km V005", "variable_list" : [ "Water_Vapor_High", "Processing_Flag", "Total_Ozone", "K_Index", "Brightness_Temperature", "Guess_Moisture_Profile", "Solar_Zenith", "Retrieved_Moisture_Profile", "Latitude", "Sensor_Azimuth", "Retrieved_Temperature_Profile", "Scan_Start_Time", "Lifted_Index", "Water_Vapor_Direct", "Total_Totals", "Quality_Assurance_Infrared", "Tropopause_Height", "Surface_Elevation", "Water_Vapor_Low", "Longitude", "Guess_Temperature_Profile", "Surface_Temperature", "Water_Vapor", "Sensor_Zenith", "Solar_Azimuth", "Quality_Assurance", "Retrieved_Height_Profile", "Cloud_Mask", "Surface_Pressure" ], "dataset_id": "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km V005" }


k1 = {"unique_name": "GHRSST Level 2P USA NASA MODIS Aqua SST:1", "short_name": "GHRSST LEVEL 2P USA NASA MODIS AQUA SST", "keyword_list": ["OCEANS->OCEAN_OPTICS->OCEAN_COLOR", "OCEANS->OCEAN_TEMPERATURE->SEA_SURFACE_TEMPERATURE"], "long_name": "GHRSST L2P Skin Sea Surface Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite", "version": "1", "dataset_id": "GHRSST Level 2P USA NASA MODIS Aqua SST:1"}
k2 = {"unique_name": "AIRS_Aqua Level 2 Support retrieval (AIRS+AMSU) V005", "short_name": "AIRX2SUP", "keyword_list": ["ATMOSPHERE->AIR_QUALITY->CARBON_MONOXIDE", "ATMOSPHERE->AIR_QUALITY->TROPOSPHERIC_OZONE", "ATMOSPHERE->ALTITUDE->GEOPOTENTIAL_HEIGHT", "ATMOSPHERE->ALTITUDE->TROPOPAUSE", "ATMOSPHERE->ATMOSPHERIC_TEMPERATURE->SURFACE_AIR_TEMPERATURE", "ATMOSPHERE->ATMOSPHERIC_TEMPERATURE->TEMPERATURE_PROFILES", "ATMOSPHERE->ATMOSPHERIC_WATER_VAPOR->PRECIPITABLE_WATER", "ATMOSPHERE->ATMOSPHERIC_WATER_VAPOR->WATER_VAPOR_PROFILES", "ATMOSPHERE->CLOUDS->CLOUD_AMOUNT/FREQUENCY", "ATMOSPHERE->CLOUDS->CLOUD_TOP_PRESSURE", "ATMOSPHERE->CLOUDS->CLOUD_TOP_TEMPERATURE", "ATMOSPHERE->PRECIPITATION->PRECIPITATION_RATE", "ATMOSPHERE->ATMOSPHERIC_RADIATION->OUTGOING_LONGWAVE_RADIATION", "LAND_SURFACE->LAND_TEMPERATURE->SKIN_TEMPERATURE", "LAND_SURFACE->SURFACE_RADIATIVE_PROPERTIES->EMISSIVITY", "OCEANS->OCEAN_TEMPERATURE->SEA_SURFACE_TEMPERATURE", "ATMOSPHERE->ATMOSPHERIC_CHEMISTRY->CARBON_AND_HYDROCARBON_COMPOUNDS", "ATMOSPHERE->ATMOSPHERIC_CHEMISTRY->METHANE", "ATMOSPHERE->ATMOSPHERIC_CHEMISTRY->SULFUR_COMPOUNDS", "ATMOSPHERE->ATMOSPHERIC_CHEMISTRY->SULFUR_DIOXIDE", "CLIMATE_INDICATORS->ATMOSPHERIC/OCEAN_INDICATORS->TEMPERATURE_INDICES"], "long_name": "AIRS/Aqua Level 2 Support retrieval (AIRS+AMSU)", "version": "005", "dataset_id": "AIRS/Aqua Level 2 Support retrieval (AIRS+AMSU) V005"}
k3 = {"unique_name": "MODIS_Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km V005", "short_name": "MOD07_L2", "keyword_list": ["ATMOSPHERE->ATMOSPHERIC_CHEMISTRY/OXYGEN_COMPOUNDS->OZONE", "ATMOSPHERE->ATMOSPHERIC_TEMPERATURE->AIR_TEMPERATURE", "ATMOSPHERE->ATMOSPHERIC_TEMPERATURE->ATMOSPHERIC_STABILITY", "ATMOSPHERE->ATMOSPHERIC_WATER_VAPOR->DEW_POINT", "ATMOSPHERE->ATMOSPHERIC_WATER_VAPOR->HUMIDITY", "ATMOSPHERE->ATMOSPHERIC_WATER_VAPOR->PRECIPITABLE_WATER"], "long_name": "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km", "version": "5", "dataset_id": "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km V005"}
k4 = {"unique_name": "MODIS_Terra Aerosol 5-Min L2 Swath 10km V005 NRT", "short_name": "MOD04_L2", "keyword_list": ["ATMOSPHERE->AEROSOLS->AEROSOL_PARTICLE_PROPERTIES", "ATMOSPHERE->AEROSOLS->CLOUD_CONDENSATION_NUCLEI", "ATMOSPHERE->AEROSOLS->AEROSOL_EXTINCTION", "ATMOSPHERE->AEROSOLS->AEROSOLS_OPTICAL_DEPTH/THICKNESS", "ATMOSPHERE->AEROSOLS->AEROSOL_RADIANCE", "ATMOSPHERE->AEROSOLS->CARBONACEOUS_AEROSOLS", "ATMOSPHERE->AEROSOLS->DUST/ASH/SMOKE", "ATMOSPHERE->AEROSOLS->NITRATE_PARTICLES", "ATMOSPHERE->AEROSOLS->ORGANIC_PARTICLES", "ATMOSPHERE->AEROSOLS->PARTICULATE_MATTER", "ATMOSPHERE->AEROSOLS->SULFATE_PARTICLES", "ATMOSPHERE->ATMOSPHERIC_RADIATION->RADIATIVE_FLUX", "ATMOSPHERE->ATMOSPHERIC_RADIATION->REFLECTANCE", "ATMOSPHERE->ATMOSPHERIC_RADIATION->OPTICAL_DEPTH/THICKNESS"], "long_name": "MODIS/Terra Aerosol 5-Min L2 Swath 10km", "version": "5", "dataset_id": "MODIS/Terra Aerosol 5-Min L2 Swath 10km V005 NRT"}


def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def temp_sanitize_names():
	keywords_docs = db.ks.find()
	for keywords_doc in keywords_docs:
		db.ks.update({"dataset_id":keywords_doc["dataset_id"]}, {"$set": {"unique_name": sanitize(keywords_doc["dataset_id"])}})
	print "Ks update complete"

	variables_docs = db.vs.find()
	for variables_doc in variables_docs:
		db.vs.update({"dataset_id":variables_doc["dataset_id"]}, {"$set": {"unique_name": sanitize(variables_doc["dataset_id"])}})
	print "vs update complete"

	maps_docs = db.ms.find()
	for maps_doc in maps_docs:
		db.ms.update({"dataset_id":maps_doc["dataset_id"]}, {"$set": {"unique_name": sanitize(maps_doc["dataset_id"])}})
	print "ms update complete"



def insert_variables(variables):
	db.vs.insert(variables)
	print "variables insert completed."


def insert_keywords(keywords):
	db.ks.insert(keywords)
	print "Keywords insert completed."


def insert():
	unique_name = sanitize(ks_main.get("dataset_id"))
	to_insert_ks = ks_main
	to_insert_ks["unique_name"] = unique_name

	to_insert_vs = {}
	to_insert_vs["unique_name"] = unique_name
	to_insert_vs["dataset_id"] = ks_main["dataset_id"]
	to_insert_vs["variable_list"] = vs_main

	print "TO INSERT ..."
	print to_insert_vs
	print to_insert_ks

	insert_keywords(to_insert_ks)
	insert_variables(to_insert_vs)

	print "Insert completed"

def main():
	# temp_sanitize_names()
	# insert_keywords([k1, k2, k3, k4])
	# insert_variables([v1, v2, v3, v4])
	# insert()
	pass

if __name__ == '__main__':
	main()