Summary:	Minimalistic plugin API for video effects - common package
Summary(pl.UTF-8):	Minimalistyczne API wtyczek efektów wideo - wspólny pakiet
Name:		frei0r
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://piksel.no/frei0r/releases/%{name}-plugins-%{version}.tar.gz
# Source0-md5:	a2eb63feeeb0c5cf439ccca276cbf70c
URL:		http://frei0r.org/
BuildRequires:	gavl-devel >= 0.2.3
BuildRequires:	opencv-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frei0r is a minimalistic plugin API for video effects. The main
emphasis is on simplicity for an API that will round up the most
common video effects into simple filters, sources and mixers that can
be controlled by parameters.

This is common package for all Frei0r plugins.

%description -l pl.UTF-8
Frei0r to minimalistyczne API wtyczek efektów wideo. Główny nacisk
położony jest na prostotę API, które będzie zamykało większość
popularnych efektów graficznych w proste filtry, źródła i miksery,
które można sterować parametrami.

Ten pakiet jest wspólny dla wszystkich wtyczek Frei0r.

%package plugins
Summary:	Base set of Frei0r plugins
Summary(pl.UTF-8):	Podstawowy zestaw wtyczek Frei0r
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugins
Base set of Frei0r plugins.

%description plugins -l pl.UTF-8
Podstawowy zestaw wtyczek Frei0r.

%package devel
Summary:	Minimalistic plugin API for video effects - development files
Summary(pl.UTF-8):	Minimalistyczne API wtyczek efektów wideo - pliki programistyczne
Group:		Development/Libraries
# doesn't require base

%description devel
Frei0r is a minimalistic plugin API for video effects. The main
emphasis is on simplicity for an API that will round up the most
common video effects into simple filters, sources and mixers that can
be controlled by parameters.

This package contains the Frei0r API header file.

%description devel -l pl.UTF-8
Frei0r to minimalistyczne API wtyczek efektów wideo. Główny nacisk
położony jest na prostotę API, które będzie zamykało większość
popularnych efektów graficznych w proste filtry, źródła i miksery,
które można sterować parametrami.

Ten pakiet zawiera plik nagłówkowy API Frei0r.

%prep
%setup -q

%build
# --enable-cpuflags (default) detects MMX/SSE/SSE2/SSSE3 basing on /proc/cpuinfo on build host
%configure \
	--disable-cpuflags
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/frei0r-1

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/frei0r-1/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/frei0r.h
%{_pkgconfigdir}/frei0r.pc
