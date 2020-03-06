Summary:	Raft consensus protocol library
Name:		raft
Version:	0.9.17
Release:	1
License:	LGPLv3
Group:		Libraries
Source0:	https://github.com/canonical/raft/archive/v%{version}.tar.gz
# Source0-md5:	7e3cfa6682d12646f8f3df3350a64b73
URL:		https://github.com/canonical/raft
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fully asynchronous C implementation of the Raft consensus protocol.

The library has modular design: its core part implements only the core
Raft algorithm logic, in a fully platform independent way. On top of
that, a pluggable interface defines the I/O implementation for
networking (send/receive RPC messages) and disk persistence (store log
entries and snapshots).

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite3-devel(wal_replication)

%description devel
This package contains development files for the %{name} library.

%package static
Summary:	Static libraries for %{name} development
Summary(pl.UTF-8):	Statyczne biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static %{name} library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libraft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraft.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraft.so
%{_libdir}/libraft.la
%{_includedir}/raft.h
%dir %{_includedir}/raft
%{_includedir}/raft/*.h
%{_pkgconfigdir}/raft.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libraft.a
