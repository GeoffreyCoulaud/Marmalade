# Contributing

## Setting up a local development environment

Marmalade is supposed to be run as a flatpak.  
To build the project, the simplest is to use `GNOME Builder`.

1. Generate the openapi jellyfin client from the openapi spec

```sh
pipx install openapi-python-client --include-deps
openapi-python-client \
    generate \
    --overwrite \
    --path "data/jellyfin-openapi.json" \
    --output-path "src/jellyfin_openapi_client"
```

2. In gnome builder, build and run the project

## Updating the python dependencies

1. Update `requirements.txt` with the runtime dependencies 
2. Update `requirements.dev.txt` with the dev dependencies
3. Create a virtual environment, and install the dependencies

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.dev.txt
```

4. Install `flatpak-pip-generator`
Note: assumes `~/.local/bin` is in your `$PATH`

```sh
wget https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/refs/heads/master/pip/flatpak-pip-generator
chmod u+x flatpak-pip-generator
mv flatpak-pip-generator ~/.local/bin
```

5. Update the flatpak manifest with the new python dependencies

```sh
flatpak-pip-generator -r requirements.txt
```