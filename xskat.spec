%define debug_package %{nil}

Summary: The card game Skat as defined by the official Skat Order
Name: xskat
Version: 4.0
Release: 12
Source0: http://www.gulu.net/xskat/%{name}-%{version}.tar.bz2
Source1: http://www.xskat.de/skat_icon.png
License: GPL
Group: Games/Cards
Url: http://www.xskat.de/xskat.html
BuildRequires: pkgconfig(x11)
BuildRequires: rman gccmakedep
BuildRequires: imagemagick
BuildRequires: imake

%description
XSkat lets you play the card game Skat as defined by
the official Skat Order on any Un*x machine running X11.

Features

* Single- and multiplayer mode.
* Playing over LAN or IRC.
* Game lists and logs.
* Three types of scoring.
* English or German text.
* German or French suited cards.
* Different computer strategies.
* Pre-definable card distributions.
* Variations: Ramsch, Bock, Kontra & Re, ... 

%prep
%setup -q

%build
%configure --bindir=%_gamesbindir
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT{%{_gamesbindir},%{_mandir}/{man1,de/man1},%{_menudir}}
install xskat $RPM_BUILD_ROOT%{_gamesbindir}
install xskat.man $RPM_BUILD_ROOT%{_mandir}/man1/xskat.1
install xskat-de.man $RPM_BUILD_ROOT%{_mandir}/de/man1/xskat.1

mkdir -p %buildroot%_iconsdir
#convert icon.xbm %buildroot%_iconsdir/%name.png
install -c -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xskat
Comment=The Skat game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Cards;Game;CardGame;
EOF

%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%_datadir/applications/mandriva*
%_iconsdir/%name.png
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%doc README* CHANGE*
