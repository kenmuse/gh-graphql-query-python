import requests
import argparse

parser = argparse.ArgumentParser(description="Query API",
 formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("token", help = "PAT token for querying")
args = parser.parse_args()

headers = {"Authorization": "token " + args.token }

QUERY = """
{
    rateLimit {
        remaining
        resetAt
    }
}
"""

request = requests.post('https://api.github.com/graphql', json={'query': QUERY}, headers=headers)
response = request.json()
if request.status_code == 200:
    limit = response["data"]["rateLimit"]
    remaining = limit["remaining"]
    reset = limit["resetAt"]
    print("Limit: %d\nResets at: %s" % (remaining, reset) )
else:
    raise Exception("Error (%d) %s" % (request.status_code, response["message"]))