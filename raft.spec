Summary:	Raft consensus protocol library
Summary(pl.UTF-8):	Biblioteka protokołu consensusu Raft
Name:		raft
Version:	0.16.0
Release:	1
License:	LGPL v3 with exception
Group:		Libraries
#Source0Download: https://github.com/canonical/raft/releases
Source0:	https://github.com/canonical/raft/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	057709b57989c8880775d821ea9a1413
URL:		https://github.com/canonical/raft
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	libuv-devel >= 1.8.0
BuildRequires:	lz4-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.752
Requires:	libuv >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fully asynchronous C implementation of the Raft consensus protocol.

The library has modular design: its core part implements only the core
Raft algorithm logic, in a fully platform independent way. On top of
that, a pluggable interface defines the I/O implementation for
networking (send/receive RPC messages) and disk persistence (store log
entries and snapshots).

%description -l pl.UTF-8
W pełni asynchroniczna implementacja w C protokołu consensusu Raft.

Biblioteka jest zaprojektowana modułowo: główna część implementuje
tylko podstawową logikę algorytmu Raft w sposób w pełni niezależny od
platformy. Powyżej niej rozszerzalny interfejs definiuje implementację
we/wy warstwy sieciowej (wysyłanie/odbiór komunikatów RPC) oraz
przechowywanie na dysku (zapisywanie wpisów logu oraz migawek).

%package devel
Summary:	Header files for Raft library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Raft
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for the Raft library.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki nagłówkowe biblioteki Raft.

%package static
Summary:	Static libraries for Raft library
Summary(pl.UTF-8):	Statyczne biblioteki Raft
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static Raft library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę Raft.

%package apidocs
Summary:	API documentation for Raft library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Raft
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Raft library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Raft.

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libraft.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/libraft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraft.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraft.so
%{_includedir}/raft.h
%{_includedir}/raft
%{_pkgconfigdir}/raft.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libraft.a

%files apidocs
%defattr(644,root,root,755)
%doc docs/build/{_static,*.html,*.js}
