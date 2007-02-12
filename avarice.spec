Summary:	AVR JTAG ICE interface to GNU Debugger GDB
Summary(pl.UTF-8):	Interfejs AVR JTAG ICEa dla GNU debugera GDB
Name:		avarice
Version:	2.3
Release:	0.1
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/avarice/%{name}-%{version}.tar.gz
# Source0-md5:	0fafa811914f47d3075888d8554ba37f
URL:		http://avarice.sourceforge.net/
Requires:	gdb >= 6.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVaRICE is a program which interfaces the GNU Debugger GDB with the
AVR JTAG ICE available from Atmel.

%description -l pl.UTF-8
AVaRICE jest programem, który jest nakładką na GNU debugera GDB dla
AVR JTAG ICEa firmy Atmel.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
