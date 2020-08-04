#!/usr/bin/tclsh

set arch "x86_64"
set base "ahven-2.7"
set fileurl "https://www.ahven-framework.com/releases/ahven-2.7.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force ahven.gpr.gp.patch build/SOURCES
file copy -force ahven_tests.gpr.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb ahven.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz
