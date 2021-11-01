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
        pipeline = [
            {
                '$group': {
                    '_id': '$country_name',
                    'average_population': {'$avg': '$midyear_population'},
                    'min_population': {'$min': '$midyear_population'},
                    'max_population': {'$max': '$midyear_population'},
                },
            }, {
                '$project': {
                    '_id': 0,
                    'country': '$_id',
                    'average_population': {'$floor': '$average_population'},
                    'min_population': 1,
                    'max_population': 1,
                },
            },
        ]
        if country is None:
            pipeline.append({'$sort': {'country': direction}})
        else:
            pipeline.insert(0, {'$match': {'country_name': country}})

        query = self.db['midyear_population'].aggregate(pipeline)
        return list(query)
