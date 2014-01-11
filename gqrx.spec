Summary:	Software defined radio receiver powered by GNU Radio and Qt
Name:		gqrx
Version:	2.2.0
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Engineering
URL:		http://gqrx.dk/
Source0:	http://downloads.sourceforge.net/gqrx/%{name}-%{version}-src.tar.gz
# Source0-md5:	ff771b9c31ee17f704859398362b8cc0
BuildRequires:	boost-devel
BuildRequires:	gnuradio-devel >= 3.7
BuildRequires:	gr-osmosdr-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	qt-devel

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
%setup -q

%build
qmake-qt4 gqrx.pro

%{__make} \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*
