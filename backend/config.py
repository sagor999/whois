import os

api_base_url = '/api/v1'

es_base_url = {
    'users': os.environ['ELASTICSEARCH_URL']+'/whois-users',
}
