# nginx_install.pp

# Update package lists
exec { 'apt-update':
  command => '/usr/bin/apt-get update -y',
  path    => ['/bin', '/usr/bin'],
}

# Install nginx web server
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Configure nginx on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @("EOL"),
server {
    listen 80 default_server;
    server_name _;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /custom_404.html {
        internal;
        root /usr/share/nginx/html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dphzDKZa6xk;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
EOL
  require => Package['nginx'],
}

# Start nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create index.html
file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Service['nginx'],
}

# Create custom_404.html
file { '/usr/share/nginx/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
  require => Service['nginx'],
}
