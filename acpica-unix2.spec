#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : acpica-unix2
Version  : 20170629
Release  : 18
URL      : https://acpica.org/sites/acpica/files/acpica-unix2-20170629.tar.gz
Source0  : https://acpica.org/sites/acpica/files/acpica-unix2-20170629.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: acpica-unix2-bin
BuildRequires : bison
BuildRequires : flex

%description
/*
* Miscellaneous instructions for building and using the iASL compiler.
*/
Last update 9 December 2013.

%package bin
Summary: bin components for the acpica-unix2 package.
Group: Binaries

%description bin
bin components for the acpica-unix2 package.


%prep
%setup -q -n acpica-unix2-20170629

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1498773783
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1498773783
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/acpibin
/usr/bin/acpidump
/usr/bin/acpiexamples
/usr/bin/acpiexec
/usr/bin/acpihelp
/usr/bin/acpinames
/usr/bin/acpisrc
/usr/bin/acpixtract
/usr/bin/iasl
