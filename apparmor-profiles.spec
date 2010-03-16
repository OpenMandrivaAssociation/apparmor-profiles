%define rev 1351

Summary:	Base AppArmor profiles
Name:		apparmor-profiles
Version:	2.3
Release:	%mkrel 1.%{rev}.3
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

