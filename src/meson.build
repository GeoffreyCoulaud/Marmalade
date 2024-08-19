blueprints = custom_target('blueprints',
  # TODO find a way to deduplicate this and the gresource
  input: files(
    'templates/auth_quick_connect_view.blp',
    'templates/auth_user_select_view.blp',
    'templates/disconnect_dialog.blp',
    'templates/help-overlay.blp',
    'templates/item_card.blp',
    'templates/list_box_row_content.blp',
    'templates/loading_view.blp',
    'templates/scrollable_shelf.blp',
    'templates/server_add_dialog.blp',
    'templates/server_browser_headerbar.blp',
    'templates/server_browser_view.blp',
    'templates/server_home_page.blp',
    'templates/servers_list_row.blp',
    'templates/servers_list_view.blp',
    'templates/shelf.blp',
    'templates/shelf_page.blp',
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
