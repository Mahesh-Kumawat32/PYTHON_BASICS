book = {
    "name" :'hindi',
    "author":"premchand",
    'pages': 100
}

# for i in book.keys():     #access using keys() methods
#     print(i)

# for i in book.values():   #access using values() methods
#     print(i)

# for i,j in book.items():  #access using items() methods
#     print(i,":",j)

# print(book.get('name'))     #get()
# print(book.keys())          #keys()
# print(book.values())        #values()
# print(book.items())         #items()
# print(book.pop("name"))     #pop(key)
# print(book)
# print(book.update({'pages':50}))    #update({keys:values})----->to update some existing value
# print(book.update({'city': 'Jodhpur'})) #update({keys:values})------>to add some value in the dictionary
# book.popitem()                            #popitem()-->remove the last inserted key value pair
# book.setdefault('city','Jodhpur')       #setdefault()---->syntax: dict_name.setdefault('key','value')
# k = book.copy()                             #copy()
# print(k)
# book.clear()                #clear()--->empty dictionary
# print(sorted(book.items()))   #sorted()--->  to sort a dictionary we use sorted method
# print(book)
