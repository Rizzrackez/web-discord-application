from labstack import Client


def get_currency(currency_from, currency_to):
    client = Client("H0V67cQzRL8vXV9zutVTebMnPYW-XbhRIDFTbhx6jFibdB3mnQyVb")
    service = client.currency()
    try:
        response = service.convert({
            'amount': 1,
            'from': currency_from,
            'to': currency_to
        })

        print(response)

        return response
    except Exception:
        return {'time': "undefined currency", 'amount': "undefined currency"}

