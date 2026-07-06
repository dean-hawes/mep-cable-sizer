import pandas as pd
from math import sqrt

def get_inputs():
    while True:
        try:
            current = float(input("Enter the load in Amps: "))
            volts = float(input("Enter the the Voltage: "))
            length = float(input("Enter the length of the run in metres: "))
            phase = int(input("Enter phase ('1' for single-phase, '3' for 3-phase): "))

            if current <= 0 or volts <= 0 or length <= 0:
                print("\n[ERROR]: Inputs must be positive")
                continue
            if phase not in (1, 3):
                print("\n[ERROR]: Phase input must be '1' or '3'")
                continue
        except ValueError:
            print("[ERROR]: Please enter valid numbers only.")

        else:
            return current, volts, length, phase


def get_OhmsPer_M(current, volts, length, phase):
    volt_drop = volts * 0.03
    if phase == 1:        
        ohmPer_m = volt_drop/(2 * current * length)
    elif phase == 3:
        ohmPer_m = volt_drop/(sqrt(3) * current * length)
    print(f'Maximum ohms per meter for {length} = {ohmPer_m}')
    return(ohmPer_m)

def get_minimum_cable(ohmPer_m, dataframe):
    safe_cables = dataframe[dataframe['Copper_OhmsPer_m'] <= ohmPer_m]
    if safe_cables.empty:
        print("[Alert]: No cable large enough in current database")
    else:
        min_cable = safe_cables.iloc[0]['CrossSection_mm2']
        print("\n" + "-"*64)
        print(f"\nMinimum cable required to stay within 3% voltage drop is {min_cable}mm")
        print("\n" + "-"*64 + "\n")

def exit_prompt():
    while True:
        try:
            user_input = int(input("Enter '1' For another cable run calculation or '2' to exit: "))
            if user_input == 1:
                return True
            if user_input == 2:
                return False
            print("\n[ERROR]: Invalid Selection. Please enter either '1' to calculate another cable run or '2' to exit.")
        except ValueError:
            print("\n[ERROR]: Invalid Input. Please enter either '1' to calculate another cable run or '2' to exit: ")

df = pd.read_csv('Cable calculator/copper&aluminium_values.csv')
df.rename(columns={'Copper_OhmsPerKm': 'Copper_OhmsPer_m', 'Aluminum_OhmsPerKm': 'Aluminum_OhmsPer_m'}, inplace=True)
df['Copper_OhmsPer_m'] = df['Copper_OhmsPer_m'] / 1000
df['Aluminum_OhmsPer_m'] = df['Aluminum_OhmsPer_m'] / 1000

df.sort_values('Copper_OhmsPer_m', inplace=True, ascending=False)

while True:
    current, volts, length, phase = get_inputs()
    ohm_perM_for_run = get_OhmsPer_M(current, volts, length, phase)
    get_minimum_cable(ohm_perM_for_run, df)

    continue_prompt = exit_prompt()
    if continue_prompt == False:
        break
