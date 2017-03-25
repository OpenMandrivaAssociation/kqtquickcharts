Summary:	Qt Quick plugin to render beautiful and interactive charts
Name:		kqtquickcharts
Version:	17.03.80
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
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)

%description
Qt Quick plugin to render beautiful and interactive charts.

%files
%doc COPYING AUTHORS
%{_includedir}/KF5/kqtquickcharts_version.h
%{_libdir}/cmake/KQtQuickCharts/KQtQuickChartsVersion.cmake
%{_libdir}/qml/org/kde/charts/BarChart.qml
%{_libdir}/qml/org/kde/charts/Label.qml
%{_libdir}/qml/org/kde/charts/LegendItem.qml
%{_libdir}/qml/org/kde/charts/LineChart.qml
%{_libdir}/qml/org/kde/charts/LineLabel.qml
%{_libdir}/qml/org/kde/charts/XYChart.qml
%{_libdir}/qml/org/kde/charts/libkqtquickcharts.so
%{_libdir}/qml/org/kde/charts/qmldir


#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
