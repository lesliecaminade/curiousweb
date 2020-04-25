from electronics.power_electronics_engine import *
from geas.physics_engine import *

topics_keys = [
    'Mathematics',
    'Sciences',
    'Electronics',
    'Electronic Communications',
]

subtopics_keys = [
    'Electronics: Power Electronics',
    'Sciences: One Dimension Kinematics',
    'Sciences: Kinetics'
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
    example_2_19,
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
]


questions_by_subtopic = {
    subtopics_keys[0]:power_electronics,
    subtopics_keys[1]:one_dimension_kinematics,
    subtopics_keys[2]:kinetics,
}

questions_by_topic ={
    topics_keys[3]: power_electronics,
    topics_keys[2]: one_dimension_kinematics + kinetics,
}
