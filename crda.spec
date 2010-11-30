Name:		crda
Version:	1.1.1
Release:	%mkrel 2
Summary:	Software to upload wireless regulatory information into kernel
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory/CRDA
Source:		http://wireless.kernel.org/download/crda/crda-%{version}.tar.bz2
Requires:	udev
Requires:	wireless-regdb
BuildRequires:	libgcrypt-devel
BuildRequires:	libnl-devel
BuildRequires:	python-m2crypto
BuildRequires:	wireless-regdb
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CRDA acts as the udev helper for communication between the kernel and
userspace for regulatory compliance. It relies on nl80211 for
communication. CRDA is intended to be run only through udev
communication from the kernel. The user should never have to run it
manually except if debugging udev issues.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" V=1

%install
rm -rf %{buildroot}
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
