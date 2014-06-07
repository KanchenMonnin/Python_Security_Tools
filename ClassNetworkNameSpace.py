#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Programme : SecLnx Network NameSpace
# Auteur : Monnin Kanchen
# Licence : GPL
######################################

u"""

Network namespace can be use if you isolate a process in a 
container. The network namespace can be to connected with
openVswitch. With this programme, youc can creat and manage 
your network namespace.

"""

# Importation of external module :

from __future__ import unicode_literals
import os
import sys
import subprocess


class netns(object):

	def __init__(self, name, network):

		# Name of you Netns
		self.netns_name = name

		# network of your namespace
		# format : 192.168.1.0/24
		self.netns_net = network


	def creat(self,netns_net, netns_name):

		# activation routing forward
		subprocess.call("echo","net.ipv4.ip_forward = 1",">","/etc/sysctl")

		# create netns
		subprocess.call(["ip","netns","ad",netns_name])

		# Create two virtual eth one for netns and the other one can be connected to openVswitch or
		# the hote
		subprocess.call(["ip", "link", "add", "veth0", "type", "veth", "peer", "name", "veth1"])

		subprocess.call(["ip", "link", "set", "veth1", "netns", netns_name])

		# network of the network nameSpace
		octet_network = netns_net.split(".")

		# Format : ['192','168,'1',['0','24']]
		octet_network[3] = octet_network[3].split("/")

		# Adresse interface veth1 
		for i in octet_network[0,2]:

			addr.


	def netns_commandes(commande,netns_name):

		subprocess.call("ip","netns","exec",netname, commande)

	
	@
	def my_subprocess(shell):

		commande = shell

		tab_commande = commande.split(" ")

		for i in tab_commande[]:

			envoi ="\""+i+"\""+","

		return subprocess.call([envoi])




