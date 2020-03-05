#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

mkdir -p ./{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cp build.sh SOURCES
spectool -g -C SOURCES fluent-bit-clickhouse.spec
rpmbuild --quiet --define "_topdir `pwd`" -bb fluent-bit-clickhouse.spec
