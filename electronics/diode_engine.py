from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import math
import random
from fractions import Fraction
from generator.latex_engine import LATEX_SOLUTION_PREFIX as lp
from generator.latex_engine import LATEX_SOLUTION_SUFFIX as ls

x, y, z = sympy.symbols('x y z', real = True)#generic variables

class floyd_2_1_a:
    def __init__(self,*args,**kwargs):

        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(ran.main(1000))
        bulkresistance = c.resistance(10, 'e12')

        self.question = f"""Determine the forward voltage and forward current for the diode with a supply voltage of {supplyvoltage.V:.4g} V  and a limiting resistor of {resistance.kohms:.4g} kohms. Also find the voltage across the limiting resistor in each case. Assume r'd = {bulkresistance.ohms:.4g} ohms at the determined value of forward current."""

        #using ideal model
        currentideal = c.current( supplyvoltage.V / resistance.ohms)
        diodevoltageideal = c.voltage(float(0))
        resistorvoltageideal = c.voltage(supplyvoltage.V)

        #using practical model
        diodevoltagepractical = c.voltage(0.7)
        currentpractical = c.current( (supplyvoltage.V - diodevoltagepractical.V) / resistance.ohms   )
        resistorvoltagepractical = c.voltage( currentpractical.A * resistance.ohms)

        #using complete model

        currentcomplete = c.current(
        (supplyvoltage.V - 0.7 ) / ( resistance.ohms + bulkresistance.ohms)
        )
        diodevoltagecomplete = c.voltage( 0.7 + currentcomplete.A * bulkresistance.ohms)
        resistorvoltagecomplete = c.voltage( currentcomplete.A * resistance.ohms)

        self.answer = f"""{diodevoltageideal.V:.4g} V, {currentideal.A:.4g} A, {resistorvoltageideal.V:.4g} V; {diodevoltagepractical.V:.4g} V, {currentpractical.A:.4g} A, {resistorvoltagepractical.V:.4g} V; {diodevoltagecomplete.V:.4g} V, {currentcomplete.A:.4g} A, {resistorvoltagecomplete.V:.4g} V."""


class floyd_2_1_b:
    def __init__(self,*args,**kwargs):

        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(1000, 'e12')
        #bulkresistance = c.resistance(ran.main(10))
        reversecurrent = c.current(ran.main(1), 'uA')

        self.question = f"""Determine the reverse voltage and reverse current for the diode with a supply voltage of {supplyvoltage.V:.4g} V  and a limiting resistor of {resistance.kohms:.4g} kohms. Also find the voltage across the limiting resistor in each case. Assume IR = {reversecurrent.uA:.4g} uA."""

        #using ideal model
        currentideal = c.current(0)
        diodevoltageideal = c.voltage(supplyvoltage.V)
        resistorvoltageideal = c.voltage(0)

        #using practical model
        diodevoltagepractical = c.voltage(supplyvoltage.V)
        currentpractical = c.current(0)
        resistorvoltagepractical = c.voltage(0)

        #using complete model

        currentcomplete = c.current( reversecurrent.A )
        resistorvoltagecomplete = c.voltage( reversecurrent.A * resistance.ohms)
        diodevoltagecomplete = c.voltage(supplyvoltage.V - resistorvoltagecomplete.V)


        self.answer = f"""{diodevoltageideal.V:.4g} V, {currentideal.A:.4g} A, {resistorvoltageideal.V:.4g} V; {diodevoltagepractical.V:.4g} V, {currentpractical.A:.4g} A, {resistorvoltagepractical.V:.4g} V; {diodevoltagecomplete.V:.4g} V, {currentcomplete.A:.4g} A, {resistorvoltagecomplete.V:.4g} V."""

class floyd_2_2:
    def __init__(self,*args,**kwargs):

        peakvoltage = c.voltage(ran.main(50))

        self.question = f"""What is the average value of a half wave rectified voltage having a peak value of {peakvoltage.V:.4g} V?"""

        averagevoltage = c.voltage(  peakvoltage.V / math.pi  )

        self.answer = f"""{averagevoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{ave}}}} &= \\frac{{1}}{{ \\pi}} V_{{ \\text{{peak}}}} \\\\
&= \\frac{{1}}{{ \\pi}} \\cdot {peakvoltage.V:.4g} \\\\
&= {averagevoltage.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_3:
    def __init__(self,*args,**kwargs):
        diodes = ['1N4001', '1N4004']
        diode = diodes[random.randint(0, len(diodes) - 1)]
        resistance = c.resistance(1000, 'e12')
        voltages = [ran.main(100), ran.main(5)]
        peakinputvoltage = c.voltage(voltages[random.randint(0,1)])


        self.question = f"""A half wave rectifier circuit consists of a {diode} diode and a load resistance of {resistance.kohms:.4g} kohms. If the input is an AC voltage with a peak value of {peakinputvoltage.V:.4g} V, determine the peak output voltage of the half wave rectifier."""
        peakoutputvoltage = c.voltage(peakinputvoltage.V - 0.7)
        self.answer = f"""{peakoutputvoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{o}}}} &= V_{{ \\text{{i}}}} - 0.7 \\\\
&= {peakinputvoltage.V:.4g} - 0.7 \\\\
&= {peakoutputvoltage.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_4:
    def __init__(self,*args,**kwargs):

        primaryvoltage = c.voltage(ran.main(170, 'int'))
        turnsratio = Fraction(ran.main(5, 'int')).limit_denominator(1000)
        resistance = c.resistance(1000, 'e12')

        self.question = f"""Determine the peak value of the output voltage of a power supply system consisting of a transformer with a turns ratio of {turnsratio.numerator}:{turnsratio.denominator} and a half wave rectifier circuit consisting of a single 1N4002 diode. The load resistance is {resistance.kohms:.4g} kohms and the peak supply voltage on the primary of the transformer is {primaryvoltage.kV:.4g} kV."""
        secondaryvoltage = c.voltage(primaryvoltage.V / turnsratio)
        peakoutputvoltage = c.voltage( secondaryvoltage.V - 0.7)
        self.answer = f"""{peakoutputvoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{s}}}} &= \\frac{{ V_{{ \\text{{p}}}} }} {{ n }} \\\\
&= \\frac{{ {primaryvoltage.V:.4g}}} {{ \\frac{{ {turnsratio.numerator}}} {{ {turnsratio.denominator}}} }} \\\\
&= {secondaryvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{o}}}} &= V_{{ \\text{{s}}}} - 0.7 \\\\
&= {secondaryvoltage.V:.4g} - 0.7 \\\\
&= {peakoutputvoltage.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_5:
    def __init__(self,*args,**kwargs):

        peakinputvoltage = c.voltage(ran.main(15))

        self.question = f"""Find the average value of a full wave rectified voltage having a peak value of {peakinputvoltage.V:.4g} V."""

        averagevoltage = c.voltage((2 / math.pi) * peakinputvoltage.V)

        self.answer = f"""{averagevoltage.V:.4g} V"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{ave}}}} &= \\frac{{2}}{{ \\pi}} V_{{ \\text{{peak}}}} \\\\
&= \\frac{{2}}{{ \\pi}} \\cdot {peakinputvoltage.V:.4g} \\\\
&= {averagevoltage.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_6:
    def __init__(self,*args,**kwargs):

        turnsratio = ran.main(5, 'int')
        peakinputvoltage = c.voltage(ran.main(100))
        loadresistance = c.resistance(10e3, 'e12')

        self.question = f"""A center - tapped power supply consists of a transformer with a turns ratio of {turnsratio:.4g}:1, two 1N4001 diodes, and a load resistance of {loadresistance.kohms:.4g} kohms. An input voltage of {peakinputvoltage.V:.4g} V peak is applied at the primary of the transformer. a) Show the voltage waveforms across each half of the secondary winding and across RL b) What minimum PIV rating must the diodes have?"""

        secondaryvoltage = c.voltage( peakinputvoltage.V / turnsratio)

        halfwindingvoltage = c.voltage(secondaryvoltage.V / 2)
        peakloadvoltage = c.voltage(halfwindingvoltage.V - 0.7)

        PIV = c.voltage( 2*peakloadvoltage.V + 0.7)

        self.answer = f"""{halfwindingvoltage.V:.4g} Vpeak sine wave, {peakloadvoltage.V:.4g} Vpeak full wave rectified waveform, {PIV.V:.4g} V"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{secondary}}}} &= \\frac {{ V_{{ \\text{{primary}}}} }} {{n}}  \\\\
&= \\frac{{ {peakinputvoltage.V:.4g}}} {{ \\frac{{ {turnsratio}}} {{1}}}} \\\\
&= {secondaryvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{half winding}}}} &= \\frac{{ V_{{ \\text{{secondary}}}}}} {{2}} \\\\
&= \\frac{{ {secondaryvoltage.V:.4g}}} {{2}} \\\\
&= {halfwindingvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{peak load}}}} &= V_{{ \\text{{half winding}}}} - 0.7 \\\\
&= {halfwindingvoltage.V:.4g} - 0.7 \\\\
&= {peakloadvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
PIV &= 2 V_{{ \\text {{peak load}}}} + 0.7 \\\\
&= 2 \\cdot {peakloadvoltage.V:.4g} + 0.7 \\\\
&= {PIV.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_7:
    def __init__(self,*args,**kwargs):

        rmssecondaryvoltage = c.voltage(ran.main(12))
        loadresistance = c.resistance(1000, 'e12')


        self.question = f"""Determine the peak output voltage for a bridge rectifier attached to a transformer secondary with a rms voltage of {rmssecondaryvoltage.V:.4g} V. The load resistance is {loadresistance.kohms:.4g} kohms. Assuming the practical model, what PIV rating is required for the diodes?"""

        peaksecondaryvoltage = c.voltage( 1.414 * rmssecondaryvoltage.V)

        peakloadvoltage = c.voltage(peaksecondaryvoltage.V - 1.4)

        PIV = c.voltage(peakloadvoltage.V + 0.7)

        self.answer = f"""{peakloadvoltage.V:.4g} V, {PIV.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{peak secondary}}}} &= \\frac{{ \\sqrt{{2}}}}{{2}} V_{{ \\text{{rms secondary}}}} \\\\
&= \\frac{{ \\sqrt{{2}} }} {{2}} \\cdot {rmssecondaryvoltage.V:.4g} \\\\
&= {peaksecondaryvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{peak load}}}} &= V_{{ \\text{{peak secondary}}}} - 1.4 \\\\
&= {peaksecondaryvoltage.V:.4g} - 1.4 \\\\
&= {peakloadvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
PIV &= V_{{ \\text{{peak load}}}} + 0.7 \\\\
&= {peakloadvoltage.V:.4g} + 0.7 \\\\
&= {PIV.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_8:
    def __init__(self,*args,**kwargs):
        regen = 1
        while regen:
            primaryvoltagerms = c.voltage(ran.main(120,'int'))
            turnsratio = ran.main(10, 'int')
            capacitance = c.capacitance(ran.main(1000), 'uF')
            frequency = c.frequency(120)
            loadresistance = c.resistance(220, 'e12')


            self.question = f"""Determine the ripple factor for a filtered bridge rectifier with a primary supply voltage of {primaryvoltagerms.kV:.4g} kVrms, 60 Hz, a turns ratio of {turnsratio:.4g} : 1, uses four 1N4001 diodes, capacitance of {capacitance.uF:.4g} uF, and load resistance of {loadresistance.ohms:.4g} ohms."""

            primaryvoltagepeak = c.voltage(primaryvoltagerms.V * 1.414)
            secondaryvoltagepeak = c.voltage(primaryvoltagepeak.V / turnsratio)
            peakloadvoltage = c.voltage(secondaryvoltagepeak.V - 1.4)
            ripplevoltage = c.voltage(
            (1 / (frequency.Hz * loadresistance.ohms * capacitance.F)) * peakloadvoltage.V
            )
            dcvoltage = c.voltage(
            (1 - (1/(2*frequency.Hz*capacitance.F*loadresistance.ohms)))*peakloadvoltage.V
            )
            ripplefactor = c.percentage(ripplevoltage.V/dcvoltage.V, 'decimal')
            if ripplefactor.percent > 0:
                regen = 0

            self.answer = f"""{ripplefactor.decimal:.4g}, {ripplefactor.percent:.4g} %"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{peak primary}}}} &= \\frac{{ \\sqrt{{2}}}} {{2}} V_{{ \\text{{rms primary}}}} \\\\
&= \\frac{{ \\sqrt{{2}}}}{{2}} \\cdot {primaryvoltagerms.V:.4g} \\\\
&= {primaryvoltagepeak.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{peak secondary}}}} &= \\frac{{ V_{{ \\text{{peak primary}}}}}} {{ n }} \\\\
&= \\frac{{ {primaryvoltagepeak.V:4g}}} {{ \\frac{{ {turnsratio}}} {{ 1}}}} \\\\
&= {secondaryvoltagepeak.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{peak load}}}} &= V_{{ \\text{{peak secondary}}}} - 1.4 \\\\
&= {secondaryvoltagepeak.V:.4g} - 1.4 \\\\
&= {peakloadvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{ripple}}}} &= \\frac{{ V_{{ \\text{{peak load}}}}    }} {{ f R C}}\\\\
&= \\frac{{ {peakloadvoltage.V:.4g}}} {{ {frequency.Hz:.4g} \\cdot {loadresistance.ohms:.4g} \\cdot {capacitance.F:.4g}}} \\\\
&= {ripplevoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{dc}}}} &= \\left(1 - \\frac{{1}}{{2 f C R}}\\right) V_{{ \\text{{peak load}}}} \\\\
&= \\left(1 - \\frac{{1}}{{2 \\cdot {frequency.Hz:.4g} \\cdot {capacitance.F:.4g} \\cdot {loadresistance.ohms:.4g}}}\\right) \\cdot {peakloadvoltage.V:.4g} \\\\
&= {dcvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
\\gamma &= \\frac{{ V_{{ \\text{{ripple}}}}}} {{ V_{{ \\text{{dc}}}}}} \\\\
&= \\frac{{ {ripplevoltage.V:.4g}}} {{ {dcvoltage.V:.4g}}} \\\\
&= {ripplefactor.percent} \\% \\\\
{ls}"""

class floyd_2_9:
    def __init__(self,*args,**kwargs):

        noloadvoltage = c.voltage(ran.main(5.18))
        fullloadvoltage = c.voltage(noloadvoltage.V - ran.main(0.03))

        self.question = f"""A certain 7805 regulator has a measured no-load output voltage of {noloadvoltage.V:.4g} V and a full load output of {fullloadvoltage.V:.4g} V. What is the load regulation expressed as a percentage?"""

        loadregulation = c.percentage(
        (noloadvoltage.V - fullloadvoltage.V) / (fullloadvoltage.V) , 'decimal'
        )

        self.answer = f"""{loadregulation.percent:.4g} %"""
        self.latex_solution = f"""{lp}
LR &= \\frac{{ V_{{ \\text{{NL}}}}   - V_{{ \\text{{FL}}}}   }} {{ V_{{ \\text{{FL}}}}}} \\\\
&= \\frac{{ {noloadvoltage.V:.4g} - {fullloadvoltage.V:.4g}}} {{ {fullloadvoltage.V:.4g}}} \\\\
&= {loadregulation.percent:.4g} \\% \\\\
{ls}"""

class floyd_2_10:
    def __init__(self,*args,**kwargs):

        supplyvoltage = c.voltage(int(ran.main(10)))
        Rlimiting = c.resistance(10e3, 'e12')
        Rload = c.resistance(100e3, 'e12')


        self.question = f"""A parallel negative clipper has a limiting resistor of {Rlimiting.kohms:.4g} kohms and a 1N914 diode (silicon). It is attached to a load resistance of {Rload.kohms:.4g} kohms and a source voltage of {supplyvoltage.V:.4g} Vpeak. Determine the peak voltages of the output voltage across the load."""

        minvoltage = c.voltage(-0.7)
        maxvoltage = c.voltage( supplyvoltage.V *  ((Rload.ohms)/(Rload.ohms + Rlimiting.ohms)) )

        self.answer = f"""{minvoltage.V:.4g} V, {maxvoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{min}}}} &= - 0.7 \\text{{ V}} \\\\
\\\\
V_{{ \\text{{max}}}} &= V_{{ \\text{{supply}}}} \\frac{{ R_{{ \\text{{load}}}} }} {{ R_{{ \\text{{load}}}} + R_{{ \\text{{limiting}}}}   }} \\\\
&= {supplyvoltage.V:.4g} \\cdot \\frac{{ {Rload.ohms:.4g}}} {{ {Rload.ohms:.4g} + {Rlimiting.ohms:4g}}} \\\\
&= {maxvoltage.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_11:
    def __init__(self,*args,**kwargs):

        Vsource = c.voltage(int(ran.main(10)))
        R1 = c.resistance(1000, 'e12')
        VD1 = c.voltage(int(ran.main(5)))
        VD2 = c.voltage(int(ran.main(5)))


        self.question = f"""Determine the peak voltages of the following circuit. The source voltage is {Vsource.V:.4g} Vpeak, the voltage source with D1 is {VD1.V:.4g} V, the voltage source with D2 is {VD2.V:.4g} V, and R1 is {R1.kohms:.4g} kohms."""

        maxvoltage = c.voltage( VD1.V + 0.7)
        minvoltage = c.voltage( -VD2.V - 0.7 )

        self.image = "1jh1zj3sg858ms6f7r3l.png"
        self.answer = f"""{minvoltage.V:.4g} V, {maxvoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{max}}}} &= V_{{ \\text{{D1}}}} + 0.7 \\\\
&= {VD1.V:.4g} + 0.7 \\\\
&= {maxvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{min}}}} &= - V_{{ \\text{{D2}}}} - 0.7 \\\\
&= - {VD2.V:.4g} - 0.7 \\\\
&= {minvoltage.V:4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_12:
    def __init__(self,*args,**kwargs):

        R2 = c.resistance(100, 'e12')
        R3 = c.resistance(220, 'e12')
        Vsource = c.voltage(18)
        Vbiassource = c.voltage(12)
        self.image = 'no15x1d0qzdtbd1ydymr.png'
        self.question = f"""Determine the peak voltages of the output of the following circuit if R2 = {R2.ohms:.4g} ohms and R3 = {R3.ohms:.4g} ohms."""

        Vbias = c.voltage(
        ( (R3.ohms) / (R3.ohms + R2.ohms)) * Vbiassource.V
        )

        maxvoltage = c.voltage(Vbias.V + 0.7)
        minvoltage = c.voltage(-Vsource.V)

        self.answer = f"""{float(minvoltage.V):.4g} V, {maxvoltage.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{bias}}}} &= \\frac{{ R_3 }} {{ R_3 + R_2 }}   V_{{ \\text{{bias source}}}} \\\\
&= \\frac{{ {R3.ohms:.4g}}} {{ {R3.ohms:.4g} + {R2.ohms:.4g}}}  \\cdot {Vbiassource.V:.4g} \\\\
&= {Vbias.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{max}}}} &= V_{{ \\text{{bias}}}} + 0.7 \\\\
&= {Vbias.V:.4g} + 0.7 \\\\
&= {maxvoltage.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{min}}}} &= - V_{{ \\text{{source}}}} \\\\
&= - {Vsource.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_2_13:
    def __init__(self,*args,**kwargs):

        Vsource = c.voltage(int(ran.main(24)))
        C1 = c.capacitance(int(ran.main(10)), 'uF')
        Rload = c.resistance(10e3, 'e12')

        self.question = f"""A negative clamper has C = {C1.uF:.4g} uF and a 1N914(silicon) diode. It is attached to a load resistance of {Rload.kohms:.4g} kohms. If the peak source voltage is {Vsource.V:.4g} Vpeak, determine the peak voltages, and Dc output voltages."""

        Vdc = c.voltage( - (Vsource.V - 0.7))
        Vmax = c.voltage(0.7)
        Vmin = c.voltage(Vdc.V - Vsource.V)

        self.answer = f"""{Vdc.V:.4g} V, {Vmax.V:.4g} V, {Vmin.V:.4g} V"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{dc}}}} &= - \\left( V_{{ \\text{{source}}}} - 0.7\\right) \\\\
&= - \\left( {Vsource.V:.4g} - 0.7\\right) \\\\
&= {Vdc.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{max}}}} &= 0.7 \\\\
\\\\
V_{{ \\text{{min}}}} &= V_{{ \\text{{dc}}}} - V_{{ \\text{{source}}}} \\\\
&= {Vdc.V:.4g} - {Vsource.V:.4g} \\\\
&= {Vmin.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_3_5:
    def __init__(self,*args,**kwargs):

        Vz = c.voltage(int(ran.main(51))/10)
        Iz = c.current(int(ran.main(49)), 'mA')
        Izk = c.current(1, 'mA')
        Zz = c.resistance(int(ran.main(7)))
        R1 = c.resistance(100, 'e12')
        Pzmax = c.power(1)
        self.image = 'd17z552uz3ava3j77llr.png'
        self.question = f"""Determine the minimum and the maximum input voltages that can be regulated by the zener diode. R = {R1.ohms:.4g} ohms, Zener diode: Vz = {Vz.V:.4g} V, Iz = {Iz.mA:.4g} mA, Izk = {Izk.mA:.4g} mA, Zz = {Zz.ohms:.4g} ohms at Iz. Pzmax = {Pzmax.W:.4g} W."""

        deltaVz = c.voltage( (Iz.A - Izk.A) * Zz.ohms)
        Voutmin = c.voltage(Vz.V - deltaVz.V)
        Vinmin = c.voltage( Izk.A * R1.ohms + Voutmin.V )

        Izmax = c.current(Pzmax.W / Vz.V)
        deltaVzmax = c.voltage((Izmax.A - Iz.A)*Zz.ohms)
        Voutmax = c.voltage(Vz.V + deltaVzmax.V)
        Vinmax = c.voltage(Voutmax.V + Izmax.A * R1.ohms)

        self.answer = f"""{Vinmin.V:.4g} V, {Vinmax.V:.4g} V"""

        self.latex_solution = f"""{lp}
\\Delta V_{{ \\text{{z}}}} &= \\left(I_{{ \\text{{z}}}}    - I_{{ \\text{{zk}}}}\\right) Z_{{ \\text{{z}}}} \\\\
&= \\left( {Iz.A:.4g} - {Izk.A:.4g}\\right) \\cdot {Zz.ohms:.4g} \\\\
&= {deltaVz.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{out min}}}} &= V_{{ \\text{{z}}}} - \\Delta V_{{ \\text{{z}}}} \\\\
&= {Vz.V:.4g} - {deltaVz.V:.4g} \\\\
&= {Voutmin.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{in min}}}} &= I_{{ \\text{{zk}}}} R_1 + V_{{ \\text{{out min}}}} \\\\
&= {Izk.A:.4g} \\cdot {R1.ohms:.4g} + {Voutmin.V:.4g} \\\\
&= {Vinmin.V:4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{z max}}}} &= \\frac{{ P_{{ \\text{{z max}}}}}} {{ V_{{ \\text{{z}}}}}} \\\\
&= \\frac{{ {Pzmax.W:.4g}}} {{ {Vz.V:.4g}}} \\\\
&= {Izmax.A:.4g} \\text{{ A}} \\\\
\\\\
\\Delta V_{{ \\text{{z max}}}} &= \\left( I_{{ \\text{{z max}}}} - I_{{ \\text{{z}}}}\\right) Z_{{ \\text{{z}}}} \\\\
&= \\left({Izmax.A:.4g} - {Iz.A:.4g}\\right) \\cdot {Zz.ohms:.4g} \\\\
&= {deltaVzmax.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{out max}}}} &= V_{{ \\text{{z}}}} + \\Delta V_{{ \\text{{z max}}}} \\\\
&= {Vz.V:.4g} + {deltaVzmax.V:.4g} \\\\
&= {Voutmax.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{in max}}}} &= V_{{ \\text{{out max}}}} + I_{{ \\text{{z max}}}} R_1 \\\\
&= {Voutmax.V:.4g} + {Izmax.A:.4g} \\cdot {R1.ohms:.4g} \\\\
&= {Vinmax.V:.4g} \\text{{ V}} \\\\
{ls}"""

class floyd_3_6:
    def __init__(self,*args,**kwargs):
        repeat = True
        while repeat:
            Vz = c.voltage(int(ran.main(12)))
            Vin = c.voltage(Vz.V + int(ran.main(12)))
            Rs = c.resistance(470, 'e12')
            Izk = c.current(random.randint(1,3), 'mA')
            Izm = c.current(int(ran.main(50)), 'mA')
            Izk_int = int(Izk.mA)
            Izm_int = int(Izm.mA)

            self.image = '2qq8d3u9659jmxxe5nps.png'
            self.question = f"""For an input voltage of {Vin.V:.4g} V, determine the minimum and the maximum load currents for which the zener diode will maintain regulation. What is the minimum value of RL that can be used? R = {Rs.ohms:.4g} ohms, Vz = {Vz.V:.4g} V, Izk = {Izk.mA:.4g} mA, and Izm = {Izm.mA:.4g} mA. Assume an ideal zener diode where Zz = 0 ohms and Vz remains a constant {Vz.V:.4g} V over the range of current values, for simplicity."""

            Itotal = c.current(
            (Vin.V - Vz.V) / Rs.ohms
            )
            Itotal_frac = Fraction(int(Vin.V - Vz.V), int(Rs.ohms) )

            if Itotal.A <= Izm.A:
                repeat = True
            else:
                Iloadmin_int = Izk_int - Izm_int
                Rloadmax = c.resistance(Vz.V / Iloadmin_int )
                repeat = False

            Iloadmax = Itotal_frac - Izk_int

            Rloadmin = c.resistance(Vz.V / Iloadmax)




        self.answer = f"""{Iloadmin.mA:.4g} mA, {Iloadmax.mA:.4g} mA, {Rloadmin.ohms:.4g} ohms, {Rloadmax.ohms:.4g} ohms"""
        self.latex_solution = f"""{lp}
I_{{ \\text{{total}}}} &= \\frac{{ V_{{ \\text{{in}}}}  - V_{{ \\text{{z}}}}  }} {{ R_{{ \\text{{s}}}}}} \\\\
&= \\frac{{ {Vin.V:.4g} - {Vz.V:.4g} }} {{ {Rs.ohms:.4g}}} \\\\
&= {Itotal.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{load min}}}} &= I_{{ \\text{{total}}}} - I_{{ \\text{{zm}}}} \\\\
&= {Itotal.A:.4g} - {Izm.A:.4g} \\\\
&= {Iloadmin.A:.4g} \\text{{ A}} \\\\
\\\\
R_{{ \\text{{load max}}}} &= \\frac{{ V_{{ \\text{{z}}}}}} {{ I_{{ \\text{{load min}}}}}} \\\\
&= \\frac{{ {Vz.V:.4g}}} {{ {Iloadmin.A:.4g}}} \\\\
&= {Rloadmax.ohms:.4g} \\Omega \\\\
\\\\
I_{{ \\text{{load max}}}} &= I_{{ \\text{{total}}}} - I_{{ \\text{{zk}}}} \\\\
&= {Itotal.A:.4g} - {Izk.A:.4g} \\\\
&= {Iloadmax.A:.4g} \\text{{ A}} \\\\
\\\\
R_{{ \\text{{load min}}}} &= \\frac{{ V_{{ \\text{{z}}}}}} {{ I_{{ \\text{{load max}}}}}} \\\\
&= \\frac{{ {Vz.V:.4g}}} {{ {Iloadmax.A:4g}}} \\\\
&= {Rloadmin.ohms:.4g} \\Omega \\\\
{ls}"""

class floyd_3_7:
    def __init__(self,*args,**kwargs):

        Vin = c.voltage(int(ran.main(24)))
        Vz = c.voltage(int(ran.main(15)))
        Iz = c.current(int(ran.main(17)), 'mA')
        Izk = c.current(int(ran.main(25))/100, 'mA')
        Zz = c.resistance(int(ran.main(14)))
        Pzmax = c.power(1)

        self.image = 'af6qgi3si4t4i7zhf6oc.png'
        self.question = f"""For an input voltage of {Vin.V:.4g} V, a) Determine Vout at Izk and a Izm. b) Calculate the value of R that should be used. c) Determine the minimum value of RL that can be used. Specifications for the diode are: Vz = {Vz.V:.4g} V @ Iz = {Iz.mA:.4g} mA, Izk = {Izk.mA:.4g} mA, and Zz = {Zz.ohms:.4g} ohms, Pzmax = {Pzmax.W:.4g} W."""

        VoutIzk = c.voltage(Vz.V - (Iz.A - Izk.A)*Zz.ohms)
        Izm = c.current(Pzmax.W / Vz.V)
        VoutIzm = c.voltage(Vz.V + (Izm.A - Iz.A)*Zz.ohms)

        R = c.resistance(
        (Vin.V - VoutIzm.V) / Izm.A
        )

        Itotal = c.current((Vin.V - VoutIzk.V) / R.ohms)
        Iload = c.current(Itotal.A - Izk.A)
        Rloadmin = c.resistance(VoutIzk.V / Iload.A)


        self.answer = f"""{VoutIzk.V:.4g} V, {VoutIzm.V:.4g} V, {R.ohms:.4g} ohms, {Rloadmin.ohms:.4g} ohms"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{out Izk}}}} &= V_{{ \\text{{z}}}} - \\left(I_{{ \\text{{z}}}} - I_{{ \\text{{zk}}}}\\right) Z_{{ \\text{{z}}}} \\\\
&= {Vz.V:.4g} - \\left({Iz.A:.4g} - {Izk.A:.4g}\\right) \\cdot {Zz.ohms:.4g} \\\\
&= {VoutIzk.V:.4g} \\text{{ V}} \\\\
\\\\
I_{{ \\text{{zm}}}} &= \\frac{{ P_{{ \\text{{z max}}}}}} {{ V_{{ \\text{{z}}}}}}\\\\
&= \\frac{{ {Pzmax.W:.4g}}} {{ {Vz.V:.4g}}} \\\\
&= {Izm.A:.4g} \\text{{ A}} \\\\
\\\\
V_{{ \\text{{out Izm}}}} &= V_{{ \\text{{z}}}} + \\left(I_{{ \\text{{zm}}}} - I_{{ \\text{{z}}}}\\right) Z_{{ \\text{{z}}}} \\\\
&= {Vz.V:.4g} + \\left({Izm.A:.4g} - {Iz.A:.4g}\\right) \\cdot {Zz.ohms:.4g} \\\\
&= {VoutIzm.V:.4g} \\text{{ V}} \\\\
\\\\
R &= \\frac{{ V_{{ \\text{{in}}}} - V_{{ \\text{{out Izm}}}}       }} {{ I_{{ \\text{{zm}}}}}} \\\\
&= \\frac{{ {Vin.V:.4g} - {VoutIzm.V:.4g}}} {{ {Izm.A:.4g}}}  \\\\
&= {R.ohms:.4g} \\Omega \\\\
\\\\
I_{{ \\text{{total}}}} &= \\frac{{ V_{{ \\text{{in}}}} - V_{{ \\text{{out Izk}}}}}} {{ R}} \\\\
&= \\frac{{ {Vin.V:.4g} - {VoutIzk.V}}} {{ {R.ohms:.4g}}} \\\\
&= {Itotal.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{load}}}} &= I_{{ \\text{{total}}}} - I_{{ \\text{{zk}}}} \\\\
&= {Itotal.A:.4g} - {Izk.A:.4g} \\\\
&= {Iload.A:.4g} \\text{{ A}} \\\\
\\\\
R_{{ \\text{{load min}}}} &= \\frac{{ V_{{ \\text{{out Izk}}}}}} {{ I_{{ \\text{{load}}}}}} \\\\
&= \\frac{{ {VoutIzk.V:.4g}}} {{ {Iload.A:.4g}}} \\\\
&= {Rloadmin.ohms:.4g} \\Omega \\\\
{ls}"""


class floyd_3_8_a:
    def __init__(self,*args,**kwargs):

        R1 = c.resistance(random.randint(1,5)*1000)
        Vz1 = c.voltage(int(ran.main(33))/10)
        Vz2 = c.voltage(int(ran.main(51))/10)
        self.image = '6d29y6yjxl43lz61pue2.png'
        self.question = f"""With a peak input voltage of 50V, determine the minimum and maximum voltage of the output waveform for the zener limiting circuit. R = {R1.kohms:.4g} kohms, top zener voltage = {Vz1.V:.4g} V, bottom zener voltage = {Vz2.V:.4g} V. """

        vmaximum = c.voltage(Vz2.V + 0.7)
        vminimum = c.voltage(-(Vz1.V + 0.7))

        self.answer = f"""{vmaximum.V:.4g} V, {vminimum.V:.4g} V"""

        self.latex_solution = f"""{lp}
V_{{ \\text{{max}}}} &= V_{{ \\text{{z2}}}} + 0.7 \\\\
&= {Vz2.V:.4g} + 0.7 \\\\
&= {vmaximum.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{min}}}} &= - V_{{ \\text{{z1}}}} - 0.7 \\\\
&= - {Vz1.V:.4g} - 0.7 \\\\
&= {vminimum.V:.4g} \\text{{ V}}\\\\
{ls}"""
#-----------------------------------------------------------

class boylestad_2_4():
    def __init__(self):
        E = c.voltage(ran.main(8))
        VD = c.voltage(0.7)
        R = c.resistance(ran.main(2.2), 'kohms')

        I = c.current(
            (E.V - VD.V) / R.ohms
            )
        self.image = 'screenshot-from-2020-01-14-13-47-10-1.png'
        self.question = f"""For the series diode configuration on the figure, determine ID. E = {E.V:.4g} V, R = {R.kohms:.4g} kohms"""
        self.answer = f"""{I.mA:.4g} mA"""
        self.latex_solution = f"""{lp}
I &= \\frac{{ E - V_{{ \\text{{D}}}}}} {{R}} \\\\
&= \\frac{{ {E.V:.4g} - {VD.V:.4g}}} {{ {R.ohms:.4g}}} \\\\
&= {I.A:.4g} \\text{{ A}} \\\\
{ls}"""

class boylestad_2_6():
    def __init__(self):
        E = c.voltage(ran.main(0.5))
        R = c.resistance(ran.main(1.2), 'kohms')
        VD = c.voltage(0.7)
        if E.V < 0.7:
            I = c.current(0)
            self.latex_solution = f"""{lp}
\\text{{ supply less than  0.7 V}} \\\\
I &= 0 A \\\\
{ls}"""
        else:
            I = c.current(
                (E.V - VD.V) / R.ohms
                )
            self.latex_solution = f"""{lp}
I &= \\frac{{ E - V_{{ \\text{{D}}}}}} {{R}} \\\\
&= \\frac{{ {E.V:.4g} - {VD.V:.4g}}} {{ {R.ohms:.4g}}} \\\\
&= {I.A:.4g} \\text{{ A}} \\\\
{ls}"""

        self.question = f"""For the series diode configuration , determine ID. E = {E.V:.4g} V, R = {R.kohms:.4g} kohms"""
        self.answer = f"""{I.mA:.4g} mA"""
        self.image = 'screenshot-from-2020-01-14-13-56-29.png'


class boylestad_2_9():
    def __init__(self):
        E1 = c.voltage(ran.main(10))
        E2 = c.voltage( - ran.main(5))
        VD = c.voltage(0.7)
        R1 = c.resistance(4.7e3, 'e12')
        R2 = c.resistance(2.2e3, 'e12')
        equation = sympy.Eq(
            - E1.V + x*(R1.ohms + R2.ohms) - VD.V - E2.V, 0
            )
        I = c.current(sympy.solveset(equation, x).args[0])
        V1 = c.voltage(I.A * R1.ohms)
        V2 = c.voltage(I.A * R2.ohms)
        VO = V2
        self.image = 'screenshot-from-2020-01-14-14-16-32.png'
        self.question = f"""Determine I, V1, V2 and VO for the series dc configuration of the figure, E1 = {E1.V:.4g} V, E2 = {E2.V:.4g} V, R1 = {R1.kohms:.4g} kohms, R2 = {R2.kohms:.4g} kohms"""
        self.answer= f"""{I.mA:.4g} mA, {V1.V:.4g} V, {V2.V:.4g} V, {VO.V:.4g} V"""
        self.latex_solution = f"""{lp}
- E_1 &+ I \\left( R_1 + R_2\\right) - V_{{ \\text{{D}}}} - E_2 = 0 \\\\
- {E1.V:.4g} &+ I \\left({R1.ohms:.4g}  + {R2.ohms:.4g} \\right) - {VD.V:.4g} - {E2.V:.4g} = 0 \\\\
I &= {I.A:.4g} \\text{{ A}}\\\\
\\\\
V_1 &= I R_1 \\\\
&= {I.A:.4g} \\cdot {R1.ohms:.4g} \\\\
&= {V1.V:.4g} \\text{{ V}} \\\\
\\\\
V_2 &= I R_2 \\\\
&= {I.A:.4g} \\cdot {R2.ohms:.4g} \\\\
&= {V2.V:.4g} \\text{{ V}} \\\\
\\\\
V_O &= V_2 \\\\
V_O &= {VO.V:.4g} \\text{{ V}} \\\\
{ls}"""

class boylestad_2_10():
    def __init__(self):
        E = c.voltage(ran.main(10))
        R = c.resistance(330, 'e12')
        VD = c.voltage(0.7)

        I1 = c.current(
            (E.V - VD.V) / R.ohms
            )

        ID1 = c.current(I1.A / 2)
        ID2 = ID1
        VO = VD
        self.image = 'screenshot-from-2020-01-14-14-25-46.png'
        self.question = f"""Determine VO, I1, ID1, ID2 for the parallel diode configuration of the figure, E = {E.V:.4g} V, R = {R.ohms:.4g} ohms"""
        self.answer = f"""{VO.V:.4g} V, {I1.mA:.4g} mA, {ID1.mA:.4g} mA, {ID2.mA:.4g} mA"""
        self.latex_solution = f"""{lp}
I_1 &= \\frac{{ E - V_{{ \\text{{D}}}}}} {{R}} \\\\
&= \\frac{{ {E.V:.4g} - {VD.V:.4g}}} {{ {R.ohms:.4g}}} \\\\
&= {I1.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{D1}}}} &= I_1 \\\\
&= {ID1.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{D2}}}} &= I_{{ \\text{{D2}}}} \\\\
&= {ID2.A:.4g} \\text{{A}} \\\\
\\\\
V_{{ \\text{{O}}}} &= V_{{ \\text{{D}}}} \\\\
&= {VO.V:.4g} \\text{{ V}}\\\\
{ls}"""


class boylestad_2_11():
    def __init__(self):
        VTO = c.voltage(2)
        VBR = c.voltage(3)
        E = c.voltage(ran.main(8))
        ION = c.current(ran.main(20), 'mA')

        R = c.resistance(
            (E.V - VTO.V) / ION.A
            )
        self.image = 'screenshot-from-2020-01-14-14-36-57.png'
        self.question = f"""There are two LEDS that can be used as a polarity detector. Apply a positive source and the green light results. Negative supplies result in a red light. Find the resistor R to ensure that a current of {ION.mA:.4g} mA through the "on" diode for the configuration in the figure. Both diodes have a reverse breakdown voltage of {VBR.V:.4g} V and an average turn-on voltage of {VTO.V:.4g} V. E = {E.V:.4g} V"""
        self.answer = f"""{R.ohms:.4g} ohms"""
        self.latex_solution = f"""{lp}
R &= \\frac{{ E - V_{{ \\text{{TO}}}}}} {{ I_{{ \\text{{ON}}}}}} \\\\
&= \\frac{{ {E.V:.4g} - {VTO.V:.4g}}} {{ {ION.A:.4g}}} \\\\
&= {R.ohms:.4g} \\Omega \\\\
{ls}"""

class boylestad_2_12():
    def __init__(self):
        E = c.voltage(ran.main(12))
        R = c.resistance(2.2e3, 'e12')

        I = c.current(
            (E.V - 0.7) / R.ohms
            )

        VO = c.voltage( I.A * R.ohms )
        self.image = 'screenshot-from-2020-01-14-14-42-22.png'
        self.question = f"""Determine the voltage V0 for the network of the figure. E = {E.V:.4g} V"""
        self.answer = f"""{VO.V:.4g} V"""
        self.latex_solution = f"""{lp}
I &= \\frac{{ E - 0.7 }} {{ R}} \\\\
&= \\frac{{ {E.V:.4g} - 0.7}} {{ {R.ohms:.4g}}} \\\\
&= {I.A:.4g} \\text{{A}} \\\\
\\\\
V_{{ \\text{{O}}}} &= I R \\\\
&= {I.A:.4g} \\cdot {R.ohms:.4g} \\\\
&= {VO.V:.4g} \\text{{V}} \\\\
{ls}"""

class boylestad_2_13():
    def __init__(self):
        repeat = True
        while repeat:

            E = c.voltage(ran.main(20))
            R1 = c.resistance(3.3e3, 'e12')
            R2 = c.resistance(5.6e3, 'e12')

            I1 = c.current( 0.7 / R1.ohms)

            equation = sympy.Eq(
                - E.V + 0.7 + 0.7 + x * R2.ohms, 0
                )

            I2 = c.current(sympy.solveset(equation, x).args[0])
            ID2  = c.current(I2.A - I1.A)

            if I2.A > I1.A:
                repeat = False
        self.image = 'screenshot-from-2020-01-14-14-49-25.png'
        self.question = f"""Determine the currents I1, I2, and ID2 for the network of the figure. E = {E.V:.4g} V, R1 = {R1.kohms:.4g} kohms, R2 = {R2.kohms:.4g} kohms"""
        self.answer = f"""{I1.mA:.4g} mA, {I2.mA:.4g} mA, {ID2.mA:.4g} mA"""
        self.latex_solution = f"""{lp}
I_1 &= \\frac{{ 0.7 }} {{ R_1 }} \\\\
&= \\frac{{ 0.7}} {{ {R1.ohms:.4g}}} \\\\
&= {I1.A:.4g} \\text{{A}} \\\\
\\\\
0 &= - E + 0.7 + 0.7 + I R_2 \\\\
0 &= - {E.V:.4g} + 0.7 + 0.7 + I \\cdot {R2.ohms:.4g} \\\\
I_2 &= {I2.A:.4g} \\text{{ A}} \\\\
\\\\
I_{{ \\text{{D2}}}} &= I_2 - I_1  \\\\
&= {I2.A:.4g} - {I1.A:.4g} \\\\
&= {ID2.A:.4g} \\text{{A}} \\\\
{ls}"""

class boylestad_2_14():
    def __init__(self):
        E = c.voltage(ran.main(10))
        R = c.resistance(1000, 'e12')

        I = c.current(
            (E.V - 0.7) / R.ohms
            )

        VO = c.voltage( I.A * R.ohms )
        self.image = 'screenshot-from-2020-01-14-17-25-05.png'
        self.question = f"""Determine VO for the network of the figure. E = {E.V:.4g} V and R = {R.kohms:.4g} kohms"""
        self.answer = f"""{VO.V:.4g} V"""
        self.latex_solution = f"""{lp}
I &= \\frac{{ E - 0.7 }} {{R}} \\\\
&= \\frac{{ {E.V:.4g} - 0.7 }} {{ {R.ohms:.4g}}} \\\\
&= {I.A:.4g} \\text{{A}} \\\\
\\\\
V_{{ \\text{{O}}}} &= I R \\\\
&= {I.A:.4g} \\cdot {R.ohms:.4g} \\\\
&= {VO.V:.4g} \\text{{V}} \\\\
{ls}"""

class boylestad_2_15():
    def __init__(self):
        E = c.voltage(ran.main(10))
        zero = c.voltage(0)
        E1 = random.choice([E, zero])
        E2 = random.choice([E, zero])
        R = c.resistance(1000, 'e12')

        if E1.V > 0 and E2.V > 0 :
            VO = E
            self.latex_solution = f"""{lp}
V_{{ \\text{{O}}}} &= E \\\\
&= {VO.V:.4g} \\text{{V}} \\\\
{ls}"""
        else:
            VO = c.voltage(0.7)
            self.latex_solution = f"""{lp}
V_{{ \\text{{O}}}} &= 0 \\\\
{ls}"""
        self.image = 'screenshot-from-2020-01-15-07-55-52-1.png'
        self.question = f"""Determine the output level for the circuit at the figure. E = {float(E.V):.4g}, E1 = {float(E1.V):.4g} V, E2 = {float(E2.V):.4g} V, R = {R.kohms:.4g} kohms."""
        self.answer = f"""{VO.V:.4g} V"""

class boylestad_2_16():
    def __init__(self):
        VI_peak = c.voltage(ran.main(20))
        R = c.resistance(2000, 'e12')
        VI_peak_2 = c.voltage(VI_peak.V * 10)

        VDC1 = c.voltage( - VI_peak.V * 0.318)
        VDC2 = c.voltage( - (VI_peak.V - 0.7 ) * 0.318)
        VDC3 = c.voltage( - (VI_peak_2.V - 0.7) * 0.318)

        self.image = 'screenshot-from-2020-01-15-08-13-58.png'
        self.question = f"""Determine the output voltage of the circuit and the input voltage shown if a) Vi(peak) = {VI_peak.V:.4g} V, and an ideal diode. b) Vi(peak) = {VI_peak.V:.4g} V, and a silicon diode. c) Vi(peak) = {VI_peak_2.V:.4g} V,  and a silicon diode. In all cases, R = {R.kohms:.4g}"""

        self.answer = f"""{VDC1.V:.4g} V, {VDC2.V:.4g} V, {VDC3.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{DC1}}}} &= - V_{{ \\text{{i peak}}}} \\frac{{1}}{{ \\pi}} \\\\
&= - {VI_peak.V:.4g} \\cdot \\frac{{1}}{{ \\pi}}\\\\
&= {VDC1.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DC2}}}} &= - \\left( V_{{ \\text{{i peak}}}} - 0.7 \\right) \\frac{{1}}{{ \\pi}} \\\\
&= - \\left({VI_peak.V:.4g} - 0.7 \\right) \\frac{{ 1}}{{ \\pi}} \\\\
&= {VDC2.V:.4g} \\text{{ V}} \\\\
\\\\
V_{{ \\text{{DC3}}}} &= - \\left( V_{{ \\text{{i peak 2}}}} - 0.7 \\right) \\frac{{1}}{{ \\pi}} \\\\
&= - \\left({VI_peak_2.V:.4g} - 0.7 \\right) \\frac{{ 1}}{{ \\pi}} \\\\
&= {VDC3.V:.4g} \\text{{ V}} \\\\
{ls}"""

class boylestad_2_17():
    def __init__(self):
        VI_peak = c.voltage(ran.main(10))
        R = c.resistance(ran.main(2000), 'e12')

        VO = c.voltage( (VI_peak.V / 2) * 0.636 )
        PIV = c.voltage(VI_peak.V / 2)

        self.image = 'screenshot-from-2020-01-15-08-24-01.png'
        self.question = f"""Determine the output waveform for the network on the figure and calculate the output DC level and the required PIV of each diode. Vi(peak) = {VI_peak.V:.4g} V and all resistors are {R.kohms:.4g} kohms"""
        self.answer = f"""{PIV.V:.4g} V"""
        self.latex_solution = f"""{lp}
V_{{ \\text{{O}}}} &= \\frac{{ V_{{ \\text{{i peak}}}}}} {{2}} \\cdot \\frac{{ 2}} {{ \\pi}} \\\\
&= \\frac{{ {VI_peak.V:.4g}}} {{2}} \\cdot \\frac{{ 2}} {{ \\pi}} \\\\
&= {VO.V:.4g} \\text{{V}} \\\\
\\\\
PIV &= \\frac{{ V_{{ \\text{{i peak}}}}}} {{2}} \\\\
&= {PIV.V:.4g} \\text{{V}} \\\\
{ls}"""
