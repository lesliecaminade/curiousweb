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
    'Sciences: Constant Acceleration in One Dimension',
]

constant_acceleration_in_one_dimension = [
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
    subtopics_keys[1]:constant_acceleration_in_one_dimension,
}

questions_by_topic ={
    topics_keys[3]: power_electronics,
    topics_keys[2]: constant_acceleration_in_one_dimension,
}
