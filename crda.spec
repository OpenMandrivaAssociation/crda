Name:		crda
Version:	1.1.3
Release:	2
Summary:	Software to upload wireless regulatory information into kernel
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source0:	http://wireless.kernel.org/download/crda/crda-%{version}.tar.bz2
Requires:	udev
Requires:	wireless-regdb
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	python-m2crypto
BuildRequires:	wireless-regdb

%description
CRDA acts as the udev helper for communication between the kernel and
userspace for regulatory compliance. It relies on nl80211 for
communication. CRDA is intended to be run only through udev
communication from the kernel. The user should never have to run it
manually except if debugging udev issues.

%prep
%setup -q
#% patch0 -p2

%build
export CFLAGS="%{optflags}"
%make 
#CFLAGS="%{optflags}" V=1

%install
%makeinstall_std
mkdir -p %{buildroot}%{_prefix}/lib/crda

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%dir %{_prefix}/lib/crda
%{_mandir}/man8/crda.8*
%{_mandir}/man8/regdbdump.8*
/lib/udev/rules.d/85-regulatory.rules
%defattr(0755,root,root,0755)
/sbin/crda
/sbin/regdbdump
