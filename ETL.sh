#!/bin/bash

./oc_bin/oc version
echo $oct 
echo $ocs
./oc_bin/oc login --token=$oct --server=$ocs
./oc_bin/oc project $ocp
./oc_bin/oc port-forward $ocpd $ocpf:$ocpt &


python3 src/main.py $test_mode