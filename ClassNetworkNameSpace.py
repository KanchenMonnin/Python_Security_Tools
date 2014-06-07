#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Programme : SecLnx Network NameSpace
# Auteur : Monnin Kanchen
# Licence : GPL
######################################

u"""
Explications
 
 

"""

# Importation of external module :

from __future__ import unicode_literals
import os
import sys
import subprocess


class netns(object):

	def __init__(self, name, network):

		# Nom du network nameSpace
		self.netns_name = name

		# Sous réseau du network nameSpace
		# format : 192.168.1.0/24
		self.netns_net = network


	def creat(self,netns_net, netns_name):

		# Activation du routtage pour distribution avec systemd
		subprocess.call("echo","net.ipv4.ip_forward = 1",">","/etc/sysctl")

		# Création de l'espace de nommage
		subprocess.call(["ip","netns","ad",netns_name])

		# Création des deux cartes virtuelles
		subprocess.call(["ip", "link", "add", "veth0", "type", "veth", "peer", "name", "veth1"])

		# Liaison de la carte veth1 au namespace
		subprocess.call(["ip", "link", "set", "veth1", "netns", netns_name])

		# Sous réseau du network nameSpace
		octet_network = netns_net.split(".")

		# Format sortie : ['192','168,'1',['0','24']]
		octet_network[3] = octet_network[3].split("/")

		# Adresse carte veth1 
		for i in octet_network[0,2]:

			addr.


	def netns_commandes(commande,netns_name):

		subprocess.call("ip","netns","exec",netname, commande)

	# Rendre la fonction commme étant un object
	@
	def my_subprocess(shell):

		commande = shell

		tab_commande = commande.split(" ")

		for i in tab_commande[]:

			envoi ="\""+i+"\""+","

		return subprocess.call([envoi])




