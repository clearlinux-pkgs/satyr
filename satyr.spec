#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : satyr
Version  : 0.31
Release  : 36
URL      : https://github.com/abrt/satyr/archive/0.31/satyr-0.31.tar.gz
Source0  : https://github.com/abrt/satyr/archive/0.31/satyr-0.31.tar.gz
Summary  : Automatic problem management with anonymous reports
Group    : Development/Tools
License  : GPL-2.0
Requires: satyr-bin = %{version}-%{release}
Requires: satyr-lib = %{version}-%{release}
Requires: satyr-license = %{version}-%{release}
Requires: satyr-man = %{version}-%{release}
Requires: satyr-python = %{version}-%{release}
Requires: satyr-python3 = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : doxygen
BuildRequires : gperf
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libunwind-coredump)
BuildRequires : pkgconfig(nettle)
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
Requires: satyr-license = %{version}-%{release}

%description bin
bin components for the satyr package.


%package dev
Summary: dev components for the satyr package.
Group: Development
Requires: satyr-lib = %{version}-%{release}
Requires: satyr-bin = %{version}-%{release}
Provides: satyr-devel = %{version}-%{release}
Requires: satyr = %{version}-%{release}

%description dev
dev components for the satyr package.


%package lib
Summary: lib components for the satyr package.
Group: Libraries
Requires: satyr-license = %{version}-%{release}

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
Requires: satyr-python3 = %{version}-%{release}

%description python
python components for the satyr package.


%package python3
Summary: python3 components for the satyr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the satyr package.


%prep
%setup -q -n satyr-0.31
cd %{_builddir}/satyr-0.31

%build
## build_prepend content
export CFLAGS="$CFLAGS -fcommon"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597873661
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static --without-python2
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1597873661
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/satyr
cp %{_builddir}/satyr-0.31/COPYING %{buildroot}/usr/share/package-licenses/satyr/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsatyr.so.4
/usr/lib64/libsatyr.so.4.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/satyr/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/satyr.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
