import subprocess

path = 'directory/pathname/%(title)s .%(ext)s'
choice = 0
string =[]

subprocess.call(["sudo", "pip", "install", "-U", "youtube-dl"])

while(choice != 1):
    string.append(input("\nCopy Paste Link: "))
    while True:
        try:
            choice = int(input("More links? Yes:0\n             No:1\n"))
        except ValueError:
            print("\nI didn't understand that\n")
            continue
        else:
            break
    if choice == 1:
        break

for i in range(len(string)):
    subprocess.call(["youtube-dl","--extract-audio","--audio-format","mp3","-o", path, string[i]])
