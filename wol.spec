%define name wol
%define version 0.7.1
%define release %mkrel 2

Summary: Wake On LAN client
Name: %name
Version: %version
Release: %release
Url: http://ahh.sourceforge.net/wol/
License : GPL
Group: Networking/Other
Source: %{name}-%{version}.tar.bz2

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


%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(-,root,root)
#%doc COPYING INSTALL README 
%doc COPYING README 
%{_bindir}/*
%{_datadir}/info/*
%{_datadir}/man/man1/*


