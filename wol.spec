%define name wol
%define version 0.7.1
%define release  8

Summary: Wake On LAN client
Name: %name
Version: %version
Release: %release
Url: http://ahh.sourceforge.net/wol/
License : GPL
Group: Networking/Other
Source: %{name}-%{version}.tar.bz2
Buildroot: %_tmppath/%name-%version-buildroot

%description
wol implements Wake On LAN functionality in a small program. 
It wakes up hardware that is Magic Packet compliant.
Consider you have a sleeping or turned-off computer and you 
want to remotely wake him up. Just type wol MAC-ADDRESS and 
the host wakes up (OK, it will boot ;-). 

%prep

%setup -q

%build
#aclocal
#automake
%configure

%make

%install

rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}




%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(-,root,root)
#%doc COPYING INSTALL README 
%doc COPYING README 
%{_bindir}/*
%{_datadir}/info/*
%{_datadir}/man/man1/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7.1-6mdv2010.0
+ Revision: 434969
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.1-5mdv2009.0
+ Revision: 262124
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.1-4mdv2009.0
+ Revision: 256341
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.7.1-2mdv2008.1
+ Revision: 129443
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import wol


* Tue Aug 16 2005 Emmanuel Blindauer <mdk@agat.net> 0.7.1-2mdk
- yearly rebuild

* Fri Aug 13 2004 Emmanuel Blindauer <mdk@agat.net> 0.7.1-1mdk
- initial package



