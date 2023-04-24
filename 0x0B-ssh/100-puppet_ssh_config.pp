#!/usr/bin/pup
# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set
# up your client SSH configuration file so that you can connect to a
# server without typing a password.
# Your SSH client configuration must be configured to use 
# the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to 
# authenticate using a password

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  content => 'IdentityFile ~/.ssh/school\n PasswordAuthentication no\n User ubuntu\n Host 34.227.89.176\n',
  mode   => '0644',
}
