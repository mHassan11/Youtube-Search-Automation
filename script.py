from search_yt import youtube_search
import random
import json


def main():
    file = "query.txt"
    temp = open(file,'r').read().split('\t\n')
    print(len(temp))
    selected_list = random.sample(temp, 50)

    print(len(selected_list))
    dict_result = {}
    for query_term in selected_list:
        print("Looking up",query_term)
        result_list, tot = youtube_search(query_term, "1")
        dict_result[query_term] = result_list

    with open('result.json', 'w') as fp:
        json.dump(dict_result, fp)
main()