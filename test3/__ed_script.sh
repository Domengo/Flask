#!/bin/bash

cd '/usercode'

sh -c "cp -r /usercode/* /usr/local/educative " >> '/usercode/__ed_stdout.txt' 2>> '/usercode/__ed_stderr.txt'
exit 0