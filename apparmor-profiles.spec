%define rev 1351

Summary:	Base AppArmor profiles
Name:		apparmor-profiles
Version:	2.3
Release:	%mkrel 1.%{rev}.4
License:	GPL
Group:		System/Base
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
Source0:	%{name}-%{version}-%{rev}.tar.gz
Source1:	usr.sbin.slapd.apparmor
Patch:		apparmor-profiles-2.1.2-1091-avahi.patch
Patch1:		apparmor-profiles-2.1.2-1091-nscd.patch
Requires:	apparmor-parser
Requires(post):	apparmor-parser
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Buildarch:	noarch

%description
AppArmor is a security framework that proactively protects the operating system
and applications.

This package contains the basic AppArmor profiles (aka security policy).

%prep
%setup -q
# no backup as it touches a profile and they all get copied during %%install
%patch -p1
%patch1 -p1
install -m 0644 %{SOURCE1} apparmor/profiles/extras/usr.sbin.slapd

%install
rm -rf %{buildroot}

%{makeinstall_std} EXTRASDIR=%{buildroot}%{_sysconfdir}/apparmor/profiles/extras

# remove profiles shipped elsewhere
rm -f   %{buildroot}%{_sysconfdir}/apparmor.d/sbin.rpcbind \
        %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.traceroute \
        %{buildroot}%{_sysconfdir}/apparmor.d/bin.ping \
        %{buildroot}%{_sysconfdir}/apparmor.d/bin.netstat \
        %{buildroot}%{_sysconfdir}/apparmor.d/sbin.syslogd \
        %{buildroot}%{_sysconfdir}/apparmor.d/sbin.klogd \
        %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.ntpd

%posttrans
/sbin/service apparmor condreload

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor.d
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.*
%config(noreplace) %{_sysconfdir}/apparmor.d/sbin.*
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/program-chunks
%dir %{_sysconfdir}/apparmor.d/tunables
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/*
%config(noreplace) %{_sysconfdir}/apparmor.d/program-chunks/*
%config(noreplace) %{_sysconfdir}/apparmor.d/tunables/*
%dir %{_sysconfdir}/apparmor
%dir %{_sysconfdir}/apparmor/profiles
%dir %{_sysconfdir}/apparmor/profiles/extras
%{_sysconfdir}/apparmor/profiles/extras/README
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/usr.*
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/etc.*
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/sbin.*
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/bin.*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-1.1351.4mdv2011.0
+ Revision: 609987
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-1.1351.3mdv2010.1
+ Revision: 521353
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3-1.1351.2mdv2010.0
+ Revision: 413034
- rebuild

* Sat Jan 03 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.3-1.1351.1mdv2009.1
+ Revision: 323495
- Updated to r1351 (as shipped by SuSE 11.1).

* Wed Aug 06 2008 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 2.3-1.1245.1mdv2009.0
+ Revision: 264713
- updated to version 2.3 svnrev 1245

* Fri Mar 14 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.7mdv2008.1
+ Revision: 187850
- fix nscd profile (reported by Vincent Panel <yohonet@gmail.com>)

* Thu Mar 06 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.6mdv2008.1
+ Revision: 181085
- avahi-daemon profile: allow it to read /etc/lsb-release

* Fri Feb 29 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.5mdv2008.1
+ Revision: 176831
- include a writable slapd.d rule in openldap's profile
- let openldap read the rootcerts

* Fri Feb 29 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.4mdv2008.1
+ Revision: 176818
- included initial profile for openldap (slapd)

* Thu Feb 28 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.3mdv2008.1
+ Revision: 176451
- drop syslog profile patch: we are no longer shipping that profile here (it's in the syslog package)

* Thu Feb 28 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.2mdv2008.1
+ Revision: 176375
- remove profiles that are shipped elsewhere

* Wed Feb 27 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1091.1mdv2008.1
+ Revision: 175858
- re-added forgotten syslogd profile patch
- rpcbind needs setgid too
- updated apparmor-profiles to 2.1.2-1091
- copied to apparmor-profiles
- apparmor-parser updated to 2.1.2-1088
- apparmor becomes apparmor-parser

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1-1.1076.2mdv2008.1
+ Revision: 154124
- rebuild for new perl

* Tue Jan 08 2008 Andreas Hasenack <andreas@mandriva.com> 2.1-1.1076.1mdv2008.1
+ Revision: 146893
- updated to svn revision 1076

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Andreas Hasenack <andreas@mandriva.com> 2.1-1.961.5mdv2008.0
+ Revision: 91191
- remove more profiles from standard package: they are shipped in their own packages now

* Wed Sep 19 2007 Andreas Hasenack <andreas@mandriva.com> 2.1-1.961.4mdv2008.0
+ Revision: 91061
- drop rpcbind profile, it's shipped in the rpcbind package now

* Fri Sep 14 2007 Andreas Hasenack <andreas@mandriva.com> 2.1-1.961.3mdv2008.0
+ Revision: 85766
- bonobo file is under a noarch libdir
- build dbus and gnome applet packages

* Fri Sep 14 2007 Andreas Hasenack <andreas@mandriva.com> 2.1-1.961.1mdv2008.0
+ Revision: 85546
- install perl module in arch dir as the makefile does for x86_64 (doesn't seem right, though)
- make it not require an installed libapparmor-devel to build
- added swig to buildrequires
- added profile for rpcbind
- fix default syslog profile
- obsolete apparmor-docs (manpages are in each package now)
- better place for the LibAppArmor module
- build apache-mod_apparmor package
- install LibAppArmor.pm
- added utils subpackage
- Import apparmor

