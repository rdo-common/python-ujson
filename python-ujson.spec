%global modname ujson
%global srcname ultrajson

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{modname}
Version:        1.35
Release:        1%{?dist}
Summary:        An ultra fast JSON encoder and decoder written in pure C

License:        BSD
URL:            https://github.com/esnme/ultrajson
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz
# https://github.com/esnme/ultrajson/commit/39435177118c9fbc5d3863879c6e4616fd4c12c5
Patch0001:      0001-do-not-forcefully-remove-the-build-directory-manuall.patch

%global _description \
UltraJSON is an ultra fast JSON encoder and decoder written in\
pure C with bindings for Python.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  pytz
BuildRequires:  python-blist
BuildRequires:  python-unittest2
%{?python_provide:%python_provide python2-%{modname}}

%description -n python2-%{modname} %{_description}

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytz
BuildRequires:  python3-blist
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
PYTHONPATH=%{buildroot}%{python2_sitearch} %{__python2} tests/tests.py -v
%if 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} tests/tests.py -v
%endif

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.rst
%{python2_sitearch}/%{modname}-%{version}-py%{python2_version}.egg-info/
%{python2_sitearch}/%{modname}.so

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{modname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{modname}*.so
%endif

%changelog
* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.35-1
- Update to 1.35
- Run test suite
- Spec cleanups

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.33-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 1.33-2
- Rebuilt for Python3.5 rebuild

* Sat Aug 1 2015 Julien Enselme <jujens@jujens.eu> - 1.33-1
- Update to 1.33
- Enable python3 subpackage
- Update SPEC to match packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Dec 19 2012 Kushal Das <kushal@fedoraproject.org> 1.23-1
- Intial package
