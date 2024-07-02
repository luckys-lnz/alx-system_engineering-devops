# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Redirect /redirect_me to YouTube
file { '/etc/nginx/conf.d/redirect.conf':
  ensure  => file,
  content => 'location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }',
  notify  => Service['nginx'],
}

# Ensure Nginx is running
service { 'nginx':
  ensure => running,
  enable => true,
}

