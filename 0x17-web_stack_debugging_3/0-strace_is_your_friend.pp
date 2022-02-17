# Puttet script that fixes wrong extensions on assets loading

exec { 'Update loaded files extensions':
    command => "sudo sed -i 's/.phpp/.php/g' wp-settings.php ",
    cwd     => "/var/www/html",
    path    => "/usr/bin"
}
