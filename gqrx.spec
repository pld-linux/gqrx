#
%bcond_with	pulseaudio
#
Summary:	Software defined radio receiver powered by GNU Radio and Qt
Name:		gqrx
Version:	2.11.5
Release:	1
License:	GPL v3+
Group:		Applications/Engineering
Source0:	https://github.com/csete/gqrx/releases/download/v%{version}/%{name}-sdr-%{version}-src.tar.xz
# Source0-md5:	fed4994d5c04daf70cb19e2393da7a04
URL:		http://gqrx.dk/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	boost-devel
BuildRequires:	gnuradio-devel >= 3.7
BuildRequires:	gr-osmosdr-devel
%if %{with pulseaudio}
BuildRequires:	pulseaudio-devel
%else
BuildRequires:	portaudio-devel
%endif
BuildRequires:	qt5-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
%setup -q -n %{name}-sdr-%{version}

%build
install -d build
cd build
qmake-qt5 \
	PREFIX=%{_prefix} \
	AUDIO_BACKEND=%{?with_pulseaudio:pulse}%{!?with_pulseaudio:portaudio} \
	../gqrx.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/gqrx
