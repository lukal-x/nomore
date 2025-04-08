# No more

than this! A single unified package solving problems that usually require installation and maintenance of dozens of 1000 line long micro libraries.
A single dependency containing all the things you wish you already had and didn't have to introduce as dependencies in your project.

Built alongside https://x.com/cardcraft_sol

## As a replacement
Proxy/wrapper code can be written to behave like popular microdependencies but under the hood uses nomore - this way users can uninstall e.g. `requests` but point it to `nomore.http.client.wrappers.requests` like so

```python
from nomore.http.client import HTTPClientAliases

requests = HTTPClientAliases.requests

# use it
requests.post("http://example.com", json={"lorem": "ipsum"})

# or in cases where someone does "from requests import get"
get = HTTPClientAliases.requests.get

# use it
get("http://example.com")
```
