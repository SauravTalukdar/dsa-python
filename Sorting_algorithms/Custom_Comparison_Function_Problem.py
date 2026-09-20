#we need to sort "top notebooks of the week",which are objects in terms of likes in decreasing order

class Notebook:
    def __init__(self,title,username,likes):
        self.title = title
        self.username = username
        self.likes = likes
    def __repr__(self):
        return f'Notebook {self.username}/{self.title},{self.likes}'

#making some notebooks
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('python-numpy', 'tanushka', 592)            
nb2 = Notebook('linear-regression', 'saurav', 532)
nb3 = Notebook('logistic-regression', 'vikas', 31)
nb4 = Notebook('feedforward-nn', 'sonaksh', 94)
nb5 = Notebook('cifar10-cnn', 'biraj', 2)
nb6 = Notebook('cifar10-resnet', 'tanya', 29)
nb7 = Notebook('anime-gans', 'hemanth', 80)
nb8 = Notebook('python-fundamentals', 'bibek', 136)

notebooks = [nb0,nb1,nb2,nb3,nb4,nb5,nb6,nb7,nb8]

#we compare likes of notebooks(notice we say lesser if nb1(morelikes)>nb2(lesslikes) 
#because we are arranging in decreasing order,so we get the lesser index(position)
def compare_likes(nb1,nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare = compare_likes):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    left = objs[:mid]
    right = objs[mid:]
    return merge(merge_sort(left, compare), 
                 merge_sort(right, compare),compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]   

sorted_notebooks = merge_sort(notebooks, compare_likes)

print(sorted_notebooks)

