Summary: Enterprise Volume Management System utilities
Name: evms
Version: 0.9.0
Release: 1
Copyright: GPL
Group: System Environment/Base
Source0: http://prdownloads.sourceforge.net/evms/evms-%{version}.tar.gz
URL: http://www.sourceforge.net/projects/evms
Packager: Kevin Corry <corryk@us.ibm.com>
Buildroot: /var/tmp/%{name}-root

%description
This package contains the user-space tools needed to manage EVMS (Enterprise
Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel patched
with the most recent EVMS code. This code is available in the source package
on the project web page http://www.sf.net/projects/evms/.

Please see the EVMS-HOWTO on the project web page or in the source package
for detailed instructions on patching your kernel with EVMS and using the
tools after installation.

%prep
%setup

%build
cd engine
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
cd engine
make prefix="$RPM_BUILD_ROOT/usr" exec_prefix="$RPM_BUILD_ROOT/usr" install

%post
ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,-,root)
/usr/lib/libdlist.so.1.0
/usr/lib/libevms-0.9.0.so
/usr/lib/evms/libaixregmgr.0.1.0.so
/usr/lib/evms/libbbr.1.0.0.so
/usr/lib/evms/libdefsegmgr.1.0.0.so
/usr/lib/evms/libdrivelink.1.0.0.so
/usr/lib/evms/liblocaldskmgr.1.0.0.so
/usr/lib/evms/liblvmregmgr.0.8.0.so
/usr/lib/evms/libmdregmgr.0.1.0.so
/usr/lib/evms/libos2regmgr.1.0.0.so
/usr/lib/evms/libsnapshot.2.0.0.so
/usr/sbin/evms
/usr/sbin/evmsgui
/usr/sbin/evmsn
/usr/sbin/evms_devnode_fixup
/usr/sbin/evms_rediscover
/usr/sbin/evms_lvcreate
/usr/sbin/evms_lvdisplay
/usr/sbin/evms_lvextend
/usr/sbin/evms_lvreduce
/usr/sbin/evms_lvremove
/usr/sbin/evms_lvscan
/usr/sbin/evms_pvcreate
/usr/sbin/evms_pvdisplay
/usr/sbin/evms_pvremove
/usr/sbin/evms_pvscan
/usr/sbin/evms_vgcreate
/usr/sbin/evms_vgdisplay
/usr/sbin/evms_vgextend
/usr/sbin/evms_vgreduce
/usr/sbin/evms_vgremove
/usr/sbin/evms_vgscan
/usr/include/evms/appAPI.h
/usr/include/evms/appstructs.h
/usr/include/evms/common.h
/usr/include/evms/enginestructs.h
/usr/include/evms/frontend.h
/usr/include/evms/fullengine.h
/usr/include/evms/options.h
/usr/include/evms/plugfuncs.h
/usr/include/evms/plugin.h

%changelog
* Mon Jan 14 2002 Kevin Corry <corryk@us.ibm.com>
- updated necessary entries for 0.9.0 release.
- added evms_rediscover utility.

* Tue Dec 11 2001 Kevin Corry <corryk@us.ibm.com>
- updated necessary entries for 0.2.4 release.
- added text-mode UI, dev-node fixup program, new LVM utilities, MD region
  manager, and AIX region manager.

* Mon Nov 5 2001 Kevin Corry <corryk@us.ibm.com>
- updated necessary entries for 0.2.3 release.

* Fri Nov 2 2001 Kevin Corry <corryk@us.ibm.com>
- updated necessary entries for 0.2.2 release.

* Tue Oct 23 2001 Kevin Corry <corryk@us.ibm.com>
- added comments about requiring kernel patch and rebuild

* Sat Oct 20 2001 Kevin Corry <corryk@us.ibm.com>
- added OS/2 region manager library
- added more LVM-compatible utilities

* Thu Oct 11 2001 Kevin Corry <corryk@us.ibm.com>
- added new LVM-compatible utilities
- updated version numbers of all plugin libraries

* Tue Oct 9 2001 Hollis Blanchard <hollis@austin.ibm.com>
- added %post ldconfig (so the libevms.so symlink is created)
- removed BBR makefile patch
- autoconf before configure

* Sun Oct 7 2001 Hollis Blanchard <hollis@austin.ibm.com>
- initial spec
 
