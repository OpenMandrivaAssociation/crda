Name:		crda
Version:	1.1.2
Release:	2
Summary:	Software to upload wireless regulatory information into kernel
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source:		http://wireless.kernel.org/download/crda/crda-%{version}.tar.bz2
BuildRequires:	libgcrypt-devel
BuildRequires:	libnl3-devel
BuildRequires:	python-m2crypto
BuildRequires:	wireless-regdb
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
# (tpg) use libnl3
sed -i -e 's#NLLIBS += -lnl-genl#NLLIBS += -lnl-genl-3#g' Makefile

%setup_compile_flags
%make V=1

%install
%makeinstall_std
mkdir -p %{buildroot}%{_prefix}/lib/crda

%files
%doc LICENSE
%dir %{_prefix}/lib/crda
%{_mandir}/man8/crda.8*
%{_mandir}/man8/regdbdump.8*
/lib/udev/rules.d/85-regulatory.rules
%defattr(0755,root,root,0755)
/sbin/crda
/sbin/regdbdump
