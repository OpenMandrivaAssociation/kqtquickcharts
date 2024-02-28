Summary:	Qt Quick plugin to render beautiful and interactive charts
Name:		kqtquickcharts
Version:	24.02.0
Release:	1
License:	LGPLv2.1+
Group:		Development/KDE and Qt
Url:		http://edu.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)

%description
Qt Quick plugin to render beautiful and interactive charts.

%files
%doc COPYING AUTHORS
%dir %{_libdir}/qt5/qml/org/kde/charts
%{_includedir}/KF5/kqtquickcharts_version.h
%{_libdir}/cmake/KQtQuickCharts/KQtQuickChartsVersion.cmake
%{_libdir}/cmake/KQtQuickCharts/KQtQuickChartsConfig.cmake
%{_libdir}/qt5/qml/org/kde/charts/*.qml
%{_libdir}/qt5/qml/org/kde/charts/libkqtquickcharts.so
%{_libdir}/qt5/qml/org/kde/charts/qmldir

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
