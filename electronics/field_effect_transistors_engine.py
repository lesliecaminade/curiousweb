from generator import constants_conversions as c
from generator import random_handler as ran
import sympy as sym
import math
import random
from generator.latex_engine import LATEX_SOLUTION_PREFIX as lp
from generator.latex_engine import LATEX_SOLUTION_SUFFIX as ls

x, y, z = sym.symbols('x y z', real = True)#generic variables

class boylestad_7_1:
	def __init__(self,**kwargs):
		print('preparing 7_1')
		regen = True
		counter = 100
		while regen and (not counter < 0 ):
			counter = counter - 1

			vdd = c.voltage(ran.main(16))
			rd = c.resistance(ran.main(2000))
			rg = c.resistance(ran.main(1e6))
			vgg = c.voltage(ran.main(2))
			idss = c.current(ran.main(10), 'mA')
			vgsoff = c.voltage(ran.main(-8))

			self.question = f"""Determine: VDS for a fixed bias JFET circuit with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, VGG = {vgg.V:.4g} V, RG = {rg.Mohms:.4g} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:.4g} mA and Vgsoff = {vgsoff.V:.4g} V. The source is grounded."""

			idsat = c.current(vdd.V / rd.ohms)
			vgs = c.voltage( -vgg.V )
			id = c.current(
			idss.A * (1 - (vgs.V / vgsoff.V))**2
			)
			vds = c.voltage(vdd.V - id.A * rd.ohms)
			vd = c.voltage(vds.V)
			vg = c.voltage(vgs.V)
			vs = c.voltage(0)

			if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
				regen = False

		self.answer = f"""{vds.V:.4g} V"""

		self.latex_solution = f"""{lp}
I_{{ \\text{{D sat}}}} &= \\frac{{ V_{{ \\text{{DD}}}}}} {{ R_{{ \\text{{D}}}}}} \\\\
&= \\frac{{ {vdd.V:.4g}}} {{ {rd.ohms:.4g}}} \\\\
&= {idsat.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= - V_{{ \\text{{GG}}}} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ V_{{ \\text{{GS}}}}}} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
&= {idss.A:.4g} \\left(1 - \\frac{{ {vgs.V:.4g}}} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
&= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}}}} &= V_{{ \\text{{GS}}}} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{S}}}} &= 0 \\text{{ V}} \\\\
{ls}"""

class DC_Fixed_Bias():
	def __init__(self,**kwargs):
		print('preparing DC fixed bias')
		regen = True
		while regen:

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			rg = c.resistance(ran.main(kwargs['rg']))
			vgg = c.voltage(ran.main(kwargs['vgg']))
			idss = c.current(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))

			self.question = f"""Determine: VDS for a fixed bias JFET circuit with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, VGG = {vgg.V:.4g} V, RG = {rg.Mohms:.4g} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:.4g} mA and Vgsoff = {vgsoff.V:.4g} V. The source is grounded."""
			idsat = c.current(vdd.V / rd.ohms)
			vgs = c.voltage( -vgg.V )
			id = c.current(
			idss.A * (1 - (vgs.V / vgsoff.V))**2
			)
			vds = c.voltage(vdd.V - id.A * rd.ohms)
			vd = c.voltage(vds.V)
			vg = c.voltage(vgs.V)
			vs = c.voltage(0)

			if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
				regen = False

		self.answer = f"""{vds.V:.4g} V"""
# 		self.latex_solution = f"""{lp}
# V_{{ \\text{{GS}}}} &= -V_{{ \\text{{GG}}}} \\\\
# &= {vgs.V:.4g} \\text{{ V}} \\\\
# \\\\
# I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ V_{{ \\text{{GS}}}}}} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
# &= {idss.A:.4g} \\left(1 -  \\frac{{ {vgs.V:.4g}}} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
# &= {id.A:.4g} \\text{{ A}} \\\\
# \\\\
# V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
# &= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
# &= {vds.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} \\\\
# &= {vds.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{G}}}} &= V_{{ \\text{{GS}}}} \\\\
# &= {vg.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{S}}}} &= 0 \\text{{ V}} \\\\
# {ls}"""

class boylestad_7_2:
	def __init__(self,*args,**kwargs):
		print('preparing 7_2')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(20))
			rd = c.resistance(ran.main(3300))
			rg = c.resistance(ran.main(1e6))
			rs = c.resistance(ran.main(1e3))
			idss = c.current(ran.main(8), 'mA')
			vgsoff = c.voltage(ran.main(-6))

			self.question = f"""Determine VDS for a self-biased JFET with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RG = {rg.Mohms:.4g} Mohms, RS = {rs.kohms:.4g} kohms, and VSS = 0V. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V. The source resistance and the gate resistance are grounded."""

			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x, domain = sym.S.Reals)
			print(idset)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(  - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print(vgslist[i])
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vs = c.voltage(id.A * rs.ohms)
					vg = c.voltage(0)
					vd = c.voltage(vds.V + vs.V)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1- \\frac{{ - I_{{ \\text{{D}}}}  R_{{ \\text{{S}}}}    }}{{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ - I_{{ \\text{{D}} }} \\cdot {rs.ohms:.4g}   }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}}\\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{S}}}} + R_{{ \\text{{D}}}}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rs.ohms:.4g} + {rd.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}}}} &= 0 \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} + V_{{ \\text{{S}}}} \\\\
&= {vds.V:.4g} + {vs.V:.4g} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
{ls}"""

class DC_Self_Biased():
	def __init__(self,**kwargs):
		print('preparing DC Self Biased')
		regen = True
		while regen:

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			rg = c.resistance(ran.main(kwargs['rg']))
			rs = c.resistance(ran.main(kwargs['rs']))
			idss = c.current(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))


			self.question = f"""Determine VDS for a self-biased JFET with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RG = {rg.Mohms:.4g} Mohms, RS = {rs.kohms:.4g} kohms, and VSS = 0V. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V. The source resistance and the gate resistance are grounded."""

			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(  - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print(vgslist[i])
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vs = c.voltage(id.A * rs.ohms)
					vg = c.voltage(0)
					vd = c.voltage(vds.V + vs.V)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
# 		self.latex_solution = f"""{lp}
# I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1- \\frac{{ - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}}    }}{{{ V_{{ \\text{{GS off}}}}}}}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g} }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
# \\\\
# V_{{ \\text{{GS}}}} &= - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
# &= - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
# &= {vgs.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{S}}}} + R_{{ \\text{{D}}}}\\right)\\\\
# &= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rs.ohms:.4g} + {rd.ohms:.4g}\\right)\\\\
# &= {vds.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
# &= {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
# &= {vs.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{G}}}} &= 0 \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} + V_{{ \\text{{S}}}} \\\\
# &= {vds.V:.4g} + {vs.V:.4g} \\\\
# &= {vd.V:.4g} \\text{{ V}} \\\\
# {ls}"""


class boylestad_7_4:
	def __init__(self,*args,**kwargs):
		print('preparing 7_4')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(16))
			rd = c.resistance(ran.main(2.4e3))
			r1 = c.resistance(ran.main(2.1e6))
			r2 = c.resistance(ran.main(270e3))
			rs = c.resistance(ran.main(1.5e3))
			idss = c.current(ran.main(8), 'mA')
			vgsoff = c.voltage(ran.main(-4))


			self.question = f"""Determine VDS for a voltage divider biased JFET with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, R2(bleeder) = {r2.kohms:.4g} kohms and both the bleeder and source resistances are grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""

			vg = c.voltage(
			(r2.ohms * vdd.V) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
			)

			idsat = c.current(vdd.V / (rd.ohms  + rs.ohms ))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( vg.V - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rd.ohms + rs.ohms))

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idss.A and idlist[i] < idsat.A:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vd = c.voltage(vdd.V - id.A * rd.ohms)
					vs = c.voltage(id.A * rs.ohms)
					vds = c.voltage(vdslist[i])
					vdg = c.voltage(vd.V - vg.V)
					regen = False


		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}} }}   R_{{ \\text{{2}}}}   }} {{ R_{{ \\text{{1}} }}  + R_{{ \\text{{2}}}}  }} \\\\
&= \\frac{{ {vdd.V:.4g}  \\cdot {r2.ohms:.4g}}} {{ {r1.ohms:.4g} + {r2.ohms:.4g}}} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}}   }} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ {vg.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g}   }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {id.A:.4g} \\cdot {rs.ohms} \\\\
&= {vs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{D}}}}  + R_{{ \\text{{S}}}}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rd.ohms:.4g} + {rs.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DG}}}} &= V_{{ \\text{{D}}}} - V_{{ \\text{{G}}}} \\\\
&= {vd.V:.4g} - {vg.V:.4g} \\\\
&= {vdg.V:.4g} \\text{{ V}} \\\\
{ls}"""


class DC_Voltage_Divider():
	def __init__(self, **kwargs):
		print('preparing DC_voltage_Divider')
		regen = True
		while regen:

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			r1  =  c.resistane(ran.main(kwargs['r1']))
			r2 = c.resistance(ran.main(kwargs['r2']))
			rs = c.resistance(ran.main(kwargs['rs']))
			idss = c.current(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))


			self.question = f"""Determine VDS for a voltage divider biased JFET with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, R2(bleeder) = {r2.kohms:.4g} kohms and both the bleeder and source resistances are grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""

			vg = c.voltage(
			(r2.ohms * vdd.V) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
			)

			idsat = c.current(vdd.V / (rd.ohms  + rs.ohms ))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( vg.V - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rd.ohms + rs.ohms))

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idss.A and idlist[i] < idsat.A:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vd = c.voltage(vdd.V - id.A * rd.ohms)
					vs = c.voltage(id.A * rs.ohms)
					vds = c.voltage(vdslist[i])
					vdg = c.voltage(vd.V - vg.V)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
# 		self.latex_solution = f"""{lp}
# V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}} }}   R_{{ \\text{{2}}}}   }} {{ R_{{ \\text{{1}} }}  + R_{{ \\text{{2}}}}  }} \\\\
# &= \\frac{{ {vdd.V:.4g}  \\cdot {r2.ohms:.4g}}} {{ {r1.ohms:.4g} + {r2.ohms:.4g}}} \\\\
# &= {vg.V:.4g} \\text{{ V}} \\\\
# \\\\
# I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}}   }} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ {vg.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g}   }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
# \\\\
# V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
# &= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
# &= {vgs.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{D}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
# &= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
# &= {vd.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
# &= {id.A:.4g} \\cdot {rs.ohms} \\\\
# &= {vs.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{D}}}}  + R_{{ \\text{{S}}}}\\right) \\\\
# &= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rd.ohms:.4g} + {rs.ohms:.4g}\\right) \\\\
# &= {vds.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{DG}}}} &= V_{{ \\text{{D}}}} - V_{{ \\text{{G}}}} \\\\
# &= {vd.V:.4g} - {vg.V:.4g} \\\\
# &= {vdg.V:.4g} \\text{{ V}} \\\\
# {ls}"""


class boylestad_7_5:
	def __init__(self,*args,**kwargs):
		print('preparing 7_5')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(12))
			rd = c.resistance(ran.main(1.5e3))
			rs = c.resistance(ran.main(680))
			idss = c.current(ran.main(12), 'mA')
			vgsoff = c.voltage(ran.main(-6))


			self.question = f"""Determine VDS for a common-gate JFET configuration with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.ohms:.4g} ohms, with the gate and the source resistance grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""


			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)

			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( - idlist[i] * rs.ohms)
				vdslist.append(   (vdd.V - idlist[i] * rd.ohms) - (idlist[i] * rs.ohms) )

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print('VDStest' + str(vdslist[i]))
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vd = c.voltage(vdd.V - id.A * rd.ohms)
					vg = c.voltage(0)
					vs = c.voltage(id.A * rs.ohms)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} }} {{  V_{{ \\text{{GSoff}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g}     }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}}\\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}}}} &= 0 \\text{{ V}}\\\\
\\\\
V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vs.V:.4g} \\text{{ V}} \\\\
{ls}"""

class DC_Common_Gate():
	def __init__(self,**kwargs):
		print('preparing DC Common Gate')
		regen = True
		while regen:

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			rs = c.resistance(ran.main(kwargs['rs']))
			idss = c.current(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))


			self.question = f"""Determine VDS for a common-gate JFET configuration with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.ohms:.4g} ohms, with the gate and the source resistance grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""


			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)

			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( - idlist[i] * rs.ohms)
				vdslist.append(   (vdd.V - idlist[i] * rd.ohms) - (idlist[i] * rs.ohms) )

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print('VDStest' + str(vdslist[i]))
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vd = c.voltage(vdd.V - id.A * rd.ohms)
					vg = c.voltage(0)
					vs = c.voltage(id.A * rs.ohms)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""

class boylestad_7_6:
	def __init__(self,*args,**kwargs):
		print('preparing 7_6')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(18))
			rd = c.resistance(ran.main(1.8e3))
			r1 = c.resistance(ran.main(110e6))
			r2 = c.resistance(ran.main(10e6))
			rs = c.resistance(ran.main(750))
			idss = c.current(ran.main(6), 'mA')
			vgsoff = c.voltage(ran.main(-3))


			self.question  = f"""For an n - channel depletion type MOSFET biased by a voltage divider method, determine VDS, if VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, R2(bleeder) = {r2.Mohms:.4g} Mohms, RS = {rs.ohms:.4g} ohms. The bleeder resistor and the source resistor are grounded. The MOSFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vg.V - idlist[i] * rs.ohms)
				vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vdslist[i] > 0 and vgslist[i] > vgsoff.V and idlist[i] < idsat.A:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}} }}  R_{{ \\text{{2}}}} }} {{ R_{{ \\text{{1}} }}   + R_{{ \\text{{2}}}} }} \\\\
&= \\frac{{ {vdd.V:.4g} \\cdot {r2.ohms:.4g}}} {{ {r1.ohms:.4g}  + {r2.ohms:.4g}}} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ V_{{ \\text{{G}} }}  - I_{{ \\text{{D}} }}  R_{{ \\text{{S}} }} }} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ {vg.V:.4g} - I_{{ \\text{{D}} }}  \\cdot {rs.ohms:.4g}}} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left( R_{{ \\text{{D}}}} + R_{{ \\text{{S}}}}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rd.ohms:.4g} + {rs.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
{ls}"""

class DC_DMOS_Voltage_Divider():
	def __init__(self,**kwargs):
		print('preparing 7_6')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			r1 = c.resistance(ran.main(kwargs['r1']))
			r2 = c.resistance(ran.main(kwargs['r2']))
			rs = c.resistance(ran.main(kwargs['rs']))
			idss = c.current(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))

			self.question  = f"""For an n - channel depletion type MOSFET biased by a voltage divider method, determine VDS, if VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, R2(bleeder) = {r2.Mohms:.4g} Mohms, RS = {rs.ohms:.4g} ohms. The bleeder resistor and the source resistor are grounded. The MOSFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vg.V - idlist[i] * rs.ohms)
				vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vdslist[i] > 0 and vgslist[i] > vgsoff.V and idlist[i] < idsat.A:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		self.answer = f"""{vds.V:.4g} V"""

class boylestad_7_8:
	def __init__(self,*args,**kwargs):
		print('preparing 7_8')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(18))
			rd = c.resistance(ran.main(1.8e3))
			r1 = c.resistance(ran.main(110e6))
			r2 = c.resistance(ran.main(10e6))
			rs = c.resistance(ran.main(750))
			idss = c.current(ran.main(6), 'mA')
			vgsoff = c.voltage(ran.main(-3))


			self.question  = f"""For an n - channel depletion type MOSFET biased by a voltage divider method, determine VDS, if VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, R2(bleeder) = {r2.Mohms:.4g} Mohms, RS = {rs.ohms:.4g} ohms. The bleeder resistor and the source resistor are grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rs.ohms + rd.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vg.V - idlist[i] * rs.ohms)
				vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vdslist[i] > 0 and vgslist[i] > vgsoff.V and idlist[i] < idsat.A:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}} }}  R_{{ \\text{{2}}}}    }} {{ R_{{ \\text{{1}} }}   + R_{{ \\text{{2}}}}  }} \\\\
&= \\frac{{ {vdd.V:.4g} \\cdot {r2.ohms:.4g}}} {{ {r1.ohms:.4g} + {r2.ohms:.4g}}} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{G}} }}  - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }}   }} {{ V_{{ \\text{{GSoff}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ {vg.V:.4g} - I_{{ \\text{{D}} }}  \\cdot {rs.ohms:.4g}  }} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{D}} }} + R_{{ \\text{{S}} }}   \\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\left({rd.ohms:.4g} + {rs.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
{ls}"""


class boylestad_7_10:
	def __init__(self,*args,**kwargs):
		print('preparing 7_10')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(12))
			rd = c.resistance(ran.main(2000))
			rf = c.resistance(ran.main(10e6))
			idon = c.current(ran.main(6), 'mA')
			vgsth = c.voltage(ran.main(3))
			vgson = c.voltage(vgsth.V + ran.main(5))

			self.question = f"""Determine VDSQ for an enhancement type MOSFET that uses a feedback biasing arrangement with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RF = {rf.Mohms:.4g} Mohms, and the source grounded. The MOSFET has characteristics IDon = {idon.mA:.4g} mA, VGSon = {vgson.V:.4g} V, and VGSth = {vgsth.V:.4g} V."""

			k  = (idon.A) / ((vgson.V - vgsth.V)**2)

			equation = sym.Eq(
			x,
			k * (( ((vdd.V) - (x * rd.ohms)) - vgsth.V )**2)
			)
			idsat = c.current(vdd.V / (rd.ohms))
			idset = sym.solveset(equation, x, domain = sym.Reals)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vdd.V - idlist[i] * rd.ohms)
				vdslist.append(vdd.V - idlist[i] * rd.ohms)

			for i in range(len(idlist)):
				if vgslist[i] > vgsth.V and vdslist[i] > 0:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vgs.V)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
k &= \\frac{{ I_{{ \\text{{D on}}}}}} {{ \\left( V_{{ \\text{{GS on}} }} - V_{{ \\text{{GS th}}}}\\right)^2}} \\\\
&= \\frac{{ {idon.A:.4g}}} {{ \\left({vgson.V:.4g} - {vgsth.V:.4g}\\right)^2}} \\\\
&= {k:.4g} \\frac{{A}} {{ V^2}} \\\\
\\\\
I_{{ \\text{{D}}}} &= k \\left( \\left(V_{{ \\text{{DD}} }} - I_{{ \\text{{D}} }} R_{{ \\text{{D}} }} \\right) - V_{{ \\text{{GS th}}}}	\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {k:.4g} \\left( \\left({vdd.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rd.ohms:.4g}\\right) - {vgsth.V:.4g}	\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
{ls}"""


class DC_EMOS_Feedback_Biasing():
	def __init__(self,**kwargs):
		print('preparing DC_EMOS_Feedback_Biasing')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			rf = c.resistance(ran.main(kwargs['rf']))
			idon = c.current(ran.main(kwargs['idon']))
			vgsth = c.voltage(ran.main(kwargs['vgsth']))
			vgson = c.voltage(ran.main(kwargs['vgson']))

			self.question = f"""Determine VDSQ for an enhancement type MOSFET that uses a feedback biasing arrangement with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RF = {rf.Mohms:.4g} Mohms, and the source grounded. The MOSFET has characteristics IDon = {idon.mA:.4g} mA, VGSon = {vgson.V:.4g} V, and VGSth = {vgsth.V:.4g} V."""

			k  = (idon.A) / ((vgson.V - vgsth.V)**2)

			equation = sym.Eq(
			x,
			k * (( ((vdd.V) - (x * rd.ohms)) - vgsth.V )**2)
			)
			idsat = c.current(vdd.V / (rd.ohms))
			idset = sym.solveset(equation, x, domain = sym.Reals)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vdd.V - idlist[i] * rd.ohms)
				vdslist.append(vdd.V - idlist[i] * rd.ohms)

			for i in range(len(idlist)):
				if vgslist[i] > vgsth.V and vdslist[i] > 0 and vgson.V > vgsth.V:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vgs.V)
					regen = False

		self.answer = f"""{vds.V:.4g} V"""

class boylestad_7_11:
	def __init__(self,*args,**kwargs):
		print('preparing 7_11')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(40))
			rd = c.resistance(ran.main(3000))
			r1 = c.resistance(ran.main(22e6))
			r2 = c.resistance(ran.main(18e6))
			rs = c.resistance(ran.main(0.82e3))
			vgsth = c.voltage(ran.main(5))
			idon = c.current(ran.main(3), 'mA')
			vgson = c.voltage(vgsth.V + ran.main(5))

			self.question = f"""Determine VDS for an enhancement MOSFET in a voltage divider configuration where VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, RS = {rs.kohms:.4g} kohms, R2(bleeder) = {r2.Mohms:.4g} Mohms where the bleeder and the source resistors are grounded. The MOSFET has characteristics VGSth = {vgsth.V:.4g} V, IDon = {idon.mA:.4g} mA at VGSon = {vgson.V:.4g} V."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r2.ohms + r1.ohms)
			)

			k = (idon.A) / ((vgson.V - vgsth.V)**2)

			equation = sym.Eq(
			x,
			k * (((vg.V - x * rs.ohms) - vgsth.V )**2)
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x, domain = sym.Reals)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vg.V - idlist[i] * rs.ohms)
				vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vgslist[i] > vgsth.V and vdslist[i] > 0:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		self.answer = f"""VDS = {vds.V:.4g} V"""
		self.latex_solution = f"""{lp}
V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}} }} R_{{ \\text{{2}} }} }} {{ R_{{ \\text{{1}} }} + R_{{ \\text{{2}} }} }} \\\\
&= \\frac{{ {vdd.V:.4g} \\cdot {r2.ohms:.4g} }} {{ {r1.ohms:.4g} + {r2.ohms:.4g}}} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\
k &= \\frac{{ I_{{ \\text{{D on}} }} }} {{ \\left(V_{{ \\text{{GSon}} }} - V_{{ \\text{{GSth}}}}  \\right)^2 }} \\\\
&= \\frac{{ {idon.A:.4g}}} {{ \\left( {vgson.V:.4g} - {vgsth.V:.4g}\\right)^2}} \\\\
&= {k:.4g} \\frac{{A}} {{V^2}} \\\\
\\\\
I_{{ \\text{{D}}}} &= k \\left(	\\left( V_{{ \\text{{G}} }} - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} \\right) - V_{{ \\text{{GSth}}}}	\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {k:.4g} \\left( \\left( {vg.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g}	\\right) - {vgsth.V:.4g}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left( R_{{ \\text{{S}} }} + R_{{ \\text{{D}}}}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left({rs.ohms:.4g} + {rd.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{V}} \\\\
{ls}"""

class DC_EMOS_Voltage_Divider():
	def __init__(self,**kwargs):
		print('preparing DC_EMOS_Voltage_Divider')
		regen = True
		while regen:

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			r1 = c.resistance(ran.main(kwargs['r1']))
			r2 = c.resistance(ran.main(kwargs['r2']))
			rs = c.resistance(ran.main(kwargs['rs']))
			vgsth = c.voltage(ran.main(kwargs['vgsth']))
			idon = c.current(ran.main(kwargs['idon']))
			vgson = c.voltage(ran.main(kwargs['vgson']))

			self.question = f"""Determine VDS for an enhancement MOSFET in a voltage divider configuration where VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, R1(limiter) = {r1.Mohms:.4g} Mohms, RS = {rs.kohms:.4g} kohms, R2(bleeder) = {r2.Mohms:.4g} Mohms where the bleeder and the source resistors are grounded. The MOSFET has characteristics VGSth = {vgsth.V:.4g} V, IDon = {idon.mA:.4g} mA at VGSon = {vgson.V:.4g} V."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r2.ohms + r1.ohms)
			)

			k = (idon.A) / ((vgson.V - vgsth.V)**2)


			equation = sym.Eq(
			x,
			k * (((vg.V - x * rs.ohms) - vgsth.V )**2)
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x, domain = sym.Reals)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(vg.V - idlist[i] * rs.ohms)
				vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vgslist[i] > vgsth.V and vdslist[i] > 0 and vgson.V > vgsth.V:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		self.answer = f"""VDS = {vds.V:.4g} V"""


class boylestad_8_7:
	def __init__(self,*args,**kwargs):
		print('preparing 8_7')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(16))
			rd = c.resistance(ran.main(2000))
			rg = c.resistance(ran.main(1e6))
			vgg = c.voltage(ran.main(2))
			idss = c.current(ran.main(10), 'mA')
			vgsoff = c.voltage(ran.main(-8))
			yos = c.conductance(ran.main(40), 'uS')

			self.question = f"""Determine: Zi, Zo, Av considering rd, and Av without considering rd, for a fixed bias JFET circuit with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, VGG = {vgg.V:.4g} V, RG = {rg.Mohms:.4g} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:.4g} mA and Vgsoff = {vgsoff.V:.4g} V. The source is grounded."""


			idsat = c.current(vdd.V / rd.ohms)
			vgs = c.voltage( -vgg.V )
			id = c.current(
			idss.A * (1 - (vgs.V / vgsoff.V))**2
			)
			vds = c.voltage(vdd.V - id.A * rd.ohms)
			vd = c.voltage(vds.V)
			vg = c.voltage(vgs.V)
			vs = c.voltage(0)

			if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
				regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * ( 1 -  (vgs.V / vgsoff.V))
		)

		rdsmall = c.resistance( 1/ yos.S )

		zi = c.resistance( rg.ohms )

		zo = rd.parallel(rdsmall)

		av = - gm.S * zo.ohms

		av_nord = - gm.S * rd.ohms

		self.answer = f"""{zi.Mohms:.4g} Mohms, {zo.kohms:.4g} kohms, {av:.4g}, {av_nord:.4g}"""

		self.latex_solution = f"""{lp}
V_{{ \\text{{GS}}}} &= - V_{{ \\text{{GG}}}} \\\\
&= {vgs.V:.4g} \\text{{V}} \\\\
\\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{GS}} }} }}{{ V_{{ \\text{{GSoff}} }} }}\\right)^2 \\\\
&= {idss.A:.4g} \\left( 1 - \\frac{{ {vgs.V:.4g}}} {{ {vgsoff.V:.4g}}}\\right)^2 \\\\
&= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}} }} - I_{{ \\text{{D}} }} R_{{ \\text{{D}} }} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}} }} &= V_{{ \\text{{DS}}}} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}} }} &= V_{{ \\text{{GS}}}} \\\\
&= {vg.V:.4g} \\text{{ v}} \\\\
\\\\
V_{{ \\text{{S}}}} &= 0 \\text{{ V}} \\\\
\\\\
g_{{ \\text{{m}}}} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }} {{| V_{{ \\text{{GSoff}} }} | }}  \\left(1 -  \\frac{{ V_{{ \\text{{GS}}}}}} {{ V_{{ \\text{{GSoff}}}}}}\\right)\\\\
&= \\frac{{ 2 \\cdot {idss.A:.4g}}} {{| {vgsoff.V:.4g}|}} \\left(1 -  \\frac{{ {vgs.V:.4g}}} {{ {vgsoff.V:.4g}}}\\right)\\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\
r_{{ \\text{{d}}}} &= \\frac{{1}}{{y_{{ \\text{{os}}}}}} \\\\
&= \\frac{{1}}{{ {yos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i}}}} &= R_{{ \\text{{G}}}} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o}}}} &= R_{{ \\text{{D}}}} || r_{{ \\text{{d}}}} \\\\
&= {rd.ohms:.4g} || {rdsmall.ohms:.4g} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\
A_{{ \\text{{v}}}} &= - g_{{ \\text{{m}} }} Z_{{ \\text{{o}}}} \\\\
&= - {gm.S:.4g} \\cdot {zo.ohms:.4g} \\\\
&= {av:.4g} \\\\
\\\\
A_{{ \\text{{v nord}}}} &= - g_{{ \\text{{m}} }} R_{{ \\text{{S}}}}\\\\
&= - {gm.S:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {av_nord} \\\\
{ls}"""

class AC_Fixed_Bias():
	def __init__(self,**kwargs):
		print('preparing AC_Fixed_Bias')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(16))
			rd = c.resistance(ran.main(2000))
			rg = c.resistance(ran.main(1e6))
			vgg = c.voltage(ran.main(2))
			idss = c.current(ran.main(10), 'mA')
			vgsoff = c.voltage(ran.main(-8))
			yos = c.conductance(ran.main(40), 'uS')

			vdd = c.voltage(ran.main(kwargs['vdd']))
			rd = c.resistance(ran.main(kwargs['rd']))
			rg = c.resistance(ran.main(kwargs['rg']))
			vgg = c.voltage(ran.main(kwargs['vgg']))
			idss = c.voltage(ran.main(kwargs['idss']))
			vgsoff = c.voltage(ran.main(kwargs['vgsoff']))

			yos = c.conductance(ran.main(kwargs['yos']))

			self.question = f"""Determine: Zi, Zo, Av considering rd, and Av without considering rd, for a fixed bias JFET circuit with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, VGG = {vgg.V:.4g} V, RG = {rg.Mohms:.4g} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:.4g} mA and Vgsoff = {vgsoff.V:.4g} V. The source is grounded."""


			idsat = c.current(vdd.V / rd.ohms)
			vgs = c.voltage( -vgg.V )
			id = c.current(
			idss.A * (1 - (vgs.V / vgsoff.V))**2
			)
			vds = c.voltage(vdd.V - id.A * rd.ohms)
			vd = c.voltage(vds.V)
			vg = c.voltage(vgs.V)
			vs = c.voltage(0)

			if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
				regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * ( 1 -  (vgs.V / vgsoff.V))
		)

		rdsmall = c.resistance( 1/ yos.S )

		zi = c.resistance( rg.ohms )

		zo = rd.parallel(rdsmall)

		av = - gm.S * zo.ohms

		av_nord = - gm.S * rd.ohms

		self.answer = f"""{zi.Mohms:.4g} Mohms, {zo.kohms:.4g} kohms, {av:.4g}, {av_nord:.4g}"""

# 		self.latex_solution = f"""{lp}
# V_{{ \\text{{GS}}}} &= - V_{{ \\text{{GG}}}} \\\\
# &= {vgs.V:.4g} \\text{{ V}} \\\\
# \\\\
# I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{GS}}}}}} {{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {idss.A:.4g} \\cdot \\left( 1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g} }}\\right)^2 \\\\
# I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
# \\\\
# V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
# &= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
# &= {vds.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} \\\\
# &= {vd.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{G}}}} &= V_{{ \\text{{GS}}}} \\\\
# &= {vg.V:.4g} \\text{{ V}} \\\\
# \\\\
# V_{{ \\text{{S}}}} &= 0 \\text{{ V}} \\\\
# \\\\
# g_{{ \\text}} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }} {{| V_{{ \\text{{GS}}}}|}}					\\left(1 - \\frac{{ V_{{ \\text{{ GS}} }} }} {{ V_{{ \\text{{GS off}} }} }}      \\right) \\\\
# &= \\frac{{ 2 \\cdot {idss.A:.4g} }} }} {{| {vgsoff.V:.4g}|}}					\\left(1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g} }} \\right) \\\\
# &= {gm.S:.4g} \\text{{ S}} \\\\
# \\\\
# r_{{ \\text{{d}}}} &= \\frac{{ 1}} {{ y_{{ \\text{{os}}}}}} \\\\
# &= \\frac{{ 1}} {{ {yos.S:.4g}}} \\\\
# &= {rdsmall.ohms:.4g} \\Omega \\\\
# \\\\
# Z_{{ \\text{{i}}}} &= R_{{ \\text{{G}}}} \\\\
# &= {zi.ohms:.4g} \\Omega \\\\
# \\\\
# Z_{{ \\text{{o}}}} &= R_{{ \\text{{D}}}} || r_{{ \\text{{d}}}} \\\\
# &= {rd.ohms:.4g} || {rdsmall.ohms:.4g} \\\\
# &= {zo.ohms:.4g} \\Omega \\\\
# \\\\
# A_{{ \\text{{v}}}} &= - g_{{ \\text{{m}}}} Z_{{ \\text{{o}}}} \\\\
# &= - {gm.S:.4g} \\cdot {zo.ohms:.4g} \\\\
# &= {av:.4g} \\\\
# \\\\
# A_{{ \\text{{v nord}}}} &= - g_{{ \\text{{m}}}} R_{{ \\text{{D}}}} \\\\
# &= - {gm.S:.4g} \\cdot {rd.ohms:.4g} \\\\
# &= {av_nord.ohms:.4g} \\\\
# {ls}"""

class boylestad_8_8:
	def __init__(self,*args,**kwargs):
		print('preparing 8_8')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(20))
			rd = c.resistance(ran.main(3300))
			rg = c.resistance(ran.main(1e6))
			rs = c.resistance(ran.main(1e3))
			idss = c.current(ran.main(8), 'mA')
			vgsoff = c.voltage(ran.main(-6))
			gos = c.conductance(ran.main(20), 'uS')

			self.question = f"""Determine Zi, Zo with and without the effects of rd, and Av with and without the effects of rd, for a self-biased unbypased source resistance JFET with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RG = {rg.Mohms:.4g} Mohms, RS = {rs.kohms:.4g} kohms, and VSS = 0V. The JFET characteristics are IDSS = {idss.mA:.4g} mA and VGSoff = {vgsoff.V:.4g} V. The source resistance and the gate resistance are grounded. The value of gos = {gos.uS:.4g} uS"""

			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)
			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append(  - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms))

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print(vgslist[i])
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vs = c.voltage(id.A * rs.ohms)
					vg = c.voltage(0)
					vd = c.voltage(vds.V + vs.V)
					regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
		)

		rdsmall = c.resistance( 1 / gos.S)

		zi = c.resistance( rg.ohms )

		zo = c.resistance(
		((1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms)) * rd.ohms ) /
		(1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms) + (rd.ohms / rdsmall.ohms))
		)

		zo_nord = c.resistance( rd.ohms )

		av = (
		( - gm.S * rd.ohms ) /
		(1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms) + (rd.ohms / rdsmall.ohms))
		)

		av_nord = (
		( - gm.S * rd.ohms )/
		( 1 + gm.S * rs.ohms )
		)

		self.answer = f"""{zi.Mohms:.4g} Mohms, zo w/ rd = {zo.kohms:.4g} kohms, zo w/o rd = {zo_nord.kohms:.4g} kohms, Av w/ rd = {av:.4g}, Av w/o rd = {av_nord:.4g}"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}} }} \\left(1- \\frac{{ - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} }}{{ V_{{ \\text{{GSoff}}}} }}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left( 1 - \\frac{{ - I_{{ \\text{{D}} }}  \\cdot {rs.ohms:.4g} }}{{ {vgsoff.V:.4g}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}} }} &= - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} \\\\
&= - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}} }} &= V_{{ \\text{{DD}} }} - I_{{ \\text{{D}}}} \\left(R_{{ \\text{{S}} }} + R_{{ \\text{{D}} }}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\left( {rs.ohms:.4g} + {rd.ohms:.4g}\\right)\\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{S}}}} &= I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}}}} &= 0 \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DS}}}} + V_{{ \\text{{S}}}} \\\\
&= {vds.V:.4g} + {vs.V:.4g} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
g_{{ \\text{{m}} }} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }}{{ |V_{{ \\text{{GSoff}} }}| }}  \\left(1 - \\frac{{ V_{{ \\text{{GS}} }} }} {{ V_{{ \\text{{GS off}} }} }}\\right) \\\\
&= \\frac{{ 2 \\cdot {idss.A:.4g}}} {{|{vgsoff.V:.4g}|}} \\left( 1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g}}}   \\right) \\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\
r_{{ \\text{{d}} }} &= \\frac{{1}}{{g_{{ \\text{{os}} }} }} \\\\
&= \\frac{{1}} {{ {gos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i}} }} &= R_{{ \\text{{G}} }} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o}} }} &= R_{{ \\text{{D}} }} 	\\frac{{ 1 + g_{{ \\text{{m}} }} R_{{ \\text{{S}} }} + \\frac{{ R_{{ \\text{{S}} }} }} {{ r_{{ \\text{{d}} }} }}     }}	{{ 1 + g_{{ \\text{{m}} }} R_{{ \\text{{S}} }} + \\frac{{ R_{{ \\text{{S}} }} }} {{ r_{{ \\text{{d}} }} }}  + \\frac{{ R_{{ \\text{{D}} }} }} {{ r_{{ \\text{{d}} }}  }}     }} \\\\
&= {rd.ohms:.4g} \\cdot 	\\frac{{ 1 + {gm.S:.4g}  \\cdot {rs.ohms:.4g} + \\frac{{ {rs.ohms:.4g} }} {{ {rdsmall.ohms:.4g} }}     }}	{{ 1 + {gm.S:.4g} \\cdot {rs.ohms:.4g} + \\frac{{ {rs.ohms:.4g} }} {{ {rdsmall.ohms:.4g} }}  + \\frac{{ {rd.ohms:.4g} }} {{ {rdsmall.ohms:.4g}  }}     }} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o nord}}}} &= R_{{ \\text{{D}}}} \\\\
&= {zo_nord.ohms:.4g} \\Omega \\\\
\\\\
A_{{ \\text{{v}} }} &= \\frac{{   - g_{{ \\text{{m}}}} R_{{ \\text{{D}} }}	}} {{ 	1 + g_{{ \\text{{m}}}} R_{{ \\text{{S}}}} + \\frac{{ R_{{ \\text{{S}} }} }} {{ r_{{ \\text{{d}}}}}} + 	\\frac{{ R_{{ \\text{{D}} }} }} {{ r_{{ \\text{{d}} }} }}		}} \\\\
&= \\frac{{ - {gm.S:.4g} \\cdot {rd.ohms:.4g}	}} {{ 1 + {gm.S:.4g} \\cdot {rs.ohms:.4g} + \\frac{{ {rs.ohms:.4g} }} {{ {rdsmall.ohms:.4g} }} + \\frac{{ {rd.ohms:.4g} }} {{ {rdsmall.ohms:.4g}}} }}\\\\
&= {av:.4g} \\\\
{ls}"""

class boylestad_8_9:
	def __init__(self,*args,**kwargs):
		print('preparing 8_9')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(12))
			rd = c.resistance(ran.main(3.6e3))
			rs = c.resistance(ran.main(1.1e3))
			idss = c.current(ran.main(10), 'mA')
			vgsoff = c.voltage(ran.main(-4))
			gos = c.conductance(ran.main(50), 'uS')
			vi = c.voltage(ran.main(40), 'mV')

			self.question = f"""Determine: Zi with and without considering rd, Zo with and without considering rd, and Vo with and without considering rd for a common-gate JFET configuration with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.ohms:.4g} ohms, with the gate and the source resistance grounded. The JFET characteristics are IDSS = {idss.mA:.4g} mA, VGSoff = {vgsoff.V:.4g} V, gos = {gos.uS:.4g} uS and the input is a {vi.mV:.4g} mV signal."""


			equation = sym.Eq(
			x,
			idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
			)

			idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( - idlist[i] * rs.ohms)
				vdslist.append(   (vdd.V - idlist[i] * rd.ohms) - (idlist[i] * rs.ohms) )

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print('VDStest' + str(vdslist[i]))
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vd = c.voltage(vdd.V - id.A * rd.ohms)
					vg = c.voltage(0)
					vs = c.voltage(id.A * rs.ohms)
					regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
		)

		rdsmall = c.resistance( 1 / gos.S)

		zi = rs.parallel(c.resistance(
			(rdsmall.ohms + rd.ohms) /
			(1 + gm.S * rdsmall.ohms))
		)

		zi_nord = rs.parallel(c.resistance(1 / gm.S))

		zo = rd.parallel(rdsmall)

		zo_nord = c.resistance(rd.ohms)

		av = (
		(gm.S * rd.ohms + (rd.ohms / rdsmall.ohms)) /
		(1 + (rd.ohms/ rdsmall.ohms))
		)

		av_nord = gm.S * rd.ohms

		vo = c.voltage( vi.V * av)

		vo_nord = c.voltage( vi.V * av_nord)

		self.answer = f"""zi w/ rd= {zi.kohms:.4g} kohms, zi w/o rd = {zi_nord.kohms:.4g} kohms, zo w/ rd = {zo.kohms:.4g} kohms, zo w/o rd = {zo_nord.kohms:.4g} kohms, vo w/ rd = {vo.V:.4g} V, vo w/o rd = {vo_nord.V:.4g} V"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{D}} }} &= I_{{ \\text{{DSS}} }}  \\left(1 - \\frac{{ V_{{ \\text{{GS}} }} }} {{ V_{{ \\text{{GSoff}}}} }} \\right)^2 \\\\
I_{{ \\text{{D}} }} &= I_{{ \\text{{DSS}} }}  \\left(1 - \\frac{{ - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} }} {{ V_{{ \\text{{GSoff}} }} }} \\right)^2 \\\\
I_{{ \\text{{D}} }} &= {idss.A:.4g} \\cdot  \\left(1 - \\frac{{ - I_{{ \\text{{D}} }} \\cdot {rs.ohms:.4g} }} {{ {vgsoff.V:.4g} }} \\right)^2 \\\\
I_{{ \\text{{D}} }} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= - I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} \\\\
&= - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{D}}}} &= V_{{ \\text{{DD}} }} - I_{{ \\text{{D}} }} R_{{ \\text{{D}} }} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vd.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{G}} }} &= 0 \\text{{ V}} \\\\
\\\\
V_{{ \\text{{S}} }} &= I_{{ \\text{{D}} }} R_{{ \\text{{S}} }} \\\\
&= {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vs.V:.4g} \\text{{ V}} \\\\
\\\\

g_{{ \\text{{m}} }} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }}  {{ |V_{{ \\text{{GSoff}} }}| }}  \\left(1 - \\frac{{ V_{{ \\text{{GS}} }} }} {{ V_{{ \\text{{GS off}} }} }}\\right) \\\\
&= \\frac{{ 2 \\cdot {idss.A:.4g} }}   {{|{vgsoff.V:.4g}|}}  \\left(1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g}}}\\right) \\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\
r_{{ \\text{{d}} }} &= \\frac{{1}}  {{g_{{ \\text{{os}} }}   }} \\\\
&= \\frac{{ 1}} {{ {gos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i}} }} &= R_{{ \\text{{S}} }} || \\frac{{ r_{{ \\text{{d}} }} + R_{{ \\text{{D}} }} }} {{ 1 + \\frac{{ R_{{ \\text{{D}} }} }} {{ r_{{ \\text{{d}} }} }} }} \\\\
&= {rs.ohms:.4g} || \\frac{{ {rdsmall.ohms:.4g} + {rd.ohms:.4g} }} {{ 1 + \\frac{{ {rd.ohms:.4g} }} {{ {rdsmall.ohms:.4g} }} }} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i nord}} }} &= R_{{ \\text{{S}} }} || \\frac{{1}} {{ g_{{ \\text{{m}} }} }} \\\\
&= {rs.ohms:.4g} || \\frac{{1}} {{ {gm.S:.4g}}} \\\\
&= {zi_nord.ohms:.4g} \\Omega \\\\
\\\\

Z_{{ \\text{{o}} }} &= R_{{ \\text{{D}} }} || r_{{ \\text{{d}} }} \\\\
&= {rd.ohms:.4g} || {rdsmall.ohms:.4g} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o nord}} }} &= R_{{ \\text{{D}} }} \\\\
&= {rd.ohms:.4g} \\Omega \\\\
\\\\

A_{{ \\text{{v}} }} &= \\frac{{
		g_{{ \\text{{m}} }} R_{{ \\text{{D}} }} + \\frac{{ R_{{ \\text{{D}} }} }} {{ r_{{ \\text{{d}} }} }}
	}}
	{{
		1  + \\frac{{ R_{{ \\text{{D}} }} }} {{ r_{{ \\text{{d}} }} }}
	}} \\\\
&= \\frac{{ {gm.S:.4g} \\cdot {rd.ohms:.4g} + \\frac{{ {rd.ohms:.4g} }}{{ {rdsmall.ohms:.4g} }}	}} {{ 1  + \\frac{{ {rd.ohms:.4g} }} {{ {rdsmall.ohms:.4g} }} }} \\\\
&= {av:.4g} \\\\
\\\\

A_{{ \\text{{v nord}} }} &= g_{{ \\text{{m}} }} R_{{ \\text{{D}} }} \\\\
&= {gm.S:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {av_nord:.4g} \\\\
\\\\

V_{{ \\text{{o}} }} &= V_{{ \\text{{i}} }} A_{{ \\text{{v}} }} \\\\
&= {vi.V:.4g} \\cdot {av:.4g} \\\\
&= {vo.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{o nord}} }} &= V_{{ \\text{{i}} }} A_{{ \\text{{v nord}} }} \\\\
&= {vi.V:.4g} \\cdot {av_nord:.4g} \\\\
&= {vo_nord.V:.4g} \\text{{ V}} \\\\
{ls}"""

class boylestad_8_10:
	def __init__(self,*args,**kwargs):
		print('preparing 8_10')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(9))
			rs = c.resistance(ran.main(2.2e3))
			rg = c.resistance(ran.main(1e6))
			idss = c.current(ran.main(16), 'mA')
			vgsoff = c.voltage(ran.main(-4))
			gos = c.conductance(ran.main(25), 'uS')

			self.question = f"""A source follower network has VDD = {vdd.V:.4g} V, RS = {rs.kohms:.4g} kohms, RG = {rg.Mohms:.4g} Mohms. The gate resistance and the source resistance are both grounded. The network uses a JFET with characteristics IDSS = {idss.mA:.4g} mA, VGSoff = {vgsoff.V:.4g} V, and gos = {gos.uS:.4g} uS. Determine Zi, Zo, and Av with and without considering rd."""

			equation = sym.Eq(
			x,
			idss.A * ( 1 - (( - x * rs.ohms) / (vgsoff.V)))**2
			)

			idsat = c.current(vdd.V / rs.ohms)
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * rs.ohms )

			for i in range(len(idlist)):
				if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
					#print('VDStest' + str(vdslist[i]))
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					vd = c.voltage( vdd.V )
					vg = c.voltage( vgs.V )
					vs = c.voltage( id.A * rs.ohms )
					regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
		)

		rdsmall = c.resistance( 1 / gos.S)

		zi = c.resistance(rg.ohms)

		zo = rdsmall.parallel(rs).parallel(c.resistance(1/gm.S))

		zo_nord = rs.parallel(c.resistance(1/gm.S))

		av = (
		( gm.S * (rdsmall.parallel(rs).ohms)) /
		( 1 + gm.S * (rdsmall.parallel(rs).ohms))
		)

		av_nord = (
		(gm.S * rs.ohms) /
		(1 + gm.S * rs.ohms)
		)

		self.answer = f"""zi = {zi.kohms:.4g} kohms, zo w/ rd = {zo.kohms:.4g} kohms, zo w/o rd = {zo_nord.kohms:.4g} kohms, av w/ rd = {av:.4g}, av w/o rd = {av_nord:.4g}"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ V_{{ \\text{{GS}}}} }} {{ V_{{ \\text{{GS off}}}} }}  \\right)^2 \\\\
I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left(1 - \\frac{{ - I_{{ \\text{{D}}}}  R_{{ \\text{{S}}}} }} {{ V_{{ \\text{{GS off}}}} }}  \\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\left(1 - \\frac{{ - I_{{ \\text{{D}}}}  {rs.ohms:.4g} }} {{ {vgsoff.V:.4g} }}  \\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= - {idss.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
g_{{ \\text{{m}}}} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }}{{|V_{{ \\text{{GSoff}}}}|}}  \\left(1 - \\frac{{ V_{{ \\text{{GS}} }} }} {{ V_{{ \\text{{GS off}}}}}}\\right) \\\\
&= \\frac{{ 2 \\cdot {idss.A:.4g} }}{{|{vgsoff.V:.4g}|}}  \\left(1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g}}}\\right) \\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\
r_{{ \\text{{d}}}} &= \\frac{{ 1}} {{ g_{{ \\text{{os}}}}}} \\\\
&= \\frac{{1}}{{ {gos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i}}}} &= R_{{ \\text{{G}}}} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o}}}} &= r_{{ \\text{{d}}}} || R{{ \\text{{S}}}} || \\frac{{ 1}} {{ g_{{ \\text{{m}}}}}} \\\\
&= {rdsmall.ohms:.4g} || {rs.ohms:.4g} || \\frac{{ 1}} {{ {gm.S:.4g}}} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o nord}}}} &= R_{{ \\text{{S}}}} || \\frac{{1}}{{ g_{{ \\text{{m}}}}}} \\\\
&= {rs.ohms:.4g} || \\frac{{ 1}}{{ {gm.S:.4g}}} \\\\
&= {zo_nord.ohms:.4g} \\Omega \\\\
\\\\
A_{{ \\text{{v}}}} &= \\frac{{ g_{{ \\text{{m}}}}   \\left(r_{{ \\text{{d}}}} || R_{{ \\text{{S}}}}\\right)    }}	{{ 1 + g_{{ \\text{{m}}}}   \\left(r_{{ \\text{{d}}}} || R_{{ \\text{{S}}}}\\right)   }} \\\\
&= \\frac{{ {gm.S:.4g}   \\left({rdsmall.ohms:.4g} || {rs.ohms:.4g}\\right)    }}	{{ 1 + {gm.S:.4g}   \\left({rdsmall.ohms:.4g} || {rs.ohms:.4g}\\right)   }} \\\\
&= {av:.4g} \\\\
\\\\
A_{{ \\text{{v nord}}}} &= \\frac{{ g_{{ \\text{{m}}}} R_{{ \\text{{S}}}}   }} {{ 1 + g_{{ \\text{{m}}}} R_{{ \\text{{S}}}} }} \\\\
&= \\frac{{ {gm.S:.4g} \\cdot {rs.ohms:.4g}   }} {{ 1 + {gm.S:.4g} \\cdot {rs.ohms:.4g} }} \\\\
&= {av_nord:.4g} \\\\
{ls}"""

class boylestad_8_11:
	def __init__(self,*args,**kwargs):
		print('preparing 8_11')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(18))
			r1 = c.resistance(ran.main(110e6))
			r2 = c.resistance(ran.main(10e6))
			rd = c.resistance(ran.main(1.8e3))
			rs = c.resistance(ran.main(150))
			idss = c.current(ran.main(6), 'mA')
			vgsoff = c.voltage(ran.main(-3))
			gos = c.conductance(ran.main(10), 'uS')

			self.question = f"""An n - channel DMOSFET is biased in a common source,  voltage divider network with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RS = {rs.ohms:.4g} ohms, R1 (limiter) = {r1.Mohms:.4g} Mohms and R2 (bleeder) = {r2.Mohms:.4g} Mohms. The source resistance and the bleeder resistance are grounded with an installed bypass capacitor across the source resistance. The DMOSFET characteristics are IDSS = {idss.mA:.4g} mA, VGSoff = {vgsoff.V:.4g} V and gos = {gos.uS:.4g} uS. Determine Zi, Zo and Av."""

			vg = c.voltage(
			(vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
			)

			equation = sym.Eq(
			x,
			idss.A * ( 1 - ( ( vg.V - x * rs.ohms ) / ( vgsoff.V)  ))**2
			)

			idsat = c.current(vdd.V / (rs.ohms + rd.ohms))
			idset = sym.solveset(equation, x)
			idlist = list(idset)
			vgslist = []
			vdslist = []

			for i in range(len(idlist)):
				vgslist.append( vg.V - idlist[i] * rs.ohms)
				vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms) )

			for i in range(len(idlist)):
				if vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A:  #and idlist[i] < idss.A: vgslist[i] < 0 and
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vdslist[i])
					regen = False

		gm = c.conductance(
		(2 * idss.A / abs(vgsoff.V)) * (1 - ((vgs.V) / (vgsoff.V)))
		)

		rdsmall = c.resistance( 1 / gos.S)

		zi = r1.parallel(r2)

		zo = rdsmall.parallel(rd)

		av = - gm.S * zo.ohms

		self.answer = f"""{zi.Mohms:.4g} Mohms, {zo.kohms:.4g} kohms, {av:.4g}"""

		self.latex_solution = f"""{lp}
V_{{ \\text{{G}}}} &= \\frac{{ V_{{ \\text{{DD}}}} R_{{ \\text{{2}}}}}} {{ R_{{ \\text{{1}}}}  + R_{{ \\text{{2}}}} }} \\\\
&= \\frac{{ {vdd.V:.4g} \\cdot {r2.ohms:.4g} }} {{ {r1.ohms:.4g}  + {r2.ohms:.4g} }} \\\\
&= {vg.V:.4g} \\text{{ V}} \\\\
\\\\

I_{{ \\text{{D}}}} &= I_{{ \\text{{DSS}}}} \\left( 1 - \\frac{{ V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}}    }}{{ V_{{ \\text{{GS off}}}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {idss.A:.4g} \\cdot \\left( 1 - \\frac{{ {vg.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rs.ohms:.4g}   }}{{ {vgs.V:.4g} }}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\

V_{{ \\text{{GS}}}} &= V_{{ \\text{{G}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{S}}}} \\\\
&= {vg.V:.4g} - {id.A:.4g} \\cdot {rs.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\

V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} \\left(	R_{{ \\text{{D}}}} + R_{{ \\text{{S}}}}\\right) \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot \\left( {rd.ohms:.4g} + {rs.ohms:.4g}\\right) \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\

g_{{ \\text{{m}}}} &= \\frac{{ 2 I_{{ \\text{{DSS}} }} }}{{|V_{{ \\text{{GSoff}}}}|}}  \\left(1 - \\frac{{ V_{{ \\text{{GS}} }} }} {{ V_{{ \\text{{GS off}}}}}}\\right) \\\\
&= \\frac{{ 2 \\cdot {idss.A:.4g} }}{{|{vgsoff.V:.4g}|}}  \\left(1 - \\frac{{ {vgs.V:.4g} }} {{ {vgsoff.V:.4g}}}\\right) \\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\

r_{{ \\text{{d}}}} &= \\frac{{ 1}} {{ g_{{ \\text{{os}}}}}} \\\\
&= \\frac{{1}}{{ {gos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\

Z_{{ \\text{{i}}}} &= R_{{ \\text{{1}}}} || R_{{ \\text{{2}}}} \\\\
&= {r1.ohms:.4g} || {r2.ohms:.4g} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\

Z_{{ \\text{{o}}}} &= R_{{ \\text{{D}}}} || r_{{ \\text{{d}}}} \\\\
&= {rd.ohms:.4g} || {rdsmall.ohms:.4g} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\

A_{{ \\text{{v}}}} &= - g_{{ \\text{{m}}}} Z_{{ \\text{{o}}}} \\\\
&= - {gm.S:.4g} \\cdot {zo.ohms:.4g} \\\\
&= {av:.4g} \\\\
{ls}"""

class boylestad_8_12:
	def __init__(self,*args,**kwargs):
		print('preparing 8_12')
		regen = True
		while regen:
			vdd = c.voltage(ran.main(12))
			rd = c.resistance(ran.main(2000))
			rf = c.resistance(ran.main(10e6))
			idon = c.current(ran.main(6), 'mA')
			vgsth = c.voltage(ran.main(3))
			vgson = c.voltage(vgsth.V + ran.main(5))
			gos = c.conductance(ran.main(20), 'uS')

			self.question = f"""Determine Zi with and without rd, Zo with and without rd, and Av with and without rd, for an enhancement type MOSFET that uses a feedback biasing arrangement with VDD = {vdd.V:.4g} V, RD = {rd.kohms:.4g} kohms, RF = {rf.Mohms:.4g} Mohms, and the source grounded. The MOSFET has characteristics IDon = {idon.mA:.4g} mA, VGSon = {vgson.V:.4g} V, and VGSth = {vgsth.V:.4g} V. Note also that gos = {gos.uS:.4g} uS"""

			k  = (idon.A) / ((vgson.V - vgsth.V)**2)

			equation = sym.Eq(
			x,
			k * (( ((vdd.V) - (x * rd.ohms)) - vgsth.V )**2)
			)
			idsat = c.current(vdd.V / (rd.ohms))
			idset = sym.solveset(equation, x, domain = sym.Reals)
			idlist = list(idset)
			vgslist = [0]
			vdslist = [0]

			for i in range(len(idlist)):
				vgslist.append(vdd.V - idlist[i] * rd.ohms)
				vdslist.append(vdd.V - idlist[i] * rd.ohms)

			for i in range(len(idlist)):
				if vgslist[i] > vgsth.V and vdslist[i] > 0:
					id = c.current(idlist[i])
					vgs = c.voltage(vgslist[i])
					vds = c.voltage(vgs.V)
					regen = False

		gm = c.conductance( 2 * k * (vgs.V - vgsth.V ))
		rdsmall = c.resistance(1 / gos.S)
		zi = c.resistance(
		(rf.ohms + rdsmall.parallel(rd).ohms ) /
		(1 + gm.S * (rdsmall.parallel(rd).ohms))
		)
		zi_nord = c.resistance(
		(rf.ohms) /
		(1 + gm.S * rd.ohms)
		)
		zo = rf.parallel(rdsmall).parallel(rd)
		zo_nord = c.resistance(rd.ohms)
		av = - gm.S * zo.ohms
		av_nord = - gm.S * zo_nord.ohms

		self.answer = f"""Zi w/ rd = {zi.Mohms:.4g} Mohms, Zi w/o rd = {zi_nord.Mohms:.4g} Mohms, Zo w/ rd = {zo.kohms:.4g} kohms, Zo w/o rd = {zo_nord.kohms:.4g} kohms, Av w/ rd = {av:.4g}, Av w/o rd = {av_nord:.4g}"""
		self.latex_solution = f"""{lp}
k &= \\frac{{ I_{{ \\text{{on}}}}}} {{ \\left(	V_{{ \\text{{GSon}}}} - V_{{ \\text{{GSth}}}}\\right)^2 }} \\\\
&= \\frac{{ {idon.A:.4g} }} {{ \\left( {vgson.V:.4g} - {vgsth.V:.4g}\\right)^2 }} \\\\
&= {k:.4g} \\frac{{A}}{{V^2}} \\\\
\\\\
I_{{ \\text{{D}}}} &= k \\left(	V_{{ \\text{{DD}}}}	- I_{{ \\text{{D}}}} R_{{ \\text{{D}}}}	- V_{{ \\text{{GSth}}}}\\right)^2 \\\\
I_{{ \\text{{D}}}} &= {k:.4g} \\cdot \\left( {vdd.V:.4g} - I_{{ \\text{{D}}}} \\cdot {rd.ohms:.4g} - {vgsth.V:.4g} \\right)^2 \\\\
I_{{ \\text{{D}}}} &= {id.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{GS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vgs.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DS}}}} &= V_{{ \\text{{DD}}}} - I_{{ \\text{{D}}}} R_{{ \\text{{D}}}} \\\\
&= {vdd.V:.4g} - {id.A:.4g} \\cdot {rd.ohms:.4g} \\\\
&= {vds.V:.4g} \\text{{ V}} \\\\
\\\\
g_{{ \\text{{m}}}} &= 2 k \\left( V_{{ \\text{{GS}}}} - V_{{ \\text{{GSth}}}}\\right) \\\\
&= 2 \\cdot {k:.4g} \\cdot \\left( {vgs.V:.4g} - {vgsth.V:.4g}\\right) \\\\
&= {gm.S:.4g} \\text{{ S}} \\\\
\\\\
r_{{ \\text{{d}}}} &= \\frac{{ 1}} {{ g_{{ \\text{{os}}}}}}\\\\
&= \\frac{{1}} {{ {gos.S:.4g}}} \\\\
&= {rdsmall.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i}}}} &= \\frac{{ R_{{ \\text{{F}}}} + r_{{ \\text{{d}}}} || R_{{ \\text{{D}}}} }}		{{1 + g_{{ \\text{{m}}}}  \\left( r_{{ \\text{{d}}}} + R_{{ \\text{{D}}}}\\right)  }} \\\\
&= \\frac{{ {rf.ohms:.4g} + {rdsmall.ohms:.4g} || {rd.ohms:.4g} }}		{{1 + {gm.S:.4g}  \\cdot  \\left( {rdsmall.ohms:.4g} + {rd.ohms:.4g}\\right)  }} \\\\
&= {zi.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{i nord}}}} &= \\frac{{ R_{{ \\text{{F}}}}	}} {{ 1 + g_{{ \\text{{m}}}} R_{{ \\text{{D}}}}		}} \\\\
&= \\frac{{ {rf.ohms:.4g}	}} {{ 1 + {gm.S:.4g} \\cdot {rd.ohms:.4g}	}} \\\\
&= {zi_nord.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o}}}} &= R_{{ \\text{{F}}}} || r_{{ \\text{{d}}}} || R_{{ \\text{{D}}}} \\\\
&= {rf.ohms:.4g} || {rdsmall.ohms:.4g} || {rd.ohms:.4g} \\\\
&= {zo.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{o nord}}}} &= R_{{ \\text{{D}}}} \\\\
&= {zo_nord.ohms:.4g} \\Omega \\\\
\\\\
A_{{ \\text{{v}}}} &= - g_{{ \\text{{m}}}} Z_{{ \\text{{o}}}} \\\\
&= - {gm.S:.4g} \\cdot {zo.ohms:.4g} \\\\
&= {av:.4g} \\\\
\\\\
A_{{ \\text{{v nord}}}} &= - g_{{ \\text{{m}}}} Z_{{ \\text{{o nord}}}} \\\\
&= - {gm.S:.4g} \\cdot {zo_nord.ohms:.4g} \\\\
&= {av_nord:.4g} \\\\
{ls}"""
