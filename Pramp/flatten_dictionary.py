# Flatten a Dictionary
# A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type(i.e an integer, boolean, double, string etc) or other dictionaries(dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

# Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

# # , Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.
# If you’re using a compiled language such Java, C++, C

# If a certain key is empty, it should be excluded from the output(see e in the example below).

# Example:

# input:  dict = {
#     "Key1": "1",
#     "Key2": {
#         "a": "2",
#         "b": "3",
#         "c": {
#             "d": "3",
#             "e": {
#                 "": "1"
#             }
#         }
#     }
# }

# output: {
#     "Key1": "1",
#     "Key2.a": "2",
#             "Key2.b": "3",
#             "Key2.c.d": "3",
#             "Key2.c.e": "1"
# }
# Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

# Constraints:

# [time limit] 5000ms
# [input] Dictionary dict
# [output] Dictionary

def flatten_dictionary(dictionary):
  res = {}
  flatten_dictionary_key_builder(dictionary, '', res)
  return res


def flatten_dictionary_key_builder(dictionary, total_key, res):
    for key in dictionary:
        if type(dictionary[key]) is dict:
          if total_key == "":
            flatten_dictionary_key_builder(dictionary[key], key, res)
          elif key != "":
            flatten_dictionary_key_builder(
                dictionary[key], total_key + '.' + key, res)
          else:
            flatten_dictionary_key_builder(dictionary[key], total_key, res)
        elif total_key == "":
            res[key] = dictionary[key]
        elif key == "":
            res[total_key] = dictionary[key]
        else:
            res[total_key + '.' + key] = dictionary[key]
