Summary:	EFL Terminal Emulator
Name:		terminology
Version:	0.4.0
Release:	1
License:	BSD
Group:		Terminals
URL:		http://www.enlightenment.org/
Source:		http://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.bz2
# Non-devel packages are needed to compile themes
BuildRequires:	e
BuildRequires:	ecore
BuildRequires:	eet
BuildRequires:	edje
BuildRequires:	elementary
BuildRequires:	emotion
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(ecore-imf)
BuildRequires:	pkgconfig(ecore-imf-evas)
BuildRequires:	pkgconfig(ecore-input)
BuildRequires:	pkgconfig(ecore-ipc)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(eldbus)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(ethumb_client)
BuildRequires:	pkgconfig(evas)
Requires:	edje
Requires:	elementary
Requires:	emotion
Requires:	ethumb

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

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

