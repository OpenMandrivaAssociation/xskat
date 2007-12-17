%define name xskat 
%define version 4.0
%define release %mkrel 5

Summary: The card game Skat as defined by the official Skat Order
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.gulu.net/xskat/%{name}-%{version}.tar.bz2
License: GPL
Group: Games/Cards
Url: http://www.xskat.de/xskat.html
BuildRequires: X11-devel
BuildRequires: rman gccmakedep
BuildRequires: ImageMagick
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
convert icon.xbm %buildroot%_iconsdir/%name.png
(cd $RPM_BUILD_ROOT
cat > ./%{_menudir}/%{name} <<EOF
?package(%{name}):\
needs="X11"\
title="Xskat"\
longtitle="The Skat game"\
command="%{_gamesbindir}/%{name}"\
section="More Applications/Games/Cards" \
icon="cards_section.png" xdg="true"
EOF
)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xskat
Comment=The Skat game
Exec=%{name}
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Cards;Game;CardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%_datadir/applications/mandriva*
%{_menudir}/%{name}
%_iconsdir/%name.png
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%doc README* CHANGE*



