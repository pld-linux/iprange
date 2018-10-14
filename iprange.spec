Summary:	iprange utility
Name:		iprange
Version:	1.0.4
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	https://github.com/firehol/iprange/releases/download/v1.0.4/%{name}-%{version}.tar.xz
# Source0-md5:	f3126b8c239eaa51d79591748f091c7b
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
%doc ChangeLog README.md COPYING
%attr(755,root,root) %{_bindir}/iprange
%{_mandir}/man1/iprange.1*
