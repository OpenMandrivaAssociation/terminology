%define	efl_version 1.26.1
Summary:	EFL Terminal Emulator
Name:		terminology
Version:	1.14.0
Release:	1
License:	BSD
Group:		Terminals
URL:		https://www.enlightenment.org/
Source:		https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
# Non-devel packages are needed to compile themes
BuildRequires:	e
BuildRequires:  meson
BuildRequires:	pkgconfig(efl) => %{efl_version}
Conflicts:	evas_generic_loaders <= 1.13.2
Conflicts:	pm-utils
Requires:	efl => %{efl_version}
Requires:	e

%description
EFL Terminal Emulator.

%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_bindir}/ty*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/man/man1/terminology-helpers.1.*
%{_datadir}/man/man1/tyalpha.1.*
%{_datadir}/man/man1/tybg.1.*
%{_datadir}/man/man1/tycat.1.*
%{_datadir}/man/man1/tyls.1.*
%{_datadir}/man/man1/typop.1.*
%{_datadir}/man/man1/tyq.1.*
%{_datadir}/man/man1/tysend.1.*
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*
%{_localedir}*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%meson

%build
%meson_build

%install
%meson_install

#find_lang %{name}
