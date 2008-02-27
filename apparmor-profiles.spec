%define rev 1091

Summary:	Base AppArmor profiles
Name:		apparmor-profiles
Version:	2.1.2
Release:	%mkrel 1.%{rev}.1
License:	GPL
Group:		System/Base
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
Source0:	%{name}-%{version}-%{rev}.tar.gz
Source1:	sbin.rpcbind
Patch:		apparmor-2.1-961-syslogd.patch
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
%patch -p0

%install
rm -rf %{buildroot}

%{makeinstall_std} EXTRASDIR=%{buildroot}%{_sysconfdir}/apparmor/profiles/extras
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/

%posttrans
/sbin/service apparmor condreload

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor.d
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.*
%config(noreplace) %{_sysconfdir}/apparmor.d/sbin.*
%config(noreplace) %{_sysconfdir}/apparmor.d/bin.*
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

