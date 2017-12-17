from bs4 import BeautifulSoup
import wget
import os

# Setup
file_url = "https://www.mybuilder.com/profile/view/fgneacsu/feedback"


part_1 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt1?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D"
part_2 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt2?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D"
part_3 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt3?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D"
part_4 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt4?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D"
part_5 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt5?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D"
parts = ((part_1, "part_1.html"), (part_2, "part_2.html"), (part_3, "part_3.html"), (part_4, "part_4.html"), (part_5, "part_5.html"))


password = ""

def createSoup(url, file):
    file_name = wget.download(url, file)
    html_content = open(file, "r")
    return BeautifulSoup(html_content, 'html.parser')

for part in parts:
    part_soup = createSoup(part[0], part[1])
    print(part_soup)
    password = password + str(part_soup)
    #print(lepart)

try:
    for part in parts:
        os.remove(part[1])
except FileNotFoundError:
    print("No file found to delete")

print("Password: "+password)


