#%%
f = open("textfile.txt", "r")
lines = [] 
for line in f:
    lines.append(line) 
f.close()
# %%
with open("textfile.txt") as f: 
    lines = []
    for line in f:
        lines.append(line)


# %%
with open(r"subfolder/textfile2.txt") as f:
    lines = []
    for line in f:
        lines.append(line)
# %%
with open(r"subfolder/subsubfolder/textfile3.txt") as f:
    lines = []
    for line in f:
        lines.append(line)
# %%
with open(r"../readme.md") as f:
    lines = []
    for line in f:
        lines.append(line)
# %%
with open(r"../Lecture_00/helloworld.py") as f:
    lines = []
    for line in f:
        lines.append(line)
# %%
with open(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\04_Assignments\Assignment_4\cereal.csv") as f: 
    lines = []
    for line in f:
        lines.append(line)
# %%
