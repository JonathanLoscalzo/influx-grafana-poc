from generation import generate
import numpy as np
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting Generation")

data = generate()
dates = data.index
times = dates.astype(int) // 10**9
values = data.value.values

logging.info("Start transformation")
def definir_accion(d):
    if d==1:
        return 'entrar'
    elif d==-1:
        return 'salir'
    else: 
        return '\'\''

df = pd.DataFrame({"value":values, "timestamp":times})
df["Measure"] = "Personas"
df['device'] = 'd1'
df['sensor'] = 'reflectivo'
df['accion'] = df.value.apply(definir_accion)
df['dia'] = dates.day_name()

format_to="{}, device={}, sensor={}, accion={} value={}, {}"

# https://stackoverflow.com/questions/54313463/pandas-datetime-to-unix-timestamp-seconds
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#from-timestamps-to-epoch
# pd.to_datetime(['2019-01-15 13:30:00']).astype(int) / 10**9

df["str_format"]=df.apply(lambda x: f"{x['Measure']},device={x['device']},sensor={x['sensor']},accion={x['accion']},dia={x['dia']} value={x['value']} {x['timestamp']}", axis=1)
logging.info("Start writing Personas_data")

df.str_format.to_csv('Personas_data.txt', header=False, index=False, sep='\t', mode='a')

logging.info("End of script")