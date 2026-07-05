import pandas as pd

def get_inputs():
    current = float(input("Enter the load in Amps: "))
    volts = float(input("Enter the the Voltage: "))
    length = float(input("Enter the length of the run in metres: "))
    return [current, volts, length]

def get_OhmsPer_M(current, volts, length):
    volt_drop = volts * 0.03
    ohmPer_m = volt_drop/(2 * current * length)
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

inputs = get_inputs()
current, voltage, length = inputs
ohm_perM_for_run = get_OhmsPer_M(current, voltage, length)
get_minimum_cable(ohm_perM_for_run, df)
