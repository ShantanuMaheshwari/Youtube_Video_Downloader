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

while i < no_of_links:
    if paste != pyperclip.paste():
        paste = pyperclip.paste()
        url_list.append(paste)
        print(paste)
        i += 1

file = open(file_name, 'a')
file.write('\n'.join(url_list))
file.close()
