#
# spec file for package ahven
#

%define libname libahven
%define soname 27

Name:           ahven
Version:        2.7
Release:        2
Summary:        A unit testing framework for Ada Programming Language
License:        ISC
Group:          Development/Libraries
URL:            https://www.ahven-framework.com/
Source:         http://www.ahven-framework.com/releases/%{name}-%{version}.tar.gz
BuildRequires:  gcc-ada
BuildRequires:  make

%description
Ahven is a simple unit testing library (or a framework) for the Ada
programming language. It is loosely modeled after Junit and some ideas are
taken from Aunit.

Features:
· Simple API
· Small size (Ahven about has 3K SLOC)
· JUnit-compatible test results in XML format;
  this allows integration with tools like Jenkins or TeamCity.
  Strict coding style (enforced by AdaControl)
· Plain Ada 95 code, no Ada 2005 features used,
  but can be compiled as Ada 2005 or Ada 2012 code if needed
· Portable across different compilers and operating systems
· Permissive Open Source license (ISC)


%package -n %{libname}%{soname}
Summary:        Library files for Ahven
Group:          System/Libraries

%description -n %{libname}%{soname}
The %{libname}%{soname} package contains library files for Ahven.


%package devel
Summary:        Development files for Ahven
Requires:       %{name} = %{version}
Requires:       %{libname}%{soname} = %{version}

%description devel 
The %{name}-devel package contains source code and linking information for
developing applications that use Ahven.

%prep
%setup -q

%build
make prefix=/usr libdir=%{_libdir}

%install
make DESTDIR=%{buildroot} install

%check
make check

%post -n %{libname}%{soname} -p /sbin/ldconfig
%postun -n %{libname}%{soname} -p /sbin/ldconfig

%files -n %{libname}%{soname}
%{_libdir}/*.so.*

%files
%license LICENSE.txt
%doc README.rst ROADMAP NEWS.txt

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}
%dir /usr/share/gpr
/usr/share/gpr/ahven.gpr

%changelog

