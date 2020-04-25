# -*- coding: utf-8 -*-

import empro.toolkit.sipi as sipi

def main():
	momentum_dir=r"F:\ADS2017\Momentum\12.62"
	try:
		sipi.setMomentumDir(momentum_dir)
	except:
		pass
	path=r"F:/FedevelAcademy/Learn to Design your own Board/Files/28Pins/!Design Files/V1I1/28Pins_Project_V1I1/ADS_Simulations/ArduinoUno"
	lib=r"28Pins_Project_V1I1_PCB_lib"
	subst=r"28Pins_Project_V1I1_PCB_lib/28Pins_Project_V1I1_PCB.subst"
	substlib=r"28Pins_Project_V1I1_PCB_lib"
	substname=r"28Pins_Project_V1I1_PCB"
	ltdSubst=r"simulation/28%Pins_%Project_%V1%I1_%P%C%B_lib/28%Pins_%Project_%V1%I1_%P%C%B/sipi%Setup1/proj.ltd"
	cell=r"28Pins_Project_V1I1_PCB"
	layout=r"layout"
	sipiSetup=r"sipiSetup1"
	libS3D=r"simulation/28%Pins_%Project_%V1%I1_%P%C%B_lib/28%Pins_%Project_%V1%I1_%P%C%B/sipi%Setup1/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"F:\ADS2017"

	sipi.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, ltd_subst=ltdSubst, cell=cell, layout_view=layout, sipi_view=sipiSetup, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
