Summary:	Qt Quick plugin to render beautiful and interactive charts
Name:		kqtquickcharts
Version:	16.12.2
Release:	1
License:	LGPLv2.1+
Group:		Development/KDE and Qt
Url:		http://edu.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

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
