%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}
Name:           python-ujson
Version:        1.23
Release:        4%{?dist}
Summary:        An ultra fast JSON encoder and decoder written in pure C

Group:          Development/Libraries
License:        BSD
URL:            http://pypi.python.org/pypi/ujson
Source0:        http://pypi.python.org/packages/source/u/ujson/ujson-%{version}.zip
BuildRequires:  python2-devel python-setuptools


%description
UltraJSON is an ultra fast JSON encoder and decoder written in
pure C with bindings for Python


%prep
%setup -q -n ujson-%{version}

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1  --root $RPM_BUILD_ROOT




%files
%doc README.rst
%{python_sitearch}/ujson*



%changelog
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Dec 19 2012 Kushal Das <kushal@fedoraproject.org> 1.23-1
- Intial package
