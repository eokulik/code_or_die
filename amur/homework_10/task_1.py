import json
from urllib import request


def get_geocint_report():
    req = request.Request('https://geocint.kontur.io/geocint/report.json',
                          method='GET')
    response_raw = request.urlopen(req)
    response_json = json.load(response_raw)
    pretty_response_json = json.dumps(response_json, indent=3)
    print(pretty_response_json)


get_geocint_report()
