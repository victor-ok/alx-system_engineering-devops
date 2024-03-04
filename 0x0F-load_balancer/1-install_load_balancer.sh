#!/usr/bin/env bash
# Installs HAProxy version 1.8 with the following configurations:
#+    Enables management via the init script.
#+    Distributes requests using a round-robin algorithm.


apt-get install -y --no-install-recommends software-properties-common
add-apt-repository -y ppa:vbernat/haproxy-2.8
apt-get install haproxy=2.8.\*
apt-get update

sudo service haproxy start

echo 'frontend theproxy
	bind *:80
	default_backend my_backend_servers

backend my_backend_servers
	balance roundrobin
	server 470001-web-01 52.73.30.202:80
	server 470001-web-02 52.207.68.183:80' | sudo tee -a /etc/haproxy/haproxy.cfg

sudo service haproxy reload
