#
# Conditional build:
%bcond_without	opencv		# OpenCV support
#
%ifarch x32
%undefine	with_opencv
%endif

Summary:	Minimalistic plugin API for video effects - common package
Summary(pl.UTF-8):	Minimalistyczne API wtyczek efektów wideo - wspólny pakiet
Name:		frei0r
Version:	3.2.1
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/dyne/frei0r/releases
Source0:	https://github.com/dyne/frei0r/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d72555cc6c578360164e6eda5640642f
URL:		https://frei0r.dyne.org/
BuildRequires:	cmake >= 3.12
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	doxygen
BuildRequires:	gavl-devel >= 0.2.3
BuildRequires:	libstdc++-devel >= 6:4.7
%{?with_opencv:BuildRequires:	opencv-devel >= 1:4.0.0}
BuildRequires:	pkgconfig
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

%package plugins-cairo
Summary:	Frei0r plugins that use Cairo library
Summary(pl.UTF-8):	Wtyczki Frei0r wykorzystujące bibliotekę Cairo
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo >= 1.0.0

%description plugins-cairo
Frei0r plugins that use Cairo library: cairoaffineblend, cairoblend,
cairogradient, cairoimagegrid, ndvi.

%description plugins-cairo -l pl.UTF-8
Wtyczki Frei0r wykorzystujące bibliotekę Cairo: cairoaffineblend,
cairoblend, cairogradient, cairoimagegrid, ndvi.

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

%build
mkdir -p build
cd build
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	%{!?with_opencv:-DWITHOUT_OPENCV:BOOL=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md ChangeLog README.md
%dir %{_libdir}/frei0r-1

%files plugins
%defattr(644,root,root,755)
%{_libdir}/frei0r-1/3dflippo.so
%{_libdir}/frei0r-1/B.so
%{_libdir}/frei0r-1/G.so
%{_libdir}/frei0r-1/IIRblur.so
%{_libdir}/frei0r-1/R.so
%{_libdir}/frei0r-1/RGB.so
%{_libdir}/frei0r-1/addition.so
%{_libdir}/frei0r-1/addition_alpha.so
%{_libdir}/frei0r-1/aech0r.so
%{_libdir}/frei0r-1/alpha0ps_alpha0ps.so
%{_libdir}/frei0r-1/alpha0ps_alphagrad.so
%{_libdir}/frei0r-1/alpha0ps_alphaspot.so
%{_libdir}/frei0r-1/alphaatop.so
%{_libdir}/frei0r-1/alphain.so
%{_libdir}/frei0r-1/alphainjection.so
%{_libdir}/frei0r-1/alphaout.so
%{_libdir}/frei0r-1/alphaover.so
%{_libdir}/frei0r-1/alphaxor.so
%{_libdir}/frei0r-1/balanc0r.so
%{_libdir}/frei0r-1/baltan.so
%{_libdir}/frei0r-1/bgsubtract0r.so
%{_libdir}/frei0r-1/blend.so
%{_libdir}/frei0r-1/bluescreen0r.so
%{_libdir}/frei0r-1/brightness.so
%{_libdir}/frei0r-1/burn.so
%{_libdir}/frei0r-1/bw0r.so
%{_libdir}/frei0r-1/c0rners.so
%{_libdir}/frei0r-1/camerashake.so
%{_libdir}/frei0r-1/cartoon.so
%{_libdir}/frei0r-1/cluster.so
%{_libdir}/frei0r-1/colgate.so
%{_libdir}/frei0r-1/color_only.so
%{_libdir}/frei0r-1/coloradj_RGB.so
%{_libdir}/frei0r-1/colordistance.so
%{_libdir}/frei0r-1/colorenhance.so
%{_libdir}/frei0r-1/colorhalftone.so
%{_libdir}/frei0r-1/colorize.so
%{_libdir}/frei0r-1/colortap.so
%{_libdir}/frei0r-1/composition.so
%{_libdir}/frei0r-1/contrast0r.so
%{_libdir}/frei0r-1/curves.so
%{_libdir}/frei0r-1/d90stairsteppingfix.so
%{_libdir}/frei0r-1/darken.so
%{_libdir}/frei0r-1/defish0r.so
%{_libdir}/frei0r-1/delay0r.so
%{_libdir}/frei0r-1/delaygrab.so
%{_libdir}/frei0r-1/denoise_hqdn3d.so
%{_libdir}/frei0r-1/difference.so
%{_libdir}/frei0r-1/distort0r.so
%{_libdir}/frei0r-1/dither.so
%{_libdir}/frei0r-1/divide.so
%{_libdir}/frei0r-1/dodge.so
%{_libdir}/frei0r-1/edgeglow.so
%{_libdir}/frei0r-1/elastic_scale.so
%{_libdir}/frei0r-1/emboss.so
%{_libdir}/frei0r-1/equaliz0r.so
%{_libdir}/frei0r-1/euclid_eraser.so
%{_libdir}/frei0r-1/filmgrain.so
%{_libdir}/frei0r-1/flippo.so
%{_libdir}/frei0r-1/gamma.so
%{_libdir}/frei0r-1/gateweave.so
%{_libdir}/frei0r-1/glitch0r.so
%{_libdir}/frei0r-1/glow.so
%{_libdir}/frei0r-1/grain_extract.so
%{_libdir}/frei0r-1/grain_merge.so
%{_libdir}/frei0r-1/hardlight.so
%{_libdir}/frei0r-1/heatmap0r.so
%{_libdir}/frei0r-1/hue.so
%{_libdir}/frei0r-1/hueshift0r.so
%{_libdir}/frei0r-1/invert0r.so
%{_libdir}/frei0r-1/ising0r.so
%{_libdir}/frei0r-1/kaleid0sc0pe.so
%{_libdir}/frei0r-1/keyspillm0pup.so
%{_libdir}/frei0r-1/lenscorrection.so
%{_libdir}/frei0r-1/letterb0xed.so
%{_libdir}/frei0r-1/levels.so
%{_libdir}/frei0r-1/lighten.so
%{_libdir}/frei0r-1/lightgraffiti.so
%{_libdir}/frei0r-1/lissajous0r.so
%{_libdir}/frei0r-1/luminance.so
%{_libdir}/frei0r-1/mask0mate.so
%{_libdir}/frei0r-1/measure_pr0be.so
%{_libdir}/frei0r-1/measure_pr0file.so
%{_libdir}/frei0r-1/medians.so
%{_libdir}/frei0r-1/multiply.so
%{_libdir}/frei0r-1/nervous.so
%{_libdir}/frei0r-1/nois0r.so
%{_libdir}/frei0r-1/normaliz0r.so
%{_libdir}/frei0r-1/nosync0r.so
%{_libdir}/frei0r-1/ntsc.so
%{_libdir}/frei0r-1/onecol0r.so
%{_libdir}/frei0r-1/overlay.so
%{_libdir}/frei0r-1/partik0l.so
%{_libdir}/frei0r-1/perspective.so
%{_libdir}/frei0r-1/pixeliz0r.so
%{_libdir}/frei0r-1/pixs0r.so
%{_libdir}/frei0r-1/plasma.so
%{_libdir}/frei0r-1/posterize.so
%{_libdir}/frei0r-1/premultiply.so
%{_libdir}/frei0r-1/primaries.so
%{_libdir}/frei0r-1/rgbnoise.so
%{_libdir}/frei0r-1/rgbsplit0r.so
%{_libdir}/frei0r-1/saturat0r.so
%{_libdir}/frei0r-1/saturation.so
%{_libdir}/frei0r-1/scanline0r.so
%{_libdir}/frei0r-1/screen.so
%{_libdir}/frei0r-1/select0r.so
%{_libdir}/frei0r-1/sharpness.so
%{_libdir}/frei0r-1/sigmoidaltransfer.so
%{_libdir}/frei0r-1/sleid0r_push-down.so
%{_libdir}/frei0r-1/sleid0r_push-left.so
%{_libdir}/frei0r-1/sleid0r_push-right.so
%{_libdir}/frei0r-1/sleid0r_push-up.so
%{_libdir}/frei0r-1/sleid0r_slide-down.so
%{_libdir}/frei0r-1/sleid0r_slide-left.so
%{_libdir}/frei0r-1/sleid0r_slide-right.so
%{_libdir}/frei0r-1/sleid0r_slide-up.so
%{_libdir}/frei0r-1/sleid0r_wipe-barn-door-h.so
%{_libdir}/frei0r-1/sleid0r_wipe-barn-door-v.so
%{_libdir}/frei0r-1/sleid0r_wipe-circle.so
%{_libdir}/frei0r-1/sleid0r_wipe-down.so
%{_libdir}/frei0r-1/sleid0r_wipe-left.so
%{_libdir}/frei0r-1/sleid0r_wipe-rect.so
%{_libdir}/frei0r-1/sleid0r_wipe-right.so
%{_libdir}/frei0r-1/sleid0r_wipe-up.so
%{_libdir}/frei0r-1/sobel.so
%{_libdir}/frei0r-1/softglow.so
%{_libdir}/frei0r-1/softlight.so
%{_libdir}/frei0r-1/sopsat.so
%{_libdir}/frei0r-1/spillsupress.so
%{_libdir}/frei0r-1/squareblur.so
%{_libdir}/frei0r-1/subtract.so
%{_libdir}/frei0r-1/tehroxx0r.so
%{_libdir}/frei0r-1/test_pat_B.so
%{_libdir}/frei0r-1/test_pat_C.so
%{_libdir}/frei0r-1/test_pat_G.so
%{_libdir}/frei0r-1/test_pat_I.so
%{_libdir}/frei0r-1/test_pat_L.so
%{_libdir}/frei0r-1/test_pat_R.so
%{_libdir}/frei0r-1/three_point_balance.so
%{_libdir}/frei0r-1/threelay0r.so
%{_libdir}/frei0r-1/threshold0r.so
%{_libdir}/frei0r-1/timeout.so
%{_libdir}/frei0r-1/tint0r.so
%{_libdir}/frei0r-1/transparency.so
%{_libdir}/frei0r-1/twolay0r.so
%{_libdir}/frei0r-1/uvmap.so
%{_libdir}/frei0r-1/value.so
%{_libdir}/frei0r-1/vertigo.so
%{_libdir}/frei0r-1/vignette.so
%{_libdir}/frei0r-1/water.so
%{_libdir}/frei0r-1/xfade0r.so

%files plugins-cairo
%defattr(644,root,root,755)
%{_libdir}/frei0r-1/cairoaffineblend.so
%{_libdir}/frei0r-1/cairoblend.so
%{_libdir}/frei0r-1/cairogradient.so
%{_libdir}/frei0r-1/cairoimagegrid.so
%{_libdir}/frei0r-1/mirr0r.so
%{_libdir}/frei0r-1/ndvi.so

%files plugins-gavl
%defattr(644,root,root,755)
%{_libdir}/frei0r-1/scale0tilt.so
%{_libdir}/frei0r-1/vectorscope.so
%{_libdir}/frei0r-1/rgbparade.so

%if %{with opencv}
%files plugins-opencv
%defattr(644,root,root,755)
%{_libdir}/frei0r-1/facebl0r.so
%{_libdir}/frei0r-1/facedetect.so
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/frei0r.h
%{_includedir}/frei0r.hpp
%{_includedir}/frei0r
%{_pkgconfigdir}/frei0r.pc
