import pandas as pd
from math import sqrt

def get_inputs():
    while True:
        try:
            current = float(input("Enter the load in Amps: "))
            volts = float(input("Enter the the Voltage: "))
            length = float(input("Enter the length of the run in metres: "))
            phase = int(input("Enter phase (1 for single-phase, 3 for 3-phase): "))
            if current > 0 and volts > 0 and length > 0 and (phase in (1, 3)):
                return current, volts, length, phase
            elif phase not in (1, 3):
                raise ValueError
            print("Numbers must be greater than 0")
        except ValueError:
            print("Please enter valid numbers.")

def get_OhmsPer_M(current, volts, length, phase):
    volt_drop = volts * 0.03
    if phase == 1:        
        ohmPer_m = volt_drop/(2 * current * length)
    elif phase == 3:
        ohmPer_m = volt_drop/(sqrt(3) * current * length)
    print(f'Maximum ohms per meter for {length} = {ohmPer_m}')
    return(ohmPer_m)

def get_minimum_cable(ohmPer_m, dataframe):
    safe_cables = df[df['Copper_OhmsPer_m'] <= ohmPer_m]
    if safe_cables.empty:
        print("No cable large enough in current database")
    else:
        min_cable = safe_cables.iloc[0]['CrossSection_mm2']
        print(f"Minimum cable required to stay within 3% voltage drop is {min_cable}mm")


df = pd.read_csv('Cable calculator/copper&aluminium_values.csv')
df.rename(columns={'Copper_OhmsPerKm': 'Copper_OhmsPer_m', 'Aluminum_OhmsPerKm': 'Aluminum_OhmsPer_m'}, inplace=True)
df['Copper_OhmsPer_m'] = df['Copper_OhmsPer_m'] / 1000
df['Aluminum_OhmsPer_m'] = df['Aluminum_OhmsPer_m'] / 1000

current, volts, length, phase = get_inputs()
ohm_perM_for_run = get_OhmsPer_M(current, volts, length, phase)
get_minimum_cable(ohm_perM_for_run, df)
