import pyperclip

"""pyperclip doesn't work on linux, run commands:
'sudo apt-get install xsel'  to install the xsel utility.
'sudo apt-get install xclip' to install the xclip utility.
"""

url_list = []
paste = ''
i = 0

no_of_links = int(input("Enter number of links to be pasted: "))
file_name = input('Enter file name: ')
print("After copying first link press Enter, then copy rest of the links. ")
print("Links will be pasted in the above file automatically")
input()

while i < no_of_links:
    if paste != pyperclip.paste():
        paste = pyperclip.paste()
        url_list.append(paste)
        print(paste)
        i += 1

file = open(file_name, 'a')
file.write('\n'.join(url_list))
file.close()
