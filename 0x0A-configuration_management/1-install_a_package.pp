# Using Puppet, install puppet-lint:

package { 'puppet-lint':
  ensure   => '2.5.0',
  source   => 'https://rubygems.org',
  provider => 'gem',
}
