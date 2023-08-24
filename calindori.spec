%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200710
#define commit 5a433437347f738eddcdd9e10bf16a75ef81b1fc

Name:		calindori
Version:	23.08.0
Release:	%{?git:0.%{git}.}1
Summary:	Calendar and todo management application for Plasma Mobile
%if 0%{?git}
Source0:        https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(PkgConfig)

%description
Calendar and todo management application for Plasma Mobile.

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang calindac
%find_lang calindori

%files -f calindac.lang -f calindori.lang
%{_sysconfdir}/xdg/autostart/org.kde.calindac.desktop
%{_bindir}/calindac
%{_bindir}/calindori
%{_datadir}/applications/org.kde.calindori.desktop
%{_datadir}/icons/hicolor/scalable/apps/calindori.svg
%{_datadir}/knotifications5/calindac.notifyrc
%{_datadir}/dbus-1/services/org.kde.calindac.service
%{_datadir}/metainfo/org.kde.calindori.appdata.xml
