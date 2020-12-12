# RLANPorts

* By using a template in DNAC, enable all RLAN ports on 1815W and 9105 APs *

---

**ToDo's:**

 - add error handling
 - add some command line options to specify things like ap or template name,
   or iterate through projects/templates in DNAC and have user select
 - create/push the project and template so the user doesn't have to

---

## Motivation

I had a customer that deployed hundreds of C9105 APs and wanted a way to bulk-enable
all the LAN ports on those APs. Cisco currently does not have a way to do that.

By using templates and the dnacentersdk, the code will pull all the APs from the controller
and apply the template to the 1815 and 9105 AP types.

The DNA Center I used has self-signed certs, so you might want to disable the verification
on the DNA call, as well as ignore urllib3 warnings. Do that at your own risk.

## Features

This is feature limited - information is hardcoded in the python script. Adjust as needed.

## Technologies & Frameworks Used

This uses Python 3.x for the code of the application. Other packages:

 - dnacentersdk

**Cisco Products & Services:**

This was built/tested against DNA Center v2.1.2.4

## Installation

You might want to do this in a python virtual environment.

Clone this repo. After doig that, do:

  pip install -r requirements.txt

to get the required packages installed.

Create a template in DNA Center under Tools -> Template Editor. Use
the sample template in the repository.

Edit the portconfig.py script to specify:
 - the template name you just created
 - wireless controller IP address
 - DNA Center URL, username, and password


## Usage

Just run the portconfig.py script. No CLI options exist at this time


## Future changes

This was just a proof of concept, but I think being able to specify a subset
of APs on the command line would be helpful. Also, the APIs allow you to create
templates in DNAC. The tool should be able to create/deploy/delete the template.

## Authors & Maintainers

- Eric Pylko <erpylko@cisco.com>

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
