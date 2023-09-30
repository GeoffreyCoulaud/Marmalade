blueprints = custom_target('blueprints',
  # TODO find a way to deduplicate this with the gresource
  input: files(
    'templates/window.blp',
    'templates/help-overlay.blp',
    'templates/servers_view.blp',
    'templates/server_home_view.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('marmalade',
  configure_file(
    input: 'marmalade.gresource.xml.in',
    output: 'marmalade.gresource.xml',
    configuration: conf
  ),
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: blueprints,
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

install_data(
  [
    '__init__.py',
    'main.py',
    'server.py',
    'reactive_set.py',
    configure_file(
      input: 'build_constants.py.in',
      output: 'build_constants.py',
      configuration: conf
    )
  ], 
  install_dir: moduledir
)
