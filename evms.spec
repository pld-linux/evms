Summary:	Enterprise Volume Management System utilities
Summary(pl):	Narzêdzia do Enterprise Volume Management System
Name:		evms
Version:	0.9.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/evms/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.sourceforge.net/projects/evms/
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
Conflicts:	kernel < 2.4.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains the user-space tools needed to manage EVMS
(Enterprise Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel
patched with the most recent EVMS code.

%description -l pl
Ten pakiet zawiera narzêdzia potrzebne do zarz±dzania wolumenami
dyskowymi EVMS (Enterprise Volume Management System).

Aby u¿ywaæ tych narzêdzi, musisz mieæ j±dro z odpowiednio now± ³at±
EVMS.

%package devel
Summary:	Header files and develpment documentation for EVMS
Summary(es):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para EVMS
Summary(pl):	Pliki nag³ówkowe i dokumetacja do EVMS
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para a EVMS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for EVMS.

%description devel -l pl
Pliki nag³ówkowe oraz biblioteki developerskie EVMS.

%package static
Summary:	Static EVMS libraries
Summary(es):	Biblioteca estática usada no desenvolvimento de aplicativos com EVMS
Summary(pl):	Biblioteka statyczna EVMS
Summary(pt_BR):	Biblioteca estática de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static EVMS libraries.

%description static -l pl
Statyczne biblioteki EVMS.

%package ncurses
Summary:	Ncurses interface for EVMS
Summary(pl):	Interfejs u¿ytkownika w ncurses dla EVMS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description ncurses
Ncurses interface for EVMS.

%description ncurses -l pl
Graficzny interfejs u¿ytkownika w ncurses dla EVMS.

%package X11
Summary:	GUI interface for EVMS
Summary(pl):	Graficzny interfejs u¿ytkownika dla EVMS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description X11
GUI interface for EVMS.

%description X11 -l pl
Graficzny interfejs u¿ytkownika dla EVMS.

%prep
%setup -q
%patch0 -p1

%build
cd engine
autoconf
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure \
	--with-plugins=all \
	--with-interfaces=all
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_sbindir}

%{__make} -C engine install \
	prefix="$RPM_BUILD_ROOT%{_prefix}" \
	exec_prefix="$RPM_BUILD_ROOT%{_prefix}" \
	sbindir="$RPM_BUILD_ROOT%{_sbindir}" \
	mandir="$RPM_BUILD_ROOT%{_mandir}"

mv $RPM_BUILD_ROOT%{_sbindir}/evmsgui $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_sbindir}

gzip -9nf CHANGES *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/evms
%attr(755,root,root) %{_sbindir}/evms_*
%dir %{_libdir}/evms
%attr(755,root,root) %{_libdir}/evms/*.so
%attr(755,root,root) %{_libdir}/libdlist-*.so
%attr(755,root,root) %{_libdir}/libevms-*.so
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/evms
%attr(755,root,root) %{_libdir}/libdlist.so
%attr(755,root,root) %{_libdir}/libevms.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files ncurses
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/evmsn

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/%{_sbindir}/evmsgui
