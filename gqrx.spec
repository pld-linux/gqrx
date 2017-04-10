#
%bcond_with	pulseaudio
#
Summary:	Software defined radio receiver powered by GNU Radio and Qt
Name:		gqrx
Version:	2.3.2
Release:	4
License:	GPL v3+
Group:		Applications/Engineering
Source0:	http://downloads.sourceforge.net/gqrx/%{name}-%{version}.tar.xz
# Source0-md5:	2dae602db3e7d637a01c7deced7fad4f
Patch0:		%{name}-nopulse.patch
URL:		http://gqrx.dk/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	boost-devel
BuildRequires:	gnuradio-devel >= 3.7
BuildRequires:	gr-osmosdr-devel
%if %{with pulseaudio}
BuildRequires:	pulseaudio-devel
%else
BuildRequires:	portaudio-devel
%endif
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
qmake-qt4 \
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
