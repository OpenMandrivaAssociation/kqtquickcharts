Summary:	Qt Quick plugin to render beautiful and interactive charts
Name:		kqtquickcharts
Version:	15.12.3
Release:	2
License:	LGPLv2.1+
Group:		Development/KDE and Qt
Url:		http://edu.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

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
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
