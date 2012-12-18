Summary:	EFL Terminal Emulator
Name:		terminology
Version:	0.2.0
Release:	1
License:	BSD
Group:		Terminals
URL:		http://www.enlightenment.org/
Source:		http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Non-devel packages are needed to compile themes
BuildRequires:	e
BuildRequires:	ecore
BuildRequires:	eet
BuildRequires:	edje
BuildRequires:	elementary
BuildRequires:	emotion
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
Requires:	edje
Requires:	elementary
Requires:	emotion


%description
EFL Terminal Emulator.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/%{name}.png
