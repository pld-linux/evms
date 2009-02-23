Summary:	Enterprise Volume Management System utilities
Summary(pl.UTF-8):	Narzędzia do Enterprise Volume Management System
Name:		evms
Version:	2.5.5
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/evms/%{name}-%{version}.tar.gz
# Source0-md5:	45b463f0cbade194dc0a08be432b572e
Patch0:		%{name}-link.patch
URL:		http://evms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	glibc-static
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-ext-devel
Conflicts:	kernel < 2.4.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		_libdir		/%{_lib}

%description
This package contains the user-space tools needed to manage EVMS
(Enterprise Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel
patched with the most recent EVMS code.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia potrzebne do zarządzania wolumenami
dyskowymi EVMS (Enterprise Volume Management System).

Aby używać tych narzędzi, musisz mieć jądro z odpowiednio nową łatą
EVMS.

%package devel
Summary:	Header files for EVMS
Summary(es.UTF-8):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para EVMS
Summary(pl.UTF-8):	Pliki nagłówkowe dla EVMS
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para a EVMS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for EVMS.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla EVMS.

%package static
Summary:	Static EVMS library
Summary(es.UTF-8):	Biblioteca estática usada no desenvolvimento de aplicativos com EVMS
Summary(pl.UTF-8):	Statyczna biblioteka EVMS
Summary(pt_BR.UTF-8):	Biblioteca estática de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EVMS library.

%description static -l pl.UTF-8
Statyczna biblioteka EVMS.

%package ncurses
Summary:	Ncurses interface for EVMS
Summary(pl.UTF-8):	Interfejs użytkownika w ncurses dla EVMS
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description ncurses
Ncurses interface for EVMS.

%description ncurses -l pl.UTF-8
Graficzny interfejs użytkownika w ncurses dla EVMS.

%package X11
Summary:	GUI interface for EVMS
Summary(pl.UTF-8):	Graficzny interfejs użytkownika dla EVMS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description X11
GUI interface for EVMS.

%description X11 -l pl.UTF-8
Graficzny interfejs użytkownika dla EVMS.

%prep
%setup -q
%patch0 -p1

head -n 1420 aclocal.m4 > acinclude.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}

%configure

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/evms.conf $RPM_BUILD_ROOT%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog INSTALL* PLUGIN* TERMINOLOGY
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/evms.conf
%attr(755,root,root) %{_sbindir}/evms*
%exclude %{_sbindir}/evmsn
%exclude %{_sbindir}/evmsgui
%dir %{_libdir}/evms
%dir %{_libdir}/evms/%{version}
%attr(755,root,root) %{_libdir}/evms/%{version}/*.so
%attr(755,root,root) %{_libdir}/libevms-*.so.*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevms.so
%{_includedir}/evms

%files static
%defattr(644,root,root,755)
%{_libdir}/libevms.a

%files ncurses
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/evmsn

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/evmsgui
