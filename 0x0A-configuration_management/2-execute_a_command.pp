# Using Puppet to create a manifest that kills a process named killmenow.

exec { 'killmenow':
  # kil process
  command => 'pkill -f killmenow',

  # path to the prcess to kill
  path    => '/usr/bin:/usr/sbin:/bin'
}
