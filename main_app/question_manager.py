from electronics.power_electronics_engine import *
from geas.physics_engine import *
from electronics.diode_engine import *
from electronics.field_effect_transistors_engine import *
from electronics.energy_conversion_engine import *

topics_keys = [
    'Mathematics',
    'Sciences',
    'Electronics',
    'Electronic Communications',
]

subtopics_keys = [
    'Electronics: Power Electronics',
    'Sciences: One Dimension Kinematics',
    'Sciences: Kinetics',
    'Sciences: Work-Energy Theorem',
    'Electronics: Diode Circuits',
    'Electronics: Field Effect Transistors',
    'Electronics: Energy Conversion',

]

one_dimension_kinematics = [
    example_2_1,
    example_2_2,
    example_2_3,
    example_2_4,
    example_2_8,
    example_2_9,
    example_2_10,
    example_2_11,
    example_2_12,
    example_2_13,
    example_2_14,
    example_2_15,
    example_2_16,
    example_2_17,
    example_2_18,
    # example_2_19,
    example_2_20,
    example_2_21,
]

kinetics = [
    example_3_1,
    example_3_2,
    example_3_3,
    example_3_4,
    example_3_5,
    example_3_6,
    example_3_7,
    example_3_8,
    example_3_9,
    example_3_10,
    example_3_11,
    example_3_13,
    example_3_14,
    example_3_15,
    example_3_16,
    example_3_17,
    example_3_18,
    example_3_19,
    example_3_20,
    example_3_21,
    example_3_22,
    example_3_23,
    example_3_24,
    example_3_25,
    example_3_26,
]

power_electronics = [
    fewson_2_1,
    fewson_2_2,
    fewson_2_3,
    fewson_2_4,
    fewson_2_5,
    fewson_3_1,
    fewson_3_3,
    fewson_3_4,
    fewson_3_5,
    fewson_3_6,
    fewson_3_8,
    fewson_3_9,
    fewson_3_10,
]

work_energy_theorem = [
    schaums_6_1,
    schaums_6_2,
    schaums_6_3,
    schaums_6_4,
    schaums_6_6,
    schaums_6_7,
    schaums_6_8,
    schaums_6_9,
    schaums_6_10,
    schaums_6_11,
    schaums_6_12,
    schaums_6_13,
    schaums_6_16,
    schaums_6_17,
    schaums_6_18,
    schaums_6_19,
    schaums_6_20,
    schaums_6_21,
    schaums_6_23,
]

diode = [
    floyd_2_2,
    floyd_2_3,
    floyd_2_4,
    floyd_2_5,
    floyd_2_6,
    floyd_2_7,
    floyd_2_8,
    floyd_2_9,
    floyd_2_10,
    floyd_2_11,
    floyd_2_12,
    floyd_2_13,
    floyd_3_5,
    #floyd_3_6, floating point problem
    floyd_3_7,
    floyd_3_8_a,
    boylestad_2_4,
    boylestad_2_6,
    boylestad_2_9,
    boylestad_2_10,
    boylestad_2_11,
    boylestad_2_12,
    boylestad_2_13,
    boylestad_2_14,
    boylestad_2_15,
    boylestad_2_16,
    boylestad_2_17,
]

field_effect_transistors = [
    boylestad_7_1,
    boylestad_7_2,
    boylestad_7_4,
    boylestad_7_5,
    boylestad_7_6,
    boylestad_7_8,
    boylestad_7_10,
    boylestad_7_11,
    boylestad_8_7,
    boylestad_8_8,
    boylestad_8_9,
    boylestad_8_10,
    boylestad_8_11,
    boylestad_8_12,
]

energy_conversion = [
    johnbird_4_1,
]

questions_by_subtopic = {
    subtopics_keys[0]:power_electronics,
    subtopics_keys[1]:one_dimension_kinematics,
    subtopics_keys[2]:kinetics,
    subtopics_keys[3]:work_energy_theorem,
    subtopics_keys[4]:diode,
    subtopics_keys[5]:field_effect_transistors,
    subtopics_keys[6]:energy_conversion,

}

questions_by_topic = {
    topics_keys[3]: power_electronics + diode + field_effect_transistors,
    topics_keys[2]: one_dimension_kinematics + kinetics + work_energy_theorem,
}
