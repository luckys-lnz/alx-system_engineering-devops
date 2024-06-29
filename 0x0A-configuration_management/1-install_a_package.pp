# Using Puppet to install Flask version 2.1.0

package { 'flask':

  # Ensure the specified version of Flask is installed
  ensure   => '2.1.0',

  # Use pip3 as the package provider
  provider => 'pip3',
}

# Specify the Werkzeug version to ensure flask is compatible
package { 'Werkzeug':

  # Werkzeug version
  ensure   => '2.1.1',

  # Use pip3 as the package provider
  provider => 'pip3',
}

