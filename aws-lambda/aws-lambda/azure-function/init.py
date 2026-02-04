import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'User')
    logging.info('Azure Function executed successfully.')

    return func.HttpResponse(
        f"Hello {name}, response from Azure Function",
        status_code=200
    )
