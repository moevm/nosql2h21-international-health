from typing import Optional

from backend.helper import MongoClient, get_direction, get_mongo_client


class Repository(object):
    def __init__(self, db: str):
        self.client: MongoClient = get_mongo_client()
        self.db = self.client[db]

    async def get_country_names(self, sort_by: str = 'country_area', ascending: bool = False):
        direction = await get_direction(ascending)
        return list(self.db['country_names_area'].find({}, {'_id': 0}).sort(sort_by, direction))

    async def get_population_information(self, country: Optional[str] = None, ascending: bool = True):
        direction = await get_direction(ascending)
        group_section = {
            '_id': '$country_name',
            'average_population': {'$avg': '$midyear_population'},
            'min_population': {'$min': '$midyear_population'},
            'max_population': {'$max': '$midyear_population'},
        }
        project_section = {
            '_id': 0,
            'country': '$_id',
            'average_population': {'$floor': '$average_population'},
            'min_population': 1,
            'max_population': 1,
        }

        if country is None:
            sort_section = {'country': direction}
            match_section = {}
        else:
            sort_section = {}
            match_section = {'country_name': country}

        pipeline = [
            {'$match': match_section},
            {'$group': group_section},
            {'$project': project_section},
        ]

        if sort_section:
            pipeline.append({'$sort': sort_section})

        query = self.db['midyear_population'].aggregate(pipeline)
        return list(query)

    async def get_growth_rate(self, mode: str = 'birth', country: Optional[str] = None, year: Optional[int] = None):
        project_section = {
            '_id': 0,
            'country': '$country_name',
            f'{mode}_rate': f'$crude_{mode}_rate',
            'year': 1,
        }

        match_section = {}
        if country is not None:
            match_section['country_name'] = country
        if year is not None:
            match_section['year'] = year

        pipeline = [{'$match': match_section}, {'$project': project_section}]

        query = self.db['birth_death_growth_rates'].aggregate(pipeline)
        return list(query)
