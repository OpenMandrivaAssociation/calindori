%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit 6a433437347f738eddcdd9e10bf16a76ef81b1fc

Name:		calindori
Version:	25.08.2
Release:	%{?git:0.%{git}.}1
Summary:	Calendar and todo management application for Plasma Mobile
%if 0%{?git}
Source0:        https://invent.kde.org/plasma-mobile/calindori/-/archive/%{gitbranch}/calindori-%{gitbranchd}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/calindori-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(PkgConfig)

%rename plasma6-calindori

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Calendar and todo management application for Plasma Mobile.

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.kde.calindac.desktop
%{_bindir}/calindac
%{_bindir}/calindori
%{_datadir}/applications/org.kde.calindori.desktop
%{_datadir}/icons/hicolor/scalable/apps/calindori.svg
%{_datadir}/knotifications6/calindac.notifyrc
%{_datadir}/dbus-1/services/org.kde.calindac.service
%{_datadir}/metainfo/org.kde.calindori.appdata.xml
