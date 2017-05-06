Summary:	Software to upload wireless regulatory information into kernel
Name:		crda
Version:	3.18
Release:	3
License:	ISC
Group:		System/Configuration/Hardware
Url:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source0:	https://www.kernel.org/pub/software/network/crda/%{name}-%{version}.tar.xz
# From Fedora.
# This script sets regulatory domain for a country based on the 
# current time zone.
# '/usr/sbin/iw' was replaced with just 'iw'.
Source1:	setregdomain
Source2:	setregdomain.1
# Adapted from Fedora
# Add udev rule to call setregdomain on wireless device add.
Patch0:		regulatory-rules-setregdomain.patch
Patch1:		crda-3.18-no-ldconfig.patch
Patch2:		crda-3.18-no-werror.patch
Patch3:		crda-3.18-openssl.patch
Patch4:		crda-3.18-cflags.patch
Patch5:		crda-3.18-libreg-link.patch
Patch6:		crda-3.18-remove-not-needed-headers.patch
BuildRequires:	python-m2crypto
BuildRequires:	wireless-regdb
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libnl-3.0)
Requires:	udev
Requires:	wireless-regdb

%description
CRDA acts as the udev helper for communication between the kernel and
userspace for regulatory compliance. It relies on nl80211 for
communication. CRDA is intended to be run only through udev
communication from the kernel. The user should never have to run it
manually except if debugging udev issues.

%package devel
Summary:	Header files for use with libreg from CRDA
Group:		Development/C

%description devel
Header files to make use of libreg for accessing regulatory info.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
sed -i -e 's|^#!/usr/bin/env python|#!%{__python2}|' utils/key2pub.py

make CC=%{__cc} PREFIX=%{_prefix} SBINDIR=%{_sbindir} LIBDIR=%{_libdir} WERROR= USE_OPENSSL=1

%install
%makeinstall_std MANDIR=%{_mandir}/ SBINDIR=%{_sbindir}/ LIBDIR=%{_libdir}/ USE_OPENSSL=1
mkdir -p %{buildroot}%{_prefix}/lib/crda
install -D -pm 0755 %{SOURCE1} %{buildroot}%{_sbindir}
install -D -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/setregdomain.1

#Just in case any applications need crda exactly in /sbin
mkdir -p %{buildroot}/sbin/
ln -s %{_sbindir}/crda %{buildroot}/sbin/

%check
make USE_OPENSSL=1 CC="%{__cc}" verify

%files
%doc LICENSE
%dir %{_prefix}/lib/crda
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man8/crda.8*
%{_mandir}/man8/regdbdump.8*
/lib/udev/rules.d/85-regulatory.rules
# A symlink, in case any applications still need crda in /sbin
/sbin/crda
%{_sbindir}/crda
%{_sbindir}/regdbdump
%{_sbindir}/setregdomain
%{_libdir}/libreg.so

%files devel
%{_includedir}/reglib/nl80211.h
%{_includedir}/reglib/regdb.h
%{_includedir}/reglib/reglib.h
