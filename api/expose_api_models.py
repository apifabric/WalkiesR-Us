from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger(__name__)

app_logger.debug("\napi/expose_api_models.py - endpoint for each table")


def expose_models(api, method_decorators = []): 
    """
        Declare API - on existing SAFRSAPI to expose each model - API automation 
        - Including get (filtering, pagination, related data access) 
        - And post/patch/update (including logic enforcement) 

        Invoked at server startup (api_logic_server_run) 

        You typically do not customize this file 
        - See https://apilogicserver.github.io/Docs/Tutorial/#customize-and-debug 
    """
    api.expose_object(database.models.Administrator, method_decorators= method_decorators)
    api.expose_object(database.models.Dog, method_decorators= method_decorators)
    api.expose_object(database.models.Owner, method_decorators= method_decorators)
    api.expose_object(database.models.DogSizePriceHistory, method_decorators= method_decorators)
    api.expose_object(database.models.Walker, method_decorators= method_decorators)
    api.expose_object(database.models.Feedback, method_decorators= method_decorators)
    api.expose_object(database.models.Notification, method_decorators= method_decorators)
    api.expose_object(database.models.Payment, method_decorators= method_decorators)
    api.expose_object(database.models.WalkRequest, method_decorators= method_decorators)
    api.expose_object(database.models.Review, method_decorators= method_decorators)
    api.expose_object(database.models.SystemLog, method_decorators= method_decorators)
    api.expose_object(database.models.WalkRequestDog, method_decorators= method_decorators)
    api.expose_object(database.models.WalkerAvailability, method_decorators= method_decorators)
    api.expose_object(database.models.WalkerHistory, method_decorators= method_decorators)
    api.expose_object(database.models.WalkerPrice, method_decorators= method_decorators)
    return api
