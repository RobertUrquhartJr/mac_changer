#!usr/bin/env python3

# remember to check what is imported
import subprocess
import optparse
import re

# step 4 condensing all of step 2


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--interface",
        dest="interface",
        help="Interface to change it's MAC address.",
    )
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (
        options,
        arguments,
    ) = (
        parser.parse_args()
    )  # because options were moved INSIDE of this function on step 4 it is not accessible outside of it.
    # what returning parser does it send this the results to get_arguments below when it is called.
    # step 5, adding if statement that will throw an error if something is left out, instead of generic error.
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


# step 3 is adding functions to clean it up. condensing all of step 1.
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# step 6 is creating "get current mac" we'll use subprocess.check_output to test it. must be after options to test.
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # import re here then you can use this formula found in pythex to search for the MAC address.
    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)
    )
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


# step 2

# # object that can handle user input using argument
# parser = optparse.OptionParser()
#
# # add options to the object
# parser.add_option("-i", "--interface" , dest="interface" , help="Interface to change it's MAC address.")
# parser.add_option("-m", "--mac" , dest="new_mac" , help="New MAC address")
#
# # allows object to understand user information. also returns arguments and values to a variable if you give it one.
# (options, arguments) = parser.parse_args()
# # because using two variables in one line will need 2 brackets
# # options will return values and arguments will return arguments..we're only looking at values.
# # this is where we get options.interface


# step 1.
# next 2 lines cleared when we call change_mac below in step 3.
# interface = options.interface #raw_input ("interface >")
# new_mac = options.new_mac #raw_input("new MAC >")
# print("[+] Changing MAC address for " + interface + " to " + new_mac)
#
# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])

# subprocess.call("ifconfig " + interface + " down ", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
# subprocess.call("ifconfig " + interface + " up ", shell=True)
# this section is the 1st version of the list. list is used to secure the info and not get hijacked.


# another part of step 4 is get arguments being called and now having values for options
# that can then be passed below to change_mac function.
# this needs to be first so that it can pass below.
# in step 5 this is moved back up to the function to keep it with the if statement. created new variable called options.
options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = ", str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")

# must call change_mac from step 3
# change_mac(options.interface, options.new_mac) #temp commented out when checking check_output.
