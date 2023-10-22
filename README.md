# rdns-cidr
Generate forward (A) and reverse dns (PTR) records using python.

A simple script to automate rdns creation.

Usage:
python3 rdns-cidr.py -cidr 1.1.1.0/24 -host {reverseIP}.srv.imgay.host -F -R

By adding -F and -R we generate forward and reverse dns entries.
