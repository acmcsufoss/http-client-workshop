# Using This Demo

This document is for anyone who wants to use this repository in their own demo
or workshop.

## Using cURL and jq
curl and jq are ubiquitous tools that are very useful for getting familiar with
an HTTP api.

For example, using
```sh
curl https://pokeapi.co/api/v2/berry/oran
```
will get you this hunk of unformatted json:
```
{"firmness":{"name":"super-hard","url":"https://pokeapi.co/api/v2/berry-firmness/5/"},"flavors":[{"flavor":{"name":"spicy
","url":"https://pokeapi.co/api/v2/berry-flavor/1/"},"potency":10},{"flavor":{"name":"dry","url":"https://pokeapi.co/api/
v2/berry-flavor/2/"},"potency":10},{"flavor":{"name":"sweet","url":"https://pokeapi.co/api/v2/berry-flavor/3/"},"potency"
:0},{"flavor":{"name":"bitter","url":"https://pokeapi.co/api/v2/berry-flavor/4/"},"potency":10},{"flavor":{"name":"sour",
"url":"https://pokeapi.co/api/v2/berry-flavor/5/"},"potency":10}],"growth_time":4,"id":7,"item":{"name":"oran-berry","url
":"https://pokeapi.co/api/v2/item/132/"},"max_harvest":5,"name":"oran","natural_gift_power":60,"natural_gift_type":{"name
":"poison","url":"https://pokeapi.co/api/v2/type/4/"},"size":35,"smoothness":20,"soil_dryness":15}
```
  
Simply piping into jq improves it's readability massively:
```sh
curl https://pokeapi.co/api/v2/berry/oran | jq
```

Response:
```json
{
  "firmness": {
    "name": "super-hard",
    "url": "https://pokeapi.co/api/v2/berry-firmness/5/"
  },
  "flavors": [
    {
      "flavor": {
        "name": "spicy",
        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
      },
      "potency": 10
    },
    ...
}
```
  
Furthermore, jq can be used to filter specific fields:
```sh
curl https://pokeapi.co/api/v2/berry/oran | jq .firmness
```
Response:
```json
{
  "name": "super-hard",
  "url": "https://pokeapi.co/api/v2/berry-firmness/5/"
}
```

## Tips for using API exploration while writing the client
- First, check out a completed HTTP client example in the `completed` branch of
this repository.
- Before using some piece of data from the response
data, make sure to explore that section of the API with curl and jq to give the
audience a better feel for where the data is coming from.
- Working with JSON lists are trickier than with standard fields in this case.
