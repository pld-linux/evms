Summary:	Enterprise Volume Management System utilities
Summary(pl):	Narzêdzia do Enterprise Volume Management System
Name:		evms
Version:	2.5.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/evms/%{name}-%{version}.tar.gz
# Source0-md5:	def675ffe19037dcb74f1393530ee4c7
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

%description -l pl
Ten pakiet zawiera narzêdzia potrzebne do zarz±dzania wolumenami
dyskowymi EVMS (Enterprise Volume Management System).

Aby u¿ywaæ tych narzêdzi, musisz mieæ j±dro z odpowiednio now± ³at±
EVMS.

%package devel
Summary:	Header files for EVMS
Summary(es):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para EVMS
Summary(pl):	Pliki nag³ówkowe dla EVMS
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para a EVMS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for EVMS.

%description devel -l pl
Pliki nag³ówkowe dla EVMS.

%package static
Summary:	Static EVMS library
Summary(es):	Biblioteca estática usada no desenvolvimento de aplicativos com EVMS
Summary(pl):	Statyczna biblioteka EVMS
Summary(pt_BR):	Biblioteca estática de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EVMS library.

%description static -l pl
Statyczna biblioteka EVMS.

%package ncurses
Summary:	Ncurses interface for EVMS
Summary(pl):	Interfejs u¿ytkownika w ncurses dla EVMS
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description ncurses
Ncurses interface for EVMS.

%description ncurses -l pl
Graficzny interfejs u¿ytkownika w ncurses dla EVMS.

%package X11
Summary:	GUI interface for EVMS
Summary(pl):	Graficzny interfejs u¿ytkownika dla EVMS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description X11
GUI interface for EVMS.

%description X11 -l pl
Graficzny interfejs u¿ytkownika dla EVMS.

%prep
%setup -q
%patch0 -p1

%build
mv aclocal.m4 evms.m4

%{__gettextize}
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/ -I ./
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
