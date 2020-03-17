%define snapshot 20200312
%define commit c0288562a5dd7a9964f6e0f3bd571e002f6b9152

Name:		calindori
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	Calendar and todo management application for Plasma Mobile
Source0:	https://invent.kde.org/kde/calindori/-/archive/master/calindori-%{snapshot}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
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
BuildRequires:	cmake(PkgConfig)

%description
Calendar and todo management application for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-master-%{commit}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/autostart/org.kde.calindac.desktop
%{_bindir}/calindac
%{_bindir}/calindori
%{_datadir}/applications/org.kde.phone.calindori.desktop
%{_datadir}/dbus-1/interfaces/org.kde.calindac.xml
%{_datadir}/icons/hicolor/scalable/apps/calindori.svg
%{_datadir}/knotifications5/calindac.notifyrc
%{_datadir}/metainfo/org.kde.phone.calindori.appdata.xml
