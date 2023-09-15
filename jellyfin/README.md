# Automatic Jellyfin OpenAPI Bindings

## Generating bindings

The Jellyfin API bindings are generated with the help of [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

To regenerate the bindings, follow `openapi-python-client`'s instructions with a recent Jellyfin OpenAPI specification, remove the existing bindings in `src`, then move the generated `jellyfin_api_client` package out of the generated boilerplate project and into the `src` directory.

```sh
curl \
	"https://api.jellyfin.org/openapi/stable/jellyfin-openapi-10.8.10.json" \
	--output "jellyfin-openapi-10.8.10.json"
openapi-python-client generate --path "jellyfin-openapi-10.8.10.json"
rm -rf ../src/jellyfin_api_client
mv jellyfin-api-client/jellyfin_api_client ../src/jellyfin_api_client
```

## Updating dependencies

The generated subproject will contain a `pyproject.toml` file intended to be used with poetry.  
Since we use flatpak to distribute Marmalade, we will need to extract the requirements out of it and into `requirements.txt`.

When generating new API bindings, make sure to:
- Update `requirements.txt` according to `jellyfin-api-client/pyproject.toml`
- Then regenerate `python3-jellyfin-api.json` with the help of [flatpak-pip-generator](https://github.com/flatpak/flatpak-builder-tools/tree/de56f4702638739f930f4afa648686f12ac4d724/pip)

```sh
flatpak-pip-generator -r "requirements.txt" -o "python3-jellyfin-api"
mv python3-jellyfin-api.json ..
```

## Using the bindings

For an example usage of the generated binding, take a look at the `openapi-python-client` end-to-end tests' README [here](https://github.com/openapi-generators/openapi-python-client/tree/c93dfb061792bf34e97d53870eeac18a755ccbd2/end_to_end_tests/golden-record)