Summary:	Python Documentation Utilities
Name:		python-docutils
Version:	0.11
Release:	1
License:	Public Domain, BSD, GPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/d/docutils/docutils-%{version}.tar.gz
# Source0-md5:	20ac380a18b369824276864d98ec0ad6
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docutils is a modular system for processing documentation into useful
formats, such as HTML, XML, and LaTeX. For input Docutils supports
reStructuredText, an easy-to-read, what-you-see-is-what-you-get
plaintext markup syntax.

%prep
%setup -qn docutils-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/rst*
%{py_sitescriptdir}/docutils
%{py_sitescriptdir}/*.egg-info

