Summary:	Software to upload wireless regulatory information into kernel
Name:		crda
Version:	3.18
Release:	1
License:	ISC
Group:		System/Configuration/Hardware
Url:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source0:	https://www.kernel.org/pub/software/network/crda/%{name}-%{version}.tar.xz
Source1:	keys-ssl.c
Patch0:		crda-3.18-fix-makefile.patch
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

%prep
%setup -q
%apply_patches
cp %{SOURCE1} .

%build
%setup_compile_flags

make CC=%{__cc} USE_OPENSSL=1

%install
%makeinstall_std USE_OPENSSL=1
mkdir -p %{buildroot}%{_prefix}/lib/crda

%check
make USE_OPENSSL=1 CC="%{__cc}" verify

%files
%doc LICENSE
%dir %{_prefix}/lib/crda
%{_mandir}/man8/crda.8*
%{_mandir}/man8/regdbdump.8*
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump

