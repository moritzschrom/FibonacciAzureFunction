import logging

import azure.functions as func


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    length = req.params.get('length')
    if not length:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            length = req_body.get('length')

    if length:
        fib_sequence = fibonacci(int(length))
        return func.HttpResponse(json.dumps(fib_sequence))
    else:
        return func.HttpResponse(
             "Please pass a length parameter on the query string or in the request body",
             status_code=400
        )