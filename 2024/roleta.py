"""Fun idea just oughta my league (for now)"""


import random


def random_programming_language():
    languages = [
        "Haskell",
        "Go", 
        # "Java", 
        "Python",
        # "LISP",
        # "C", 
        #"C++", 
        #"Rust",
        #"JavaScript",
        #"R",
        #"Ocaml",
        #"Lua",
        #"Ruby"
    ]
    #rare_languages = ["Prolog", "Assembly"]
    rare_languages = ["", ""]
    
    weights = [1] * len(languages) + [0.01, 0.01]
    all_languages = languages + rare_languages
    
    chosen_language = random.choices(all_languages, weights=weights, k=1)[0]
    return chosen_language


print(random_programming_language())
