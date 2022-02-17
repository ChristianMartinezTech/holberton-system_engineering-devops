# Puppet script that fixes wrong extensions on assets loading

exec { 'Update loaded files extensions':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  provider => 'shell',
}
