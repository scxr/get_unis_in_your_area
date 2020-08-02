from requests import get
import json
from math import radians, cos, sin, asin, sqrt
import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self,master):
        self.master = master
        master.title='Clearing finder'
        self.mtxt = tkinter.StringVar(None)
        self.mtxt.set('0')
        self.entry = tkinter.Entry(master, textvariable=self.mtxt,relief=tkinter.SUNKEN)
        self.entry.pack()
        self.button = tkinter.Button(master,text="Search",command=self.get_needed)
        self.button.pack()


    def get_needed(self):
        l,la = get_ip_long_lat()
        uni_info = parse_into_list()
        output = []
        for i in uni_info:
            to_check = i.split(';')
            l2,la2 = to_check[1],to_check[2]
            d = get_distance_haversine(l,la,l2,la2)
            if d <= float(self.entry.get()):
                output.append(f'Name : {to_check[0]} | Contact: {to_check[3]} ')

        with open('in_your_area.txt','w') as f:
            f.write('\n'.join(output))
        tkinter.messagebox.showinfo('FOUND',f'WE FOUND {len(output)} UNIS IN THE AREA SPECIFIED')

def get_ip_long_lat():
    url = 'http://ipinfo.io/json'
    response = get(url)
    to_parse = json.loads(response.content)['loc'].split(',')
    longitude = to_parse[0]
    latitude = to_parse[1]
    return longitude,latitude

def parse_into_list():
    with open('../uni_infos.txt','r') as f:
        uni_info = f.read().split('\n')
    return uni_info

def get_distance_haversine(l1,la1,l2,la2):
    #convert decimals to radians
    l1,l2,la1,la2 = map(radians,[float(l1),float(l2),float(la1),float(la2)]) 
    
    #formula stuff
    difference_l = l2 - l1
    difference_la = la2-la1
    a = sin(difference_la/2)**2 + cos(la1) * cos(la2) * sin(difference_l/2)**2
    c = 2* asin(sqrt(a))
    earth_rad = 3959.87433
    return c*earth_rad


if __name__ == "__main__":
    root = tkinter.Tk()
    runit = GUI(root)
    root.mainloop()




