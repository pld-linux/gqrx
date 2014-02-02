Summary:	Software defined radio receiver powered by GNU Radio and Qt
Name:		gqrx
Version:	2.2.0
Release:	3
License:	GPL v3+
Group:		Applications/Engineering
Source0:	http://downloads.sourceforge.net/gqrx/%{name}-%{version}-src.tar.gz
# Source0-md5:	ff771b9c31ee17f704859398362b8cc0
URL:		http://gqrx.dk/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	boost-devel
BuildRequires:	gnuradio-devel >= 3.7
BuildRequires:	gr-osmosdr-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
%setup -q

%build
install -d build
cd build
qmake-qt4 \
	PREFIX=%{_prefix} \
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
