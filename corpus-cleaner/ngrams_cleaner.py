with open("ngrams_terminet/candidatos_backup/2_gram/N,BugFeature,Spoladore.txt", "r") as file:
    file = file.read()


def str_2_list(text_file):
    converted_2_list = text_file.split('\n')
    converted_2_list = converted_2_list[50:55]
    return converted_2_list

def list_2_set(converted_2_list):
    
    return new_list



# Function call:
print(list_2_set(str_2_list(file)))