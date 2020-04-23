import random


class chapter_7_1():
	def __init__(self):
		
		choice_a = 'ASCII'
		choice_b = 'Baudot code'
		choice_c = 'Morse code #'
		choice_d = 'none of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The first digital code was the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_2():
	def __init__(self):
		
		choice_a = 'an amplifier'
		choice_b = 'a filter'
		choice_c = 'a regenerative amplifier #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In a digital transmission, signal degradation can be removed using"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_3():
	def __init__(self):
		
		choice_a = 'Time - Division multiplexing #'
		choice_b = 'Time - Domain multiplexing'
		choice_c = 'Ten - Digital Manchester'
		choice_d = 'Ten Dual - Manchester'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""TDM stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_4():
	def __init__(self):
		
		choice_a = 'I = ktB #'
		choice_b = 'C = 2B log_2 M'
		choice_c = 'C = B log_2 (1 + S/N )'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Hartley's Law is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_5():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M) #'
		choice_c = 'C = Blog_2(1 + S/N)'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Shannon-Hartley theorem is :"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_6():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M)'
		choice_c = 'C = Blog_2(1 + S/N) #'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Shannon Limit is given by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_7():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M)'
		choice_c = 'C = Blog_2(1 + S/N)'
		choice_d = 'SR = 2 fmax #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Nyquist rate can be expressed as:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_8():
	def __init__(self):
		
		choice_a = 'a sample-and-hold circuit #'
		choice_b = 'true binary numbers'
		choice_c = 'a fixed sample rate'
		choice_d = 'an analog-to-digital converter'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Natural sampling does not use"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_9():
	def __init__(self):
		
		choice_a = 'They are two types of sampling error'
		choice_b = 'You can ahve one or the other,  but not both'
		choice_c = 'Aliasing is a technique to prevent foldover distortion'
		choice_d = 'They are the same thing #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""What is true about aliasing and foldover distortion?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_10():
	def __init__(self):
		
		choice_a = 'noise'
		choice_b = 'too many samples per second'
		choice_c = 'too few samples per second #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Folover distortion is caused by """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_11():
	def __init__(self):
		
		choice_a = 'a sample alias'
		choice_b = 'PAM #'
		choice_c = 'PCM'
		choice_d = 'PDM'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The immediate result of sampling is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_12():
	def __init__(self):
		
		choice_a = 'PDM'
		choice_b = 'PWM'
		choice_c = 'PPM'
		choice_d = 'PPS #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Which of these is not a pulse-modulation technique"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_13():
	def __init__(self):
		
		choice_a = 'decreases as the sample rate increases'
		choice_b = 'decreases as the sample rate decreases'
		choice_c = 'decreases as the bits per sample increases #'
		choice_d = 'decreases as the bits per sample decreases'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Quantizing noise (quantization noise)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_14():
	def __init__(self):
		
		choice_a = 'the strong transmittable signal to the weakest discernable signal #'
		choice_b = 'the maximum rate of conversion to the minimum rate of conversion'
		choice_c = 'the maximum bits per sample to the minimum bits per sample'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The dynamic range of a system is the ratio of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_15():
	def __init__(self):
		
		choice_a = 'compress the range of base-band frequencies'
		choice_b = 'reduce dynamic range at higher bit-rates'
		choice_c = 'preserve dynamic range while keeping bit-rate low #'
		choice_d = 'maximize the useable bandwidth in digital transmission'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Companding is used to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_16():
	def __init__(self):
		
		choice_a = 'the Logarithmic Law'
		choice_b = 'the A Law'
		choice_c = 'the alpha law '
		choice_d = 'the mu law #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In North America, companding uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_17():
	def __init__(self):
		
		choice_a = 'the Logarithmic Law'
		choice_b = 'the A Law #'
		choice_c = 'the alpha law'
		choice_d = 'the mu law'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In Europe, companding uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_18():
	def __init__(self):
		
		choice_a = 'Coder - Decoder #'
		choice_b = 'Coded - Carrier'
		choice_c = 'Code - Compression'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Codec stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_19():
	def __init__(self):
		
		choice_a = '4 - bit numbers'
		choice_b = '8 - bit numbers #'
		choice_c = '12 - bit numbers'
		choice_d = '16 - bit numbers'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A typical codec in a telephone system sends and receives"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_20():
	def __init__(self):
		
		choice_a = 'transmits fewer bits per sample'
		choice_b = 'requires a much higher sampling rate'
		choice_c = 'can suffer slope overload'
		choice_d = 'all of the above #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to PCM, delta modulation"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_21():
	def __init__(self):
		
		choice_a = 'the signal changes too rapidly'
		choice_b = 'the signal does not change #'
		choice_c = 'the bit rate is too high'
		choice_d = 'the sample is too large'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In delta modulation, "granular noise" is produced when"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_22():
	def __init__(self):
		
		choice_a = 'with a lower bit rate but reduced quality'
		choice_b = 'with a lower bit rate but the same quality #'
		choice_c = 'only over shorter distances'
		choice_d = 'only if the voice is band-limited'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to PCM, adaptive delta modulation can transmit voice:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_23():
	def __init__(self):
		
		choice_a = 'AMI'
		choice_b = 'Manchester'
		choice_c = 'unipolar NRZ #'
		choice_d = 'bipolar RZ'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Which coding scheme requires DC continuity"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_24():
	def __init__(self):
		
		choice_a = 'is a biphase code'
		choice_b = 'has a level transition in the middle of every bit period'
		choice_c = 'provides string timing information'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Manchester coding"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_25():
	def __init__(self):
		
		choice_a = '1 #'
		choice_b = '2'
		choice_c = '4'
		choice_d = '8'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of framing bits in DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_26():
	def __init__(self):
		
		choice_a = 'detect errors'
		choice_b = 'carry signaling'
		choice_c = 'synchronize the transmitter and receiver #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Framing bits in DS - 1 are used to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_27():
	def __init__(self):
		
		choice_a = 'detect errors'
		choice_b = 'carry signaling #'
		choice_c = 'synchronize the transmitter and receiver'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""So-called "stolen" bits in DS - 1 are used to """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_28():
	def __init__(self):
		
		choice_a = '1'
		choice_b = '2'
		choice_c = '4'
		choice_d = '8 #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of bits per sample in DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_29():
	def __init__(self):
		
		choice_a = '8k #'
		choice_b = '56k '
		choice_c = '64k'
		choice_d = '1.544 x 10^6'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of samples per second is DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_30():
	def __init__(self):
		
		choice_a = '8k #'
		choice_b = '56k'
		choice_c = '64k'
		choice_d = '1.544 x 10^6'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The bitrate for each channel in DS - 1"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_31():
	def __init__(self):
		
		choice_a = '1.544 Mbps #'
		choice_b = '64 kbps '
		choice_c = '56 kbps'
		choice_d = '8 kbps'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In DS -1, bites are transmitter over a T - 1 cable at"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_32():
	def __init__(self):
		
		choice_a = 'Manchester coding'
		choice_b = 'bipolar RZ AMI coding #'
		choice_c = 'NRZ coding'
		choice_d = 'pulse-width coding'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A T-1 cable uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_33():
	def __init__(self):
		
		choice_a = '6'
		choice_b = '12 #'
		choice_c = '24'
		choice_d = '48'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of frames in a superframe is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_34():
	def __init__(self):
		
		choice_a = 'twisted - pair wire #'
		choice_b = 'coaxial cable'
		choice_c = 'fiber-optic cable'
		choice_d = 'microwave'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A typical T - 1 line uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_35():
	def __init__(self):
		
		choice_a = 'on-hook / off-hook condition'
		choice_b = 'busy signal'
		choice_c = 'ringing'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Signaling is used to indicate"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_36():
	def __init__(self):
		
		choice_a = 'constructing a model of the transmission medium'
		choice_b = 'constructing a model of the human vocal system #'
		choice_c = 'find redundancies in the digitized data'
		choice_d = 'using lossless techniques'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A vocoder implements compression by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_37():
	def __init__(self):
		
		choice_a = 'much better'
		choice_b = 'somewhat better'
		choice_c = 'about the same'
		choice_d = 'not as good #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to standard PCM systems, the quality of the output of a vocoder is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""





#wave propagation

class chapter_15_1():
	def __init__(self):
		
		choice_a = 'Armstrong'
		choice_b = 'Hertz'
		choice_c = 'Maxwell #'
		choice_d = 'Marconi'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Radio waves were first predicted mathematically by:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_2():
	def __init__(self):
		
		choice_a = 'Armstrong'
		choice_b = 'Hertz #'
		choice_c = 'Maxwell'
		choice_d = 'Marconi'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Radio waves were first demonstrated experimentally by:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_3():
	def __init__(self):
		
		choice_a = 'the microprocessor chip #'
		choice_b = 'the miniature cell site'
		choice_c = 'high power microwave transmitters'
		choice_d = 'all of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""The technology that made cell phones practical was"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_4():
	def __init__(self):
		
		choice_a = 'high power levels'
		choice_b = 'high antennas'
		choice_c = 'reuse of frequencies #'
		choice_d = 'all of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Cellphones reduce much of the problems of mobile communications with"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_5():
	def __init__(self):
		
		choice_a = 'radio waves'
		choice_b = 'light'
		choice_c = 'gamma waves'
		choice_d = 'all of the above #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Which of the following are electromagnetic:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_6():
	def __init__(self):
		
		choice_a = 'perpendicular to each other'
		choice_b = 'perpendicular to the direction of travel'
		choice_c = 'both (a) and (b)'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""The electric and magnetic fields of a radio wave are:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_7():
	def __init__(self):
		
		choice_a = 'Transverse Electromagnetic #'
		choice_b = 'Transmitted Electromagnetic'
		choice_c = 'True Electromagnetic'
		choice_d = 'None of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""TEM stands for:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_8():
	def __init__(self):
		
		choice_a = '3 x 10^6 meters per second'
		choice_b = '300 x 10^6 meters per second #'
		choice_c = '3 x 10^6 miles per second'
		choice_d = '300 x 10^6 miles per second'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In free space, radio waves travel at a speed of:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_9():
	def __init__(self):
		
		choice_a = 'vertical '
		choice_b = 'horizontal '
		choice_c = 'circular'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Which is a possible polarization for an electromagnetic wave:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_10():
	def __init__(self):
		
		choice_a = 'vertical '
		choice_b = 'horizontal'
		choice_c = 'circular'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Which polarization can be reasonably well received by a circularly polarized antenna?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_11():
	def __init__(self):
		
		choice_a = '1'
		choice_b = '2 #'
		choice_c = '3'
		choice_d = 'many'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of circular polarization modes (directions) is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_12():
	def __init__(self):
		
		choice_a = 'an isotropic radiator #'
		choice_b = 'a vertically polarized radiator'
		choice_c = 'a groundwave antenna'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""An antenna has 'gain' as compared to:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_13():
	def __init__(self):
		
		choice_a = 'the E and I fields of the radiated power'
		choice_b = 'the effective isotropic radiated power #'
		choice_c = 'the effective internal reflected power'
		choice_d = 'the electric-field intensity of the radiated power'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""EIRP stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_14():
	def __init__(self):
		
		choice_a = 'losses in the characteristic impedance of free space'
		choice_b = 'losses due to absorption in the upper atmosphere'
		choice_c = 'the decrease in energy per square meter due to expansion of the wavefront #'
		choice_d = 'the decrease in energy per square meter due to the absorption of the wavefront'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The "attenuation of free space" is due to:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_15():
	def __init__(self):
		
		choice_a = 'beow about 2 MHz #'
		choice_b = 'above about 20 MHz'
		choice_c = 'at microwave frequencies'
		choice_d = 'when using horizontally polarized waves'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Ground wave are the most effective"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_16():
	def __init__(self):
		
		choice_a = 'a flat insulating surface of the right size'
		choice_b = 'a flat dielectric surface of the right size'
		choice_c = 'a flat metallic surface of the right size #'
		choice_d = 'a flat body of water'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Radio waves would most strongly reflect off:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_17():
	def __init__(self):
		
		choice_a = 'reflection'
		choice_b = 'diffusion'
		choice_c = 'refraction'
		choice_d = 'diffraction #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Radio waves sometimes bend around a corner because of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_18():
	def __init__(self):
		
		choice_a = 'line-of-sight #'
		choice_b = 'reflected off the ionosphere'
		choice_c = 'same as sky waves '
		choice_d = 'radio waves used for satellite communications'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Space waves are"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_19():
	def __init__(self):
		
		choice_a = 'are line-of-sight'
		choice_b = '"bounce" off the ionosphere #'
		choice_c = 'are same as space'
		choice_d = 'are radio waves used for satellite communications'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Sky waves"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_20():
	def __init__(self):
		
		choice_a = 'close to the transmitter'
		choice_b = 'for from the transmitter'
		choice_c = 'in the "silent" zone'
		choice_d = 'in the "skip" zone #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Sky waves cannot be "heard" """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_21():
	def __init__(self):
		
		choice_a = 'fading #'
		choice_b = 'diffraction'
		choice_c = 'frequency diversion'
		choice_d = 'spatial diversity'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A 20-dB reduction in the strength of a radio wave due to reflection is called:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_22():
	def __init__(self):
		
		choice_a = 'fading'
		choice_b = 'diffraction	'
		choice_c = 'multipath distortion #	'
		choice_d = 'cancellation due to reflection	'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f""""Ghosts" on a TV screen are an example of:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_23():
	def __init__(self):
		
		choice_a = 'send a message multiple times over a channel'
		choice_b = 'send a message over multiple channels at the same time'
		choice_c = 'extend the range of a radio communications system #'
		choice_d = 'cancel the effects of fading '
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A repeater is used to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_24():
	def __init__(self):
		
		choice_a = 'high power '
		choice_b = 'repeaters'
		choice_c = 'the radio horizon'
		choice_d = 'the reuse of frequencies #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Cellular phone systems rely on:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_25():
	def __init__(self):
		
		choice_a = 'the cell area is increased'
		choice_b = 'the cell area is split #'
		choice_c = 'the power levels are increased'
		choice_d = 'the number of channels is reduced'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""If the number of cellphone users within a cell increases above some limit:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_26():
	def __init__(self):
		
		choice_a = 'a handoff process occurs #'
		choice_b = 'a sectoring process occurs'
		choice_c = 'both cells will handle the call'
		choice_d = 'nothing occurs'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""As a cellphone user passes from one cell to another"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_27():
	def __init__(self):
		
		choice_a = 'a funnel receiver'
		choice_b = 'a rake receiver #'
		choice_c = 'multiple receiver'
		choice_d = 'none of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""To receive several data streams at once, a CDMA spread-spectrum system uses:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_28():
	def __init__(self):
		
		choice_a = 'highest layer of the atmosphere'
		choice_b = 'middle layer of the atmosphere'
		choice_c = 'lowest layer of the atmosphere #'
		choice_d = 'the most ionized layer of the atmosphere'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The troposphere is the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_15_29():
	def __init__(self):
		
		choice_a = 'used for radio telephony'
		choice_b = 'used to send data by radio #'
		choice_c = 'also called "ducting"'
		choice_d = 'not possible'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Meteor-trail propagation is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


#antenna

class chapter_16_1():
	def __init__(self):
		
		choice_a = 'the radiated signal #'
		choice_b = 'the reflected signal'
		choice_c = 'the SWR'
		choice_d = 'all of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""The real part of an antenna's input impedance is due to:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_2():
	def __init__(self):
		
		choice_a = 'a Marconi antenna'
		choice_b = 'a Hertz antenna #'
		choice_c = 'a Yagi antenna'
		choice_d = 'none of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""A half-wave dipole is sometimes called:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_3():
	def __init__(self):
		
		choice_a = 'one wavelength '
		choice_b = 'on half-wavelength'
		choice_c = 'slightly longer than half-wavelength'
		choice_d = 'slightly shorter than a half-wavelength #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The end-to-end length of a half-wave dipole antenna is actually:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_4():
	def __init__(self):
		
		choice_a = 'standing wave pattern around the antenna'
		choice_b = 'SWR along the feed cable'
		choice_c = 'radiation resistance of the antenna #'
		choice_d = 'I^2 R loss of the antenna '
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The radiation of energy from an antenna can be seen in the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_5():
	def __init__(self):
		
		choice_a = 'in one direction'
		choice_b = 'in two directions #'
		choice_c = 'in all directions'
		choice_d = 'depends on the number of elements'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Measured on the ground, the field strength of a horizontally polarized half-wave dipole antenna is strongest"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_6():
	def __init__(self):
		
		choice_a = 'directivity #'
		choice_b = 'selectivity'
		choice_c = 'active antenna'
		choice_d = 'resonance'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The ability of an antenna to radiate more energy in one direction than in other directions is called:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_7():
	def __init__(self):
		
		choice_a = '0 dB #'
		choice_b = '3 dB'
		choice_c = '10 dB'
		choice_d = 'infinite'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The front-to-back ratio of a half-wave dipole antenna is:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_8():
	def __init__(self):
		
		choice_a = 'from + 90 deg to - 90 deg'
		choice_b = 'from front to back'
		choice_c = 'between half power points #'
		choice_d = 'between the minor side-lobes'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""An antenna's beamwidth is measured:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_9():
	def __init__(self):
		
		choice_a = 'equivalent radiation pattern '
		choice_b = 'effective radiation pattern'
		choice_c = 'equivalent radiation power'
		choice_d = 'effective radiated power #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""ERP stands for:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_10():
	def __init__(self):
		
		choice_a = 'radio signals reflecting off the ground #'
		choice_b = 'builldings and other structures on the ground'
		choice_c = 'fading '
		choice_d = 'faulty connection of the feed cable ground'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f""""Ground Effects" refers to the effects on an antenna's radiation pattern caused by:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_11():
	def __init__(self):
		
		choice_a = 'mounted vertically #'
		choice_b = 'mounted horizontally'
		choice_c = 'at least one half-wavelength long'
		choice_d = 'at least one wavelength long'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A 1-MHz monopole antenna must be:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_12():
	def __init__(self):
		
		choice_a = 'dipole '
		choice_b = 'folded dipole'
		choice_c = 'ferrite "loopstick" #'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The typical antenna in an AM radio is a:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_13():
	def __init__(self):
		
		choice_a = 'gamma rays'
		choice_b = 'Faraday rotation #'
		choice_c = 'helical rotation'
		choice_d = 'the distance travelled'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The polarization of plane waves received from a satellite is changed by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_14():
	def __init__(self):
		
		choice_a = 'will not transmit'
		choice_b = 'will not receive '
		choice_c = 'will cause SWR on the feed cable #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""A nonresonant antenna:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_15():
	def __init__(self):
		
		choice_a = 'resistive #'
		choice_b = 'inductive '
		choice_c = 'capacitive'
		choice_d = 'infinite'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""At resonance, the input impedance to a lossless antenna should be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_16():
	def __init__(self):
		
		choice_a = 'a shorted stub'
		choice_b = 'a loading coil'
		choice_c = 'an LC network'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""An antenna can be matched to a feedline using"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_17():
	def __init__(self):
		
		choice_a = 'the number of lobes increases #'
		choice_b = 'the number of nodes increases'
		choice_c = 'efficiency decreases'
		choice_d = 'none of the choices '
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""As the length of the a long wire antenna is increased"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_18():
	def __init__(self):
		
		choice_a = 'phased'
		choice_b = 'driven'
		choice_c = 'parasitic'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Arrays can be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_19():
	def __init__(self):
		
		choice_a = 'Marconi'
		choice_b = 'Yagi #'
		choice_c = 'Log-Periodic Dipole'
		choice_d = 'stacked array'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""An array with one driven element, a reflector, and one or more directors is called an"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_20():
	def __init__(self):
		
		choice_a = 'Low-Power Dipole Array'
		choice_b = 'Low-Power Directed Array'
		choice_c = 'Log-Periodic Dipole Array #'
		choice_d = 'Log Power Dipole Array'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""LPDA stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_21():
	def __init__(self):
		
		choice_a = 'collimated #'
		choice_b = 'phased'
		choice_c = 'dispersed'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""The radiated beam from a parabolic dish transmitting antenna is:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_22():
	def __init__(self):
		
		choice_a = 'center'
		choice_b = 'edges'
		choice_c = 'focus #'
		choice_d = 'horn'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The energy picked up by a parabolic antenna is concentrated at the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_23():
	def __init__(self):
		
		choice_a = 'an echo chamber'
		choice_b = 'an anechoic chamber #'
		choice_c = 'a vacuum chamber'
		choice_d = 'an RF reflective chamber'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Antennas are often tested in """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_16_24():
	def __init__(self):
		
		choice_a = 'a slotted line'
		choice_b = 'a dipole'
		choice_c = 'an EIRP meter'
		choice_d = 'a field strength meter #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Field strength at a distance from an antenna is measured with"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_1():
	def __init__(self):
		
		choice_a = 'section '
		choice_b = 'hop #'
		choice_c = 'skip'
		choice_d = 'jump'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Another term for a single microwave link is a """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_2():
	def __init__(self):
		
		choice_a = 'FM'
		choice_b = 'SSB'
		choice_c = 'QAM'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Microwave systems use"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_3():
	def __init__(self):
		
		choice_a = '90%'
		choice_b = '99%'
		choice_c = '99.9%'
		choice_d = '99.99% #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The typical reliability of a microwave system is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_4():
	def __init__(self):
		
		choice_a = '2 watts #'
		choice_b = '20 watts'
		choice_c = '200 watts'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""A typical microwave system uses a transmitted power of about"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_5():
	def __init__(self):
		
		choice_a = 'reliability'
		choice_b = 'noise level #'
		choice_c = 'jitter'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""In analog microwave systems, additional repeaters increase the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_6():
	def __init__(self):
		
		choice_a = 'reliability'
		choice_b = 'noise level '
		choice_c = 'jitter #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""In digital microwave systems, additional repeaters increase the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_7():
	def __init__(self):
		
		choice_a = 'Loss of skip'
		choice_b = 'Loss of signal'
		choice_c = 'Line of sight #'
		choice_d = 'Line of signal'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""LOS stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_8():
	def __init__(self):
		
		choice_a = 'a very narrow microwave beam #'
		choice_b = 'a very wide microwave beam'
		choice_c = 'excessive noise'
		choice_d = 'jitter'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Too much antenna gain causes"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_9():
	def __init__(self):
		
		choice_a = '60 percent of the Faraday zone'
		choice_b = '60 percent of the Fresnel zone #'
		choice_c = '60 percent of the height of the antenna tower'
		choice_d = '60 percent of the highest obstacle height'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The microwave signal should be clear from obstacles by at least"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_10():
	def __init__(self):
		
		choice_a = 'a carrier-to-noise ratio that exceeds a given value #'
		choice_b = 'an ERP level that exceeds a given value'
		choice_c = 'an energy-per-hertz level that exceeds a given value'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Satisfactory performance of an analog microwave system is defined as """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_11():
	def __init__(self):
		
		choice_a = 'low level of transmitted power'
		choice_b = 'high level of ERP'
		choice_c = 'good energy per bit per transmitted Watt ratio'
		choice_d = 'good energy per bit per noise density ratio #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Satisfactory performance of a digital microwave system requires a """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_12():
	def __init__(self):
		
		choice_a = 'multipath reception'
		choice_b = 'attenuation due to weather'
		choice_c = 'ducting '
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Fading is caused by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_13():
	def __init__(self):
		
		choice_a = 'diversity'
		choice_b = 'power '
		choice_c = 'high - gain antennas #'
		choice_d = 'all of the choices '
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The effects of fading due to multipath reception are often reduced by using"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_14():
	def __init__(self):
		
		choice_a = 'always'
		choice_b = 'when distance exceeds line of sight #'
		choice_c = 'above 10 GHz'
		choice_d = 'below 10 GHz'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Repeaters are used in a microwave system"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_15():
	def __init__(self):
		
		choice_a = 'IF type '
		choice_b = 'baseband type'
		choice_c = 'regenerative type'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""Microwave repeaters can be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_16():
	def __init__(self):
		
		choice_a = 'less bandwidth is required '
		choice_b = 'accumulation of noise is reduced #'
		choice_c = 'it requires less power '
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		
		
		self.question = f"""An advantage of digital techniques over analog in a microwave system is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_17():
	def __init__(self):
		
		choice_a = 'multichannel microwave distribution system'
		choice_b = 'multipoint microwave distribution system'
		choice_c = 'multichannel multipoint distribution system #'
		choice_d = 'multiple microwave distribution systems'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""MMDS stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_18():
	def __init__(self):
		
		choice_a = 'local microwave distribution system'
		choice_b = 'local multipoint distribution system #'
		choice_c = 'local mutichannel distribution system'
		choice_d = 'low-power microwave distribution system'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""LMDS stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_18_19():
	def __init__(self):
		
		choice_a = 'bidirectional #'
		choice_b = 'unidirectional'
		choice_c = 'multidirectional'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		 
		
		self.question = f"""LMDS is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

