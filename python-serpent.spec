# Created by pyp2rpm-3.3.3
%bcond_without tests
%global pypi_name serpent

Name:           python-%{pypi_name}
Version:        1.30.2
Release:        1
Summary:        Serialization based on ast.literal_eval

License:        MIT
URL:            https://github.com/irmen/Serpent
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with tests}
BuildRequires:  python-attrs
BuildRequires:  python-pytz
%endif

%description
Serpent is a simple serialization library based on ast.literal_eval.Because it
only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.*There is also a Java and a .NET (C)
implementation available.

%{?python_provide:%python_provide python-%{pypi_name}}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} setup.py test
%endif


%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
#%%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

