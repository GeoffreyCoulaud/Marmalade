project('marmalade',
          version: '0.1.0',
    meson_version: '>= 0.62.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

i18n = import('i18n')
gnome = import('gnome')
python = import('python')

pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
localedir = join_paths(get_option('prefix'), get_option('localedir'))
moduledir = join_paths(pkgdatadir, 'src')

profile = get_option('profile')
if profile == 'development'
  app_id = 'com.github.geoffreycoulaud.Marmalade.Devel'
  prefix = '/com/github/geoffreycoulaud/Marmalade/Devel'
elif profile ==  'release'
  app_id = 'com.github.geoffreycoulaud.Marmalade'
  prefix = '/com/github/geoffreycoulaud/Marmalade'
endif

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('PYTHON_VERSION', python.find_installation('python3').language_version())
conf.set('APP_ID', app_id)
conf.set('PREFIX', prefix)
conf.set('VERSION', meson.project_version())
conf.set('PROFILE', profile)
conf.set('localedir', localedir)
conf.set('pkgdatadir', pkgdatadir)

subdir('data')
subdir('src')
subdir('po')

gnome.post_install(
     glib_compile_schemas: true,
    gtk_update_icon_cache: true,
  update_desktop_database: true,
)
