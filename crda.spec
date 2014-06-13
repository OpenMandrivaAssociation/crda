Summary:	Software to upload wireless regulatory information into kernel
Name:		crda
Version:	1.1.3
Release:	9
License:	ISC
Group:		System/Configuration/Hardware
Url:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source0:	http://wireless.kernel.org/download/crda/%{name}-%{version}.tar.bz2

BuildRequires:	python-m2crypto
BuildRequires:	wireless-regdb
BuildRequires:	pkgconfig(libgcrypt)
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

%build
export CFLAGS="%{optflags}"
%make 

%install
%makeinstall_std
mkdir -p %{buildroot}%{_prefix}/lib/crda

%files
%doc LICENSE
%dir %{_prefix}/lib/crda
%{_mandir}/man8/crda.8*
%{_mandir}/man8/regdbdump.8*
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump

