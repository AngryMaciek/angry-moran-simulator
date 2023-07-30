#!/bin/bash

# create a non-root user "user" passed from the command line (or fallback);
# set shell, home, conda group, init conda;
# exec the rest (CMD) as "user"
# ~AngryMaciek

ID=${HOSTUID:-9001}
useradd --shell /bin/bash -u $ID -o -c "" -m user
export HOME=/home/user
adduser user conda &> /dev/null
/usr/sbin/gosu user /bin/bash -c "/mambaforge/bin/conda init bash &> /dev/null"
exec /usr/sbin/gosu user "$@"
