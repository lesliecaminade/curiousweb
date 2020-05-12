from generator import random_handler as ran
from generator import constants_conversions as c
import sympy as sym
import math
import random

x, y, z = sym.symbols('x y z', real = True)#generic variables
vbe = c.voltage(0.7)
VBE = c.voltage(0.7)
VTH = c.voltage(26e-3)


class Fixed_Bias():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		VCC = c.voltage(ran.main(kwargs['vcc']))
		RB = c.resistance(ran.main(kwargs['rb']))
		RC = c.resistance(ran.main(kwargs['rc']))
		BETA = ran.main(kwargs['beta'])

		try:
			ro = c.resistance(ran.main(kwargs['ro']))
			ro_flag = True
		except:
			ro = c.resistance(50_000)
			ro_flag = False


		repeat = True
		while repeat:

			IB = c.current(
				( VCC.V - VBE.V ) / RB.ohms
				)

			IC = c.current( BETA * IB.A )

			IE = c.current( (BETA + 1) * IB.A)
			if IC.A < (VCC.V / RC.ohms):
				repeat = False

		VCE = c.voltage(
			VCC.V - IC.A * RC.ohms
			)
		re = c.resistance(VTH.V / IE.A)

		ZI = RB
		ZO = RC.parallel(ro)
		AV = - ZO.ohms / re.ohms

		self.VCC = VCC
		self.RB = RB
		self.RC = RC
		self.beta = BETA
		self.BETA = BETA
		self.IB = IB
		self.IC = IC
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV

		self.description = f"""For a BJT fixed bias network with VCC = {round(VCC.V,4)} V, RB = {round(RB.kohms, 4)} kohms, RC = {round(RC.kohms, 4)} kohms, beta = {round(BETA, 2)}, and ro = {round(ro.kohms, 4)} kohms, """
		self.latex_solution = f"""{lp}
I_{{ \\text{{B}}}} &= \\frac{{ V_{{ \\text{{CC}}}} - V_{{ \\text{{BE}}}}    }} {{ R_{{ \\text{{B}}}} }} \\\\
&= \\frac{{ {VCC.V:.4g} - {VBE.V:.4g}}} {{ {RB.ohms:.4g} }}\\\\
&= {IB.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{C}}}} &= \\beta I_{{ text{{B}}}} \\\\
&= {beta:.4g} \\cdot {IB.A:.4g} \\\\
&= {IC.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{E}}}} &= \\left( \\beta + 1 \\right) I_{{ \\text{{B}}}} \\\\
&= \\left( {beta:.4g} + 1\\right) {IB.A:.4g} \\\\
&= {IE.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{CE}}}} &= V_{{ \\text{{CC}}}} - I_{{ \\text{{C}}}} R_{{ \\text{{C}}}} \\\\
&= {VCC.V:.4g} - {IC.A:.4g} \\cdot {RC.ohms:.4g} \\\\
&= {VCE.V:.4g} \\text{{ V}} \\\\
\\\\
r_{{ \\text{{e}}}} &= \\frac{{ V_{{ \\text{{TH}}}}}} {{ I_{{ \\text{{E}}}}}} \\\\
&= \\frac{{ {VTH.V:.4g}}} {{ {IE.A:.4g}}} \\\\
&= {re.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{I}}}} &= R_{{ \\text{{B}}}} \\\\
&= {RB.ohms:.4g} \\Omega \\\\
\\\\
Z_{{ \\text{{O}}}} &= R_{{ \\text{{C}}}} || r_{{ \\text{{o}}}} \\\\
&= {RC.ohms:.4g} || {ro.ohms:.4g} \\\\
&= {ZO.ohms:.4g} \\Omega \\\\
\\\\
A_{{ \\text{{v}}}} &= - \\frac{{ Z_{{ \\text{{O}}}}}} {{ r_{{ \\text{{e}}}}}} \\\\
&= - \\frac{{ {ZO.ohms:.4g}}} {{ {re.ohms:.4g}}} \\\\
&= {AV:.4g} \\\\
{ls}"""

class Emitter_Stabilized():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		repeat = True
		while repeat:
			VCC = c.voltage(ran.main(kwargs['vcc']))
			RB = c.resistance(ran.main(kwargs['rb']))
			RC = c.resistance(ran.main(kwargs['rc']))
			RE = c.resistance(ran.main(kwargs['re']))
			BETA = ran.main(kwargs['beta'])

			try:
				ro = c.resistance(ran.main(kwargs['ro']))
			except:
				ro = c.resistance(50_000)

			try:
				bypass = kwargs['bypass']
			except:
				bypass = True

			if bypass:
				bypass_string = 'bypassed'
			else:
				bypass_string = 'unbypassed'

			IB = c.current(
				(VCC.V - VBE.V) / (RB.ohms + (BETA + 1) * RE.ohms )
				)

			IC = c.current(IB.A * BETA)
			IE = c.current(IB.A * (BETA + 1))

			VCE = c.voltage(
				VCC.V - IC.A * RC.ohms - IE.A * RE.ohms
				)

			if 0 < VCE.V < VCC.V:
				repeat = False

		re = c.resistance(VTH.V / IE.A)
		beta_re = c.resistance( BETA * re.ohms)

		if bypass:
			ZI = beta_re.parallel(RB)
			ZO = RC
			AV = - ZO.ohms / re.ohms

		else:
			ZB = c.resistance( BETA * (re.ohms + RE.ohms))
			ZI = RB.parallel(ZB)
			ZO = RC
			AV = - RC.ohms / (re.ohms + RE.ohms)

		self.VCC = VCC
		self.RB = RB
		self.RC = RC
		self.beta = BETA
		self.BETA = BETA
		self.IB = IB
		self.IC = IC
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV

		self.description = f"""For a BJT emitter stabilized network ({bypass_string}) with VCC = {round(VCC.V,4)} V, RB = {round(RB.kohms, 4)} kohms, RC = {round(RC.kohms, 4)} kohms, RE = {round(RE.kohms, 4)} kohms, beta = {round(BETA, 2)}, and ro = {round(ro.kohms, 4)} kohms, """
		
class Voltage_Divider():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		repeat = True
		while repeat:

			VCC = c.voltage(ran.main(kwargs['vcc']))
			R1 = c.resistance(ran.main(kwargs['r1']))
			R2 = c.resistance(ran.main(kwargs['r2']))
			RC = c.resistance(ran.main(kwargs['rc']))
			RE = c.resistance(ran.main(kwargs['re']))
			BETA = ran.main(kwargs['beta'])

			try:
				ro = c.resistance(ran.main(kwargs['ro']))
			except:
				ro = c.resistance(50_000)

			try:
				bypass = kwargs['bypass']
			except:
				bypass = True

			if bypass:
				bypass_string = 'bypassed'
			else:
				bypass_string = 'unbypassed'

			ETH = c.voltage(
				(VCC.V * R2.ohms) / (R1.ohms + R2.ohms)
				)

			RTH = R1.parallel(R2)

			IB = c.current(
				(ETH.V - VBE.V) / (RTH.ohms + (BETA + 1) * RE.ohms)
				)

			IC = c.current(
				BETA * IB.A
				)

			IE = c.current(
				(BETA + 1) * IB.A
				)

			VCE = c.voltage(
				VCC.V - IC.A * RC.ohms - IE.A * RE.ohms
				)

			if 0 < VCE.V < VCC.V:
				repeat = False

		re = c.resistance(
			VTH.V / IE.A
			)

		if bypass:
			ZI = R1.parallel(R2)
			ZO = RC.parallel(ro)
			AV = - ZO.ohms / re.ohms
		else:
			ZB = c.resistance( BETA * (re.ohms + RE.ohms))
			RB = R1.parallel(R2)
			ZI = RB.parallel(ZB)
			ZO = RC.parallel(ro)
			AV = - RC.ohms / (re.ohms + RE.ohms)

		self.VCC = VCC
		self.R1 = R1
		self.R2 = R2
		self.RE = RE
		self.RC = RC
		self.beta = BETA
		self.BETA = BETA
		self.IB = IB
		self.IC = IC
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV
		self.description = f"""For a BJT voltage divider network ({bypass_string}) with VCC = {round(VCC.V, 4)} V, R1 = {round(R1.kohms, 4)} kohms, R2 = {round(R2.kohms, 4)} kohms, RC = {round(RC.kohms, 4)} kohms, RE = {round(RE.kohms, 4)} kohms, and utilizes a transistor with beta = {round(BETA, 2)} and ro = {round(ro.kohms, 4)} kohms, """

class Emitter_Follower():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		repeat = True
		while repeat:

			VCC = c.voltage(ran.main(kwargs['vcc']))
			RB = c.resistance(ran.main(kwargs['rb']))
			RE = c.resistance(ran.main(kwargs['re']))
			BETA = ran.main(kwargs['beta'])

			try:
				ro = c.resistance(ran.main(kwargs['ro']))
			except:
				ro = c.resistance(50_000)

			IB = c.current(
				(VCC.V - VBE.V) / (RB.ohms + (BETA + 1)*RE.ohms)
				)

			IC = c.current(BETA * IB.A)
			IE = c.current((BETA + 1) * IB.A)

			VCE = c.voltage(VCC.V - IE.A * RE.ohms)

			if 0 < VCE.V < VCC.V:
				repeat = False

		re = c.resistance(VTH.V / IE.A)
		ZB = c.resistance(
			BETA * re.ohms + (((BETA + 1) * RE.ohms) / ( 1 + (RE.ohms / ro.ohms)))
			)
		ZI = RB.parallel(ZB)

		ZO = RE.parallel(ro).parallel(c.resistance( (BETA * re.ohms) / ( BETA + 1) ))

		AV = (  (BETA + 1) * RE.ohms / ZB.ohms  ) / ( 1 + RE.ohms / ro.ohms)

		self.VCC = VCC
		self.RB = RB
		self.RE = RE
		self.beta = BETA
		self.BETA = BETA
		self.IB = IB
		self.IC = IC
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV

		self.description = f"""For a BJT emitter follower network with VCC = {round(VCC.V, 4)} V, RB = {round(RB.kohms, 4)} kohms,  RE = {round(RE.kohms, 4)} kohms, and utilizes a transistor with beta = {round(BETA, 2)} and ro = {round(ro.kohms, 4)} kohms, """

class Common_Base():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		repeat = True
		while repeat:
			VCC = c.voltage(ran.main(kwargs['vcc']))
			VEE = c.voltage(ran.main(kwargs['vee']))
			RE = c.resistance(ran.main(kwargs['re']))
			RC = c.resistance(ran.main(kwargs['rc']))

			try:
				ALPHA = kwargs['alpha']
				BETA = ALPHA / (1 - ALPHA)
			except:
				BETA = kwargs['beta']
				ALPHA = BETA / (BETA + 1)
			try:
				ro = c.resistance(ran.main(kwargs['ro']))
			except:
				ro = c.resistance(1_000_000)

			IE = c.current(
				(VEE.V - VBE.V) / RE.ohms
				)

			IB = c.current(IE.A / (BETA + 1))
			IC = c.current(IE.A * ALPHA)

			VCE = c.voltage(
				(VEE.V + VCC.V - IE.A * RE.ohms - IC.A * RC.ohms)
				)

			if 0 < VCE.V < VEE.V + VCC.V:
				repeat = False

		re = c.resistance(VTH.V / IE.A)
		ZI = RE.parallel(re)
		ZO = RC
		AV = RC.ohms / re.ohms


		self.VCC = VCC
		self.RC = RC
		self.RE = RE
		self.beta = BETA
		self.BETA = BETA
		self.IB = IB
		self.IE = IE
		self.IC = IC
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV

		self.description = f"""For a BJT common base network with VCC = {round(VCC.V, 4)} V, VEE = {round(VEE.V, 4)} RE = {round(RE.kohms, 4)} kohms,  RC = {round(RC.kohms, 4)} kohms, and utilizes a transistor with alpha = {round(ALPHA, 2)} and ro = {round(ro.kohms, 4)} kohms, """

class Collector_Feedback():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		repeat = True
		while repeat:
			VCC = c.voltage(ran.main(kwargs['vcc']))
			RC = c.resistance(ran.main(kwargs['rc']))
			RF = c.resistance(ran.main(kwargs['rf']))
			BETA = ran.main(kwargs['beta'])

			try:
				ro = c.resistance(ran.main(kwargs['ro']))
			except:
				ro = c.resistance(50_000)

			IB = c.current(
				(VCC.V - VBE.V) / (RF.ohms + BETA * RC.ohms)
				)

			IC = c.current(
				IB.A * BETA
				)

			IE = c.current(
				IB.A * (BETA + 1)
				)

			VCE = c.voltage(
				VCC.V - IC.A * RC.ohms
				)

			if 0 < VCE.V < VCC.V:
				repeat = False

		re = c.resistance(VTH.V / IE.A)

		ZI_numerator = 1 + RC.parallel(ro).ohms / RF.ohms
		ZI_denominator = 1/(BETA*re.ohms) + 1/RF.ohms + ((RC.parallel(ro).ohms) / (BETA * re.ohms * RF.ohms)) + ((RC.parallel(ro).ohms)/(RF.ohms * re.ohms))
		ZI = c.resistance(ZI_numerator / ZI_denominator)
		ZO = ro.parallel(RC).parallel(RF)

		AV = -(RF.ohms / (RC.parallel(ro).ohms + RF.ohms)) * ((RC.parallel(ro).ohms)/(re.ohms))

		self.VCC = VCC
		self.RC = RC
		self.RF = RF
		self.BETA = BETA
		self.beta = BETA
		self.IB = IB
		self.IC = IC
		self.IE = IE
		self.VCE = VCE
		self.ZI = ZI
		self.ZO = ZO
		self.AV = AV

		self.description = f"""For a BJT collector feedback network with VCC = {round(VCC.V, 4)} V, RC = {round(RC.kohms, 4)} kohms, RF = {round(RF.kohms, 4)} kohms, and transistor characteristics beta = {round(BETA, 4)} and ro = {round(ro.kohms, 4)} kohms, """



class boylestad_4_1:
	def __init__(self,*args,**kwargs):
		print("4_1")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(12))
			rb =  c.resistance(ran.main(240_000 ))
			rc =  c.resistance(ran.main(2200 ))
			beta = ran.main(50)
			self.question = f"""Determine VCEQ for the fixed bias configuration. VCC = {round(vcc.V,2)} V, RB = {round(rb.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/0p4d1k1aqsv36ctyg63x.png"""

			ib = c.current(
			(vcc.V - vbe.V) / rb.ohms
			)

			ic = c.current(
			beta * ib.A
			)

			vce = c.voltage(
			vcc.V - ic.A * rc.ohms
			)

			vb = c.voltage( vbe.V )
			vc = c.voltage( vce.V )
			vbc = c.voltage( vb.V - vc.V )

			if ic.A < vcc.V / rc.ohms:
				regen = 0

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f"""{lp}
I_{{ \\text{{B}}}} &= \\frac {{ V_{{ \\text {{CC}} - V_{{ \\text {{BE}}}}}}{{R_{{ \\text{{B}}}}}}   \\\\
& = \\frac {{ {vcc.V:.4g} {{ \\text {{ V}}}} - {vbe.V:.4g} {{ \\text {{ V}}}} }}{{ {rb.ohms:.4g} {{ \\text {{ \\Omega}}}}}} \\\\
& = {ib.A:.4g} {{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\beta}}}} \\cdot {{ I_{{ \\text {{B}}}}}}\\\\
& = {beta:.4g} \\cdot {ib.A:.4g}\\\\
& = {ic.A:.4g} {{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text{{CC}}}} - I_{{ \\text {{C}}}} \\cdot R_{{ \\text {{C}}}}\\\\
& = {vcc.V:.4g}{{ \\text {{ V}}}}-{ic.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohmd}{{ \\text {{ \\Omega}}}}\\\\
& = {vce.V:.4g} {{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{B}}}} &= V_{{ \\text {{BE}}}}\\\\
& = {vbe.V:.4g} {{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{C}}}} &= V_{{ \\text {{CE}}}}\\\\
& = {vce.V:.4g} {{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{BC}}}} &= V_{{ \\text {{B}}}} - V_{{ \\text {{C}}}}\\\\
& = {vb.V:.4g}{{ \\text {{ V}}}} - {vc.V:.4g}{{ \\text {{ V}}}}\\\\
& = {vbc.V:.4g} {{ \\text {{ V}}}} \\\\
\\\\
{ls}"""

class boylestad_4_2:
	def __init__(self,*args,**kwargs):
		print("4_2")
		vcc = c.voltage(ran.main(12))
		rb =  c.resistance(ran.main(240_000 ))
		rc =  c.resistance(ran.main(2200 ))
		beta = ran.main(50)
		self.question = f"""Determine the saturation level for the fixed bias configuration. VCC = {round(vcc.V,2)} V, RB = {round(rb.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, beta = {round(beta,2)}.
		https://lesliecaminadecom.files.wordpress.com/2019/07/0p4d1k1aqsv36ctyg63x.png"""

		icsat = c.current(
		vcc.V / rc.ohms
		)

		self.answer = f"""{round(icsat.mA,2)} mA"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{Csat}}}} &= \\frac{{V_{{ \\text {{CC}}}}}}{{R_{{ \\text {{C}}}}}} \\\\
& = \\frac {{ {vcc.V:.4g} {{ \\text {{ V}}}}}}{{ {rc.ohm:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
\\\\
{ls}"""
class boylestad_4_3:
	def __init__(self,*args,**kwargs):
		print("4_3")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(20))
			rb =  c.resistance(ran.main(430_000 ))
			rc =  c.resistance(ran.main(2000 ))
			re =  c.resistance(ran.main(1000 ))
			beta = ran.main(50)

			self.question = f"""For the emitter-bias network, determine VCE for the values VCC = {round(vcc.V,2)} V, RB = {round(rb.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, RE = {round(re.ohms,2)} ohms, beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/fr18ylk5mr6cfhryt59w.png"""

			ib = c.current(
			(vcc.V - vbe.V) / (rb.ohms + (beta + 1) * re.ohms)
			)

			ic = c.current( beta * ib.A )

			if ic.A < (vcc.V / (re.ohms + rc.ohms)):
				regen = 0

		vce = c.voltage(
		vcc.V - ic.A * (re.ohms + rc.ohms)
		)

		vc = c.voltage(
		vcc.V - ic.A * rc.ohms
		)

		ve = c.voltage(
		vc.V - vce.V
		)

		vb = c.voltage(
		vbe.V + ve.V
		)

		vbc = c.voltage(
		vb.V - vc.V
		)

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f"""{lp}
I_{{ \\text {{B}}}} &= \\frac {{V_{{ \\text{{CC}}}} - V_{{ \\text {{BE}}}}}} {{R_{{ \\text {{B}}}} + \\left {{ \\text {{ \\beta}}}} + 1 \\right}}\\\\
& = \\frac {{ {vcc.V;.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}}}}{{ {rb.ohm}{{ \\text {{ \\Omega}}}}+ \\left {{ {beta:.4g}+ 1}}\\right}}\\\\
& = {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot {{ I_{{ \\text {{B}}}}}}\\\\
&= {beta:.4g} \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot \\left R_{{ \\text {{E}}}} + R_{{ \\text {{C}}}} \\right\\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A:.4g}{{ \\text {{ A}}}} \\cdot \\left {re.ohms:.4g}{{ \\text{{ \\Omega}}}} + {rc.ohms:.4g}{{ \\Omega}}\\\\
&= {vce.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{C}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot R_{{ \\text {{C}}}}\\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A}{{ \\text {{ A}}}} \\cdot {rc.ohms}{{ \\text {{ \\Omega}}}}\\\\
& = {vd.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{E}}}} &= V_{{ \\text {{C}}}} - V_{{ \\text {{CE}}}}\\\\
&= {vc.V:.4g}{{ \\text {{ V}}}} - {vce.V:.4g}{{ \\text {{ V}}}}\\\\
&= {ve.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{B}}}} &= V_{{ \\text {{BE}}}} + V_{{ \\text {{E}}}}\\\\
&= {vbe.V:.4g}{{ \\text{{ V}}}} + {ve.V:.4g}{{ \\text {{ V}}}}\\\\
&= {vb.V} {{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{BC}}}} &= V_{{ \\text {{B}}}} - V_{{ \\text {{C}}}}\\\\
&= {vb.V} {{ \\text {{ V}}}} - {vc.V}{{ \\text {{ V}}}} \\\\
\\\\
{ls} """
class boylestad_4_6:
	def __init__(self,*args,**kwargs):
		print("4_6")
		vcc = c.voltage(ran.main(20))
		rb =  c.resistance(ran.main(430_000 ))
		rc =  c.resistance(ran.main(2000 ))
		re =  c.resistance(ran.main(1000 ))
		beta = ran.main(50)

		self.question = f"""For the emitter-bias network, determine the saturation current for the values VCC = {round(vcc.V,2)} V, RB = {round(rb.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, RE = {round(re.ohms,2)} ohms, beta = {round(beta,2)}.
		https://lesliecaminadecom.files.wordpress.com/2019/07/fr18ylk5mr6cfhryt59w.png"""

		icsat = c.current(
		vcc.V / (re.ohms + rc.ohms)
		)

		self.answer = f"""{round(icsat.A,2)} A"""
		self.latex_solution = f""" {lp}
I_{{ \\text{{Csat}}}} &= \\frac {{V_{{ \\text{{CC}}}}}}{{R_{{ \\text{{E}}}} + {{R_{{ \\text{{C}}}}}}}}\\\\
&= \\frac {{ {vcc.V:.4g}{{ \\text {{ V}}}}}}{{ {re.ohms:.4g}{{ \\text{{ \\Omega}}}} + {rc.ohms:.4g}{{ \\text{{ \\Omega}}}}}}\\\\
&= {icsat.A:.4g} {{ \\text {{ A}}}}\\\\
\\\\
{ls}"""
class boylestad_4_8:
	def __init__(self,*args,**kwargs):
		print("4_8")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(22))
			r1 =  c.resistance(ran.main(39_000 ))
			r2 =  c.resistance(ran.main(3900 ))
			rc =  c.resistance(ran.main(10_000 ))
			re =  c.resistance(ran.main(1500 ))
			beta = ran.main(100)

			self.question = f"""Determine the DC bias voltage VCE for the voltage divider configuration. VCC = {round(vcc.V,2)} V, R1(top) = {round(r1.kohms,2)} kohms, R2(bottom) = {round(r2.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, RE = {round(re.kohms,2)} kohms, beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/s2zbg7wry8s4nov813u4.png"""

			rth = r1.parallel(r2)

			eth = c.voltage(
			( r2.ohms * vcc.V ) / ( r1.ohms + r2.ohms )
			)

			ib = c.current(
			(eth.V - vbe.V) / (rth.ohms + (beta + 1) * re.ohms)
			)

			ic = c.current(
			beta * ib.A
			)

			vce = c.voltage(
			vcc.V - ic.A * (rc.ohms + re.ohms)
			)

			if ic.A < (vcc.V / (re.ohms + rc.ohms)):
				regen = 0

		self.answer = f"""{round(vce.V,2)} V"""
		Self.latex_solution = f""" {lp}
R_{{ \\text {{TH}}}} &= R_{{ \\text {{1}}}} {{ \\text {{//}}}} {{ R_{{ \\text {{2}}}}}}\\\\
&= {r1.ohms:.4g}{{ \\text {{ \\Omega}}}} {{ \\text {{//}}}} {r2.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
\\\\
E_{{ \\text {{TH}}}} &= \\frac {{ R_{{ \\text {{2}}}} \\cdot {{ V_{{ \\text {{CC}}}}}}}}{{R_{{ \\text {{1}}}} + {{R_{{ \\text{{2}}}}}}}}\\\\
&= \\frac {{ {r2.ohms:.4g}{{ \\text {{ \\Omega}}}} \\cdot {vcc.V:.4g}{{ \\text{{ V}}}}}}{{ {r1.ohms}{{ \\text {{ \\Omega}}}} + {r2.ohms}{{ \\text {{ \\Omega}}}}}}\\\\
&= {eth.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{B}}}} &= \\frac {{ E_{{ \\text {{TH}}}} - V_{{ \\text {{BE}}}}}} {{ R_{{ \\text{{TH}}}} + \\left {{ \\text {{ \\Beta}}}}+ 1 \\right \\cdot R_{{ \\text {{E}}}}}}\\\\
&= \\frac {{ {eth.V:.4g}{{ \\text {{ V}}}} - {vbe.V}{{ \\text {{ V}}}}}}{{ {rth.ohms:.4g}{{ \\text {{ \\Omega}}}} + \\left {beta:.4g} + 1 \\right \\cdot {re.ohms:,4g}{{ \\text {{ \\Omega}}}}}}\\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}}\\\\
&= {beta:.4g} \\cdot {ib.A:.4g}{{ \\text {{ A}}}}\\\\
&= {ic.A:.4g}{{ \\text {{ A}}}}\\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right\\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A:.4g}{{ \\text {{ A}}}} \\cdot \\left {rc.ohms}{{ \\text {{ \\Omega}}}} + {re.ohms}{{ \\text {{ \\Omega}}}} \\right\\\\
& = {vce.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls}"""

class boylestad_4_12:
	def __init__(self,*args,**kwargs):
		print("4_12")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(10))
			rc =  c.resistance(ran.main(4700 ))
			rf =  c.resistance(ran.main(250_000 ))
			re =  c.resistance(ran.main(1200 ))
			beta = ran.main(90)

			self.question = f"""Determine the quiescent levels of VCE for the network where VCC = {round(vcc.V,2)} V, RC = {round(rc.kohms,2)} kohms, RF = {round(rf.kohms,2)} kohms, RE = {round(re.kohms,2)} kohms, and beta = {round(beta,2)}
			https://lesliecaminadecom.files.wordpress.com/2019/07/vu3z85fuaeeq72rhgbrn.png"""

			ib = c.current(
			(vcc.V - vbe.V) / (rf.ohms + beta * ( rc.ohms + re.ohms ) )
			)

			ic = c.current(
			beta * ib.A
			)

			if ic.A < (vcc.V / ( rc.ohms + re.ohms )):
				regen = 0

		vce = c.voltage(
		vcc.V - ic.A * ( rc.ohms + re.ohms )
		)

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text {{CC}}}} - V_{{ \\text {{BE}}}} \\right}}{{ R_{{ \\text {{F}}}} + {{ \\text {{ \\Beta}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right}} \\\\
&= \\frac {{\\left {vcc.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ {rf.ohms:.4g}{{ \\text {{ \\Omega}}}} + {beta} \\cdot \\left {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} + {re.ohms:.4g}{{ \\text{{ \\Omega}}}}}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}}\\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}} \\\\
&= {beta:.4g} \\cdot {ib.A:.4g}{{ \\text{{ A}}}} \\\\
&= {ic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A:.4g}{{ \\text {{ A}}}} \\cdot \\left {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} + {re.ohms}{{ \\text {{ \\Omega}}}} \\right \\\\
&= {vce.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls}"""
class boylestad_4_14:
	def __init__(self,*args,**kwargs):
		print("4_14")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(18))
			rc =  c.resistance(ran.main(3300 ))
			rf2 =  c.resistance(ran.main(110_000 ))
			rf1 =  c.resistance(ran.main(91_000 ))
			re =  c.resistance(ran.main(510_000 ))
			beta = ran.main(75)

			self.question = f"""Determine the DC level VC for the network. VCC = {round(vcc.V,2)} V, RC = {round(rc.kohms,2)} kohms, RF1 = {round(rf1.kohms,2)} kohms, RF2 = {round(rf2.kohms,2)} kohms, RE = {round(re.kohms,2)} kohms, and beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/f21o27k3wek108bofwtq.png"""

			ib = c.current(
			(vcc.V - vbe.V) / (rf1.ohms + rf2.ohms + beta * ( rc.ohms + re.ohms ))
			)

			ic = c.current(
			beta * ib.A
			)

			ie = c.current(
			ib.A + ic.A
			)

			if ie.A < (vcc.V / (rc.ohms + re.ohms)):
				regen = 0

		vc = c.voltage(
		vcc.V - ie.A * rc.ohms
		)

		self.answer = f"""{round(vc.V,2)} V"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text {{CC}}}} - V_{{ \\text {{BE}}}} \\right}} {{R_{{ \\text {{f1}}}} + R_{{ \\text {{f2}}}} + {{ \\text {{ \\Beta}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right}} \\\\
&= \\frac {{ \\left {vcc.V;:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}}{{ {rf1.ohms:.4g}{{ \\text {{ \\Omega}}}} + {rf2.ohms:.4g}{{ \\text {{ \\Omega}}}} + {beta:.4g} \\cdot \\left {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} + {re.ohms:.4g}{{ \\text {{ \\Omega}}}} \\right}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}}\\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}} \\\\
&= {beta:.4g} \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\\\
&= {ic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{E}}}} &= I_{{ \\text {{B}}}} + I_{{ \\text {{C}}}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} {ic.A:.4g}{{ \\text {{ A}}}}\\\\
\\\\
V_{{ \\text {{C}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{E}}}} \\cdot R_{{ \\text {{C}}}} \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ie.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
&= {vc.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls}"""
class boylestad_4_16:
	def __init__(self,*args,**kwargs):
		print("4_16")
		regen = 1
		while regen:
			vee = c.voltage(ran.main(-20))
			re =  c.resistance(ran.main(2000 ))
			rb =  c.resistance(ran.main(240_000 ))
			beta = ran.main(90)

			self.question = f"""Determine VCE for the network where VEE = {round(vee.V,2)} V, RE = {round(re.kohms,2)} kohms, RB = {round(rb.kohms,2)} kohms, and beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/sjrsnbmupqf31688aept.png"""

			ib = c.current(
			(-vee.V - vbe.V) / (rb.ohms + (beta + 1) * re.ohms)
			)

			vce = c.voltage(
			- vee.V - (beta + 1) * ib.A * re.ohms
			)

			ie = c.current(
			(beta + 1) * ib.A
			)

			if ie.A < abs(-vee.V / re.ohms):
				regen = 0


		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{B}}}} &= \\frac {{ \\left -V_{{ \\text {{EE}}}} -V_{{ \\text {{BE}}}} \\right}} {{ \\left R_{{ \\text {{B}}}} + \\left {{ \\text {{ \\Beta}}}} + 1 \\right \\cdot R_{{ \\text {{E}}}} \\right}} \\\\
&= \\frac {{ \\left {-vee.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ \\left {rb.ohms:.4g}{{ \\text {{ \\Omega}}}} + \\left {beta:.4g} + 1 \\right \\cdot {re.ohms:.4g}{{ \\text {{ \\Omega}}}} \\right }} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= -V_{{ \\text {{EE}}}} - \\left {{ \\text {{ \\Beta}}}} + 1 \\right \\cdot I_{{ \\text {{B}}}} \\cdot R_{{ \\text {{E}}}} \\\\
&= {-vee.V:.4g}{{ \\text {{ V}}}} - \\left {beta:.4g} + 1 \\right \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\cdot {re.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
&= {vce.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{E}}}} &= \\left {{ \\text {{ \\Beta}}}} + 1 \\right \\cdot I_{{ \\text {{B}}}} \\\\
&= \\left {beta:.4g} + 1 \\right \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\\\
&= {ie.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""

class boylestad_4_17:
	def __init__(self,*args,**kwargs):
		print("4_17")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(10))
			vee = c.voltage(ran.main(4))
			re =  c.resistance(ran.main(1200 ))
			rc =  c.resistance(ran.main(2400 ))
			beta = ran.main(60)

			self.question = f"""Determine the voltage VCE for the common-base configuration where VEE = {round(vee.V,2)} V, VCC = {round(vcc.V,2)} V, RE = {round(re.kohms,2)} kohms, RC ={round(rc.kohms,2)} kohms and beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/iea7tq05l6f34euza4q7.png"""

			ie = c.current(
			(vee.V - vbe.V) / re.ohms
			)

			ib = c.current(
			ie.A / (beta + 1)
			)

			vce = c.voltage(
			vee.V + vcc.V - ie.A * (rc.ohms + re.ohms)
			)

			if vce.V > 0:
				regen = 0

		vcb = c.voltage(
		vcc.V - beta * ib.A * rc.ohms
		)

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{E}}}} &= \\frac {{ \\left V_{{ \\text {{EE}}}} - V_{{ ||text {{BE}}}} \\right}}{{ R_{{ \\text {{E}}}}}} \\\\
&= \\frac {{ \\left {vee.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}}{{ {re.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
&= {ie.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{B}}}} &= \\frac {{ I_{{ \\text {{E}}}}}}{{ \\left {{ \\text {{ \\Beta}}}} + 1 \\right}} \\\\
&= \\frac {{ {ie.A:.4g}{{ \\text {{ A}}}}}}{{ \\left {beta:.4g} + 1 \\right}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{EE}}}} + V_{{ \\text {{CC}}}} - I_{{ \\text {{E}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right \\\\
&= {vee.V:.4g}{{ \\text {{ V}}}} + {vcc.V:.4g}{{ \\text {{ V}}}} - {ie.A:.4g}{{ \\text {{ A}}}} \\cdot \\left {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} + {re.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
&= {vce.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{CB}}}} &= V_{{ \\text {{CC}}}} - {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}} \\cdot R_{{ \\text {{C}}}} \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {beta:.4g} \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohms}{{ \\text {{ \\Omega}}}} \\\\
&= {vcb.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls}"""
class boylestad_4_18:
	def __init__(self,*args,**kwargs):
		print("4_18")
		regen = 1
		while regen:

			vcc = c.voltage(ran.main(20))
			rc =  c.resistance(ran.main(4700 ))
			rb =  c.resistance(ran.main(680_000 ))
			beta = ran.main(120)

			self.question = f"""Determine VCE from the network where VCC = {round(vcc.V,2)} V, RC = {round(rc.kohms,2)} kohms, RB = {round(rb.kohms,2)} kohms, and beta = {round(beta,2)}.
			https://lesliecaminadecom.files.wordpress.com/2019/07/84sgobka0ptm9b1aj9qb.png"""

			ib = c.current(
			(vcc.V - vbe.V) / (rb.ohms + beta * rc.ohms)
			)

			ic = c.current(
			beta * ib.A
			)

			vce = c.voltage(
			vcc.V - ic.A * rc.ohms
			)

			if vce.V > 0:
				regen = 0

		vb = c.voltage(
		vbe.V
		)

		vc = c.voltage(
		vce.V
		)

		ve = c.voltage(0)

		vbc = c.voltage(
		vb.V - vc.V
		)

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text{{CC}}}} - V_{{ \\text {{BE}}}}}} {{ R_{{ \\text{{B}}}} + {{ \\text {{ \\Beta}}}} \\cdot R_{{ \\text {{C}}}}}} \\\\
&= \\frac {{ \\left {vcc.V:.4g}{{ \\text {{ V}}}} -{vbe.V:.4g}{{ \\text {{ V}}}} \\right}}{{ {rb.ohms:.4g}{{ \\text {{ \\Omega}}}} + {beta:.4g} \\cdot {rc.ohms}{{ \\text {{ \\Omega}}}} \\right}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}}\\\\
&= {beta:.4g} \\cdot {ib.A:4g}{{ \\text {{ A}}}}\\\\
&= {ic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot R_{{ \\text {{C}}}} \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohms:.4g} {{ \\text {{ \\Omega}}}}\\\\
&= {vce.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{B}}}} &= V_{{ \\text {{BE}}}}\\\\
&= {vbe.V:.4g}{{ \\text {{ V}}}}\\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{C}}}} &= V_{{ \\text {{CE}}}}\\\\
&= {vce.V:.4g}{{ \\text {{ V}}}}\\\\
&= {vc.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{E}}}} &= {{ \\text {{0}}}} \\\\
\\\\
V_{{ \\text {{BC}}}} &= V_{{ \\text {{B}}}} - V_{{ \\text{{C}}}}\\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} - {vc.V:.4g}{{ \\text {{ V}}}}\\\\
&= {vcb.V:.4g} {{ \\text {{ V}}}} \\\\
\\\\
{ls} """
class boylestad_4_19:
	def __init__(self,*args,**kwargs):
		print("4_19")
		regen = 1
		while regen:
			vee = c.voltage(ran.main(-9))
			rb =  c.resistance(ran.main(100_000 ))
			rc =  c.resistance(ran.main(1200 ))
			beta = ran.main(45)

			self.question = f"""Determine VB for the network where VEE = {round(vee.V,2)} V, RB = {round(rb.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, and beta = {round(beta,2)}
			https://lesliecaminadecom.files.wordpress.com/2019/07/415hm8o25ig5se9e8219.png"""

			vee = c.voltage( - vee.V)

			ib = c.current(
			(vee.V - vbe.V) / rb.ohms
			)

			ic = c.current(
			beta * ib.A
			)

			if ic.A < vee.V / rc.ohms:
				regen = 0

		vc = c.voltage(
		- ic.A * rc.ohms
		)

		vb = c.voltage(
		- ib.A * rb.ohms
		)

		self.answer = f"""{round(vb.V,2)} V"""
		self.latex_solution = f""" {lp}
V_{{ \\text {{EE}}}} &= -V_{{ \\text {{EE}}}} \\\\
&= {-vee.V:.4g} {{ \\text {{ V}}}} \\\\
& = {vee.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text {{EE}}}} - V_{{ \\text {{BE}}}} \\right}} {{ R_{{ \\text {{B}}}}}} \\\\
&= \\frac {{ \\left {vee.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ {rb.ohms}{{ \\text {{ \\Omega}}}}}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}} \\\\
&= {beta:.4g} \\cdot {ib.A:4g}{{ \\text {{ A}}}} \\\\
&= {ic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{C}}}} &= -I_{{ \\text {{C}}}} \\cdot R_{{ \\text {{C}}}} \\\\
&= -{ic.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
&= {vc.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{B}}}} &= -I_{{ \\text {{B}}}} \\cdot R_{{ \\text {{B}}}} \\\\
&= - {ib.A:.4g}{{ \\text {{ A}}}} \\cdot {rb.ohms}{{ \\text {{ \\Omega}}}} \\\\
\\\\
{ls}"""
class boylestad_4_20:
	def __init__(self,*args,**kwargs):
		print("4_20")
		regen = 1
		counter = 100_000
		while regen:

			vcc = c.voltage(ran.main(20))
			vee = c.voltage(vcc.V)
			rc =  c.resistance(2700)
			re =  c.resistance(1800)
			r1 =  c.resistance(8200)
			r2 =  c.resistance(2200)
			beta = ran.main(120)

			self.question = f"""Determine VC for the network where VCC = - VEE = {round(vcc.V,2)} V, R1(top) = {round(r1.kohms,2)} kohms, R2(bottom) = {round(r2.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, RE = {round(re.kohms,2)} kohms, and beta = {round(beta,2)}
			https://lesliecaminadecom.files.wordpress.com/2019/07/0o2i7c2ti2j3vsyovy9w.png"""

			rth = r1.parallel(r2)

			i_main = c.current(
			(vcc.V + vee.V) / (r1.ohms + r2.ohms)
			)

			eth = c.voltage(
			i_main.A * r2.ohms - vee.V
			)

			ib = c.current(
			(vee.V - eth.V - vbe.V) / (rth.ohms + (beta + 1) * re.ohms)
			)

			ic = c.current(
			beta * ib.A
			)

			counter = counter - 1
			if counter < 0:
				raise TypeError('iteration loops exceeded')
			if ic.A < ((vcc.V + vee.V) / (rc.ohms + re.ohms)):
				regen = 0

		vc = c.voltage(
		vcc.V - ic.A * rc.ohms
		)

		vb = c.voltage(
		- eth.V - ib.A * rth.ohms
		)

		self.answer = f"""{round(vc.V,2)} V"""
		self.latex_solution = f""" {ls}
R_{{ \\text {{TH}}}} &= R_{{ \\text {{1}}}} {{ \\text {{//}}}} R_{{ \\text {{2}}}} \\\\
&= {r1.ohms:.4g} {{ \\text {{ \\Omega}}}} {{ \\text {{//}}}} {r2.ohms:.4g} {{ \\text {{ \\Omega}}}} \\\\
&= {rth.ohms:.4g} {{ \\text {{ \\Omega}}}} \\\\
\\\\
I_{{ \\text {{main}}}} &= \\frac {{ \\left V-{{ \\text {{CC}}}} - V_{{ \\text {{EE}}}} \\right}} {{ \\left R_{{ \\text {{1}}}} + R_{{ \\text {{2}}}} \\right}} \\\\
&= \\frac {{ \\left {vcc.V:.4g}{{ \\text {{ V}}}} + {vee.V:.4g}{{ \\text {{ V}}}} \\right}} {{ \\left  {r1.ohms:.4g}{{ \\text {{ \\Omega}}}} + {r2.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
& = {i_main.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
E_{{ \\text {{TH}}}} &= I_{{ \\text {{MAIN}}}} \\cdot R_{{ \\text {{2}}}} - V_{{ \\text {{EE}}}} \\\\
&= {i_main.A:.4g}{{ \\text {{ A}}}} \\cdot {r2.ohms:.4g}{{ \\text {{ \\Omega}}}} - {vee.V:.4g}{{ \\text {{ V}}}} \\\\
&= {eth.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text {{EE}}}} - E_{{ \\text {{TH}}}} - V_{{ \\text {{BE}}}} \\right}} {{ \\left R_{{ \\text {{TH}}}} + \\left {{ \\text {{ \\Beta}}}} + 1 \\right \\cdot R_{{ \\text {{E}}}} \\right}} \\\\
&= \\frac {{ \\left {vee.V:.4g}{{ \\text {{ V}}}} - {eth.V:.4g}{{ \\text {{ V}}}} -{vbe.V:.4g}{{ \\text {{ V}}}} \\right}}{{ \\left {rth.ohms:.4g}{{ \\text {{ \\Omega}}}} \\left {beta:.4g} + 1 \\right \\cdot {re.ohms:.4g}{{ \\text {{ \\Omega}}}} \\right}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
I_{{ \\text {{C}}}} &= {{ \\text {{ \\Beta}}}} \\cdot I_{{ \\text {{B}}}} \\\\
&= {beta:.4g} \\cdot {ib.A:.4g}{{ \\text {{ A}}}} \\\\
&= {ic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{C}}}} = V_{{ \\text {{CC}}}} - I_{{ \\text {{C}}}} \\cdot R_{{ \\text {{C}}}} \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} - {ic.A:.4g}{{ \\text {{ A}}}} \\cdot {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
&= {vc.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{B}}}} &= -E_{{ \\text {{TH}}}} - I_{{ \\text{{B}}}} \\cdot R_{{ \\text {{TH}}}} \\\\
&= -{eth.V:.4g}{{ \\text {{ V}}}} - {ib.A:.4g}{{ \\text {{ A}}}} \\cdot {rth.ohms:.4g}{{ \\text {{ \\Omega}}}}\\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls}"""
class boylestad_4_27:
	def __init__(self,*args,**kwargs):
		print("4_27")
		vcc = c.voltage(ran.main(12))
		r1 =  c.resistance(ran.main(1100 ))

		self.question = f"""Calculate the mirrored current I in the circuit if the resistor value is {round(r1.kohms,2)} kohms and the supply voltage is {round(vcc.V,2)} V
		https://lesliecaminadecom.files.wordpress.com/2019/07/u9q74dnf127mai659ec7.png"""

		icontrol = c.current(
		(vcc.V - vbe.V) / r1.ohms
		)

		self.answer = f"""{round(icontrol.mA,2)} mA"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{control}}}} &= \\frac {{ \\left V_{{ \\text {{CC}}}} - V_{{ \\text {{BE}}}} \\right}} {{ R_{{ \\text {{1}}}}}} \\\\
&= \\frac {{ \\left {vcc.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ {r1.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
&= {icontrol.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""
class boylestad_4_28:
	def __init__(self,*args,**kwargs):
		print("4_28")
		vcc = c.voltage(ran.main(6))
		r1 =  c.resistance(ran.main(1300 ))

		self.question = f"""Calculate the current I through each of the transistors Q2 and Q3 in the circuit given that the resistor value is {round(r1.kohms,2)} kohms and the supply voltage is {round(vcc.V,2)} V.
		https://lesliecaminadecom.files.wordpress.com/2019/07/y5y4126r7lh1lf5ri0sg.png"""

		icontrol = c.current(
		(vcc.V - vbe.V) / r1.ohms
		)

		self.answer = f"""{round(icontrol.mA,2)} mA"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{control}}}} &= \\frac {{ \\left V_{{ \\text {{CC}}}} - V_{{ \\text {{BE}}}} \\right}} {{ R_{{ \\text {{1}}}}}} \\\\
&= \\frac {{ \\left {vcc.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ {r1.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
&= {icontrol.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""
class boylestad_4_29:
	def __init__(self,*args,**kwargs):
		print("4_29")
		r1 =  c.resistance(ran.main(5100 ))
		r2 =  c.resistance(ran.main(5100 ))
		r3 =  c.resistance(ran.main(2000 ))
		vee = c.voltage(ran.main(-20))

		self.question = f"""Calculate the constant current I in the circuit given that R1 = {round(r1.kohms,2)} kohms, R2 = {round(r2.kohms,2)} kohms, R3 = {round(r3.kohms,2)} kohms and the supply voltage is {round(vee.V,2)} V.
		https://lesliecaminadecom.files.wordpress.com/2019/07/9nq30cl87ky30ygt0dfn.png"""

		vb = c.voltage(
		(r1.ohms / (r1.ohms + r2.ohms)) * vee.V
		)

		ve = c.voltage(
		vb.V - vbe.V
		)

		ie = c.current(
		(ve.V - (vee.V))
		)

		self.answer = f"""{round(ie.mA,2)} mA"""
		self.latex_solution = f""" {lp}
V-{{ \\text {{B}}}} &= \\left \\frac {{R_{{ \\text {{1}}}} {{ \\left R_{{ \\text {{1}}}}}} + R_{{ \\text {{2}}}}}} \\right \\cdot V_{{ \\text {{EE}}}} \\\\
&= \\left \\frac {{ {r1.ohms:.4g}{{ \\text {{ \\Omega}}}}{{ {r1.ohms:.4g}{{ \\text {{ \\Omega}}}}}} + {r2.ohms}{{ \\text {{ \\Omega}}}}}} \\right \\cdot {vee.V:.4g}{{ \\text {{ V}}}} \\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{E}}}} &= V_{{ \\text {{B}}}} - V_{{ \\text {{BE}}}} \\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\\\
&= {ve.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{E}}}} &= \\left V_{{ \\text {{E}}}} - \\left V_{{ \\text {{EE}}}} \\right \\right \\\\
&= \\right {ve.V:.4g}{{ \\text {{ V}}}} - \\left {vee.V:.4g}{{ \\text {{ V}}}} \\right \\right \\\\
&= {ie.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""

class boylestad_4_30:
	def __init__(self,*args,**kwargs):
		print("4_30")
		vee = c.voltage(ran.main(-18))
		r1 =  c.resistance(ran.main(2200 ))
		r2 =  c.resistance(ran.main(1800 ))
		vz = c.voltage(ran.main(6.2))

		self.question = f"""Calculate the constant current I in the circuit given that R1 = {round(r1.kohms,2)} kohms, R2 = {round(r2.kohms,2)} kohms, VZ = {round(vz.V,2)} V, and the supply voltage is {round(vee.V,2)} V.
		https://lesliecaminadecom.files.wordpress.com/2019/07/j1slfpbupu27nffjrlyv.png"""

		icontrol = c.current(
		(vz.V - vbe.V) / r2.ohms
		)

		self.answer =f"""{round(icontrol.mA,2)} mA"""
		self.latex_solution = f""" {lp}
I_{{ \\text {{control}}}} &= \\frac {{ \\left V_{{ \\text {{Z}}}} - V_{{ \\text {{BE}}}} \\right}} {{ R_{{ \\text {{2}}}}}} \\\\
&= \\frac {{\\left {vz.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right }} {{ {r2.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
&= {icontrol.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""
class boylestad_4_31:
	def __init__(self,*args,**kwargs):
		print("4_31")
		regen = 1
		while regen:
			vcc = c.voltage(ran.main(-18))
			r1 =  c.resistance(ran.main(47_000 ))
			r2 =  c.resistance(ran.main(10_000 ))
			rc =  c.resistance(ran.main(2400))
			re =  c.resistance(ran.main(1100))
			beta = ran.main(120)

			self.question = f"""Determine VCE for the voltage divider bias configuration when VCC = {round(vcc.V,2)} V, R1(top) = {round(r1.kohms,2)} kohms, R2(bottom) = {round(r2.kohms,2)} kohms, RC = {round(rc.kohms,2)} kohms, RE = {round(re.kohms,2)} kohms, and beta = {round(beta,2)}. Use approximate analysis.
			https://lesliecaminadecom.files.wordpress.com/2019/07/jcacmam8963k80575b1r.png"""

			vb = c.voltage(
			(r2.ohms * vcc.V ) / (r1.ohms + r2.ohms)
			)

			ve = c.voltage(
			vb.V - vbe.V
			)

			ie = c.current(
			ve.V / re.ohms
			)

			vce = c.voltage(
			vcc.V + ie.A * (rc.ohms + re.ohms)
			)

			if vce.V < 0:
				regen = 0

		self.answer = f"""{round(vce.V,2)} V"""
		self.latex_solution = f""" {lp}
V_{{ \\text {{B}}}} &= \\frac {{ \\left R_{{ \\text {{2}}}} \\cdot V_{{ \\text {{CC}}}} \\right}}{{ \\left R_{{ \\text {{1}}}} + R_{{ \\text {{2}}}} \\right}} \\\\
&= \\frac {{ \\left {r2.ohms:.4g}{{ \\text {{ \\Omega}}}} \\cdot {vcc.V}{{ \\text {{ V}}}} \\right}}{{ \\left {r1.ohms:.4g}{{ \\text {{ \\Omega}}}} + {r2.ohms}{{ \\text {{ \\Omega}}}} \\right}} \\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
V_{{ \\text {{E}}}} &= V_{{ \\text {{B}}}} - V_{{ \\text {{BE}}}} \\\\
&= {vb.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\\\
&= {ve.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
I_{{ \\text {{E}}}} &= \\frac {{ V_{{ \\text {{E}}}}}}{{ R_{{ \\text {{E}}}}}} \\\\
&= \\frac {{ {ve.V:.4g}{{ \\text {{ V}}}}}} {{ {re.ohms:.4g}{{ \\text {{ \\Omega}}}}}} \\\\
&= {ie.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
V_{{ \\text {{CE}}}} &= V_{{ \\text {{CC}}}} + I_{{ \\text {{E}}}} \\cdot \\left R_{{ \\text {{C}}}} + R_{{ \\text {{E}}}} \\right \\\\
&= {vcc.V:.4g}{{ \\text {{ V}}}} + {ie.A:.4g}{{ \\text {{ A}}}} \\cdot \\left {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} + {re.ohms}{{ \\text {{ \\Omega}}}} \\right \\\\
&= {vce.V:.4g}{{ \\text {{ V}}}} \\\\
\\\\
{ls} """
class boylestad_4_32:
	def __init__(self,*args,**kwargs):
		print("4_32")
		icsat = c.current(ran.main(10), 'mA')
		hfe = ran.main(250)
		vcc = c.voltage(10)
		vi = c.voltage(10)

		self.question = f"""Determine maximum RB, and RC for the transistor inverter in the figure if ICsat ={round(icsat.mA,2)} mA and hfe = {round(hfe,2)}.
		https://lesliecaminadecom.files.wordpress.com/2019/07/l3yu2b6k51ubj18av592.png"""

		rc =  c.resistance(
		vcc.V / icsat.A
		)

		ib = c.current(
		icsat.A / hfe
		)

		rb =  c.resistance(
		(vi.V - vbe.V) / ib.A
		)

		self.answer = f"""{round(rb.kohms,2)} kohms, {round(rc.kohms,2)} kohms"""
		self.latex_solution = f""" {lp}
R_{{ \\text {{C}}}} &= \\frac {{ V_{{ \\text {{CC}}}}}} {{ I_{{ \\text {{Csat}}}}}} \\\\
&= \\frac {{ {vcc.V:.4g}{{ \\text {{ V}}}}}} {{ {icsat.A:.4g}{{ \\text {{ A}}}}}} \\\\
&= {rc.ohms:.4g}{{ \\text {{ \\Omega}}}} \\\\
\\\\
I_{{ \\text {{B}}}} &= \\frac {{ I_{{ \\text {{Csat}}}}}} {{ H_{{ \\text {{FE}}}}}} \\\\
&= \\frac {{ {icsat.A:.4g}{{ \\text {{ A}}}}}} {{ {hfe:.4g}}} \\\\
&= {ib.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
R_{{ \\text {{B}}}} &= \\frac {{ \\left V_{{ \\text {{I}}}} - V_{{ \\text {{BE}}}} \\right}} {{ I_{{ \\text {{B}}}}}} \\\\
&= \\frac {{ \\left {vi.V:.4g}{{ \\text {{ V}}}} - {vbe.V:.4g}{{ \\text {{ V}}}} \\right}} {{ {ib.A:.4g} {{ \\text {{ A}}}}}} \\\\
&= {rb.ohms:.4g} {{ \\text {{ \\Omega}}}} \\\\
\\\\
{ls}"""
class boylestad_4_35:
	def __init__(self,*args,**kwargs):
		print("4_35")
		rbperre_list = [250, 10, 0.01]
		rbperre = ran.main(random.choice(rbperre_list)*100)/100
		beta = ran.main(50)
		deltaICO = c.current(ran.main(19.9), 'nA')

		self.question = f"""Calculate the stability factor (SICO) and the change in IC from 25 degC to 100 degC for the transistor with beta = {round(beta,2)} and deltaICO = {round(deltaICO.nA,2)} nA for an emitter-bias arrangement with RB/RE = {round(rbperre,2)}"""

		sico = (
		(beta * ( 1 + rbperre )) / (beta + rbperre)
		)

		deltaic = c.current(
		sico * deltaICO.A
		)

		self.answer  = f"""{round(sico,2)}, {round(deltaic.nA,2)} nA"""
		self.latex_solution = f""" {lp}
S_{{ \\text {{Ico}}}} &= \\frac {{ \\left {{ \\text {{ \\Beta}}}} \\cdot \\left 1 + R_{{ \\text {{perre}}}} \\right \\right}} {{ \\left {{ \\text {{ \\Beta}}}} + R_{{ \\text {{perre}}}} \\right}} \\\\
&= \\frac {{ \\left {beta:/4g} \\cdot \\left 1 + {rbperre.ohms:.4g}{{ \\text {{ \\Omega}}}} \\right \\right}} {{ \\left {beta:.4g} + {rbperre.ohms:.4g}{{ \\text {{ \\Omega}}}} \\right}} \\\\
& = {sico:.4g} \\\\
\\\\
{{ \\text {{ \\Delta}}}} I_{{ \\text {{C}}}} &= S_{{ \\text {{ico}}}} \\cdot {{ \\text {{ \\Delta}}}} I_{{ \\text {{CO}}}} \\\\
&= {sico:.4g} \\cdot {deltaICO.A:.4g}{{ \\text {{ A}}}} \\\\
&= {deltaic.A:.4g}{{ \\text {{ A}}}} \\\\
\\\\
{ls}"""
class boylestad_4_36:
	def __init__(self,*args,**kwargs):
		print("4_36")
		regen = 1
		counter = 100
		while regen:

			beta = ran.main(100)
			deltaVBE = c.voltage(0.65-0.48)

			rba =  c.resistance(ran.main(240_000 ))
			rbb =  c.resistance(ran.main(240_000 ))
			reb =  c.resistance(ran.main(1000))
			rbc =  c.resistance(ran.main(47_000 ))
			rec =  c.resistance(ran.main(4700 ))

			self.question = f"""Determine the stability factor (SVBE) and the change in IC from 25 degC to 100 degC for the transistor with beta = {round(beta,2)} and deltaVBE = {round(deltaVBE.V,2)} for the following bias arrangements:
	a) Fixed bias with RB = {round(rba.kohms,2)} kohms.
	b) Emitter - bias with RB = {round(rbb.kohms,2)} kohms, RE = {round(reb.kohms,2)} kohms.
	c) Emitter - bias with RB = {round(rbc.kohms,2)} kohms, RE = {round(rec.kohms,2)} kohms."""

			#A
			svbea = (
			-beta / rba.ohms
			)

			deltaica = c.current(
			svbea * deltaVBE.V
			)

			#B
			svbeb = (
			( -beta / reb.ohms) / (beta + rbb.ohms/reb.ohms)
			)

			deltaicb = c.current(
			svbeb * deltaVBE.V
			)

			#C
			svbec = (
			-1 / rec.ohms
			)

			deltaicc = c.current(
			svbec * deltaVBE.V
			)

			counter = counter - 1
			if counter < 0:
				raise IterationError('iteration loops exceeded')

			if (rbb.ohms / reb.ohms) > beta and beta > (rbc.ohms/rec.ohms):
				regen = 0


		self.answer  = f"""{svbea:4.4}, {deltaica.uA:4.4} uA; {svbeb:4.4}, {deltaicb.uA:4.4} uA; {svbec:4.4}, {deltaicc.uA:4.4} uA"""
		self.latex_solution = f""" {lp}
S_{{ \\text {{vbea}}}} &= \\frac {{ - {{ \\text {{ \\Beta}}}}}} {{ R_{{ \\text {{BA}}}}}} \\\\
&= \\frac {{ -{beta:.4g}}} {{ {rba.ohms:.4g} {{ \\text {{ \\Omega}}}}}}\\\\
&= {svbea:.4g} \\\\
\\\\
{{ \\text {{ \\Delta}}}} I_{{ \\text {{CA}}}} &= S_{{ \\text {{vbea}}}} \\cdot {{ \\text {{ \\Delta}}}}V_{{ \\text {{BE}}}} \\\\
&= {svbea:.4g} \\cdot {deltaVBE.V:.4g} {{ \\text {{ V}}}}\\\\
&= {deltaica.A:.4g} {{ \\text {{ A}}}} \\\\
\\\\
S_{{ \\text {{vbeb}}}} &= \\frac  {{ \\left \\frac {{ -{{ \\text {{ \\Beta}}}}}} {{ R_{{ \\text {{EB}}}}}}  \\right}} {{ \\left {{ \\text {{ \\Beta}}}} + \\frac {{ R_{{ \\text {{BB}}}}}} {{ R_{{ \\text {{EB}}}}}} \\right}} \\\\
&= \\frac {{ \\left \\frac {{ -{beta:.4g}}} {{ {reb.ohms:.4g} {{ \\text {{ \\Omega}}}}}} \\right}} {{ {beta:.4g} + \\frac {{ {rbb.ohms} {{ \\text {{ \\Omega}}}}}} {{ {reb.ohms} {{ \\text {{ \\Omega}}}}}}}} \\\\
&= {svbeb:.4g} \\\\
\\\\
{{ \\text {{ \\Delta}}}} I_{{ \\text {{CB}}}} &= S_{{ \\text {{vbeb}}}} \\cdot {{ \\text {{ \\Delta}}}} V_{{ \\text {{BE}}}} \\\\
&= {svbeb:.4g} \\cdot {deltaVBE.V} {{ \\text {{ V}}}} \\\\
&= {deltaicb.A:.4g} {{ \\text {{ A}}}} \\\\
\\\\
S_{{ \\text {{vbec}}}} &= \\frac {{-1}} {{R_{{ \\text {{EC}}}}}} \\\\
&= \\frac {{-1}}{{ {rec.ohms:.4g} {{ \\text {{ \\Omega}}}}}} \\\\
&= {svbec:.4g} \\\\
\\\\
{{ \\text {{ \\text {{ \\Delta}}}}}}I_{{ \\text {{CC}}}} &= S_{{ \\text {{vbec}}}} \\cdot {{ \\text {{ \\Delta}}}}V_{{ \\text {{BE}}}} \\\\
&= {svbec:.4g} \\cdot {deltaVBE.V:.4g} {{ \\text {{ V}}}} \\\\
&= {deltaicc.A:.4g} {{ \\text {{ A}}}} \\\\
\\\\
{ls}"""
#chapter 5 - BJT ac analysis

VBE = c.voltage(0.7)

class boylestad_5_1():
	def __init__(self):
		fb = Fixed_Bias()
		fb.init_random(vcc = 12, rb = 470_000, rc = 3000, beta = 100, ro = 50_000)

		self.question = f"""{fb.description} determine Zi, Zo and Av."""
		self.answer = f"""{round(fb.ZI.kohms, 4)} kohms, {round(fb.ZO.kohms, 4)} kohms, {round(fb.AV, 4)}"""

class boylestad_5_2():
	def __init__(self):
		vd = Voltage_Divider()
		vd.init_random(vcc = 22, r1 = 56_000, r2 = 8200, rc = 6800, re = 1500, beta = 90, ro = 50_000)

		self.question = f"""{vd.description} determine Zi, Zo and Av."""
		self.answer = f"""{round(vd.ZI.kohms, 4)} kohms, {round(vd.ZO.kohms, 4)} kohms, {round(vd.AV, 4)}"""

class boylestad_5_3():
	def __init__(self):
		es = Emitter_Stabilized()
		es.init_random(vcc = 20, rb = 470_000, rc = 2200, re = 560, beta = 120, ro = 40_000, bypass = True)

		self.question = f"""{es.description} determine the value of Zi, Zo, and Av."""
		self.answer = f"""{round(es.ZI.ohms, 4)} ohms, {round(es.ZO.kohms, 4)} kohms, {round(es.AV, 4)}"""

class boylestad_5_4():
	def __init__(self):
		es = Emitter_Stabilized()
		es.init_random(vcc = 20, rb = 470_000, rc = 2200, re = 560, beta = 120, ro = 40_000, bypass = False)
		self.question = f"""{es.description} determine the value of Zi, Zo, and Av."""
		self.answer = f"""{round(es.ZI.kohms, 4)} kohms, {round(es.ZO.kohms, 4)} kohms, {round(es.AV, 4)}"""

class boylestad_5_5():
	def __init__(self):

		vd = Voltage_Divider()
		vd.init_random(vcc = 16, r1 = 90_000, r2 = 10_000, rc = 2200, re = 680, beta = 210, ro = 50_000, bypass = False)

		self.question = f"""{vd.description} determine the value of Zi, Zo and Av."""
		self.answer = f"""{round(vd.ZI.kohms, 4)} kohms, {round(vd.ZO.kohms, 4)} kohms, {round(vd.AV, 4)}"""

class boylestad_5_6():
	def __init__(self):

		vd = Voltage_Divider()
		vd.init_random(vcc = 16, r1 = 90_000, r2 = 10_000, rc = 2200, re = 680, beta = 210, ro = 50_000, bypass = True)

		self.question = f"""{vd.description} determine the value of Zi, Zo and Av."""
		self.answer = f"""{round(vd.ZI.kohms, 4)} kohms, {round(vd.ZO.kohms, 4)} kohms, {round(vd.AV, 4)}"""

class boylestad_5_7():
	def __init__(self):

		ef = Emitter_Follower()
		ef.init_random(vcc = 12, rb = 220_000, re = 3300, beta = 100, ro = 25_000)

		self.question = f"""{ef.description} determine the value of Zi, Zo, and Av."""
		self.answer = f"""{round(ef.ZI.kohms, 4)} kohms, {round(ef.ZO.ohms, 4)} ohms, {round(ef.AV, 4)}"""

class boylestad_5_8():
	def __init__(self):

		cb = Common_Base()
		cb.init_random(vcc = 8, vee = 2, re = 1000, rc = 5000, alpha = 0.98, ro = 1_000_000)

		self.question = f""""{cb.description} determine the value of Zi, Zo, and Av."""
		self.answer = f"""{round(cb.ZI.ohms, 4)} ohms, {round(cb.ZO.kohms, 4)} kohms, {round(cb.AV, 4)}"""

class boylestad_5_9():
	def __init__(self):

		cf = Collector_Feedback()
		cf.init_random(vcc = 9, rc = 2700, rf = 180_000, beta = 200, ro = 20_000)

		self.question = f"""{cf.description} determine the value of Zi, Zo and Av."""
		self.answer = f"""{round(cf.ZI.ohms, 4)} ohms, {round(cf.ZO.kohms, 4)} kohms, {round(cf.AV, 4)}"""
