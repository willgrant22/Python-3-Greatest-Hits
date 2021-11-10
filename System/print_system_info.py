#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Get and print system info (macOS)
# =============================================================================
import sys, os, psutil, platform, cpuinfo
from datetime import datetime

def sysInfo():
	now = datetime.now()
	exe = now.strftime("%B %d,%Y %H:%M:%S %p")
	nameF = now.strftime('%m-%d-%Y_%I꞉%M꞉%S')

	rel = platform.release()
	node = platform.node()
	mach = platform.machine()
	pro = platform.processor()
	proMod = cpuinfo.get_cpu_info()['brand_raw']
	proPer = psutil.cpu_percent()
	proCur = psutil.cpu_freq()[0] / 1000.000
	cpuAct = psutil.cpu_count(logical=False)
	cpuLog = psutil.cpu_count()

	memTot = psutil.virtual_memory()[0] / 1073741824
	memAvail = psutil.virtual_memory()[1] / 1073741824
	memPer = psutil.virtual_memory()[2]
	memUsed = psutil.virtual_memory()[3] / 1073741824

	sys = platform.system()
	if(sys == 'Darwin'):
		sys = 'Darwin (macOS)'
		vers = platform.mac_ver()[0]
		if vers >= '10.15':
			vers = vers+" "+'(Catalina)'
		elif vers < '10.15' & vers >= '10.14':
			vers = vers+" "+'(Mojave)'
		elif vers < '10.14' & vers >= '10.13':
			vers = vers+" "+'(High Sierra)'
		elif vers < '10.13' & vers >= '10.12':
			vers = vers+" "+'(Sierra)'
		else:
			vers = vers

	systemInfo = f"""
	############################# system #############################

	system				{sys}
	OS Version			{vers}
	Kernel				{rel}
	Architecture			{pro} {mach}
	node				{node}

	############################## CPU ###############################

	CPU brand_raw		{proMod}
	CPU cores			{cpuAct}
	Logical cores			{cpuLog}
	Current Usage			{proPer}%
	Current Frequency		{proCur} Ghz

	############################# MEMORY #############################

	Total Memory      		{memTot} Gb
	Available Memory  		{round(memAvail, 3)} Gb
	Used Memory       		{round(memUsed, 3)} Gb ({memPer}%)
"""
	print(systemInfo)

sysInfo()