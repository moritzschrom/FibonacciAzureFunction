import logging
import azure.functions as func
import fastapi

app=fastapi.FastAPI()

@app.get("/FibonacciService/{length}")
async def fibonacci(length: int) -> List[int]:
    def generate_fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        else:
            fib_sequence = [1, 1]
            while len(fib_sequence) < n:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence

    return generate_fibonacci(length)


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the ASGI handler."""
    return await func.AsgiMiddleware(app).handle_async(req, context)
