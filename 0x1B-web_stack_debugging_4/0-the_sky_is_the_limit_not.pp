
# Puppet manifest to increase max open files limit and optimize Nginx

class nginx_optimization {

  # Ensure Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Increase the maximum number of open files for the Nginx service
  file_line { 'increase_nginx_nofile_limit':
    path    => '/etc/systemd/system/nginx.service.d/limits.conf',
    line    => 'LimitNOFILE=10000',
    match   => '^LimitNOFILE=',
    notify  => Exec['reload-systemd'],
  }

  # Reload systemd to apply the changes
  exec { 'reload-systemd':
    command => 'systemctl daemon-reload',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/nginx.conf'],
  }

  # Manage the Nginx configuration file
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('/home/ubuntu/pupetlabs/templates/0-the_sky_is_the_limit_not.pp'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    notify  => Service['nginx'],
  }
}

# Apply the class
include nginx_optimization
