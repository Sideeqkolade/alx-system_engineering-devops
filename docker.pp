#!/usr/bin/pup
# installing a docker package

package { 'docker.io':
  ensure  => 'installed',
}
