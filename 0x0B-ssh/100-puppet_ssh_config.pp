#!/usr/bin/env bash
# Puppet to make changee in files.

file { 'ect/ssh/ssh_config':
        ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	passwordAunthentication no
	",
}
