from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException, status

from backend.repository import Repository
from backend.settings import BACKEND_PORT, DB_NAME

app = FastAPI()
repository = Repository(DB_NAME)


@app.get('/get_supported_country')
async def get_supported_country(sort_by: str = 'country_area', ascending: bool = False):
    available_sort_by_values = {'country_code', 'country_name', 'country_area'}
    if sort_by not in available_sort_by_values:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong sort_by parameter')
    return await repository.get_country_names(sort_by, ascending)


@app.get('/get_population_information')
async def get_population_information(country: Optional[str] = None, ascending: bool = True):
    available_countries = await get_supported_country()
    available_countries = [note['country_name'] for note in available_countries]
    if country not in available_countries and country is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong country parameter')
    return await repository.get_population_information(country, ascending)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=BACKEND_PORT)
