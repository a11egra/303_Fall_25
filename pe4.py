import wikipedia
import time
import concurrent.futures
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

search_list = wikipedia.search("Generative Artificial Intelligence")

#
# PART A
# 

start_time_A = time.perf_counter()

for i in range(0, len(search_list)-1):
    page = wikipedia.page(search_list[i],auto_suggest=False)
    title = page.title
    ref = page.references

    with open(f"{title}.txt", "w") as f:
        for j in range(0,len(ref)-1):
            f.write(f"{ref[j]} \n")

end_time_A = time.perf_counter()
tot_time_A = end_time_A - start_time_A
print(f"Part A took {tot_time_A} seconds.")

#
# PART B
# 


start_time_B = time.perf_counter()

def wiki_dl_and_save(topic):
    page = wikipedia.page(topic,auto_suggest=False)
    title = page.title
    ref = page.references

    with open(f"{title}.txt", "w") as f:
        for j in range(0,len(ref)-1):
            f.write(f"{ref[j]} \n")

with concurrent.futures.ThreadPoolExecutor(10) as executor:
    executor.map(wiki_dl_and_save, search_list)

end_time_B = time.perf_counter()
tot_time_B = end_time_B - start_time_B
print(f"Part B took {tot_time_B} seconds.")