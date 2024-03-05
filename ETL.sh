#!/bin/bash

./oc_bin/oc version
echo $oct 
echo $ocs

./oc_bin/oc login $ocs --token=$oct --insecure-skip-tls-verify=true
./oc_bin/oc project $ocp
export postgresPod=$(./oc_bin/oc get pods | grep database | awk '{print $1}')
echo $postgresPod
./oc_bin/oc port-forward $postgresPod $ocpf:$ocpt &


python3 src/main.py $test_mode