def language_roulet():
    import random
    
    languages = ["Java", "C++"]
    rare_languages = ["Haskell"]
    
    weights = [1] * len(languages) + [0.25] * len(rare_languages)
    all_languages = languages + rare_languages
    
    days = []
    for i in range(25):
        lang = random.choices(all_languages, weights=weights, k=1)[0]
        day_str = "".join("Day " + str(i+1) + ": " + str(lang)) + "\n"
        days.append(day_str)
    
    return days


def write_to_file(year, data):
    with open(f"{year}/days", "w") as f:
        for byte in data:
            f.write(byte)
    
    
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        year = sys.argv[1]
        write_to_file(year, language_roulet())