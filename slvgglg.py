from solverCaptcha import solveRecaptcha


def solveRecaptchas():
    result = solveRecaptcha(
        "6LeCXbUUAAAAALp9bXMEorp7ONUX1cB1LwKoXeUY",
        "https://bezkolejki.eu/lodzkiuw"
    )

    code = result['code']

    return code


print(solveRecaptchas())