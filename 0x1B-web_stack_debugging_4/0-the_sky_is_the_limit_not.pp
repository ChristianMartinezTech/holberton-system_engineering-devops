# Test Nginx setup

exec { 'changelimit':
  path    => '/bin/',
  command => 'sed -i -e "s/15/1000/g" /etc/default/nginx'
}

service { 'nginx':
  ensure    => running,
  subscribe => Exec['changelimit']
}
