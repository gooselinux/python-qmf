%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Name:           python-qmf
Version:        0.7.946106
Release:        5%{?dist}
Summary:        Python QMF library for Apache Qpid

Group:          Development/Python
License:        ASL 2.0
URL:            http://qpid.apache.org
Source0:        qpid-extras-qmf-%{version}.tar.gz
# svn export -r<rev> http://svn.apache.org/repos/asf/qpid/trunk/qpid/extras/qmf qpid-extras-qmf-0.7.<rev>
# tar czf qpid-extras-qmf-0.7.<rev>.tar.gz qpid-extras-qmf-0.7.<rev>
Patch0: 0001-Bug-593828-QMF-python-console-needs-ability-to-filte.patch
Patch1: 0002-qpid-tool-re-write.patch
Patch2: 0003-Added-missing-method-for-ObjectId.patch
Patch3: 0004-Fixed-the-keywords-for-object-timestamps.-They-were-.patch
Patch4: 0005-Bug-595914-QMF-python-console-will-occasionally-cras.patch
Patch5: 0006-Bug-602313-qpid-tool-does-not-show-correct-deleted-t.patch
Patch6: 0007-Bug-601685-Add-flow-control-to-qmf-console.patch
Patch7: 0008-Bug-604866-Adjust-heartbeat-timeout.patch
Patch8: 0009-Bug-604326-Collector-object-is-slow-to-appear.patch
Patch9: 0010-Bug-607754-1.3-qpid-config-does-not-work-against-1.2.patch
Patch10: 0011-Bug-598684-Spurious-agent-deletes-under-load.patch
Patch11: remove_qmf2.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel

Requires:       python-qpid >= 0.7

%description
Python QMF library for Apache Qpid

%prep
%setup -q -n qpid-extras-qmf-%{version}
%patch0 -p4
%patch1 -p4
%patch2 -p4
%patch3 -p4
%patch4 -p4
%patch5 -p4
%patch6 -p4
%patch7 -p4
%patch8 -p4
%patch9 -p4
%patch10 -p4
%patch11 -p4

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/qmf
%doc LICENSE.txt NOTICE.txt

%if "%{python_version}" >= "2.6"
%{python_sitelib}/qpid_qmf-*.egg-info
%endif

%changelog
* Wed Jun 30 2010 Kenneth A. Giusti <kgiusti@redhat.com> - 0.7.946106-5
- Resolves: bz609632
- Removes QMFv2 prototype code.

* Thu Jun 17 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.946106-4
- Pulled full patch set out of git.

* Thu May 20 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-3
- Additional patch to console.py
- Related: rhbz574881

* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-2
- Patch to console.py
- Related: rhbz574881

* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-1
- Rebased to svn rev 946106
- Related: rhbz574881

* Mon Apr 19 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.934605-1
- Rebased to svn rev 934605.

* Thu Apr  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.930108-1
- Rebased to svn rev 930108.

* Wed Mar  3 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-5
- Actually changed defines to globals.

* Wed Mar  3 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-4
- Changed defines to globals and moved to top.
- Removed unnecessary python Requires/BuildRequires.

* Tue Mar  2 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-3
- Added correct version to python-qpid dependency.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-2
- Conditionalize egg-info on python version.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-1
- Initial build.
