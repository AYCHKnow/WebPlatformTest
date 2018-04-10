from utils import return_hello


def main(request, response):
  response.headers.set("Cache-Control", "no-cache")
  response.content = return_hello()
