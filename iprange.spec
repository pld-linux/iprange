Summary:	iprange utility
Name:		iprange
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	https://firehol.org/download/iprange/releases/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	bab3b7d03b95beb15247b9279a44e358
URL:		https://firehol.org
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iprange - manage IP ranges.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md COPYING
%attr(755,root,root) %{_bindir}/iprange
