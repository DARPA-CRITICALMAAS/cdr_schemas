import requests
from pathlib import Path
import \
    pandas as pd  # NOTE Need openpyxl else -- ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
from urllib.parse import unquote
import pooch
from cdr_schemas.ta3_input import DataSource, LayerCategory, LayerDataType, DataFormat
from collections import namedtuple

# Our data:
# https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/edit#gid=1946475221

# Template:
# https://docs.google.com/spreadsheets/d/<KEY>/export?gid=<GID>&format=csv

# Completed
# https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/export?gid=1946475221&format=xlsx
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/export?gid=1946475221&format=xlsx"

filename = Path('ta3_layer_data.xlsx')
if filename.is_file():
    print("Spreadsheet already downloaded, skipping")
else:
    print("Downloading spreadsheet")
    # Recipe: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    with requests.get(spreadsheet_url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)

df = pd.read_excel(filename, sheet_name=None)['Original']
df_geophysics = df[df['Category'].str.contains('Geophysics')]

gk = df.groupby('Download URI')

SchemaItem = namedtuple('SchemaItem', ['local_path', 'instantiated_schema'])
schema_items = []
for data_url in gk.groups:
    match data_url:
        case "http://www.ceus-ssc.com/Database/CEUS-SSC%20Gravity%20Anomaly%20Database%20Grids.zip":
            data_file = unquote(data_url).split('/')[-1].replace(' ', '_')
            members = ['CEUS_GRAV_Isostatic_CEUSSSC_R0.tif',
                       'CEUS_GRAV_RI_CEUSSSC_R0.tif',
                       'CEUS_GRAV_RI_HD_CEUSSSC_R0.TIF',
                       'CEUS_GRAV_RI_1VD_CEUSSSC_R0.tif',
                       'CEUS_GRAV_RI_HD_1VD_CEUSSSC_R0.TIF',
                       ]
            file_path = pooch.retrieve(url=data_url, fname=data_file, known_hash=None,
                                       processor=pooch.Unzip(members=members))

            base_path = Path(file_path[0]).parent
            for tif in members:
                tif_path = base_path / tif

                matching_row = df_geophysics.loc[df_geophysics['Evidence Layer Raster prefix'] == Path(tif).stem]

                resolution_raw = matching_row['Resolution in ESRI:102008 - North_America_Albers_Equal_Area_Conic CRS'].values[0]
                resolution = resolution_raw.split('x')[0].strip(), resolution_raw.split('x')[0].split(' ')[0]
                instantiated_schema = DataSource(
                    DOI= None,
                    authors= ['Keller, G.R.'],
                    date_created= '2010',
                    last_updated= None,
                    category= LayerCategory.GEOPHYSICS,
                    subcategory=None,
                    description= matching_row['Type'].values[0],
                    derivative_ops= str(matching_row['Derivative Ops'].values[0]),
                    type=LayerDataType.CONTINUOUS,
                    resolution=resolution,
                    format=DataFormat.TIF,
                    download_url=data_url
                )
                schema_items.append(SchemaItem(local_path=tif_path, instantiated_schema=instantiated_schema))
            pass
    pass
