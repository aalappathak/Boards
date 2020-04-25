# -*- coding: utf-8 -*-

import empro.toolkit.sipi as sipi

def main():
	momentum_dir=r"F:\ADS2017\Momentum\12.62"
	try:
		sipi.setMomentumDir(momentum_dir)
	except:
		pass
	path=r"F:/AltiumDesigner_19/Projects/AcquaFlotador/PCB_Project/AcquaFlotador"
	lib=r"A_Flotador_lib"
	subst=r"A_Flotador_lib/A_Flotador.subst"
	substlib=r"A_Flotador_lib"
	substname=r"A_Flotador"
	ltdSubst=r"simulation/%A_%Flotador_lib/%A_%Flotador/sipi%Setup/proj.ltd"
	cell=r"A_Flotador"
	layout=r"layout"
	sipiSetup=r"sipiSetup"
	libS3D=r"simulation/%A_%Flotador_lib/%A_%Flotador/sipi%Setup/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"F:\ADS2017"

	sipi.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, ltd_subst=ltdSubst, cell=cell, layout_view=layout, sipi_view=sipiSetup, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
