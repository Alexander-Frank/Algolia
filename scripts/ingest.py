
from algoliasearch.search_client import SearchClient
import json
import logging

with open('merged_restaurant_info.json') as f:
    records = json.load(f)

app_id = ""
api_key = ""

# Connect and authenticate with Algolia app
client = SearchClient.create(app_id, api_key)

# Create a new index
index = client.init_index('restaurants')

try:
  index.save_objects(records, {
    # set autoGenerateObjectIDIfNotExist to false if your records contain an ObjectID
    'autoGenerateObjectIDIfNotExist': False
  })
except Exception as e:
  logging.error(str(e))
