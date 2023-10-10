blueprints = custom_target('blueprints',
  # TODO find a way to deduplicate this and the gresource
  input: files(
    'templates/auth_credentials_view.blp',
    'templates/auth_dialog.blp',
    'templates/auth_login_method_view.blp',
    'templates/auth_quick_connect_view.blp',
    'templates/auth_user_select_view.blp',
    'templates/disconnect_dialog.blp',
    'templates/help-overlay.blp',
    'templates/server_add_dialog.blp',
    'templates/server_connected_view.blp',
    'templates/server_row.blp',
    'templates/servers_list_view.blp',
    'templates/window.blp',
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
install_subdir('logging', install_dir: moduledir)
install_subdir('database', install_dir: moduledir)

install_data(
  [
    '__init__.py',
    'main.py',
    'task.py',
    'jellyfin.py',
    configure_file(
      input: 'build_constants.py.in',
      output: 'build_constants.py',
      configuration: conf
    )
  ], 
  install_dir: moduledir
)
