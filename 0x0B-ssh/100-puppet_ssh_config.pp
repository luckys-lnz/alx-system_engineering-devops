#!/usr/bin/env bash

file_line { 'Turn off passwd auth':
  path  => '~/.ssh/config',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '~/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
}
