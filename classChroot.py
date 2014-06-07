#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Programme : SecLnx Chroot
# Auteur : Monnin Kanchen
# Licence : GPL
######################################

u"""
Explications
 
 This programme can be use for :
 - Creat own chroot
 - You can creat a user and affect on a chroot
 - You can affecte any shell commande on your own chroot 
 - You can chroot a service like apache, ftp ...
 - You can    

"""

# Importation of external module :

from __future__ import unicode_literals
import os
import sys
import classChroot
import subprocess


class chroot(object):

# Constructor
	def __init__(self, name, path, service, user):

		self.nameChroot = name
		self.pathChroot = path
		self.serviceChroot = service
		self.userChroot = user

# Getteur
	def _get_name(self):
		return self.nameChroot

	def _get_path(self):
		return self.pathChroot 

# Fonction
	def creationChroot():

		name = input(u'Enter the name of your chroot : ')
		subprocess.call(["mkdir", "-p /chroot/"+"name"])
		

		print(u"Your Chroot it's done ! ")




		