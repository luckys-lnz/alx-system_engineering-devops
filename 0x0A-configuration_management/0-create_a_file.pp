# Using Puppet, create a file in /tmp.

file { '/tmp/school':
  # ensure the file exist.
  ensure  => file,
  # file contents
  content => "I love Puppet\n",
  # file permission
  mode    => '0744',
  # who the file belongs to
  owner   => 'www-data',
  # groudp to whom the file belongs to
  group   => 'www-data',
}

