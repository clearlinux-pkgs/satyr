#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : satyr
Version  : 0.26
Release  : 15
URL      : https://github.com/abrt/satyr/archive/0.26.tar.gz
Source0  : https://github.com/abrt/satyr/archive/0.26.tar.gz
Summary  : Automatic problem management with anonymous reports
Group    : Development/Tools
License  : GPL-2.0
Requires: satyr-bin
Requires: satyr-python3
Requires: satyr-lib
Requires: satyr-license
Requires: satyr-man
Requires: satyr-python
BuildRequires : Sphinx
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : pkgconfig(python)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(rpm)
BuildRequires : popt-dev

%description
Failures of computer programs are omnipresent in the information technology
industry: they occur during software development, software testing, and also in
production.  Failures occur in programs from all levels of the system stack.
The program environment differ substantially between kernel space, user space
programs written in C or C++, Python scripts, and Java applications, but the
general structure of failures is surprisingly similar between the mentioned
environments due to imperative nature of the languages and common concepts such
as procedures, objects, exceptions.

%package bin
Summary: bin components for the satyr package.
Group: Binaries
Requires: satyr-license
Requires: satyr-man

%description bin
bin components for the satyr package.


%package dev
Summary: dev components for the satyr package.
Group: Development
Requires: satyr-lib
Requires: satyr-bin
Provides: satyr-devel

%description dev
dev components for the satyr package.


%package lib
Summary: lib components for the satyr package.
Group: Libraries
Requires: satyr-license

%description lib
lib components for the satyr package.


%package license
Summary: license components for the satyr package.
Group: Default

%description license
license components for the satyr package.


%package man
Summary: man components for the satyr package.
Group: Default

%description man
man components for the satyr package.


%package python
Summary: python components for the satyr package.
Group: Default
Requires: satyr-python3

%description python
python components for the satyr package.


%package python3
Summary: python3 components for the satyr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the satyr package.


%prep
%setup -q -n satyr-0.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533053391
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1533053391
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/satyr
cp COPYING %{buildroot}/usr/share/doc/satyr/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/satyr

%files dev
%defattr(-,root,root,-)
/usr/include/satyr/abrt.h
/usr/include/satyr/core/fingerprint.h
/usr/include/satyr/core/frame.h
/usr/include/satyr/core/stacktrace.h
/usr/include/satyr/core/thread.h
/usr/include/satyr/core/unwind.h
/usr/include/satyr/deb.h
/usr/include/satyr/distance.h
/usr/include/satyr/frame.h
/usr/include/satyr/gdb/frame.h
/usr/include/satyr/gdb/sharedlib.h
/usr/include/satyr/gdb/stacktrace.h
/usr/include/satyr/gdb/thread.h
/usr/include/satyr/java/frame.h
/usr/include/satyr/java/stacktrace.h
/usr/include/satyr/java/thread.h
/usr/include/satyr/js/frame.h
/usr/include/satyr/js/platform.h
/usr/include/satyr/js/stacktrace.h
/usr/include/satyr/json.h
/usr/include/satyr/koops/frame.h
/usr/include/satyr/koops/stacktrace.h
/usr/include/satyr/location.h
/usr/include/satyr/normalize.h
/usr/include/satyr/operating_system.h
/usr/include/satyr/python/frame.h
/usr/include/satyr/python/stacktrace.h
/usr/include/satyr/report.h
/usr/include/satyr/report_type.h
/usr/include/satyr/rpm.h
/usr/include/satyr/ruby/frame.h
/usr/include/satyr/ruby/stacktrace.h
/usr/include/satyr/stacktrace.h
/usr/include/satyr/strbuf.h
/usr/include/satyr/thread.h
/usr/include/satyr/utils.h
/usr/lib64/libsatyr.so
/usr/lib64/pkgconfig/satyr.pc
/usr/share/man/man3/satyr-python.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsatyr.so.3
/usr/lib64/libsatyr.so.3.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/satyr/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/satyr.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
