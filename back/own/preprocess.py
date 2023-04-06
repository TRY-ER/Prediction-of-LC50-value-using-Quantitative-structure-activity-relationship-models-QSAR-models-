import joblib
import pandas as pd
import os


def Preprocess(data):
    cols = [ x[0] for x in data]
    col_val = [ x[1] for x in data]
    dataframe_list = ['Cell_area_measured_numeric',
                    'Cell_architecture_cat',
                    'Substrate_stack_sequence_0',
                    'Substrate_stack_sequence_1',
                    'Substrate_stack_sequence_2',
                    'Substrate_stack_sequence_3',
                    'Substrate_stack_sequence_4',
                    'ETL_stack_sequence_0',
                    'ETL_stack_sequence_1',
                    'ETL_stack_sequence_2',
                    'ETL_stack_sequence_3',
                    'ETL_stack_sequence_4',
                    'ETL_stack_sequence_5',
                    'ETL_stack_sequence_6',
                    'ETL_deposition_procedure_0',
                    'ETL_deposition_procedure_1',
                    'ETL_deposition_procedure_2',
                    'ETL_deposition_procedure_3',
                    'ETL_deposition_procedure_4',
                    'ETL_deposition_procedure_5',
                    'ETL_deposition_procedure_6',
                    'Perovskite_composition_a_ions_0',
                    'Perovskite_composition_a_ions_1',
                    'Perovskite_composition_a_ions_2',
                    'Perovskite_composition_a_ions_3',
                    'Perovskite_composition_a_ions_coefficients_0',
                    'Perovskite_composition_a_ions_coefficients_1',
                    'Perovskite_composition_a_ions_coefficients_2',
                    'Perovskite_composition_a_ions_coefficients_3',
                    'Perovskite_composition_b_ions_0',
                    'Perovskite_composition_b_ions_1',
                    'Perovskite_composition_b_ions_2',
                    'Perovskite_composition_b_ions_3',
                    'Perovskite_composition_b_ions_coefficients_0',
                    'Perovskite_composition_b_ions_coefficients_1',
                    'Perovskite_composition_b_ions_coefficients_2',
                    'Perovskite_composition_b_ions_coefficients_3',
                    'Perovskite_composition_c_ions_0',
                    'Perovskite_composition_c_ions_1',
                    'Perovskite_composition_c_ions_2',
                    'Perovskite_composition_c_ions_3',
                    'Perovskite_composition_c_ions_coefficients_0',
                    'Perovskite_composition_c_ions_coefficients_1',
                    'Perovskite_composition_c_ions_coefficients_2',
                    'Perovskite_composition_c_ions_coefficients_3',
                    'Perovskite_composition_leadfree_bool',
                    'Perovskite_band_gap_graded_bool',
                    'Perovskite_deposition_number_of_deposition_steps_numeric',
                    'Perovskite_deposition_procedure_0',
                    'Perovskite_deposition_procedure_1',
                    'Perovskite_deposition_procedure_2',
                    'Perovskite_deposition_procedure_3',
                    'Perovskite_deposition_procedure_4',
                    'Perovskite_deposition_procedure_5',
                    'Perovskite_deposition_aggregation_state_of_reactants_0',
                    'Perovskite_deposition_aggregation_state_of_reactants_1',
                    'Perovskite_deposition_aggregation_state_of_reactants_2',
                    'Perovskite_deposition_aggregation_state_of_reactants_3',
                    'Perovskite_deposition_aggregation_state_of_reactants_4',
                    'Perovskite_deposition_aggregation_state_of_reactants_5',
                    'Perovskite_deposition_synthesis_atmosphere_0',
                    'Perovskite_deposition_synthesis_atmosphere_1',
                    'Perovskite_deposition_solvents_0',
                    'Perovskite_deposition_solvents_1',
                    'Perovskite_deposition_solvents_2',
                    'Perovskite_deposition_solvents_3',
                    'Perovskite_deposition_solvents_4',
                    'Perovskite_deposition_solvents_5',
                    'Perovskite_deposition_solvents_mixing_ratios_0',
                    'Perovskite_deposition_solvents_mixing_ratios_1',
                    'Perovskite_deposition_solvents_mixing_ratios_2',
                    'Perovskite_deposition_solvents_mixing_ratios_3',
                    'Perovskite_deposition_solvents_mixing_ratios_4',
                    'Perovskite_deposition_solvents_mixing_ratios_5',
                    'Perovskite_deposition_quenching_induced_crystallisation_bool',
                    'Perovskite_deposition_thermal_annealing_temperature_0',
                    'Perovskite_deposition_thermal_annealing_temperature_1',
                    'Perovskite_deposition_thermal_annealing_time_0',
                    'Perovskite_deposition_thermal_annealing_time_1',
                    'HTL_stack_sequence_0',
                    'HTL_stack_sequence_1',
                    'HTL_stack_sequence_2',
                    'HTL_additives_compounds_0',
                    'HTL_additives_compounds_1',
                    'HTL_additives_compounds_2',
                    'HTL_additives_compounds_3',
                    'HTL_additives_compounds_4',
                    'HTL_deposition_procedure_0',
                    'HTL_deposition_procedure_1',
                    'HTL_deposition_procedure_2',
                    'HTL_deposition_procedure_3',
                    'HTL_deposition_procedure_4',
                    'HTL_deposition_procedure_5',
                    'Backcontact_stack_sequence_0',
                    'Backcontact_stack_sequence_1',
                    'Backcontact_stack_sequence_2',
                    'Backcontact_stack_sequence_3',
                    'Backcontact_stack_sequence_4',
                    'Backcontact_thickness_list_0',
                    'Backcontact_thickness_list_1',
                    'Backcontact_deposition_procedure_0',
                    'Backcontact_deposition_procedure_1',
                    'Encapsulation_bool'
]
    dataframe_dict = {}
    for key in dataframe_list:
        if key in cols:
            dataframe_dict[key] = [col_val[cols.index(key)]]
        else:
            dataframe_dict[key] = [0]
    # for key,val in zip(dataframe_list,data):
    #     dataframe_dict[key] = [val[1]]
    predict_df = pd.DataFrame(dataframe_dict)
    encoders = os.listdir("./encoders")
    exclude_lbl_enc = lambda x : x[:-2]
    enc = list(map(exclude_lbl_enc,encoders))
    mod_df = predict_df.copy()
    for col in predict_df.columns:
        if col in enc:
            lbl_enc = joblib.load(f"./encoders/{col}.z")
            mod_df[col] = lbl_enc.transform(mod_df[col])
    standard_scaler = joblib.load("./scaler/std_scaler.z")
    mod_df = standard_scaler.transform(mod_df)
    mod_df = pd.DataFrame(mod_df,columns=predict_df.columns)
    print(mod_df)
    return mod_df


#testing 
# data = [['Cell_area_measured_numeric', '0.0004'], ['Cell_architecture_cat', 'nip'], ['Substrate_stack_sequence_0', 'SLG'], ['Substrate_stack_sequence_1', 'FTO'], ['Substrate_stack_sequence_2', 'None'], ['Substrate_stack_sequence_3', 'None'], ['Substrate_stack_sequence_4', 'None'], ['ETL_stack_sequence_0', 'TiO2-c'], ['ETL_stack_sequence_1', 'TiO2-mp'], ['ETL_stack_sequence_2', 'None'], ['ETL_stack_sequence_3', 'None'], ['ETL_stack_sequence_4', 'None'], ['ETL_stack_sequence_5', 'None'], ['ETL_stack_sequence_6', 'None'], ['ETL_deposition_procedure_0', 'Spray-pyrolys'], ['ETL_deposition_procedure_1', 'Spin-coating'], ['ETL_deposition_procedure_2', 'None'], ['ETL_deposition_procedure_3', 'None'], ['ETL_deposition_procedure_4', 'None'], ['ETL_deposition_procedure_5', 'None'], ['ETL_deposition_procedure_6', 'None'], ['Perovskite_composition_a_ions_0', 'Cs'], ['Perovskite_composition_a_ions_1', 'None'], ['Perovskite_composition_a_ions_2', 'None'], ['Perovskite_composition_a_ions_3', 'None'], ['Perovskite_composition_a_ions_coefficients_0', '0.005'], ['Perovskite_composition_a_ions_coefficients_1', '0'], ['Perovskite_composition_a_ions_coefficients_2', '0'], ['Perovskite_composition_a_ions_coefficients_3', '0'], ['Perovskite_composition_b_ions_0', 'Sn'], ['Perovskite_composition_b_ions_1', 'None'], ['Perovskite_composition_b_ions_2', 'None'], ['Perovskite_composition_b_ions_3', 'None'], ['Perovskite_composition_b_ions_coefficients_0', '0'], ['Perovskite_composition_b_ions_coefficients_1', '0'], ['Perovskite_composition_b_ions_coefficients_2', '0'], ['Perovskite_composition_b_ions_coefficients_3', '0'], ['Perovskite_composition_c_ions_0', 'I'], ['Perovskite_composition_c_ions_1', 'None'], ['Perovskite_composition_c_ions_2', 'None'], ['Perovskite_composition_c_ions_3', 'None'], ['Perovskite_composition_c_ions_coefficients_0', '-4.44e-16'], ['Perovskite_composition_c_ions_coefficients_1', '0'], ['Perovskite_composition_c_ions_coefficients_2', '0'], ['Perovskite_composition_c_ions_coefficients_3', '0'], ['Perovskite_composition_leadfree_bool', 'Yes'], ['Perovskite_band_gap_graded_bool', 'No'], ['Perovskite_deposition_number_of_deposition_steps_numeric', '0'], ['Perovskite_deposition_procedure_0', 'Space-limited inverse temperature crystallization'], ['Perovskite_deposition_procedure_1', 'Ultrasonic spray'], ['Perovskite_deposition_procedure_2', 'None'], ['Perovskite_deposition_procedure_3', 'None'], ['Perovskite_deposition_procedure_4', 'None'], ['Perovskite_deposition_procedure_5', 'None'], ['Perovskite_deposition_aggregation_state_of_reactants_0', 'Liquid'], ['Perovskite_deposition_aggregation_state_of_reactants_1', 'None'], ['Perovskite_deposition_aggregation_state_of_reactants_2', 'None'], ['Perovskite_deposition_aggregation_state_of_reactants_3', 'None'], ['Perovskite_deposition_aggregation_state_of_reactants_4', 'None'], ['Perovskite_deposition_aggregation_state_of_reactants_5', 'None'], ['Perovskite_deposition_synthesis_atmosphere_0', 'N2'], ['Perovskite_deposition_synthesis_atmosphere_1', 'None'], ['Perovskite_deposition_solvents_0', 'DMSO'], ['Perovskite_deposition_solvents_1', 'None'], ['Perovskite_deposition_solvents_2', 'None'], ['Perovskite_deposition_solvents_3', 'None'], ['Perovskite_deposition_solvents_4', 'None'], ['Perovskite_deposition_solvents_5', 'None'], ['Perovskite_deposition_solvents_mixing_ratios_0', '1'], ['Perovskite_deposition_solvents_mixing_ratios_1', '0'], ['Perovskite_deposition_solvents_mixing_ratios_2', '0'], ['Perovskite_deposition_solvents_mixing_ratios_3', '0'], ['Perovskite_deposition_solvents_mixing_ratios_4', '0'], ['Perovskite_deposition_solvents_mixing_ratios_5', '0'], ['Perovskite_deposition_quenching_induced_crystallisation_bool', 'No'], ['Perovskite_deposition_thermal_annealing_temperature_0', '0'], ['Perovskite_deposition_thermal_annealing_temperature_1', '0'], ['Perovskite_deposition_thermal_annealing_time_0', '-3.55e-15'], ['Perovskite_deposition_thermal_annealing_time_1', '0'], ['HTL_stack_sequence_0', 'Selenium'], ['HTL_stack_sequence_1', 'None'], ['HTL_stack_sequence_2', 'None'], ['HTL_additives_compounds_0', 'Li(CF3SO2)2N'], ['HTL_additives_compounds_1', 'TBP'], ['HTL_additives_compounds_2', 'None'], ['HTL_additives_compounds_3', 'None'], ['HTL_additives_compounds_4', 'None'], ['HTL_deposition_procedure_0', 'Spin-coating'], ['HTL_deposition_procedure_1', 'None'], ['HTL_deposition_procedure_2', 'None'], ['HTL_deposition_procedure_3', 'None'], ['HTL_deposition_procedure_4', 'None'], ['HTL_deposition_procedure_5', 'None'], ['Backcontact_stack_sequence_0', 'Au'], ['Backcontact_stack_sequence_1', 'None'], ['Backcontact_stack_sequence_2', 'None'], ['Backcontact_stack_sequence_3', 'None'], ['Backcontact_stack_sequence_4', 'None'], ['Backcontact_thickness_list_0', '0.5'], ['Backcontact_thickness_list_1', '0'], ['Backcontact_deposition_procedure_0', 'Evaporation'], ['Backcontact_deposition_procedure_1', 'None'], ['Encapsulation_bool', 'No']]
# value = preprocess(data)
# print(value)
