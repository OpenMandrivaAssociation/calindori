#define snapshot 20200710
#define commit 5a433437347f738eddcdd9e10bf16a75ef81b1fc

Name:		calindori
Version:	21.08
Release:	1
Summary:	Calendar and todo management application for Plasma Mobile
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
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
%autosetup -p1
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
