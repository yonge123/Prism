# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2018 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.



import os, sys, traceback, time, platform, shutil
from functools import wraps

if platform.system() == "Windows":
	import _winreg, win32com


class Prism_Standalone_Functions(object):
	def __init__(self, core, plugin):
		self.core = core
		self.plugin = plugin


	def err_decorator(func):
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			exc_info = sys.exc_info()
			try:
				return func(*args, **kwargs)
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				erStr = ("%s ERROR - Prism_Plugin_Standalone %s:\n%s\n\n%s" % (time.strftime("%d/%m/%y %X"), args[0].plugin.version, ''.join(traceback.format_stack()), traceback.format_exc()))
				args[0].core.writeErrorLog(erStr)

		return func_wrapper


	@err_decorator
	def startup(self, origin):
		if "loadProject" not in self.core.prismArgs:
			return False


	@err_decorator
	def onProjectChanged(self, origin):
		pass

	
	@err_decorator
	def getCurrentFileName(self, origin, path=True):
		return ""


	@err_decorator
	def onProjectBrowserStartup(self, origin):
		origin.loadOiio()

		origin.closeParm = "closeafterloadsa"
		origin.actionStateManager.setEnabled(False)


	@err_decorator
	def projectBrowserLoadLayout(self, origin):
		pass


	@err_decorator
	def setRCStyle(self, origin, rcmenu):
		pass


	@err_decorator
	def openScene(self, origin, filepath):
		return False


	@err_decorator
	def correctExt(self, origin, lfilepath):
		return lfilepath


	@err_decorator
	def saveScene(self, origin, filepath, underscore=True):
		return


	@err_decorator
	def setSaveColor(self, origin, btn):
		btn.setPalette(origin.savedPalette)


	@err_decorator
	def clearSaveColor(self, origin, btn):
		btn.setPalette(origin.oldPalette)


	@err_decorator
	def setProject_loading(self, origin):
		pass


	@err_decorator
	def onPrismSettingsOpen(self, origin):
		pass


	@err_decorator
	def createProject_startup(self, origin):
		pass


	@err_decorator
	def editShot_startup(self, origin):
		origin.loadOiio()


	@err_decorator
	def shotgunPublish_startup(self, origin):
		pass


	@err_decorator
	def createWinStartMenu(self, origin):
		if platform.system() == "Windows":
			startMenuPath = os.path.join(os.environ["AppData"], "Microsoft", "Windows", "Start Menu", "Programs")
			trayStartup = os.path.join(startMenuPath, "Startup", "PrismTray.lnk")
			trayStartMenu = os.path.join(startMenuPath, "Prism", "PrismTray.lnk")
			pbStartMenu = os.path.join(startMenuPath, "Prism", "PrismProjectBrowser.lnk")
			settingsStartMenu = os.path.join(startMenuPath, "Prism", "PrismSettings.lnk")

			trayLnk = os.path.join(self.core.prismRoot, "Tools", "PrismTray.lnk")
			pbLnk = os.path.join(self.core.prismRoot, "Tools", "PrismProjectBrowser.lnk")
			settingsLnk = os.path.join(self.core.prismRoot, "Tools", "PrismSettings.lnk")

			cbPath = trayStartup

			toolList = [[trayLnk, "PrismTray.exe", "PrismTray.py"], [pbLnk, "PrismProjectBrowser.exe", "PrismCore.py"], [settingsLnk, "PrismSettings.exe", "PrismSettings.py"]]

			for i in toolList:
				if not os.path.exists(os.path.dirname(i[0])):
					os.makedirs(os.path.dirname(i[0]))

				self.core.createShortcut(i[0], vTarget=("%s\Python27\%s" % (self.core.prismRoot, i[1])), args=('"%s\Scripts\%s"' % (self.core.prismRoot, i[2])))

		elif platform.system() == "Linux":
			if os.path.exists(self.core.installLocPath):
				os.chmod(self.core.installLocPath, 0o777)
				
			trayStartup = "/etc/xdg/autostart/PrismTray.desktop"
			trayStartMenu = "/usr/share/applications/PrismTray.desktop"
			pbStartMenu = "/usr/share/applications/PrismProjectBrowser.desktop"
			settingsStartMenu = "/usr/share/applications/PrismSettings.desktop"

			trayLnk = os.path.join(self.core.prismRoot, "Tools", "PrismTray.desktop")
			pbLnk = os.path.join(self.core.prismRoot, "Tools", "PrismProjectBrowser.desktop")
			settingsLnk = os.path.join(self.core.prismRoot, "Tools", "PrismSettings.desktop")

			cbPath = os.path.join(self.core.prismRoot, "Tools", "PrismTray.sh")

			pMenuSource = os.path.join(self.core.prismRoot, "Tools", "Prism.menu")
			pMenuTarget = "/etc/xdg/menus/applications-merged/Prism.menu"

			if not os.path.exists(os.path.dirname(pMenuTarget)):
				try:
					os.makedirs(os.path.dirname(pMenuTarget))
				except:
					pass

			if os.path.exists(pMenuTarget):
				os.remove(pMenuTarget)

			if os.path.exists(pMenuSource) and os.path.exists(os.path.dirname(pMenuTarget)):
				shutil.copy2(pMenuSource, pMenuTarget)
				os.chmod(pMenuTarget, 0o777)
			else:
				print "could not create Prism startmenu entry"

			if os.path.exists(pbLnk):
				userName = os.environ['SUDO_USER'] if 'SUDO_USER' in os.environ else os.environ['USER']
				desktopPath = "/home/%s/Desktop/%s" % (userName, os.path.basename(pbLnk))
				if os.path.exists(desktopPath):
					try:
						os.remove(desktopPath)
					except:
						pass

				if os.path.exists(os.path.dirname(desktopPath)):
					shutil.copy2(pbLnk, desktopPath)
					uid = pwd.getpwnam(userName).pw_uid
					os.chown(desktopPath, uid, -1)

			#subprocess.Popen(['bash', "/usr/local/Prism/Tools/PrismTray.sh"])

		elif platform.system() == "Darwin":
			if os.path.exists(locFile):
				os.chmod(locFile, 0o777)
			
			userName = os.environ['SUDO_USER'] if 'SUDO_USER' in os.environ else os.environ['USER']
			trayStartup = "/Users/%s/Library/LaunchAgents/com.user.PrismTray.plist" % userName
			trayStartMenu = "/Applications/Prism/Prism Tray.app"
			pbStartMenu = "/Applications/Prism/Prism Project Browser.app"
			settingsStartMenu = "/Applications/Prism/Prism Settings.app"

			trayStartupSrc = os.path.join(self.core.prismRoot, "Tools", "com.user.PrismTray.plist")
			trayLnk = os.path.join(self.core.prismRoot, "Tools", "Prism Tray.app")
			pbLnk = os.path.join(self.core.prismRoot, "Tools", "Prism Project Browser.app")
			settingsLnk = os.path.join(self.core.prismRoot, "Tools", "Prism Settings.app")

			cbPath = os.path.join(self.core.prismRoot, "Tools", "PrismTray.sh")

			if os.path.exists(pbLnk):
				desktopPath = "/Users/%s/Desktop/%s" % (userName, os.path.splitext(os.path.basename(pbLnk))[0])
				if os.path.exists(desktopPath):
					try:
						os.remove(desktopPath)
					except:
						pass
				os.symlink(pbLnk, desktopPath)

			#subprocess.Popen(['bash', "/usr/local/Prism/Tools/PrismTray.sh"])


		if trayStartMenu != "" and not os.path.exists(os.path.dirname(trayStartMenu)):
			try:
				os.makedirs(os.path.dirname(trayStartMenu))
			except:
				pass

		if not os.path.exists(os.path.dirname(trayStartup)):
			try:
				os.makedirs(os.path.dirname(trayStartup))
				if platform.system() in ["Linux", "Darwin"]:
					os.chmod(os.path.dirname(trayStartup), 0o777)
			except:
				pass

		if os.path.exists(trayStartup):
			os.remove(trayStartup)

		if os.path.exists(trayLnk):
			if os.path.exists(os.path.dirname(trayStartup)):
				if platform.system() == "Darwin":
					if os.path.exists(trayStartupSrc):
						shutil.copy2(trayStartupSrc, trayStartup)
						os.chmod(trayStartup, 0o644)
						uid = pwd.getpwnam(userName).pw_uid
						os.chown(os.path.dirname(trayStartup), uid, -1)
						os.chown(trayStartup, uid, -1)
					#	os.system("launchctl load /Users/%s/Library/LaunchAgents/com.PrismTray.plist" % userName)
				else:
					shutil.copy2(trayLnk, trayStartup)
					os.chmod(trayStartup, 0o777)
			else:
				print "could not create PrismTray autostart entry"

			if trayStartMenu != "":
				if os.path.exists(os.path.dirname(trayStartMenu)):
					if os.path.isdir(trayLnk):
						if os.path.exists(trayStartMenu):
							shutil.rmtree(trayStartMenu)
						shutil.copytree(trayLnk, trayStartMenu)
					else:
						shutil.copy2(trayLnk, trayStartMenu)
						os.chmod(trayStartMenu, 0o777)
				else:
					print "could not create PrismTray startmenu entry"

		if pbStartMenu != "":
			if os.path.exists(pbLnk) and os.path.exists(os.path.dirname(pbStartMenu)):
				if os.path.isdir(pbLnk):
					if os.path.exists(pbStartMenu):
						shutil.rmtree(pbStartMenu)
					shutil.copytree(pbLnk, pbStartMenu)
				else:
					shutil.copy2(pbLnk, pbStartMenu)
					os.chmod(pbStartMenu, 0o777)
			else:
				print "could not create PrismProjectBrowser startmenu entry"

		if settingsStartMenu != "":
			if os.path.exists(settingsLnk) and os.path.exists(os.path.dirname(settingsStartMenu)):
				if os.path.isdir(settingsLnk):
					if os.path.exists(settingsStartMenu):
						shutil.rmtree(settingsStartMenu)
					shutil.copytree(settingsLnk, settingsStartMenu)
				else:
					shutil.copy2(settingsLnk, settingsStartMenu)
					os.chmod(settingsStartMenu, 0o777)
			else:
				print "could not create PrismSettings startmenu entry"