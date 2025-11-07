import wikipedia

search_list = wikipedia.search("Generative Artificial Intelligence")

#page = wikipedia.page(search_list[1],auto_suggest=False)
#print(page.title)
#print(page.references)

for i in (0, len(search_list)-1):
    page = wikipedia.page(search_list[i],auto_suggest=False)
    title = page.title
    ref = page.references

    with open(f"{title}.txt", "w") as f:
        f.write(ref)