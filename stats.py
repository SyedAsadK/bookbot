

def read_file(path) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(str):
        no_of_words = len(str.split())
        return no_of_words 

def count_letters(str) :
    str = str.lower()
    count = {}
    for s in str :
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    sorted_count = dict(sorted(count.items(),key=lambda item:item[1],reverse=True))
    for i in sorted_count:
        if i.isalpha():
            print(f"{i}: {sorted_count[i]} ")


    # for i in count.keys():
    #     print(f"{i}: {count[i]}",end="\n")



