import os
import zipfile

import requests
from pathlib import Path
import \
    pandas as pd  # NOTE Need openpyxl else -- ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
from urllib.parse import unquote
import pooch
import re
from cdr_schemas.ta3_input import DataSource, LayerCategory, LayerDataType, DataFormat
from collections import namedtuple
from pooch.processors import ExtractorProcessor
import netCDF4
import sciencebasepy
import time
class ExtractNetCDF(ExtractorProcessor):  # pylint: disable=too-few-public-methods
    """
    Processor that unpacks a zip archive and returns a list of all files.

    Use with :meth:`pooch.Pooch.fetch` or :func:`pooch.retrieve` to unzip a
    downloaded data file into a folder in the local data store. The
    method/function will return a list with the names of the unzipped files
    instead of the zip archive.

    The output folder is ``{fname}.unzip``.

    Parameters
    ----------
    members : list or None
        If None, will unpack all files in the zip archive. Otherwise, *members*
        must be a list of file names to unpack from the archive. Only these
        files will be unpacked.
    extract_dir : str or None
        If None, files will be unpacked to the default location (a folder in
        the same location as the downloaded zip file, with the suffix
        ``.unzip`` added). Otherwise, files will be unpacked to
        ``extract_dir``, which is interpreted as a *relative path* (relative to
        the cache location provided by :func:`pooch.retrieve` or
        :meth:`pooch.Pooch.fetch`).

    """

    @property
    def suffix(self):
        """
        String appended to unpacked archive folder name.
        Only used if extract_dir is None.
        """
        return ".extracted"

    def _all_members(self, fname):
        """Return all members from a given archive."""
        # with ZipFile(fname, "r") as zip_file:
        #     return zip_file.namelist()
        return netCDF4.Dataset(fname).variables.keys()


    def _extract_file(self, fname, extract_dir):
        """
        This method receives an argument for the archive to extract and the
        destination path.
        """
        with netCDF4.Dataset(fname) as f:
            if self.members is None:
                pass
        pass
        # with ZipFile(fname, "r") as zip_file:
        #     if self.members is None:
        #         get_logger().info(
        #             "Unzipping contents of '%s' to '%s'", fname, extract_dir
        #         )
        #         # Unpack all files from the archive into our new folder
        #         zip_file.extractall(path=extract_dir)
        #     else:
        #         for member in self.members:
        #             get_logger().info(
        #                 "Extracting '%s' from '%s' to '%s'", member, fname, extract_dir
        #             )
        #             # If the member is a dir, we need to get the names of the
        #             # elements it contains for extraction (ZipFile does not
        #             # support dirs on .extract). If it's not a dir, this will
        #             # only include the member itself.
        #             # Based on:
        #             # https://stackoverflow.com/questions/8008829/extract-only-a-single-directory-from-tar
        #             subdir_members = [
        #                 name
        #                 for name in zip_file.namelist()
        #                 if os.path.normpath(name).startswith(os.path.normpath(member))
        #             ]
        #             # Extract the data file from within the archive
        #             zip_file.extractall(members=subdir_members, path=extract_dir)

def parse_resolution(matching_row):
    resolution_raw = matching_row['Resolution in ESRI:102008 - North_America_Albers_Equal_Area_Conic CRS'].values[0]
    if pd.isnull(resolution_raw):
        resolution = None
    else:
        resolution = resolution_raw.split('x')[0].strip(), resolution_raw.split('x')[0].split(' ')[0]
    return resolution

# Our data:
# https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/edit#gid=1946475221

# Template:
# https://docs.google.com/spreadsheets/d/<KEY>/export?gid=<GID>&format=csv

# Completed
# https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/export?gid=1946475221&format=xlsx
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Up06vfwoUpanmrzVcvdK_4ZJ0WUoFPgm/export?gid=1946475221&format=xlsx"

sleep_time = 1.0
sciencebase_session = sciencebasepy.SbSession()
time.sleep(sleep_time)

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

gk = df_geophysics.groupby('Download URI')

bad_list = [
    "https://www.sciencebase.gov/catalog/file/get/619a9a3ad34eb622f692f961?f=__disk__2a%2F8f%2F2c%2F2a8f2ced08239dcc7895ffa728c8e94093c98e47",
    "https://www.sciencebase.gov/catalog/file/get/619a9a3ad34eb622f692f961?f=__disk__dc%2Fa2%2Fc4%2Fdca2c4a3f6f32b2f63853bbb00748b949c74e95a",
    "https://www.sciencebase.gov/catalog/file/get/619a9f02d34eb622f692f96c?f=__disk__ef%2F78%2F9e%2Fef789e155f8b4afe033dadfaa945ebad3a25e13d",
    "https://www.sciencebase.gov/catalog/file/get/619a9f02d34eb622f692f96c?f=__disk__ef%2Ffe%2Fcb%2Feffecbe42eee9535979fafc40a74fa4c0841d92a",
    "https://www.sciencebase.gov/catalog/file/get/62434c71d34e22d73748d369?f=__disk__32%2Ffa%2F5f%2F32fa5f37667e518cd73a62464023a49f61055b12",
    "https://www.sciencebase.gov/catalog/file/get/62434c71d34e22d73748d369?f=__disk__46%2F90%2F24%2F46902490096de71c94212d8d9dacd28c80b80d7c",
    "https://www.sciencebase.gov/catalog/file/get/62434c71d34e22d73748d369?f=__disk__a0%2F1c%2F7e%2Fa01c7e7f5563f830369a926a18b8d4bdf7ce710b"
]

SchemaItem = namedtuple('SchemaItem', ['local_path', 'instantiated_schema'])
schema_items = []
for data_url in gk.groups:
    data_file = unquote(data_url).split('/')[-1].replace(' ', '_')
    match data_url:
        case "http://www.ceus-ssc.com/Database/CEUS-SSC%20Gravity%20Anomaly%20Database%20Grids.zip" | "http://www.ceus-ssc.com/Database/Full-Spectrum%20Magnetic%20Anomaly%20Database%20for%20the%20Central%20and%20Eastern%20United%20States.zip":

            match data_url:
                case "http://www.ceus-ssc.com/Database/CEUS-SSC%20Gravity%20Anomaly%20Database%20Grids.zip":
                    members = [
                        'CEUS_GRAV_Isostatic_CEUSSSC_R0.tif',
                        'CEUS_GRAV_RI_CEUSSSC_R0.tif',
                        'CEUS_GRAV_RI_HD_CEUSSSC_R0.TIF',
                        'CEUS_GRAV_RI_1VD_CEUSSSC_R0.tif',
                        'CEUS_GRAV_RI_HD_1VD_CEUSSSC_R0.TIF',
                    ]
                    authors = ['Keller, G.R.']
                    publication_date = '2010'
                    subcategory = 'gravity'
                case "http://www.ceus-ssc.com/Database/Full-Spectrum%20Magnetic%20Anomaly%20Database%20for%20the%20Central%20and%20Eastern%20United%20States.zip":
                    members = [
                        'CEUS_MAG_DRTP_CEUSSSC_R0.TIF',
                        'CEUS_MAG_DRTP_TDR_CEUSSSC_R0.tif',
                        'CEUS_MAG_DRTP_HD_TDR_CEUSSSC_R0.TIF',
                        'CEUS_MAG_TMAG_AAS_CEUSSSC_R0.tif'
                    ]
                    authors = [
                        "Ravat, D.", "Finn, C.", "Hill, P.", "Kucks, R.", "Phillips, J.", "Blakely, R.",
                        "Bouligand, C.", "Sabaka, T.", "Elshayat, A.", "Aref, A.", "Elawadi, E."
                    ]
                    publication_date = '2009'
                    subcategory = 'magnetic'

            file_path = pooch.retrieve(url=data_url, fname=data_file, known_hash=None,
                                       processor=pooch.Unzip(members=members))

            base_path = Path(file_path[0]).parent
            for tif in members:
                tif_path = base_path / tif

                matching_row = df_geophysics.loc[df_geophysics['Evidence Layer Raster prefix'] == Path(tif).stem]

                resolution = parse_resolution(matching_row)
                instantiated_schema = DataSource(
                    DOI= None,
                    authors= authors,
                    publication_date=publication_date,
                    category= LayerCategory.GEOPHYSICS,
                    subcategory=subcategory,
                    description= matching_row['Type'].values[0],
                    derivative_ops= str(matching_row['Derivative Ops'].values[0]),
                    type=LayerDataType.CONTINUOUS,
                    resolution=resolution,
                    format=DataFormat.TIF,
                    download_url=data_url
                )
                schema_items.append(SchemaItem(local_path=tif_path, instantiated_schema=instantiated_schema))
            pass

        case 'https://ds.iris.edu/files/products/emc/emc-files/CONUS-MT-2023.r0.0-n4.nc':
            #
            # file_path = pooch.retrieve(url=data_url, fname=data_file, known_hash=None,
            #                            processor=ExtractNetCDF())
            pass

        case _:
            matching_index = gk.groups[data_url]
            matching_row = df_geophysics.loc[matching_index]
            sciencebaselink = matching_row['General Link'].values[0]
            sciencebase_id = sciencebaselink.split("/")[-1]

            sciencebase_item = sciencebase_session.get_item(sciencebase_id)
            time.sleep(sleep_time)
            try:
                file_paths = pooch.retrieve(url=data_url, fname=data_file, known_hash=None,
                                           processor=pooch.Unzip())
            except zipfile.BadZipFile:
                file_paths = pooch.retrieve(url=data_url, fname=data_file, known_hash=None)
                os.rename(file_paths, file_paths + ".tif")
                file_paths = [file_paths + ".tif"]

            tif_paths = list(filter(lambda x: x.lower().endswith('.tif') or x.endswith('.tiff'), file_paths))
            shp_paths = list(filter(lambda x: x.lower().endswith('.shp'), file_paths))

            citation = sciencebase_item["citation"]

            # find index of the citation year (b/c all authors are before that)
            year_pos = re.search("[0-9][0-9][0-9][0-9]", citation).regs[0][0]
            authors = [f"{author}." for author in citation[:year_pos].split("., ")][:-2]
            authors[-1].replace("and ", "")

            publication_date = sciencebase_item["dates"][0]["dateString"]

            resolution = parse_resolution(matching_row)
            format = "tif" if len(tif_paths) > 0 else "shp"

            instantiated_schema = DataSource(
                DOI=None,
                authors=authors,
                publication_date=publication_date,
                category=matching_row["Category"].values[0],
                subcategory=matching_row["Sub Category"].values[0],
                description=matching_row['Type'].values[0],
                derivative_ops=str(matching_row['Derivative Ops'].values[0]),
                type=LayerDataType.CONTINUOUS,
                resolution=resolution,
                format=format,
                download_url=matching_row["Download URI"].values[0]
            )
            for tif_path in tif_paths:
                schema_items.append(SchemaItem(local_path=tif_path, instantiated_schema=instantiated_schema))
            for shp_path in shp_paths:
                schema_items.append(SchemaItem(local_path=shp_path, instantiated_schema=instantiated_schema))
            pass
pass