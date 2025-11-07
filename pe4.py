import wikipedia

search_list = wikipedia.search("Generative Artificial Intelligence")

#page = wikipedia.page(search_list[1],auto_suggest=False)
#print(page.title)
#print(page.references)
print(len(search_list))

for i in range(0, len(search_list)-1):
    page = wikipedia.page(search_list[i],auto_suggest=False)
    title = page.title
    ref = page.references

    with open(f"{title}.txt", "w") as f:
        for j in range(0,len(ref)-1):
            f.write(f"{ref[j]} \n")