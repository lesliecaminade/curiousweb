import random
from est import wave_propagation_engine as engine
from est import antenna_engine as engine2
from est import microwave_engine as engine3
from num2words import num2words


def ask():
	ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
	return random.choice(ask_words)

def parse(string_input):
	string_input = str(string_input)
	return string_input.replace('**', '^').replace('*', ' ')

class Constructor():
	def __init__(self, engine_class_instances):
		#Battery - a single instance of a set of givens, and an answer for a certain problem

		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):

			#battery = engine.Some_class_from_engine
			battery = engine_class_instances[i]

			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.answer)

			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = main.question
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""       

class jma_5_43():
	def __init__(self):
		instance_list = [
		engine.jma_5_43(),        
		engine.jma_5_43(),
		engine.jma_5_43(),
		engine.jma_5_43()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_44_a():
	def __init__(self):
		instance_list = [
		engine.jma_5_44_a(),        
		engine.jma_5_44_a(),
		engine.jma_5_44_a(),
		engine.jma_5_44_a()]        
		
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    	

class jma_5_44_b():
	def __init__(self):
		instance_list = [
		engine.jma_5_44_b(),        
		engine.jma_5_44_b(),
		engine.jma_5_44_b(),
		engine.jma_5_44_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_45_a():
	def __init__(self):
		instance_list = [
		engine.jma_5_45_a(),        
		engine.jma_5_45_a(),
		engine.jma_5_45_a(),
		engine.jma_5_45_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_45_b():
	def __init__(self):
		instance_list = [
		engine.jma_5_45_b(),        
		engine.jma_5_45_b(),
		engine.jma_5_45_b(),
		engine.jma_5_45_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_46():
	def __init__(self):
		instance_list = [
		engine.jma_5_46(),        
		engine.jma_5_46(),
		engine.jma_5_46(),
		engine.jma_5_46()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_51():
	def __init__(self):
		instance_list = [
		engine.jma_5_51(),        
		engine.jma_5_51(),
		engine.jma_5_51(),
		engine.jma_5_51()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_52():
	def __init__(self):
		instance_list = [
		engine.jma_5_52(),        
		engine.jma_5_52(),
		engine.jma_5_52(),
		engine.jma_5_52()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class jma_5_55():
	def __init__(self):
		instance_list = [
		engine.jma_5_55(),        
		engine.jma_5_55(),
		engine.jma_5_55(),
		engine.jma_5_55()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class tomasi_14_1():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_1(),        
		engine.tomasi_14_1(),
		engine.tomasi_14_1(),
		engine.tomasi_14_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class tomasi_14_2():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_2(),        
		engine.tomasi_14_2(),
		engine.tomasi_14_2(),
		engine.tomasi_14_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class tomasi_14_3():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_3(),        
		engine.tomasi_14_3(),
		engine.tomasi_14_3(),
		engine.tomasi_14_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class tomasi_14_3_b():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_3_b(),        
		engine.tomasi_14_3_b(),
		engine.tomasi_14_3_b(),
		engine.tomasi_14_3_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class tomasi_14_3_c():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_3_c(),        
		engine.tomasi_14_3_c(),
		engine.tomasi_14_3_c(),
		engine.tomasi_14_3_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class tomasi_14_3_d():
	def __init__(self):
		instance_list = [
		engine.tomasi_14_3_d(),        
		engine.tomasi_14_3_d(),
		engine.tomasi_14_3_d(),
		engine.tomasi_14_3_d()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  



#ENGINE 2
class jma_17_1():
	def __init__(self):
		instance_list = [
		engine2.jma_17_1(),        
		engine2.jma_17_1(),
		engine2.jma_17_1(),
		engine2.jma_17_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class jma_17_2():
	def __init__(self):
		instance_list = [
		engine2.jma_17_2(),        
		engine2.jma_17_2(),
		engine2.jma_17_2(),
		engine2.jma_17_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_3():
	def __init__(self):
		instance_list = [
		engine2.jma_17_3(),        
		engine2.jma_17_3(),
		engine2.jma_17_3(),
		engine2.jma_17_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_4():
	def __init__(self):
		instance_list = [
		engine2.jma_17_4(),        
		engine2.jma_17_4(),
		engine2.jma_17_4(),
		engine2.jma_17_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_5():
	def __init__(self):
		instance_list = [
		engine2.jma_17_5(),        
		engine2.jma_17_5(),
		engine2.jma_17_5(),
		engine2.jma_17_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_6():
	def __init__(self):
		instance_list = [
		engine2.jma_17_6(),        
		engine2.jma_17_6(),
		engine2.jma_17_6(),
		engine2.jma_17_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_7():
	def __init__(self):
		instance_list = [
		engine2.jma_17_7(),        
		engine2.jma_17_7(),
		engine2.jma_17_7(),
		engine2.jma_17_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_8():
	def __init__(self):
		instance_list = [
		engine2.jma_17_8(),        
		engine2.jma_17_8(),
		engine2.jma_17_8(),
		engine2.jma_17_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_9():
	def __init__(self):
		instance_list = [
		engine2.jma_17_9(),        
		engine2.jma_17_9(),
		engine2.jma_17_9(),
		engine2.jma_17_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_17_10():
	def __init__(self):
		instance_list = [
		engine2.jma_17_10(),        
		engine2.jma_17_10(),
		engine2.jma_17_10(),
		engine2.jma_17_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_1():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_1(),        
		engine2.tomasi_15_1(),
		engine2.tomasi_15_1(),
		engine2.tomasi_15_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_2():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_2(),        
		engine2.tomasi_15_2(),
		engine2.tomasi_15_2(),
		engine2.tomasi_15_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_3():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_3(),        
		engine2.tomasi_15_3(),
		engine2.tomasi_15_3(),
		engine2.tomasi_15_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_4():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_4(),        
		engine2.tomasi_15_4(),
		engine2.tomasi_15_4(),
		engine2.tomasi_15_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_5():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_5(),        
		engine2.tomasi_15_5(),
		engine2.tomasi_15_5(),
		engine2.tomasi_15_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class tomasi_15_6():
	def __init__(self):
		instance_list = [
		engine2.tomasi_15_6(),        
		engine2.tomasi_15_6(),
		engine2.tomasi_15_6(),
		engine2.tomasi_15_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer


#ENgine 3
class jma_5_65():
	def __init__(self):
		instance_list = [
		engine3.jma_5_65(),        
		engine3.jma_5_65(),
		engine3.jma_5_65(),
		engine3.jma_5_65()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_66():
	def __init__(self):
		instance_list = [
		engine3.jma_5_66(),        
		engine3.jma_5_66(),
		engine3.jma_5_66(),
		engine3.jma_5_66()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_67():
	def __init__(self):
		instance_list = [
		engine3.jma_5_67(),        
		engine3.jma_5_67(),
		engine3.jma_5_67(),
		engine3.jma_5_67()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_68():
	def __init__(self):
		instance_list = [
		engine3.jma_5_68(),        
		engine3.jma_5_68(),
		engine3.jma_5_68(),
		engine3.jma_5_68()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_69():
	def __init__(self):
		instance_list = [
		engine3.jma_5_69(),        
		engine3.jma_5_69(),
		engine3.jma_5_69(),
		engine3.jma_5_69()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_70():
	def __init__(self):
		instance_list = [
		engine3.jma_5_70(),        
		engine3.jma_5_70(),
		engine3.jma_5_70(),
		engine3.jma_5_70()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_76():
	def __init__(self):
		instance_list = [
		engine3.jma_5_76(),        
		engine3.jma_5_76(),
		engine3.jma_5_76(),
		engine3.jma_5_76()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class jma_5_78():
	def __init__(self):
		instance_list = [
		engine3.jma_5_78(),        
		engine3.jma_5_78(),
		engine3.jma_5_78(),
		engine3.jma_5_78()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer