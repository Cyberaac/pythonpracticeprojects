#!/usr/bin/env python3

#This is a subnet to CIDR converter.
#Syntax: ./cidr_converter.py -s <subnet>

import optparse
import re

parser = optparse.OptionParser()

parser.add_option("-s", "--subnet", dest="al_subnet", help="Put your subnet here to convert it to CIDR. eg -s 255.255.255.0")
al_subnet = parser.parse_args()[0].al_subnet
subnet = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", al_subnet)[0]

if not al_subnet:
    print("You forgot to input subnet. --help for help.")
elif not str(subnet) == str(al_subnet):
    print("You didn't enter a valid subnet. --help for help.")
else:
    def cidr_cal(subnet):
        subnet = str(subnet)
        results_ip = re.findall(r"\d{1,3}", subnet)
        subnet_options = ["254", "252", "248", "240", "224", "192", "128"]
        subnet_cidr_options = {"254": ["7", "15", "23", "31"], "252": ["6", "14", "22", "30"], "248": ["5", "13", "21", "29"], "240": ["4", "12", "20", "28"], "224": ["3", "11", "19", "27"], "192": ["2", "10", "18", "26"], "128": ["1", "9", "17", "25"]}
        starting_num = 0
        i = True
        while i == True:
            if results_ip[starting_num] == "255":
                if starting_num == 3:
                    subnet_cidr = "32"
                    i = False
                starting_num = starting_num + 1
            elif results_ip[starting_num] == "0" and starting_num == 3:
                    subnet_cidr = "24"
                    i = False
            elif results_ip[starting_num] == "0" and starting_num == 2:
                    subnet_cidr = "16"
                    i = False
            elif results_ip[starting_num] == "0" and starting_num == 1:
                    subnet_cidr = "8"
                    i = False
            else:
                for subnet_option in subnet_options:
                    if subnet_option == results_ip[starting_num]:
                        subop = str(subnet_option)
                        subnet_cidr = subnet_cidr_options[subop][starting_num]

                        i = False
        return subnet_cidr

    cidr_results = cidr_cal(subnet)
    print("Your subnet in CIDR form is: " +'/' + cidr_results)
