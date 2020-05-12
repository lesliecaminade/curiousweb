from main_app.models import Topic, Subtopic, MultipleChoice
import random

def create_exam(subtopic, item_count):
    """pull item_count number of items from all the MUltiplceChoice objects from the existing database
    and then put them in a list"""

    items = MultipleChoice.objects.filter(subtopic = subtopic)
    #this is a QueryDictionary that contains all the questions that satisfy the requested subtopic

    items_list = list(items) #this converts the dictionary into a list
    random.shuffle(items_list) #randomize the list

    try:#this try-except tries to catch the scenario where the number of items requested exceeds the available items
        n_items_list = items_list[:item_count] #slice the number of items into item_count
    except:
        n_items_list = list(items_list) #just make with the available

    return n_items_list #this is a list of question objects returned back
