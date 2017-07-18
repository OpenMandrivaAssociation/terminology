%define	efl_version 1.19.1
Summary:	EFL Terminal Emulator
Name:		terminology
Version:	1.0.0
Release:	1
License:	BSD
Group:		Terminals
URL:		https://www.enlightenment.org/
Source:		https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
# Non-devel packages are needed to compile themes
BuildRequires:	e
#BuildRequires:	ecore
#BuildRequires:	eet
#BuildRequires:	edje
#BuildRequires:	elementary
#BuildRequires:	emotion
BuildRequires:	pkgconfig(ecore) => %{efl_version}
BuildRequires:	pkgconfig(ecore-evas) => %{efl_version}
BuildRequires:	pkgconfig(ecore-file) => %{efl_version}
BuildRequires:	pkgconfig(ecore-imf) => %{efl_version}
BuildRequires:	pkgconfig(ecore-imf-evas) => %{efl_version}
BuildRequires:	pkgconfig(ecore-input) => %{efl_version}
BuildRequires:	pkgconfig(ecore-ipc) => %{efl_version}
BuildRequires:	pkgconfig(edje) => %{efl_version}
BuildRequires:	pkgconfig(eet) => %{efl_version}
BuildRequires:	pkgconfig(efreet) => %{efl_version}
BuildRequires:	pkgconfig(eina) => %{efl_version}
BuildRequires:	pkgconfig(eldbus) => %{efl_version}
BuildRequires:	pkgconfig(elementary) => 0.21.7
BuildRequires:	pkgconfig(emotion) => %{efl_version}
BuildRequires:	pkgconfig(ethumb_client) => %{efl_version}
BuildRequires:	pkgconfig(evas) => %{efl_version}
BuildRequires:	pkgconfig(efl) => %{efl_version}
Conflicts:	evas_generic_loaders <= 1.13.2
Conflicts:	pm-utils
Requires:	efl => %{efl_version}
Requires:	edje => %{efl_version}
Requires:	elementary => 0.21.7
Requires:	emotion => %{efl_version}
Requires:	ethumb => %{efl_version}

%description
EFL Terminal Emulator.

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_bindir}/ty*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/%{name}.png
%{_mandir}/man1/%{name}.1.*
%{_localedir}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}