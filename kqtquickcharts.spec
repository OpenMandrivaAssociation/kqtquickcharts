Summary:	Qt Quick plugin to render beautiful and interactive charts
Name:		kqtquickcharts
Version:	4.14.1
Release:	1
License:	LGPLv2.1+
Group:		Development/KDE and Qt
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
Qt Quick plugin to render beautiful and interactive charts.

%files
%doc COPYING AUTHORS
%dir %{_kde_libdir}/kde4/imports/org/kde/charts
%{_kde_libdir}/kde4/imports/org/kde/charts/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.2-1
- Initial package
