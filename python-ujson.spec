%global pypi_name ujson

Name:           python-%{pypi_name}
Version:        1.33
Release:        2%{?dist}
Summary:        An ultra fast JSON encoder and decoder written in pure C

Group:          Development/Libraries
License:        BSD
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/esnme/ultrajson/master/LICENSE.txt
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tools


%description
UltraJSON is an ultra fast JSON encoder and decoder written in
pure C with bindings for Python


%package -n python2-%{pypi_name}
Summary:        An ultra fast JSON encoder and decoder written in pure C
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
UltraJSON is an ultra fast JSON encoder and decoder written in
pure C with bindings for Python


%package -n python3-%{pypi_name}
Summary:        An ultra fast JSON encoder and decoder written in pure C
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
UltraJSON is an ultra fast JSON encoder and decoder written in
pure C with bindings for Python


%prep
%setup -qn %{pypi_name}-%{version}
cp -a %{SOURCE1} .
# Remove egg-info
rm -rf *.egg-info


%build
%py2_build
%py3_build


%install
# If we install with --skip-build the build directory containing the C
# extensions are deleted before the install. So, nothing install besides the
# egg-info. See: https://github.com/esnme/ultrajson/issues/179
%{__python2} setup.py install -O1 --root %{buildroot}
%{__python3} setup.py install -O1 --root %{buildroot}


%check
# Test requires the PYTHONPATH to be updated with the result of the build. This
# requires to correctly go in the arm folder.
# See: https://lists.fedoraproject.org/pipermail/packaging/2015-July/010898.html
# %%{__python2} tests/tests.py
# Must run 2to3 before running test suite with python3
2to3 -w tests/tests.py
# %%{__python3} tests/tests.py


%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitearch}/%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitearch}/%{pypi_name}.so

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{pypi_name}*.so


%changelog
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
