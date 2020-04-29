from generator import random_handler as ran
from generator import constants_conversions as c
from generator.latex_engine import *
from generator.latex_engine import LATEX_SOLUTION_PREFIX as lp
from generator.latex_engine import LATEX_SOLUTION_SUFFIX as ls
import sympy as sym
import math
import random

x, y, z = sym.symbols('x y z', real = True)#generic variables

#fewson
class fewson_2_1:
    def __init__(self,*args,**kwargs):
        print('21')
        regen = True
        while regen:
            i = random.randint(0,1)
            ton_list = [1,3]
            ton = c.time(ran.main(ton_list[i]), 'ms')
            vsource = c.voltage(ran.main(48))
            rload = c.resistance(ran.main(24))
            freq = c.frequency(ran.main(350))

            self.question = f"""A dc to dc chopper operates from a {vsource.V:.4g} V battery source into a resistive load of {rload.ohms:.4g} ohms. The frequency of the chopper is set to {freq.Hz:.4g} Hz. Determine the average and rms load current and the load power values when chopper on time is {ton.ms:.4g} ms."""

            period = c.time(1/freq.Hz)
            print('period' + str(period.ms))
            print('ton' + str(ton.ms))
            if period.ms > ton.ms:
                regen = False

        vaverage = c.voltage(vsource.V * freq.Hz * ton.s )
        iaverage = c.current(vaverage.V / rload.ohms)
        vrms = c.voltage( vsource.V * math.sqrt(freq.Hz * ton.s))
        irms = c.current( vrms.V / rload.ohms )
        powerP = c.power( irms.A**2 * rload.ohms )

        self.answer = f"""{iaverage.A:.4g} A, {irms.A:.4g} A, {powerP.W:.4g} W"""

        self.latex_question = f"""
A dc to dc chopper operates from a {vsource.V:.4g} V battery source into a resistive load of {rload.ohms:.4g} ohms. The frequency of the chopper is set to {freq.Hz:.4g} Hz. Determine the average and rms load current and the load power values when chopper on time is {ton.ms:.4g} ms.
"""



        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
    {{V}}_{{ave}} &= {{V}}_{{in}} {{f}} {{t}}_{{on}} \\\\
     &= \\left({vsource.V:.4g} \\text{{ V}} \\right) \\left({freq.Hz:.4g} \\text{{ Hz}}\\right) \\left({ton.ms:.4g} \\text{{ ms}}\\right)   \\\\
     &= {vaverage.V:.4g} \\text{{ V}} \\\\

    {{I}}_{{ave}} &= \\frac{{{{V}}_{{ave}}}}     {{{{R}}_{{load}}}} \\\\
     &= \\frac{{{vaverage.V:.4g} \\text{{ V}}}}  {{{rload.ohms:.4g}  \\Omega}} \\\\
     &= {iaverage.A:.4g} \\text{{ A}} \\\\

    {{V}}_{{rms}} &= {{V}}_{{in}} \\sqrt{{   {{f}} {{t}}_{{on}}  }} \\\\
     &= \\left({vsource.V:.4g} \\text{{ V}} \\right) \\sqrt{{ \\left({freq.Hz:.4g} \\text{{ Hz}}\\right) \\left({ton.ms:.4g} \\text{{ ms}}\\right) }}  \\\\
     &= {vrms.V:.4g} \\text{{ V}} \\\\

    {{I}}_{{rms}} &= \\frac{{{{V}}_{{ave}}}}     {{{{R}}_{{load}}}} \\\\
     &= \\frac{{{vrms.V:.4g} \\text{{ V}}}}  {{{rload.ohms:.4g} \\Omega}} \\\\
     &= {irms.A:.4g} \\text{{ A}} \\\\

    {{P}} &= \\left({{I}}_{{rms}}\\right)^{{2}} {{R}}_{{load}} \\\\
     &= \\left( {{{irms.A:.4g} \\text{{ A}}}} \\right)  ^{{2}} \\left({{{rload.ohms:.4g}  \\Omega}} \\right) \\\\
     &= {powerP.W:.4g} \\text{{ W}} \\\\
{LATEX_SOLUTION_SUFFIX}
"""

class fewson_2_2:
    def __init__(self,*args,**kwargs):
        print('22')
        regen = True
        while regen:
            rload = c.resistance(ran.main(1))
            lload = c.inductance(ran.main(10), 'mH')
            vsource = c.voltage(ran.main(24))
            frequency = c.frequency(ran.main(100))
            ton = c.time(ran.main(5), 'ms')

            self.question = f"""A dc to dc chopper has an inductive load of {rload.ohms:.4g} ohms resistance and {lload.mH:.4g} mH inductance. Source voltage is {vsource.V:.4g} V. The frequency of the chopper is set to {frequency.Hz:.4g} Hz and the on-time to {ton.ms:.4g} ms. Determine the average, maximum, minimum, and RMS load currents."""

            period = c.time(1/frequency.Hz)
            if period.s > ton.s:
                regen = False

        toff = c.time(period.s - ton.s)

        vaverage = c.voltage( vsource.V * frequency.Hz * ton.s )
        iaverage = c.current( vaverage.V / rload.ohms )
        #y is I1, x is Io
        equation1 = sym.Eq(
        y,
        (vsource.V / rload.ohms) * (1 - math.exp(-rload.ohms * ton.s / lload.H)) + x * math.exp( - rload.ohms * ton.s / lload.H )
        )

        equation2 = sym.Eq(
        x,
        y * math.exp(- rload.ohms * toff.s / lload.H)
        )

        equation_list = [equation1, equation2]
        solution_set = sym.linsolve(equation_list, x, y)
        solution_list = list(solution_set.args[0])
        print(solution_list)
        i0 = c.current(solution_list[0])
        i1 = c.current(solution_list[1])
        print(i0.A)
        print(i1.A)
        i_of_t_charge = (vsource.V/rload.ohms) * (1 - sym.exp(-rload.ohms * x/lload.H)) + (i0.A * sym.exp(- rload.ohms * x / lload.H ))

        #print(pretty(i_of_t_charge))

        i_of_t_discharge = i1.A * sym.exp(-rload.ohms * x / lload.H)



        irms = c.current(
        math.sqrt(
        (1/period.s) * (sym.integrate(i_of_t_charge**2, (x, 0, ton.s)) + sym.integrate(i_of_t_discharge**2, (x, 0, toff.s))
        )
        )
        )
        self.answer = f"""{iaverage.A:.4g} A, {i1.A:.4g} A, {i0.A:.4g} A, {irms.A:.4g} A"""

        self.latex_question = f"""{LATEX_ITEM_PREFIX} A dc to dc chopper has an inductive load of {rload.ohms:.4g} ohms resistance and {lload.mH:.4g} mH inductance. Source voltage is {vsource.V:.4g} V. The frequency of the chopper is set to {frequency.Hz:.4g} Hz and the on-time to {ton.ms:.4g} ms. Determine the average, maximum, and minimum load currents."""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{T}} &= \\frac{{1}}   {{f}} {LATEX_END}
&= \\frac{{1}}   {{{frequency.Hz:.4g} \\text{{ Hz}}   }} {LATEX_END}
&= {period.ms:.4g} \\text{{ ms}} {LATEX_END}

{{t}}_{{off}} &= {{T}} - {{t}}_{{on}} {LATEX_END}
 &= {{{period.s:.4g} \\text{{ s}} }} - {{{ton.s:.4g} \\text{{ s}}}} {LATEX_END}
 &= {{{toff.ms:.4g} \\text{{ ms}}}} {LATEX_END}

   {{V}}_{{ave}} &= {LP}{{V}}_{{in}}{RP} {LP} {{f}}{RP} {LP}{{t}}_{{on}}{RP}{LATEX_END}
 &= {LP}{{{vsource.V:.4g} \\text{{ V}}}}{RP} {LP}{{{frequency.Hz:.4g} \\text{{ Hz}}}}{RP} {LP}{{{ton.ms:.4g} \\text{{ ms}}}}{RP}{LATEX_END}
 &= {{{vaverage.V:.4g} \\text{{ V}}}} {LATEX_END}

   {{I}}_{{ave}} &= \\frac{{{{V}}_{{ave}}}}    {{{{R}}_{{load}}}} {LATEX_END}
 &= \\frac{{{vaverage.V:.4g} \\text{{ V}}}}    {{{rload.ohms:.4g}  \\Omega}} {LATEX_END}
 &= {{{iaverage.A:.4g} \\text{{ A}}}} {LATEX_END}

 {{I}}_{{max}} &= \\frac{{{{V}}_{{in}}}} {{{{R}}_{{load}}}} {LP} 1 - e^{{\\frac{{-{{R}}_{{load}} {{t}}_{{on}}   }} {{L}}  }} {RP} + {{I}}_{{min}} e^{{\\frac{{- {{R}}_{{load}} {{t}}_{{on}}}}    {{L}}    }} {LATEX_END}
 &= \\frac{{{vsource.V:.4g} \\text{{ V}}}}    {{{rload.ohms:.4g}  \\Omega}} {LP} 1 - e^{{\\frac{{{LP}-{rload.ohms:.4g}  \\Omega{RP}{LP}{{{ton.ms:.4g} \\text{{ ms}}}}{RP}}} {{{lload.H:.4g} \\text{{ H}}}}    }} {RP}+ {{I}}_{{min}} e^{{\\frac{{ -{LP}{{{rload.ohms:.4g} \\Omega}}{RP}    {LP}{{{ton.ms:.4g} \\text{{ ms}}}}{RP}}}  {{{lload.H:.4g} \\text{{ H}}}}        }} {LATEX_END}
 {{I}}_{{min}} &= {{I}}_{{max}} e^{{\\frac{{-{{R}}_{{load}} {{t}}_{{off}}   }} {{L}}  }} {LATEX_END}
 &= {{I}}_{{max}} e^{{\\frac{{{LP}-{rload.ohms:.4g}  \\Omega{RP}{LP}{{{toff.ms:.4g} \\text{{ ms}}}}{RP}}} {{{lload.H:.4g} \\text{{ H}}}}    }}  {LATEX_END}
 {{I}}_{{max}} &= {{{i0.A:.4g} \\text{{ A}}}}{LATEX_END}
 {{I}}_{{min}} &= {{{i1.A:.4g} \\text{{ A}}}}{LATEX_END}
{LATEX_SOLUTION_SUFFIX}"""

class fewson_2_3:
    def __init__(self,*args,**kwargs):
        print('23')
        regen = True
        while regen:

            vbattery = c.voltage(ran.main(96))
            rarf = c.resistance(ran.main(100), 'mohms')
            kv = c.voltage(ran.main(10), 'mV')
            frequency = c.frequency(ran.main(125))
            period = c.time(1/frequency.Hz)
            ton = c.time(ran.main(6), 'ms')
            ia = c.current(ran.main(100))
            toff = c.time(period.s - ton.s)

            torque2 = c.torque(ran.main(10))

            self.question = f"""A dc series chopper drive has the following parameters: Battery voltage = {vbattery.V:.4g} V, (Ra + Rf) = {rarf.ohms:.4g} ohms, kv = {kv.mV:.4g} mV / Arad/s , chopper frequency = {frequency.Hz:.4g} Hz. a) Calculate the armature speed and torque with an average armature current of {ia.A:.4g} A and a chopper on time of {ton.ms:.4g} ms. b) Determine the motor speed and armature current at a torque of {torque2.Nm:.4g} Nm with on time and off time similar to situation a."""

            if period.s > ton.s:
                regen = False

        vaverage = c.voltage( vbattery.V * ton.s * frequency.Hz )
        backemf = c.voltage( vaverage.V - ia.A * rarf.ohms )
        omega = c.angularVelocity( backemf.V / (kv.V * ia.A) , 'radpers')
        torque = c.torque( kv.V * ia.A**2 )

        ia2 = c.current( math.sqrt( torque2.Nm * kv.V ))
        backemf2 = c.voltage( vaverage.V - ia2.A * rarf.ohms )
        omega2 = c.angularVelocity( backemf2.V / (kv.V * ia2.A) , 'radpers')

        self.answer = f"""{omega.revpermin:.4} rev/min, {torque.Nm:.4} Nm; {omega2.revpermin:.4} rev/min, {ia2.A:.4} A"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX} A dc series chopper drive has the following parameters: Battery voltage = {vbattery.V:.4g} V, (Ra + Rf) = {rarf.ohms:.4g} ohms, kv = {kv.mV:.4g} mV / Arad/s , chopper frequency = {frequency.Hz:.4g} Hz. a) Calculate the armature speed and torque with an average armature current of {ia.A:.4g} A and a chopper on time of {ton.ms:.4g} ms. b) Determine the motor speed and armature current at a torque of {torque2.Nm:.4g} Nm with on time and off time similar to situation a."""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{V}}_{{ave}} &= {{V}}_{{in}} {{t}}_{{on}} {{f}} {LATEX_END}
&= {LP}{vbattery.V:.4g}\\text{{ V}}{RP}   {LP}{ton.ms:.4g} \\text{{ ms}}{RP}  {LP}{frequency.Hz:.4g}\\text{{ Hz}}{RP} {LATEX_END}
&= {vaverage.V:.4g}\\text{{ V}} {LATEX_END}

{{E}}_{{b}} &= {{V}}_{{ave}} - {{I}}_{{a}} {LP}{{R}}_{{a}} + {{R}}_{{f}}{RP} {LATEX_END}
&= {vaverage.V:.4g}\\text{{ V}} - {LP}{ia.A:.4g} \\text{{ A}}{RP} {LP} {rarf.ohms:.4g} \\Omega {RP} {LATEX_END}
&= {backemf.V:.4g} \\text{{ V}} {LATEX_END}

\\omega &= \\frac{{{{E}}_{{b}}}}   {{{{k}}_{{v}} {{I}}_{{a}}}} {LATEX_END}
&= \\frac{{{backemf.V:.4g} \\text{{ V}}}}   {{{LP}{kv.V:.4g}{RP}    {LP}{ia.A:.4g}\\text{{ A}}{RP}}} {LATEX_END}
&= {omega.radpers:.4g} \\frac{{\\text{{rad}}}}      {{\\text{{s}}}} {LATEX_END}
&= {omega.revpermin:.4g} \\frac{{\\text{{rev}}}}      {{\\text{{min}}}} {LATEX_END}

\\tau &= {{k}}_{{v}} {{I}}_{{a}}^{{2}} {LATEX_END}
&= {LP}{kv.V:.4g}{RP}   {LP}{ia.A:.4g}\\text{{ A}}{RP}^{{2}} {LATEX_END}
&= {torque.Nm:.4g} \\text{{Nm}} {LATEX_END}

{{I}}_{{a2}} &= \\sqrt{{\\tau {{k}}_{{v}}}} {LATEX_END}
&= \\sqrt{{{LP}{torque.Nm:.4g}\\text{{ Nm}}{RP} {LP}{kv.V:.4g}{RP}}}{LATEX_END}
&= {ia2.A:.4g}\\text{{ A}} {LATEX_END}

{{E}}_{{b2}} &= {{V}}_{{ave}} - {{I}}_{{a2}} {LP}{{R}}_{{a}} + {{R}}_{{f}}{RP} {LATEX_END}
&= {vaverage.V:.4g}\\text{{ V}} - {LP}{ia2.A:.4g} \\text{{ A}}{RP} {LP} {rarf.ohms:.4g} \\Omega {RP} {LATEX_END}
&= {backemf2.V:.4g} \\text{{ V}} {LATEX_END}

\\omega_{{2}} &= \\frac{{{{E}}_{{b2}}}}   {{{{k}}_{{v}} {{I}}_{{a2}}}} {LATEX_END}
&= \\frac{{{backemf2.V:.4g} \\text{{ V}}}}   {{{LP}{kv.V:.4g}{RP}    {LP}{ia2.A:.4g}\\text{{ A}}{RP}}} {LATEX_END}
&= {omega2.radpers:.4g} \\frac{{\\text{{rad}}}}      {{\\text{{s}}}} {LATEX_END}
&= {omega2.revpermin:.4g} \\frac{{\\text{{rev}}}}      {{\\text{{min}}}} {LATEX_END}
{LATEX_SOLUTION_SUFFIX}
"""

class fewson_2_4:
    def __init__(self,*args,**kwargs):
        print('24')

        repeat = True
        while repeat:

            iload = c.current(ran.main(3))
            rload = c.resistance(ran.main(10))
            vbattery = c.voltage(ran.main(12))
            lchopper = c.inductance(ran.main(20), 'uH')
            cchopper = c.capacitance(ran.main(100), 'uF')
            frequency = c.frequency(ran.main(50), 'kHz')


            self.question = f"""A stepup chopper is to deliver {iload.A:.4g} A into the {rload.ohms:.4g} ohms load. The battery voltage is {vbattery.V:.4g} V , L = {lchopper.uH:.4g} uH, C = {cchopper.uF:.4g} uF, and the chopper frequency is {frequency.kHz:.4g} kHz. Determine the on-time of the chopper, the battery current variation, and the average battery current."""


            vload = c.voltage(iload.A * rload.ohms)
            if vload.V > vbattery.V:
                repeat = False


            dutycycle = c.percentage( 1 - (vbattery.V / vload.V) , 'decimal')
            period = c.time(1/frequency.Hz)
            ton = c.time(dutycycle.decimal * period.s)
            deltai = c.current( vbattery.V * ton.s / lchopper.H )

            ibattery = c.current(iload.A / (1 - dutycycle.decimal))
            ibmax = c.current( ibattery.A + deltai.A/2)
            ibmin = c.current( ibattery.A - deltai.A/2)

            self.answer = f"""{ton.us:.4g} us, {ibattery.A:.4g} A, {ibmax.A:.4g} A, {ibmin.A:.4g} A"""
            self.latex_question = f"""{LATEX_ITEM_PREFIX}A stepup chopper is to deliver {iload.A:.4g} A into the {rload.ohms:.4g} ohms load. The battery voltage is {vbattery.V:.4g} V , L = {lchopper.uH:.4g} uH, C = {cchopper.uF:.4g} uF, and the chopper frequency is {frequency.kHz:.4g} kHz. Determine the on-time of the chopper, the battery current variation, and the average battery current."""
            self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{D}} &= 1 - \\frac{{{{V}}_{{in}}}} {{{{V}}_{{load}}}} {LATEX_END}
&= 1 - \\frac{{{vbattery.V:.4g}\\text{{ V}}}} {{{vload.V:.4g}\\text{{ V}}}}{LATEX_END}
&= {dutycycle.percent:.4g} \\% {LATEX_END}

{{T}} &= \\frac {{1}} {{f}} {LATEX_END}
&= \\frac{{1}} {{{frequency.Hz:.4g}\\text{{ Hz}}}} {LATEX_END}
&= {period.ms:.4g} \\text{{ ms}} {LATEX_END}

{{t}}_{{on}} &= {{D}} {{T}} {LATEX_END}
&= {LP}{dutycycle.percent:.4g}\\%{RP} {lp}{period.ms:.4g} \\text{{ ms}}{rp}{LATEX_END}
&= {ton.ms:.4g}\\text{{ ms}} {LATEX_END}

\\Delta{{i}} &= \\frac{{{{V}}_{{in}} {{t}}_{{on}}}}      {{L}} {LATEX_END}
&= \\frac{{{lp}{vbattery.V:.4g}\\text{{ V}}{rp} {lp}{ton.ms:.4g} \\text{{ ms}}{rp}}}   {{{lchopper.uH:.4g} \\text{{ uH}}}} {LATEX_END}
&= {deltai.A:.4g} \\text{{ A}} {LATEX_END}

{{I}}_{{in}} &= \\frac {{{{I}}_{{load}}}} {{1 - D}} {LATEX_END}
&= \\frac{{{iload.A:.4g}\\text{{ A}}}}   {{1 - {dutycycle.percent:.4g} \\%}} {LATEX_END}
&= {ibattery.A:.4g} \\text{{ A}} {LATEX_END}

{{I}}_{{inmax}} &= {{I}}_{{in}} + \\frac{{\\Delta I}}{{2}} {LATEX_END}
&= {ibattery.A:.4g} \\text{{ A}} + \\frac{{{deltai.A:.4g}\\text{{ A}}}} {{2}} {LATEX_END}
&= {ibmax.A:.4g} \\text{{ A}}{LATEX_END}

{{I}}_{{inmin}} &= {{I}}_{{in}} - \\frac{{\\Delta I}}{{2}} {LATEX_END}
&= {ibattery.A:.4g} \\text{{ A}} - \\frac{{{deltai.A:.4g}\\text{{ A}}}} {{2}} {LATEX_END}
&= {ibmin.A:.4g} \\text{{ A}}{LATEX_END}
{LATEX_SOLUTION_SUFFIX}
"""
class fewson_2_5:
    def __init__(self,*args,**kwargs):
        print('25')
        toff = c.time(ran.main(20), 'us')
        vbattery = c.voltage(ran.main(96))
        iload = c.current(ran.main(100))

        self.question = f"""What value of capacitor is required to force commutate a thyristor with a turnoff time of {toff.us:.4g} us with a {vbattery.V:.4g} V and a full load current of {iload.A:.4g} A?"""

        capacitor = c.capacitance(1.43 * toff.s * iload.A / vbattery.V)

        self.answer = f"""{capacitor.uF:.4g} uF"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX}What value of capacitor is required to force commutate a thyristor with a turnoff time of {toff.us:.4g} us with a {vbattery.V:.4g} V and a full load current of {iload.A:.4g} A?"""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{C}} &= \\frac{{1.43 {{t}}_{{off}} {{I}}_{{load}}}} {{{{V}}_{{in}}}} {LATEX_END}
&= \\frac{{1.43 {lp}{toff.ms:.4g}\\text{{ ms}}{rp} {lp}{iload.A:.4g} \\text{{ A}}{rp}}}   {{{vbattery.V:.4g} \\text{{ V}}}} {LATEX_END}
&= {capacitor.uF:.4g} \\mu \\text{{F}} {LATEX_END}
{LATEX_SOLUTION_SUFFIX}
"""

class fewson_3_1:
    def __init__(self,*args,**kwargs):
        print('31')
        vsourceRMS = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        rload = c.resistance(ran.main(100))
        alpha_list = [30, 140, 120]
        i = random.randint(0,2)
        alpha = c.angle(ran.main(alpha_list[i]), 'degrees')

        self.question = f"""A thyristor half-wave half controlled converter has a supply voltage of {vsourceRMS.V:.4} V at {frequency.Hz:.4} Hz and a load resistance of {rload.ohms:.4} ohms. What are the average values of load voltage and current when the firing delay angle is {alpha.degrees:.4} degrees?"""

        if alpha.degrees > 180:
            alpha = c.angle(180, 'degrees')

        vaverage = c.voltage(
        ((math.sqrt(2) * vsourceRMS.V) / (2*math.pi)) * ( 1 + math.cos(alpha.radians))
        )

        iaverage = c.current(vaverage.V / rload.ohms)

        vrms = c.voltage(sym.sqrt(
        (1/(2*math.pi)) * sym.integrate((vsourceRMS.V * math.sqrt(2) * sym.sin(x))**2, (x, alpha.radians, sym.pi)))
        )

        irms = c.current(vrms.V / rload.ohms)

        powerP = c.power( irms.A**2 * rload.ohms )

        pf = float(powerP.W / (vsourceRMS.V * irms.A))


        self.answer = f"""{vaverage.V:.4} V, {iaverage.A:.4} A, {vrms.V:.4} V, {irms.A:.4} A, {pf:.4}"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX}A thyristor half-wave half controlled converter has a supply voltage of {vsourceRMS.V:.4} V at {frequency.Hz:.4} Hz and a load resistance of {rload.ohms:.4} ohms. What are the average values of load voltage and current when the firing delay angle is {alpha.degrees:.4} degrees?"""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{V}}_{{ave}} &= \\frac{{1}}  {{2\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ {{V}}_{{peak}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{2\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} {{V}}_{{rms}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{2\\pi}} \\int_{{{alpha.radians:.4g}}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} \\left({vsourceRMS.V:.4g}\\text{{V}} \\right)      \\sin t \\, dt}} \\\\
&= {vaverage.V:.4g} \\text{{V}} \\\\

{{I}}_{{ave}} &= \\frac{{V_{{ave}}}} {{R_{{load}}}} \\\\
&= \\frac{{{vaverage.V:.4g}}}{{{rload.ohms:.4g}}} \\\\
&= {iaverage.A:.4g} \\text{{A}} \\\\

V_{{rms}} &= \\sqrt{{\\frac{{1}}  {{2\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{\\left( {{V}}_{{peak}}  \\sin t \\right)^2\\, dt}} }}\\\\
&= \\sqrt{{\\frac{{1}}  {{2\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\left(\\sqrt{{2}} {{V}}_{{rms}}    \\sin t\\right)^2 \\, dt}} }}\\\\
&= \\sqrt{{\\frac{{1}}  {{2\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\left(\\sqrt{{2}} \\left({vsourceRMS.V:.4g}\\right)    \\sin t \\right)^2 \\, dt}} }}\\\\
&= {vrms.V:.4g} \\text{{V}}

{{I}}_{{rms}} &= \\frac{{{{V}}_{{rms}}}}     {{{{R}}_{{load}}}} {LATEX_END}
&= \\frac{{{vrms.V:.4g} \\text{{ V}}}}     {{{rload.ohms:.4g} \\Omega}} {LATEX_END}
&= {irms.A:.4g} \\text{{ A}} {LATEX_END}

{{P}} &= {{I}}_{{rms}}^{{2}} {{R}}_{{load}} \\\\
&= \\left( {irms.A:.4g}\\text{{A}}\\right)^{{2}} \\left({rload.ohms:.4g}\\Omega\\right) \\\\
&= {powerP.W:.4g}\\text{{W}} \\\\

{{pf}} &= \\frac{{P}}    {{{{V}}_{{sourceRMS}} {{I}}_{{rms}}}} \\\\
&= \\frac{{{powerP.W:.4g}\\text{{W}}}}    {{\\left( {vsourceRMS.V:.4g}\\text{{V}}\\right) \\left( {irms.A:.4g}\\text{{A}}\\right)}} \\\\
&= {pf:.4g} \\\\
{LATEX_SOLUTION_SUFFIX}"""

class fewson_3_3:
    def __init__(self,*args,**kwargs):
        print('33')
        regen = 10
        while regen > 0:
            regen = False
            capacitance = c.capacitance(ran.main(100), 'nF')
            rlow = c.resistance(ran.main(10), 'kohms')
            rhigh = c.resistance(ran.main(120), 'kohms')
            frequency = c.frequency(ran.main(50))
            vsourcerms = c.voltage(ran.main(240))

            self.question = f"""In the circuit, C = {capacitance.nF:.4} nF and R is variable from {rlow.kohms:.4} kohms to {rhigh.kohms:.4} kohms. Determine the range of the firing delay angle available. The ECG6412 hs a breakdown voltage of 63 V.
            <img class = 'col-8'src='https://lesliecaminadecom.files.wordpress.com/2019/06/9kg2vb0qwvu54wpuz28a.png'>"""

            xc = c.resistance( 1 / (2*math.pi*frequency.Hz*capacitance.F))
            vm = c.voltage(math.sqrt(2) * vsourcerms.V )

            #for rlow
            zlow = c.resistance( math.sqrt( rlow.ohms**2 + xc.ohms**2 ) )
            philow = c.angle( math.atan(xc.ohms / rlow.ohms) , 'radians' )

            try:
                omegat_phi_90_1 = c.angle(
                math.asin(63 / (vm.V * xc.ohms / zlow.ohms )) , 'radians')



                alphalow = c.angle( omegat_phi_90_1.radians - philow.radians + math.pi/2 , 'radians')

                #for rhigh
                zhigh = c.resistance( math.sqrt( rhigh.ohms**2 + xc.ohms**2 ) )
                phihigh = c.angle( math.atan(xc.ohms / rhigh.ohms) , 'radians' )


                omegat_phi_90_2 = c.angle(
                math.asin(63 / (vm.V * xc.ohms / zhigh.ohms )) , 'radians'
                )

                alphahigh = c.angle( omegat_phi_90_2.radians - phihigh.radians + math.pi/2 , 'radians')

                self.answer = f"""{alphalow.degrees:.4} deg to {alphahigh.degrees:.4} deg."""
                self.latex_question = f"""{LATEX_ITEM_PREFIX} In the circuit, C = {capacitance.nF:.4} nF and R is variable from {rlow.kohms:.4} kohms to {rhigh.kohms:.4} kohms. Determine the range of the firing delay angle available. The ECG6412 hs a breakdown voltage of 63 V.\\\\
\\includegraphics[width=\\linewidth]{{9kg2vb0qwvu54wpuz28a.png}}"""
                self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
X_{{C}} &= \\frac{{1}}{{2 \\pi f C}} \\\\
&= \\frac{{1}} {{2 \\pi \\left({frequency.Hz:.4g}\\right) \\left({capacitance.F:.4g}\\right)}} \\\\
&= {xc.ohms:.4g} \\Omega \\\\

V_{{m}} &= \\sqrt{{2}} {{V}}_{{sourcerms}} \\\\
&= \\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right) \\\\
&= {vm.V:4g} \\text{{V}} \\\\

Z_{{low}} &= \\sqrt{{   R_{{low}}^2 + X_{{C}}^2   }} \\\\
&= \\sqrt{{  \\left({rlow.ohms:.4g}\\right)^2 + \\left({xc.ohms:.4g}\\right)^2   }} \\\\
&= {zlow.ohms:.4g} \\Omega \\\\

\\phi_{{low}} &= \\arctan{{ \\frac{{X_{{C}}}}      {{R_{{low}}}}        }} \\\\
&= \\arctan{{ \\frac{{{xc.ohms:.4g}}}      {{{rlow.ohms:.4g}}}        }} \\\\
&= {philow.radians:.4g} \\text{{rad}} \\\\

\\omega{{t}}\\phi_{{90^{{circ}}}} &= \\arcsin{{\\frac{{63}}   {{\\frac{{V_m X_C}}{{Z_{{low}}}}}}    }} \\\\
&= \\arcsin{{\\frac{{63}}   {{\\frac{{\\left({vm.V:.4g}\\right) \\left({xc.ohms:.4g}\\right)}}{{\\left({zlow.ohms:.4g}\\right)}}}}    }} \\\\
&= {omegat_phi_90_1.radians:.4g} \\text{{rad}} \\\\

\\alpha_{{low}} &= \\omega{{t}}\\phi_{{90^{{\\circ}}}} - \\phi_{{low}} + \\frac{{\\pi}}{{2}} \\\\
&= {omegat_phi_90_1.radians:.4g} - {philow.radians:.4g} + \\frac{{\\pi}}{{2}} \\\\
&= {alphalow.degrees:.4g}^{{\\circ}} \\\\


Z_{{high}} &= \\sqrt{{   R_{{high}}^2 + X_{{C}}^2   }} \\\\
&= \\sqrt{{  \\left({rhigh.ohms:.4g}\\right)^2 + \\left({xc.ohms:.4g}\\right)^2   }} \\\\
&= {zhigh.ohms:.4g} \\Omega \\\\

\\phi_{{high}} &= \\arctan{{ \\frac{{X_{{C}}}}      {{R_{{high}}}}        }} \\\\
&= \\arctan{{ \\frac{{{xc.ohms:.4g}}}      {{{rhigh.ohms:.4g}}}        }} \\\\
&= {phihigh.radians:.4g} \\text{{rad}} \\\\

\\omega{{t}}\\phi_{{90^{{\\circ}}}} &= \\arcsin{{\\frac{{63}}   {{\\frac{{V_m X_C}}{{Z_{{high}}}}}}    }} \\\\
&= \\arcsin{{\\frac{{63}}   {{\\frac{{\\left({vm.V:.4g}\\right) \\left({xc.ohms:.4g}\\right)}}{{\\left({zhigh.ohms:.4g}\\right)}}}}    }} \\\\
&= {omegat_phi_90_1.radians:.4g} \\text{{rad}} \\\\

\\alpha_{{high}} &= \\omega{{t}}\\phi_{{90^{{\\circ}}}} - \\phi_{{high}} + \\frac{{\\pi}}{{2}} \\\\
&= {omegat_phi_90_1.radians:.4g} - {phihigh.radians:.4g} + \\frac{{\\pi}}{{2}} \\\\
&= {alphahigh.degrees:.4g}^{{\\circ}} \\\\
{LATEX_SOLUTION_SUFFIX}"""
            except:
                regen = True

class fewson_3_4:
    def __init__(self,*args,**kwargs):
        print('34')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(220))
            frequency = c.frequency(ran.main(50))
            alpha = c.angle(ran.main(90), 'degrees')
            rload = c.resistance(ran.main(100))
            rload2 = c.resistance(ran.main(100))

            self.question = f"""A full - wave half controlled bridge has a supply voltage of {vsourcerms.V:.4g} V at {frequency.Hz:.4g} Hz. The firing angle delay alpha = {alpha.degrees:.4g} degrees. Determine the values of average and rms currents, load power, and power factor for a a) resistive load of R = {rload.ohms:.4g} ohms, b) a highly inductive load with a resistance of R = {rload2.ohms:.4g} ohms."""

            if alpha.radians < math.pi:
                regen = False

        #for a
        vave = c.voltage(
        (1 / math.pi ) * sym.integrate(vsourcerms.V * math.sqrt(2) * sym.sin(x), (x, alpha.radians, sym.pi))
        )

        iave = c.current(vave.V / rload.ohms )

        vrms = c.voltage(math.sqrt(
        (1 / math.pi ) * sym.integrate((vsourcerms.V * math.sqrt(2) * sym.sin(x))**2, (x, alpha.radians, sym.pi)))
        )

        irms = c.current(vrms.V / rload.ohms )

        powerP = c.power(irms.A**2 * rload.ohms )
        powerS = c.power(vsourcerms.V * irms.A )
        pf = powerP.W / powerS.W

        #for b
        iaveb = c.current(iave.A)
        irmsb = c.current( iave.A * math.sqrt((math.pi - alpha.radians)/(math.pi)))
        powerPb = c.power( iave.A**2 * rload.ohms )
        powerSb = c.power( vsourcerms.V * irmsb.A )
        pfb = powerP.W / powerS.W


        self.answer = f"""{iave.A:.4g} A, {irms.A:.4g} A, {powerP.W:.4g} W, {pf:.4g}; {iaveb.A:.4g} A, {irmsb.A:.4g} A, {powerPb.W:.4g} W, {pfb:.4g}"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX} A full - wave half controlled bridge has a supply voltage of {vsourcerms.V:.4g} V at {frequency.Hz:.4g} Hz. The firing angle delay alpha = {alpha.degrees:.4g} degrees. Determine the values of average and rms currents, load power, and power factor for a a) resistive load of R = {rload.ohms:.4g} ohms, b) a highly inductive load with a resistance of R = {rload2.ohms:.4g} ohms."""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
\\text{{for situation a}} \\\\
{{V}}_{{ave}} &= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ {{V}}_{{peak}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} {{V}}_{{rms}}      \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{{alpha.radians:.4g}}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right)      \\sin t \\, dt}} \\\\
&= {vave.V:.4g} \\text{{V}} \\\\

I_{{ave}} &= \\frac{{V_{{ave}}}}     {{R_{{load}}}} \\\\
&= \\frac{{{vave.V:.4g}}}     {{{rload.ohms:4g}}} \\\\
&= {iave.A:.4g} \\text{{A}} \\\\

V_{{rms}} &= \\sqrt{{\\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{\\left( {{V}}_{{peak}}  \\sin t \\right)^2\\, dt}} }}\\\\
&= \\sqrt{{\\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\left(\\sqrt{{2}} {{V}}_{{rms}}     \\sin t\\right)^2 \\, dt}} }}\\\\
&= \\sqrt{{\\frac{{1}}  {{\\pi}} \\int_{{{alpha.radians:.4g}}}^{{\\frac{{\\pi}}{{2}}}} {{ \\left(\\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right)    \\sin t\\right)^2 \\, dt}} }}\\\\
&= {vrms.V:.4g} \\text{{V}} \\\\

I_{{rms}} &= \\frac{{V_{{rms}}}}{{R_{{load}}}} \\\\
&= \\frac{{{vrms.V:.4g}}}{{{rload.ohms:.4g}}} \\\\
&= {irms.A:.4g} \\text{{A}} \\\\

P &= I_{{rms}}^2 R_{{load}} \\\\
&= \\left({irms.A:.4g}\\right)^2 \\left({rload.ohms:.4g}\\right) \\\\
&= {powerP.W:.4g} \\text{{W}} \\\\

S &= V_{{sourcerms}} I_{{rms}} \\\\
&= \\left({vsourcerms.V:.4g}\\right) \\left({irms.A:.4g}\\right) \\\\
&= {powerS.W:.4g} \\text{{VA}}\\\\

pf &= \\frac{{P}}{{S}} \\\\
&= \\frac{{{powerP.W:.4g}}}{{{powerS.W:.4g}}} \\\\
&= {pf:.4g} \\\\

\\text{{for situation b}} \\\\
I_{{ave}} &= {iave.A:.4g} \\text{{A}} \\\\

I_{{rms}} &= I_{{ave}} \\sqrt{{ \\frac{{\\pi - \\alpha}}{{\\pi}}      }} \\\\
&= {iave.A:.4g} \\sqrt{{ \\frac{{\\pi - {alpha.radians:.4g}}}{{\\pi}}      }} \\\\
&= {irmsb.A:.4g} \\text{{A}} \\\\

P &= I_{{ave}}^2 R_{{load}} \\\\
&= \\left({iave.A:.4g}\\right)^2 \\left({rload.ohms:.4g}\\right) \\\\
&= {powerPb.W:.4g} \\text{{W}} \\\\

S &= V_{{sourcerms}} I_{{rms}} \\\\
&= \\left({vsourcerms.V:.4g}\\right) \\left({irmsb.A:.4g}\\right) \\\\
&= {powerSb.W:.4g} \\text{{VA}}\\\\

pf &= \\frac{{P}}{{S}} \\\\
&= \\frac{{{powerPb.W:.4g}}}{{{powerSb.W:.4g}}} \\\\
&= {pfb:.4g} \\\\
{LATEX_SOLUTION_SUFFIX}"""

class fewson_3_5:
    def __init__(self,*args,**kwargs):
        print('35')
        regen = True
        while regen:
            rload = c.resistance(ran.main(55))
            vsourcerms = c.voltage(ran.main(110))
            frequency = c.frequency(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')

            self.question = f"""A full - wave fully controlled bridge has a highly inductive load with a resistance of {rload.ohms:.4g} ohms, and a supply voltage of {vsourcerms.V:.4g} V at {frequency.Hz:.4g} Hz. a) Calculate the values of load current, power, and converter power factor for a firing delay angle of {alpha.degrees:.4g} degrees."""

            if alpha.radians < math.pi:
                regen = False

        vave = c.voltage(
        (2*vsourcerms.V * math.sqrt(2) /math.pi ) * math.cos(alpha.radians)
        )

        iave = c.current(vave.V / rload.ohms)

        powerP = c.power( iave.A**2 * rload.ohms )

        pf = 0.9 * math.cos( alpha.radians )

        self.answer = f"""{iave.A:.4g} A, {powerP.W:.4g} W, {pf:.4g}"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX} A full - wave fully controlled bridge has a highly inductive load with a resistance of {rload.ohms:.4g} ohms, and a supply voltage of {vsourcerms.V:.4g} V at {frequency.Hz:.4g} Hz. a) Calculate the values of load current, power, and converter power factor for a firing delay angle of {alpha.degrees:.4g} degrees."""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
{{V}}_{{ave}} &= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\alpha + \\frac{{\\pi}}{{2}}}} {{ {{V}}_{{peak}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\alpha + \\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} {{V}}_{{rms}}      \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\alpha + \\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right)      \\sin t \\, dt}} \\\\
&= {vave.V:.4g} \\text{{V}} \\\\

I_{{ave}} &= \\frac{{V_{{ave}}}}{{R_{{load}}}} \\\\
&= \\frac{{{vave.V:.4g}}}{{{rload.ohms:.4g}}} \\\\
&= {iave.A:.4g} \\text{{A}} \\\\

P &= I_{{ave}}^2 R_{{load}} \\\\
&= \\left({iave.A:.4g}\\right)^2 \\left({rload.ohms:.4g}\\right) \\\\
&= {powerP.W:.4g} \\text{{W}} \\\\

pf &= 0.9 \\cos \\left(\\alpha\\right) \\\\
&= 0.9 \\cos \\left({alpha.radians:.4g}\\right) \\\\
&= {pf:.4g} \\\\
{LATEX_SOLUTION_SUFFIX}"""

class fewson_3_6:
    def __init__(self,*args,**kwargs):
        print('36')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(240))
            frequency = c.frequency(ran.main(50))
            rload = c.resistance(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')

            self.question = f"""A {vsourcerms.V:.4g} V,  {frequency.Hz:.4g} Hz supply feeds a highly inductive load of {rload.ohms:.4g} ohms resistance through a thyristor bridge that is a) half controlled and b) full controlled. Calculate the load current, power, and power factor for each case when the firing angle delay is {alpha.degrees:.4g} degrees."""

            if alpha.degrees < 180:
                regen = False

        #for a
        vave = c.voltage(
        ( vsourcerms.V * math.sqrt(2) / math.pi ) * ( 1 + math.cos(alpha.radians))
        )
        iave = c.current( vave.V / rload.ohms )
        irms = c.current( iave.A * math.sqrt( (math.pi - alpha.radians) / (math.pi)    ))
        powerP = c.power( irms.A**2 * rload.ohms )
        powerS = c.power( vsourcerms.V * irms.A )
        pf = powerP.W / powerS.W

        #forb
        vaveb = c.voltage(
        ( 2 * vsourcerms.V * math.sqrt(2) / math.pi ) * math.cos(alpha.radians)
        )
        iaveb = c.current( vaveb.V / rload.ohms )
        irmsb = c.current( iaveb.A )
        powerPb = c.power( irmsb.A**2 * rload.ohms )
        #powerSb = c.power( vsourcerms.V * irms.A )
        pfb = 0.9 * math.cos(alpha.radians)

        self.answer = f"""{irms.A:.4g} A, {powerP.W:.4g} W, {pf:.4g}, {irmsb.A:.4g} A, {powerPb.W:.4g} W, {pfb:.4g}"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX}A {vsourcerms.V:.4g} V,  {frequency.Hz:.4g} Hz supply feeds a highly inductive load of {rload.ohms:.4g} ohms resistance through a thyristor bridge that is a) half controlled and b) full controlled. Calculate the load current, power, and power factor for each case when the firing angle delay is {alpha.degrees:.4g} degrees."""
        self.latex_solution = f"""{LATEX_SOLUTION_PREFIX}
\\text{{for situation A}} \\\\
{{V}}_{{ave}} &= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ {{V}}_{{peak}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} {{V}}_{{rms}}      \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{{alpha.radians:.4g}}}^{{\\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right)      \\sin t \\, dt}} \\\\
&= {vave.V:.4g} \\text{{V}} \\\\

I_{{ave}} &= \\frac{{V_{{ave}}}}{{I_{{ave}}}} \\\\
&= \\frac{{{vave.V:.4g}}}{{{rload.ohms:.4g}}} \\\\
&= {iave.A:.4g} \\text{{A}} \\\\

I_{{rms}} &= I_{{ave}} \\sqrt{{\\frac{{\\pi - \\alpha}}{{\\pi}}}} \\\\
&= {iave.A:.4g} \\sqrt{{\\frac{{\\pi - {alpha.radians:.4g}}}{{\\pi}}}} \\\\
&= {irms.A:.4g} \\text{{A}} \\\\

P &= \\left(I_{{rms}}\\right)^2 R_{{load}} \\\\
&= \\left({irms.A:.4g}\\right) \\left({rload.ohms:.4g}\\right) \\\\
&= {powerP.W:.4g} \\text{{W}} \\\\

S &= V_{{sourcerms}} I_{{rms}} \\\\
&= \\left({vsourcerms.V:.4g}\\right) \\left({irms.A:.4g}\\right) \\\\
&= {powerS.W:.4g} \\text{{VA}} \\\\

pf &= \\frac{{P}}{{S}} \\\\
&= \\frac{{{powerP.W:.4g}}}{{{powerS.W:.4g}}} \\\\
&= {pf:.4g} \\\\

\\text{{for situation B}} \\\\
{{V}}_{{ave}} &= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\alpha + \\frac{{\\pi}}{{2}}}} {{ {{V}}_{{peak}}  \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{\\alpha}}^{{\\alpha + \\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} {{V}}_{{rms}}      \\sin t \\, dt}} \\\\
&= \\frac{{1}}  {{\\pi}} \\int_{{{alpha.radians:.4g}}}^{{{alpha.radians:.4g} + \\frac{{\\pi}}{{2}}}} {{ \\sqrt{{2}} \\left({vsourcerms.V:.4g}\\right)      \\sin t \\, dt}} \\\\
&= {vaveb.V:.4g} \\text{{V}} \\\\

I_{{ave}} &= \\frac{{V_{{ave}}}}{{R_{{load}}}} \\\\
&= \\frac{{{vaveb.V:.4g}}}{{{rload.ohms:.4g}}} \\\\
&= {iaveb.A:.4g} \\text{{A}} \\\\

I_{{rms}} &= I_{{ave}} \\\\
&= {iaveb.A:.4g} \\text{{A}} \\\\

P &= I_{{rms}}^2 R_{{load}} \\\\
&= \\left({irmsb.A:.4g}\\right)^2 \\left({rload.ohms:.4g}\\right) \\\\
&= {powerPb.W:.4g} \\text{{W}} \\\\

pf &= 0.9 \\cos{{\\left(\\alpha\\right)}} \\\\
&= 0.9 \\cos{{{alpha.radians:.4g}}} \\\\
&= {pfb:.4g} \\\\
{LATEX_SOLUTION_SUFFIX}"""


class fewson_3_8:
    def __init__(self,*args,**kwargs):
        print('38')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(240))
            frequency = c.frequency(ran.main(50))
            ra = c.resistance(ran.main(1000), 'mohms')
            kv = c.voltage(ran.main(800), 'mV')
            speed = c.angularVelocity(ran.main(1600), 'revpermin')
            alpha_list = [30,60]
            alpha_i = random.randint(0,len(alpha_list)-1)
            alpha = c.angle(alpha_list[alpha_i], 'degrees')

            self.question = f"""A separately excited dc motor is driven from a {vsourcerms.V:.4g} V, {frequency.Hz:.4g} Hz supply using a half controlled thyristor bridge with a flywheel diode connected across the armature. The motor has an armature resistance Ra of {ra.ohms:.4g} ohms, and an armature voltage constant kv of {kv.V:.4g} V/rad/s. The field current is constant at its rated value. Assume that the armature current is steady. Determin the values of armauture current and torque for an armature speed of {speed.revpermin:.4g} rev/min and a firing delay angle of {alpha.degrees:.4g} degrees."""

            eb = c.voltage( kv.V * speed.radpers )
            vave = c.voltage( (math.sqrt(2) * vsourcerms.V / math.pi) * (1 + math.cos(alpha.radians)) )

            if vave.V > eb.V:
                regen = False

        iave = c.current((vave.V - eb.V) / ra.ohms)

        torque = c.torque( kv.V * iave.A )

        self.answer = f"""{iave.A:.4g} A, {torque.Nm:.4g} Nm"""
        self.latex_question = f"""{LATEX_ITEM_PREFIX} A separately excited dc motor is driven from a {vsourcerms.V:.4g} V, {frequency.Hz:.4g} Hz supply using a half controlled thyristor bridge with a flywheel diode connected across the armature. The motor has an armature resistance Ra of {ra.ohms:.4g} ohms, and an armature voltage constant kv of {kv.V:.4g} V/rad/s. The field current is constant at its rated value. Assume that the armature current is steady. Determin the values of armauture current and torque for an armature speed of {speed.revpermin:.4g} rev/min and a firing delay angle of {alpha.degrees:.4g} degrees."""
        self.latex_solution = f"""{lp}
E_b &= k_v \\omega \\\\
&= {kv.V:.4g} \\cdot {speed.radpers} \\\\
&= {eb.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{ave}}}} &= \\frac{{1}}{{2 \\pi }}  \\int_{{ \\alpha}}^{{ \\pi}} \\sqrt{{2}} V_{{ \\text{{rms}}}} \\sin t dt \\\\
&= \\frac{{1}}{{2 \\pi }}  \\int_{{ {alpha.radians:.4g} }}^{{ \\pi}} \\sqrt{{2}} \\cdot {vsourcerms.V:.4g}  \\sin t dt \\\\
&= {eb.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{ave}}}} &= \\frac{{ V_{{ \\text{{ave}} }}  - E_b }} {{ R_a }} \\\\
&= \\frac{{ {vave.V:.4g} - {eb.V:.4g}}} {{ {ra.ohms:.4g}}} \\\\
&= {iave.A:.4g} \\text{{ A}} \\\\
\\\\
\\tau &= k_v I_{{ \\text{{ave}}}} \\\\
&= {kv.V:.4g} \\cdot {iave.A:.4g} \\\\
&= {torque.Nm:.4g} \\text{{ Nm}} \\\\
{ls}"""

class fewson_3_9:
    def __init__(self,*args,**kwargs):
        print('39')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')

        self.question = f"""A three - phase half controlled thyristor converter has a highly inductive load of {rload.ohms:.4} ohms, and a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees:.4} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""

        num = (3 * math.sqrt(3)) / (2 * math.pi)

        vave = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(alpha.radians))

        iave = c.current( vave.V / rload.ohms )
        irms = c.current(iave.A / math.sqrt(3))
        powerP = c.power(iave.A**2 * rload.ohms)
        pf = powerP.W / (3 * vsourcerms.V * irms.A)

        #for max alpha = 0 deg

        vavemax = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(0))

        iavemax = c.current( vavemax.V / rload.ohms )
        irmsmax = c.current(iavemax.A / math.sqrt(3))
        powerPmax = c.power(iavemax.A**2 * rload.ohms)
        pfmax = powerPmax.W / (3 * vsourcerms.V * irmsmax.A)


        self.answer = f"""{vave.V:.4} V, {iave.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W, {pf:.4}, {powerPmax.W:.4} W, {pfmax:.4}"""
        self.latex_solution = f"""{lp}
\\text{{ For question A }} \\\\
V_{{ \\text{{ave}}}} &= \\frac{{1}}{{ \\frac{{2\\pi}}{{3}} }} \\int_{{ - \\frac{{ \\pi}}{{3}} + \\alpha}}^{{ \\frac{{ \\pi}}{{3}} + \\alpha }} \\sqrt{{2}} V_{{ \\text{{rms}} }} \\cos t dt \\\\
&= \\frac{{1}}{{ \\frac{{2\\pi}}{{3}} }} \\int_{{ - \\frac{{ \\pi}}{{3}} + {alpha.radians:.4g}}}^{{ \\frac{{ \\pi}}{{3}} + {alpha.radians:.4g}}} \\sqrt{{2}} \\cdot {vsourcerms.V:.4g} \\cos t dt \\\\
&= {vave.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{ave}}}} &= \\frac{{ V_{{ \\text{{ave}}}}}} {{R_{{ \\text{{load}}}}}} \\\\
&= \\frac{{ {vave.V:.4g}}} {{ {rload.ohms:.4g}}} \\\\
&= {iave.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{rms}}}} &=  \\frac{{ I_{{ \\text{{ave}}}} }} {{ \\sqrt{{3}}}} \\\\
&= \\frac{{ {iave.A:.4g}}} {{ \\sqrt{{3}}}} \\\\
&= {irms.A:.4g} \\text{{ A}} \\\\
\\\\
P &= I_{{ \\text{{ave}}}}^2 R_{{ \\text{{load}}}} \\\\
&= {iave.A:.4g}^2 \\cdot {rload.ohms:.4g} \\\\
&= {powerP.W:.4g} \\text{{ W}} \\\\
\\\\
pf &= \\frac{{ P}} {{ 3 V_{{ \\text{{rms}}}}  I_{{ \\text{{rms}}}}    }} \\\\
&= \\frac{{ {powerP.W:.4g}}} {{3 \\cdot {vsourcerms.V:.4g} \\cdot {irms.A} }}\\\\
&= {pf:.4g}\\\\
\\\\
\\text{{ For question B, same soltion}} \\\\
\\text{{ But make }} \\alpha = 0 \\\\
{ls}"""

class fewson_3_10:
    def __init__(self,*args,**kwargs):
        print('310')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')

        self.question = f"""A three - phase full controlled thyristor converter has a highly inductive load of {rload.ohms:.4} ohms, and a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees:.4} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""

        num = (3 * math.sqrt(3)) / (math.pi)

        vave = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(alpha.radians))

        iave = c.current( vave.V / rload.ohms )
        irms = c.current(iave.A * (math.sqrt(6)/3))
        powerP = c.power(iave.A**2 * rload.ohms)
        pf = powerP.W / (3 * vsourcerms.V * irms.A)

        #for max alpha = 0 deg

        vavemax = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(0))

        iavemax = c.current( vavemax.V / rload.ohms )
        irmsmax = c.current(iavemax.A  * (math.sqrt(6)/3))
        powerPmax = c.power(iavemax.A**2 * rload.ohms)
        pfmax = powerPmax.W / (3 * vsourcerms.V * irmsmax.A)


        self.answer = f"""{vave.V:.4} V, {iave.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W, {pf:.4}, {powerPmax.W:.4} W, {pfmax:.4}"""
        self.latex_solution = f"""{lp}
\\text{{ For question A }} \\\\
V_{{ \\text{{ave}}}} &= \\frac{{1}}{{ \\frac{{ \\pi}}{{3}} }} \\int_{{ - \\frac{{ \\pi}}{{6}} + \\alpha}}^{{ \\frac{{ \\pi}}{{6}} + \\alpha }} \\sqrt{{2}} V_{{ \\text{{rms}} }} \\cos t dt \\\\
&= \\frac{{1}}{{ \\frac{{ \\pi}}{{3}} }} \\int_{{ - \\frac{{ \\pi}}{{6}} + {alpha.radians:.4g}}}^{{ \\frac{{ \\pi}}{{6}} + {alpha.radians:.4g}}} \\sqrt{{2}} \\cdot {vsourcerms.V:.4g} \\cos t dt \\\\
&= {vave.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{ave}}}} &= \\frac{{ V_{{ \\text{{ave}}}}}} {{R_{{ \\text{{load}}}}}} \\\\
&= \\frac{{ {vave.V:.4g}}} {{ {rload.ohms:.4g}}} \\\\
&= {iave.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{rms}}}} &=  \\frac{{ I_{{ \\text{{ave}}}} \\sqrt{{6}} }} {{ 3 }} \\\\
&= \\frac{{ {iave.A:.4g} \\cdot \\sqrt{{6}} }} {{ 3 }} \\\\
&= {irms.A:.4g} \\text{{ A}} \\\\
\\\\
P &= I_{{ \\text{{ave}}}}^2 R_{{ \\text{{load}}}} \\\\
&= {iave.A:.4g}^2 \\cdot {rload.ohms:.4g} \\\\
&= {powerP.W:.4g} \\text{{ W}} \\\\
\\\\
pf &= \\frac{{ P}} {{ 3 V_{{ \\text{{rms}}}}  I_{{ \\text{{rms}}}}    }} \\\\
&= \\frac{{ {powerP.W:.4g}}} {{3 \\cdot {vsourcerms.V:.4g} \\cdot {irms.A} }}\\\\
&= {pf:.4g}\\\\
\\\\
\\text{{ For question B, same soltion}} \\\\
\\text{{ But make }} \\alpha = 0 \\\\
{ls}"""
