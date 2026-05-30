%define module serpent
%bcond tests 1

Name:		python-serpent
Version:	1.43
Release:	1
Summary:	Serialization based on ast.literal_eval
Group:		Development/Python
License:	MIT
URL:		https://github.com/irmen/Serpent
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytz)
%endif

%description
Serpent is a simple serialization library based on ast.literal_eval.Because it
only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.*There is also a Java and a .NET (C)
implementation available.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info
