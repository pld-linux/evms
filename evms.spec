Summary:	Enterprise Volume Management System utilities
Summary(pl):	Narzêdzia do Enterprise Volume Management System
Name:		evms
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/evms/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/evms/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the user-space tools needed to manage EVMS
(Enterprise Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel
patched with the most recent EVMS code. This code is available in the
source package on the project web page
http://www.sf.net/projects/evms/ .

Please see the EVMS-HOWTO on the project web page or in the source
package for detailed instructions on patching your kernel with EVMS
and using the tools after installation.

%description -l pl
Ten pakiet zawiera narzêdzia potrzebne do zarz±dzania wolumenami
dyskowymi EVMS (Enterprise Volume Management System).

Aby u¿ywaæ tych narzêdzi, musisz mieæ j±dro z odpowiednio now± ³at±
EVMS. Ten kod jest dostêpny na stronie projektu
http://www.sf.net/projects/evms/ .

Dok³adny opis ³atania j±dra i u¿ywania narzêdzi znajduje siê w
ECMS-HOWTO na stronie projektu lub w pakiecie ¼ród³owym.

%prep
%setup -q

%build
cd engine
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd engine
%{__make} install \
	prefix="$RPM_BUILD_ROOT%{_prefix}" \
	exec_prefix="$RPM_BUILD_ROOT%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlist.so.1.0
%attr(755,root,root) %{_libdir}/libevms-0.9.0.so
%dir %{_libdir}/evms
%attr(755,root,root) %{_libdir}/evms/libaixregmgr.0.1.0.so
%attr(755,root,root) %{_libdir}/evms/libbbr.1.0.0.so
%attr(755,root,root) %{_libdir}/evms/libdefsegmgr.1.0.0.so
%attr(755,root,root) %{_libdir}/evms/libdrivelink.1.0.0.so
%attr(755,root,root) %{_libdir}/evms/liblocaldskmgr.1.0.0.so
%attr(755,root,root) %{_libdir}/evms/liblvmregmgr.0.8.0.so
%attr(755,root,root) %{_libdir}/evms/libmdregmgr.0.1.0.so
%attr(755,root,root) %{_libdir}/evms/libos2regmgr.1.0.0.so
%attr(755,root,root) %{_libdir}/evms/libsnapshot.2.0.0.so
%attr(755,root,root) %{_sbindir}/evms
%attr(755,root,root) %{_sbindir}/evmsgui
%attr(755,root,root) %{_sbindir}/evmsn
%attr(755,root,root) %{_sbindir}/evms_devnode_fixup
%attr(755,root,root) %{_sbindir}/evms_rediscover
%attr(755,root,root) %{_sbindir}/evms_lvcreate
%attr(755,root,root) %{_sbindir}/evms_lvdisplay
%attr(755,root,root) %{_sbindir}/evms_lvextend
%attr(755,root,root) %{_sbindir}/evms_lvreduce
%attr(755,root,root) %{_sbindir}/evms_lvremove
%attr(755,root,root) %{_sbindir}/evms_lvscan
%attr(755,root,root) %{_sbindir}/evms_pvcreate
%attr(755,root,root) %{_sbindir}/evms_pvdisplay
%attr(755,root,root) %{_sbindir}/evms_pvremove
%attr(755,root,root) %{_sbindir}/evms_pvscan
%attr(755,root,root) %{_sbindir}/evms_vgcreate
%attr(755,root,root) %{_sbindir}/evms_vgdisplay
%attr(755,root,root) %{_sbindir}/evms_vgextend
%attr(755,root,root) %{_sbindir}/evms_vgreduce
%attr(755,root,root) %{_sbindir}/evms_vgremove
%attr(755,root,root) %{_sbindir}/evms_vgscan
%dir %{_includedir}/evms
%{_includedir}/evms/appAPI.h
%{_includedir}/evms/appstructs.h
%{_includedir}/evms/common.h
%{_includedir}/evms/enginestructs.h
%{_includedir}/evms/frontend.h
%{_includedir}/evms/fullengine.h
%{_includedir}/evms/options.h
%{_includedir}/evms/plugfuncs.h
%{_includedir}/evms/plugin.h
