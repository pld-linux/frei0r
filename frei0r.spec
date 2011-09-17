#
# Conditional build:
%bcond_without	opencv		# build without OpenCV support
#
Summary:	Minimalistic plugin API for video effects - common package
Summary(pl.UTF-8):	Minimalistyczne API wtyczek efektów wideo - wspólny pakiet
Name:		frei0r
Version:	1.3
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://piksel.no/frei0r/releases/%{name}-plugins-%{version}.tar.gz
# Source0-md5:	a2eb63feeeb0c5cf439ccca276cbf70c
URL:		http://frei0r.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gavl-devel >= 0.2.3
BuildRequires:	libtool >= 2:2.0
%{?with_opencv:BuildRequires:	opencv-devel >= 1.0.0}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
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

%package plugins-gavl
Summary:	Frei0r plugins that use GAVL library
Summary(pl.UTF-8):	Wtyczki Frei0r wykorzystujące bibliotekę GAVL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gavl >= 0.2.3

%description plugins-gavl
Frei0r plugins that use GAVL library: scale0tilt, vectorscope,
rgbparade.

%description plugins-gavl -l pl.UTF-8
Wtyczki Frei0r wykorzystujące bibliotekę GAVL: scale0tilt,
vectorscope, rgbparade.

%package plugins-opencv
Summary:	Frei0r plugins that use OpenCV library
Summary(pl.UTF-8):	Wtyczki Frei0r wykorzystujące bibliotekę OpenCV
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opencv >= 1.0.0

%description plugins-opencv
Frei0r plugins that use OpenCV library: facebl0r, facedetect.

%description plugins-opencv -l pl.UTF-8
Wtyczki Frei0r wykorzystujące bibliotekę OpenCV: facebl0r, facedetect.

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

sed -i -e 's/^PACKAGE_LIB_DIR=.*/PACKAGE_LIB_DIR=${libdir}/' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_libdir}/frei0r-1/3dflippo.so
%attr(755,root,root) %{_libdir}/frei0r-1/B.so
%attr(755,root,root) %{_libdir}/frei0r-1/G.so
%attr(755,root,root) %{_libdir}/frei0r-1/R.so
%attr(755,root,root) %{_libdir}/frei0r-1/RGB.so
%attr(755,root,root) %{_libdir}/frei0r-1/addition.so
%attr(755,root,root) %{_libdir}/frei0r-1/addition_alpha.so
%attr(755,root,root) %{_libdir}/frei0r-1/alpha0ps.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphaatop.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphagrad.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphain.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphainjection.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphaout.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphaover.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphaspot.so
%attr(755,root,root) %{_libdir}/frei0r-1/alphaxor.so
%attr(755,root,root) %{_libdir}/frei0r-1/balanc0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/baltan.so
%attr(755,root,root) %{_libdir}/frei0r-1/blend.so
%attr(755,root,root) %{_libdir}/frei0r-1/bluescreen0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/brightness.so
%attr(755,root,root) %{_libdir}/frei0r-1/burn.so
%attr(755,root,root) %{_libdir}/frei0r-1/bw0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/c0rners.so
%attr(755,root,root) %{_libdir}/frei0r-1/cartoon.so
%attr(755,root,root) %{_libdir}/frei0r-1/cluster.so
%attr(755,root,root) %{_libdir}/frei0r-1/color_only.so
%attr(755,root,root) %{_libdir}/frei0r-1/coloradj_RGB.so
%attr(755,root,root) %{_libdir}/frei0r-1/colordistance.so
%attr(755,root,root) %{_libdir}/frei0r-1/composition.so
%attr(755,root,root) %{_libdir}/frei0r-1/contrast0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/curves.so
%attr(755,root,root) %{_libdir}/frei0r-1/d90stairsteppingfix.so
%attr(755,root,root) %{_libdir}/frei0r-1/darken.so
%attr(755,root,root) %{_libdir}/frei0r-1/defish0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/delay0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/delaygrab.so
%attr(755,root,root) %{_libdir}/frei0r-1/difference.so
%attr(755,root,root) %{_libdir}/frei0r-1/distort0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/divide.so
%attr(755,root,root) %{_libdir}/frei0r-1/dodge.so
%attr(755,root,root) %{_libdir}/frei0r-1/edgeglow.so
%attr(755,root,root) %{_libdir}/frei0r-1/equaliz0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/flippo.so
%attr(755,root,root) %{_libdir}/frei0r-1/gamma.so
%attr(755,root,root) %{_libdir}/frei0r-1/glow.so
%attr(755,root,root) %{_libdir}/frei0r-1/grain_extract.so
%attr(755,root,root) %{_libdir}/frei0r-1/grain_merge.so
%attr(755,root,root) %{_libdir}/frei0r-1/hardlight.so
%attr(755,root,root) %{_libdir}/frei0r-1/hqdn3d.so
%attr(755,root,root) %{_libdir}/frei0r-1/hue.so
%attr(755,root,root) %{_libdir}/frei0r-1/hueshift0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/invert0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/ising0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/lenscorrection.so
%attr(755,root,root) %{_libdir}/frei0r-1/letterb0xed.so
%attr(755,root,root) %{_libdir}/frei0r-1/levels.so
%attr(755,root,root) %{_libdir}/frei0r-1/lighten.so
%attr(755,root,root) %{_libdir}/frei0r-1/lightgraffiti.so
%attr(755,root,root) %{_libdir}/frei0r-1/lissajous0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/luminance.so
%attr(755,root,root) %{_libdir}/frei0r-1/mask0mate.so
%attr(755,root,root) %{_libdir}/frei0r-1/multiply.so
%attr(755,root,root) %{_libdir}/frei0r-1/nervous.so
%attr(755,root,root) %{_libdir}/frei0r-1/nois0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/nosync0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/onecol0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/overlay.so
%attr(755,root,root) %{_libdir}/frei0r-1/partik0l.so
%attr(755,root,root) %{_libdir}/frei0r-1/perspective.so
%attr(755,root,root) %{_libdir}/frei0r-1/pixeliz0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/plasma.so
%attr(755,root,root) %{_libdir}/frei0r-1/pr0be.so
%attr(755,root,root) %{_libdir}/frei0r-1/pr0file.so
%attr(755,root,root) %{_libdir}/frei0r-1/primaries.so
%attr(755,root,root) %{_libdir}/frei0r-1/saturat0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/saturation.so
%attr(755,root,root) %{_libdir}/frei0r-1/scanline0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/screen.so
%attr(755,root,root) %{_libdir}/frei0r-1/select0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/sharpness.so
%attr(755,root,root) %{_libdir}/frei0r-1/sobel.so
%attr(755,root,root) %{_libdir}/frei0r-1/softlight.so
%attr(755,root,root) %{_libdir}/frei0r-1/sopsat.so
%attr(755,root,root) %{_libdir}/frei0r-1/squareblur.so
%attr(755,root,root) %{_libdir}/frei0r-1/subtract.so
%attr(755,root,root) %{_libdir}/frei0r-1/tehroxx0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_B.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_C.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_G.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_I.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_L.so
%attr(755,root,root) %{_libdir}/frei0r-1/test_pat_R.so
%attr(755,root,root) %{_libdir}/frei0r-1/three_point_balance.so
%attr(755,root,root) %{_libdir}/frei0r-1/threelay0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/threshold0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/tint0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/transparency.so
%attr(755,root,root) %{_libdir}/frei0r-1/twolay0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/uvmap.so
%attr(755,root,root) %{_libdir}/frei0r-1/value.so
%attr(755,root,root) %{_libdir}/frei0r-1/vertigo.so
%attr(755,root,root) %{_libdir}/frei0r-1/xfade0r.so

%files plugins-gavl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/frei0r-1/scale0tilt.so
%attr(755,root,root) %{_libdir}/frei0r-1/vectorscope.so
%attr(755,root,root) %{_libdir}/frei0r-1/rgbparade.so

%if %{with opencv}
%files plugins-opencv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/frei0r-1/facebl0r.so
%attr(755,root,root) %{_libdir}/frei0r-1/facedetect.so
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/frei0r.h
%{_pkgconfigdir}/frei0r.pc
