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
		subprocess.call(["echo","net.ipv4.ip_forward = 1",">","/etc/sysctl"])

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

			addr += "."+i  


		# veth1		
		addrVeth1 =addr + "." + "102"

		# veth0

		addrVeth0 = addrVeth1 + "." + "101" 

		# Activation veth1

		subprocess.call(["ip","netns","exec",netns_name,"ifconfig","veth1",addrVeth1+"/24","up"])
	
		#  add a route to the hote

		subprocess.call(["ip","netns","exec",netns_name,"route","add","-net",netns_net,"gw",addrVeth0])

		subprocess.call(["ip","addr","add",addrVeth0,"dev","veth0"])

		# Activation of veth0

		subprocess.call(["ip","link","set","veth0","up"])

		ip link set veth0 up