import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    route = req.route_params.get('route')
    return func.HttpResponse(route)
