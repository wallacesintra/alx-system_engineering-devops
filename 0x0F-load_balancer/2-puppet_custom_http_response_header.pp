# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'apt-update':
  command => '/usr/bin/apt-get update'
  }

package { 'nginx':
  ensure => 'installed',
    name   => 'nginx',
    }

file_line { 'append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
    line  => "\tadd_header X-Served-By ${hostname};",
      after => 'http {',
      }

exec { 'sudo service nginx restart':
  command => '/usr/sbin/service nginx restart',
  }
