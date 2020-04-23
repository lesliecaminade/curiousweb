from generator import constants_conversions as c
from generator import random_handler as ran
import math
import random
import sympy
from num2words import num2words

x, y, z, t = sympy.symbols('x y z t', real = True)


class jma_17_1():
    def __init__(self):
       rad = c.resistance(ran.main(67))
       loss = c.resistance(ran.main(5))
       eff = c.percentage(rad.ohms / (rad.ohms + loss.ohms), 'decimal')

       self.question = f"""Calculate the efficiency of a dipole antenna that has a resistance of {rad.ohms:5.4} ohms and a loss resistance of {loss.ohms:5.4} ohms, measured at the feedpoint"""
       self.answer = f"""{eff.percent:5.4} %"""

class jma_17_2():
    def __init__(self):
        gain_dbi = c.dbvalue(ran.main(5.3), 'dB')
        eff = c.percentage(random.randint(90, 99), 'percent')

        gain_dbd = c.dbvalue(gain_dbi.dB - 2.15, 'dB')
        power_gain = c.dbvalue(eff.decimal * gain_dbd.unitless)

        self.question = f"""Calculate the gain of a certain antenna relative to a dipole antenna with a gain of {gain_dbi.dB:5.4} dB with respect to an isotropic radiator. Also compute for the power gain if the antenna has an efficiency of {eff.percent:5.4} %"""

        self.answer = f"""{gain_dbd.dB:5.4} dB, {power_gain.dB:5.4} dB"""

class jma_17_3():
    def __init__(self):
        distance = c.length(ran.main(10), 'km')
        antenna_type = {'Hertzian dipole':1.5, 'half-wave dipole':1.64}
        antenna = random.choice(list(antenna_type.keys()))
        gain = antenna_type[antenna]
        power = c.power(ran.main(10))
        freq = c.frequency(ran.main(10), 'MHz')
        wavelength = c.length(3e8 / freq.Hz)

        self.question = f"""Calculate the captured power {distance.km:5.4} km away from a half-wave dipole transmitter with {power.W:5.4} W transmit power for a(n) {antenna} at {freq.MHz:5.4} MHz."""

        power_received = c.power(
            ((power.W * 1.64)/(4 * math.pi * distance.m**2)) * ((wavelength.m**2 * gain)/(4 * math.pi))
            ) 

        self.answer = f"""{power_received.nW:5.4} nW"""

class jma_17_4():
    def __init__(self):
        freq = c.frequency(ran.main(300), 'MHz')
        wavelength = c.length(3e8 / freq.Hz)

        distance_considered = c.length(random.uniform(0, wavelength.m/2))

        radiation_resistance = c.resistance(
            75 / (math.sin(math.pi * distance_considered.m / wavelength.m))
            )

        self.question = f"""Calculate the radiation resistance of a half-wave dipole antenna if the feedpoint is {distance_considered.m:5.4} m from one end at {freq.MHz:5.4} MHz"""
        self.answer = f"""{radiation_resistance.ohms:5.4} ohms"""

class jma_17_5():
    def __init__(self):
        velocity_factor = ran.main(0.63)
        freq = c.frequency(ran.main(28), 'MHz')

        self.question = f"""What is the actual length of one-half wavelength of a coax with velocity factor of {velocity_factor:5.4} at {freq.MHz:5.4} MHz?"""
        length = c.length(492 * velocity_factor / freq.MHz, 'feet')
        
        self.answer = f"""{length.ft:5.4} ft"""

class jma_17_6():
    def __init__(self):
        freq = c.frequency(ran.main(174), 'MHz')
        wavelength = c.length(3e8 / freq.Hz)

        director = c.length( wavelength.m * 0.475)
        driven = c.length(wavelength.m * 0.451)
        reflector = c.length(wavelength.m * 0.49875)

        pick = {'director':director, 'driven':driven, 'reflector':reflector}
        element = random.choice(list(pick.keys()))
        self.question = f"""A Yagi-Uda antenna is designed to receive signals centered at {freq.MHz:5.4} MHz. Calculate the length of the {element} element."""
        self.answer = f"""{pick[element].m:5.4} m"""

class jma_17_7():
    def __init__(self):
        diameter = c.length(ran.main(80), 'mm')
        pitch = c.length(ran.main(62.5), 'mm')
        turns  = int(ran.main(8))
        freq = c.frequency(ran.main(1.2), 'GHz')
        wavelength = c.length(3e8 / freq.Hz)
        gain = c.dbvalue(15 * turns * pitch.m * (math.pi * diameter.m)**2 / wavelength.m**3, 'unitless')

        beamwidth = c.angle(52 * wavelength.m * math.sqrt(wavelength.m / (turns * pitch.m)) / (math.pi * diameter.m), 'degrees')

        answers = {'gain':str(round(gain.dB, 2)) + ' dB', 'beamwidth':str(round(beamwidth.degrees, 2)) + ' degrees'}
        ask = random.choice(list(answers.keys()))
        self.question = f"""Calculate the {ask} of a helical antenna if the optimum diameter is {diameter.mm:5.4} mm, pitch of {pitch.mm:5.4} mm, with {num2words(turns)} and will operate at {freq.GHz:5.4} GHz."""
        self.answer = f"""{answers[ask]}"""

class jma_17_8():
    def __init__(self):
        diameter = c.length(ran.main(2.4), 'm')
        eff = c.percentage(ran.main(55), 'percent')
        freq = c.frequency(ran.main(6), 'GHz')
        wavelength = c.length(3e8 / freq.Hz)
        gain = c.dbvalue(
            eff.decimal * (math.pi * diameter.m / wavelength.m)**2
            )

        beamwidth_nulls = c.angle(140 * wavelength.m / diameter.m, 'degrees')

        answers = {'gain':str(round(gain.dB, 2)) + ' dB', 'beamwidth between nulls':str(round(beamwidth_nulls.degrees, 2)) + ' degrees'}
        pick = random.choice(list(answers.keys()))
        self.question = f"""Calculate the {pick} for a parabolic reflector antenna with a mouth diameter of {diameter.m:5.4} m an an illumination efficiency of {eff.decimal:5.4} opearating at {freq.GHz:5.4} GHz"""
        self.answer = f"""{answers[pick]}"""

class jma_17_9():
    def __init__(self):
        freq = c.frequency(ran.main(500), 'MHz')
        diameter = c.length(ran.main(42), 'm')
        wavelength = c.length(3e8 / freq.Hz)
        beamwidth = c.angle(
            70 * wavelength.m/ diameter.m, 'degrees'
            )

        self.question = f"""To minimize interference, a {freq.MHz:5.4} MHz dish needs to have a {beamwidth.degrees:5.4} degrees beamwidth. What diameter dish is required, in meters?"""
        self.answer = f"""{diameter.m:5.4} m """

class jma_17_10():
    def __init__(self):
        e_aperture = c.length(ran.main(60), 'mm')
        h_aperture = c.length(ran.main(80), 'mm')
        freq = c.frequency(ran.main(6), 'GHz')
        wavelength = c.length(3e8 / freq.Hz)
        

        gain = c.dbvalue( 7.5 * e_aperture.m * h_aperture.m / wavelength.m, 'unitless')

        e_beamwidth = c.angle(
            56 / 
            (e_aperture.m) , 'degrees'
            )

        h_beamwidth = c.angle(
            70 / 
            (h_aperture.m), 'degrees'
            )

        answers = {'gain':str(round(gain.dB, 2)) + ' dB', 'beamwidth in the e-plane':str(round(e_beamwidth.degrees, 2)) + ' degrees', 'beamwidth in the h-plane':str(round(e_beamwidth.degrees, 2)) + ' degrees'}

        pick = random.choice(list(answers.keys()))

        self.question = f"""Calculate the {pick} of a pyramidal horn antenna that has an aperture of {e_aperture.mm:5.4} mm in the e-plane and {h_aperture.mm:5.4} mm in the h-plane and operating at {freq.GHz:5.4} GHz."""

        self.answer = f"""{answers[pick]}"""

class tomasi_15_1:
    def __init__(self, *args, **kwargs):
        gain = c.dbvalue(ran.main(10), 'unitless')
        power = c.power(ran.main(100), 'W')
        distance = c.length(ran.main(10), 'km')
        
        self.question = f"""For a transmit antenna with a power gain A = {gain.unitless} and input power Pin = {power.W} W, determine EIRP, power density {distance.km} km from the antenna and the power density had an isotropic antenna been used with the same input power and efficiency."""
        
        eirp = c.power(power.W * gain.unitless)
        power_density = c.powerDensity((power.W * gain.unitless) / (4 * math.pi * distance.m**2))
        
        power_density_iso = c.powerDensity(power.W / (4 * math.pi * distance.m**2))
        
        self.answer = f"""EIRP: {eirp.W} W, {eirp.dBm} dBm, {eirp.dBW} dBW
Power density: {power_density.uWperm2} uW/m2
Power density if isotropic: {power_density_iso.uWperm2} uW/m2"""

class tomasi_15_2:
    def __init__(self, *args, **kwargs):
        radiation_resistance = c.resistance(ran.main(72))
        effective_resistance = c.resistance(ran.main(8))
        directive_gain = c.dbvalue(ran.main(20))
        power = c.power(ran.main(100))
        
        self.question = f"""For a transmit antenna with a radiation resistance Rr = {radiation_resistance.ohms} ohms, an effective antenna resistance Re = {effective_resistance.ohms} ohms, a directive gain D = {directive_gain.unitless}, and an input power of Pin = {power.W} W, determine the antenna efficiency, antenna gain (absolute and in dB) , radiated power (in watts, dBm, and dBW), and EIRP (in watts, dBm, and dBW)."""
        
        efficiency = c.percentage(
        radiation_resistance.ohms / (radiation_resistance.ohms + effective_resistance.ohms), 'decimal'
        )
        
        antenna_gain = c.dbvalue(
        efficiency.decimal * directive_gain.unitless
        )
        
        radiated_power = c.power(
        power.W * efficiency.decimal
        )
        
        eirp = c.power(
        power.W * antenna_gain.unitless
        )
        
        
        self.answer = f"""Efficiency: {efficiency.percent} %
Antenna Gain: {antenna_gain.unitless}, {antenna_gain.dB} dB
Radiated Power: {radiated_power.W} W, {radiated_power.dBW} dBW, {radiated_power.dBm} dBm
EIRP: {eirp.W} W, {eirp.dBW} dBW, {eirp.dBm} dBm"""


class tomasi_15_3:
    def __init__(self, *args, **kwargs):
        power_output = c.power(ran.main(40), 'dBm')
        transmission_line_loss = c.dbvalue(ran.main(3), 'dB')
        free_space_path_loss = c.dbvalue(ran.main(50), 'dB')
        directive_gain = c.dbvalue(ran.main(10))
        efficiency = c.percentage(ran.main(50), 'percent')
        
        self.question = f"""Given the free-space radio transmission system with the following transmission characteristics:
Transmitter power output: {power_output.dBm} dBm
Transmission line loss: {transmission_line_loss.dB} dB
Free-space path loss: {free_space_path_loss.dB} dB
Determine the antenna input power, radiated power, EIRP, and received power density for an antenna with directivity D = {directive_gain.unitless} and an efficiency of {efficiency.percent} %."""

        antenna_input_power = c.power(
        power_output.dBm - transmission_line_loss.dB, 'dBm'
        )
        
        radiated_power = c.power(
        antenna_input_power.dBm + 10 * math.log(efficiency.decimal, 10), 'dBm'
        )
        
        eirp = c.power(
        radiated_power.dBm + directive_gain.dB, 'dBm'
        )
        
        receive_power_density = c.power(
        eirp.dBm - free_space_path_loss.dB, 'dBm'
        )
        
        self.answer = f"""Antenna input power: {antenna_input_power.dBm} dBm
Radiated power: {radiated_power.dBm} dBm
EIRP: {eirp.dBm} dBm
Received power density: {receive_power_density.dBm} dBm"""

class tomasi_15_4:
    def __init__(self, *args, **kwargs):
        receive_power_density = c.powerDensity(ran.main(10), 'uWperm2')
        capture_area = c.area(ran.main(0.2), 'm2')
    
        self.question = f"""For a receive power density of {receive_power_density.uWperm2} uW/m2 and a receive antenna with a capture area of {capture_area.m2} m2, determine the captured power in watts and dBm."""
        
        captured_power = c.power(
        receive_power_density.Wperm2 * capture_area.m2
        )
        
        self.answer = f"""Captured power: {captured_power.W} W, {captured_power.dBm} dBm"""
        
class tomasi_15_5:
    def __init__(self, *args, **kwargs):
        frequency = c.frequency(ran.main(400), 'MHz')
        offset = c.frequency(ran.main(20), 'MHz')
        upper = c.frequency(frequency.Hz + offset.Hz)
        lower = c.frequency(frequency.Hz - offset.Hz)
        
        self.question = f"""Determine the percent bandwidth for an antenna with an optimum frequency of operation of {frequency.MHz} MHz and - 3dB frequencies of {lower.MHz} MHz and {upper.MHz} MHz."""
        
        percent_bandwidth = c.percentage(
        (upper.Hz - lower.Hz) / (frequency.Hz), 'decimal'
        )
        
        self.answer = f"""Percent Bandwidth = {percent_bandwidth.percent} %"""
        
class tomasi_15_6:
    def __init__(self, *args, **kwargs):
        diameter = c.length(ran.main(2))
        power = c.power(10)
        frequency = c.frequency(ran.main(6), 'GHz')
        antenna_efficiency = c.percentage(ran.main(55), 'percent')
        aperture_efficiency = c.percentage(antenna_efficiency.percent, 'percent')
        
        self.question = f"""For a {diameter.m}-m diameter parabolic reflector with {power.W} W of power radiated by the feed mechanism operating at {frequency.GHz} GHz with a transmit antenna efficiency of {antenna_efficiency.percent} % and an aperture efficiency of {aperture_efficiency.percent} %, determine the beamwidth, the transmit power gain, receive power gain, and the EIRP."""
        
        beamwidth = c.angle(
        (70 * 3e8) / (frequency.Hz * diameter.m) , 'degrees'
        )
        
        antenna_gain = c.dbvalue(
        antenna_efficiency.decimal * ((math.pi * diameter.m)/(3e8/frequency.Hz))**2, 'unitless'
        )
        
        eirp = c.power( 
        antenna_gain.dB + power.dBm, 'dBm'
        )
        
        self.answer = f"""Beamwidth: {beamwidth.degrees} degrees
Transmit/Receive power gain: {antenna_gain.dB} dB
EIRP: {eirp.dBm} dBm"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
