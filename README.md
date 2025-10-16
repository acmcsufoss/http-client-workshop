# HTTP Client Workshop

In this workshop, we will be creating a simple HTTP client using Python and the
popular [Requests](https://docs.python-requests.org/en/latest/index.html) library and [PokeAPI](https://pokeapi.co).

---

## Software used
- `curl` and `jq`: used for quickly familiarizing ourselves with the API
- `Python` and `Requests`: for building our client

## The client
Our client will be a CLI app that takes a pokemon's name as input and outputs
it's basic info.

## Getting started
Make sure you have Python, curl, and jq installed. All three should be available
in your systems package manager (apt, homebrew, winget, etc.)  
  
For more info, see the following links:
-  [Python download page](https://www.python.org/downloads/)
-  [jq download page](https://jqlang.org/download/)
- (you probably already have curl installed)

### Using this repository (optional)
> If you already have Python and Requests or just want to install them on your
> own, that's OK. This demo has very little boilerplate.

1. If you don't already have it, install [Python](https://www.python.org/downloads/)
2. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/):

Macos/Linux:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows:
```sh
winget install --id=astral-sh.uv  -e
```

3. Run `uv sync` to install the project's dependencies
4. Run the Python script with uv:
```sh
uv run main.py
```
