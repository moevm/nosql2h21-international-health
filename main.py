from typing import Optional

import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile, status

from backend.helper import get_mongo_client, import_file
from backend.repository import Repository
from backend.settings import BACKEND_PORT, DB_NAME

app = FastAPI()
repository = Repository(DB_NAME)


@app.get('/get_supported_countries')
async def get_supported_countries(sort_by: str = 'country_area', ascending: bool = False):
    available_sort_by_values = {'country_code', 'country_name', 'country_area'}
    if sort_by not in available_sort_by_values:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong sort_by parameter')
    return await repository.get_country_names(sort_by, ascending)


@app.get('/get_population_information')
async def get_population_information(country: Optional[str] = None, ascending: bool = True):
    available_countries = await get_supported_countries()
    available_countries = (note['country_name'] for note in available_countries)
    if country not in available_countries and country is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong country parameter')
    return await repository.get_population_information(country, ascending)


@app.get('/get_growth_rate')
async def get_growth_rate(mode: str = 'birth', country: Optional[str] = None, year: Optional[int] = None):
    available_modes = {'birth', 'death'}
    available_countries = await get_supported_countries()
    available_countries = (note['country_name'] for note in available_countries)
    if mode not in available_modes or (country not in available_countries and country is not None):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong country or mode parameters')
    return await repository.get_growth_rate(mode, country, year)


@app.post('/import_file')
async def get_supported_countries_file(file: UploadFile = File(...)):
    client = get_mongo_client()
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Please, upload only csv file')
    try:
        return await import_file(file, client, file.filename.replace('.csv', ''))
    except Exception as e:
        return {'detail': str(e)}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=BACKEND_PORT)
