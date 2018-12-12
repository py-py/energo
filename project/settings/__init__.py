from .base_settings import *


environment = os.getenv('ENVIRONMENT', 'dev')

if environment == 'dev':
    from .local_settings import *
if environment == 'prod':
    pass
if environment not in ('dev', 'prod'):
    raise Exception('Environment is not provided.')
