%define name xskat 
%define version 4.0
%define release %mkrel 10

Summary: The card game Skat as defined by the official Skat Order
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.gulu.net/xskat/%{name}-%{version}.tar.bz2
License: GPL
Group: Games/Cards
BuildRoot: %{_tmppath}/%{name}-buildroot
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
%configure2_5x --bindir=%_gamesbindir
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT{%{_gamesbindir},%{_mandir}/{man1,de/man1},%{_menudir}}
install xskat $RPM_BUILD_ROOT%{_gamesbindir}
install xskat.man $RPM_BUILD_ROOT%{_mandir}/man1/xskat.1
install xskat-de.man $RPM_BUILD_ROOT%{_mandir}/de/man1/xskat.1

mkdir -p %buildroot%_iconsdir
convert icon.xbm %buildroot%_iconsdir/%name.png
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%_datadir/applications/mandriva*
%_iconsdir/%name.png
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%doc README* CHANGE*





%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.0-10mdv2011.0
+ Revision: 615736
- the mass rebuild of 2010.1 packages

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 4.0-9mdv2010.1
+ Revision: 508757
- simplify BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 4.0-8mdv2009.0
+ Revision: 262914
- fix build (wrongly broken in r148455 on 2008-01-11)
- rebuild
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4.0-5mdv2008.1
+ Revision: 130553
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 4.0-4mdv2007.0
- fix buildrequires
- xdg menu

* Sun Mar 05 2006 Olivier Thauvin <nanardon@mandriva.org> 4.0-3mdk
- rebuild

* Fri Feb 18 2005 Götz Waschk <waschk@linux-mandrake.com> 4.0-2mdk
- fix menu
- drop prefix
- fix buildrequires

* Sat May 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.0-1mdk
- 4.0
- fix url

* Sat Jan 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.4-3mdk
- birthday rebuild
- s//usr/bin//usr/games/g

