gnome.compile_resources('marmalade',
  configure_file(
    input: 'marmalade.gresource.xml.in',
    output: 'marmalade.gresource.xml',
    configuration: conf
  ),
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

configure_file(
  input: 'marmalade.in',
  output: 'marmalade',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

install_subdir('components', install_dir: moduledir)
install_subdir('logging', install_dir: moduledir)
install_subdir('database', install_dir: moduledir)
install_subdir('jellyfin_openapi_client', install_dir: moduledir)

install_data(
  [
    '__init__.py',
    'jellyfin.py',
    'main.py',
    'shared.py',
    'task.py',
    configure_file(
      input: 'build_constants.py.in',
      output: 'build_constants.py',
      configuration: conf
    )
  ], 
  install_dir: moduledir
)
