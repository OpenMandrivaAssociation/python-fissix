Name:		python-fissix
Version:	24.4.24
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/f/fissix/fissix-%{version}.tar.gz
Summary:	Monkeypatches to override default behavior of lib2to3.
URL:		https://pypi.org/project/fissix/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Monkeypatches to override default behavior of lib2to3.

%files
%{py_sitedir}/fissix
%{py_sitedir}/fissix-*.*-info
