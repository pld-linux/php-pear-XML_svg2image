%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       svg2image
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Converts a SVG file to a PNG/JPEG image
Summary(pl):	%{_pearname} - konwersja plików SVG do obrazków PNG/JPEG
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a SVG file to a PNG/JPEG image with the help of apache-batik
(java-program), needs therefore a php with ext/java compiled-in and
the batik files from http://xml.apache.org/batik/.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa ta przekszta³ca pliki SVG do obrazków PNG/JPEG przy pomocy
programu apache-batik (w Javie), dlatego wymaga php z rozszerzeniem
java i plików batik z http://xml.apache.org/batik/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README*
%doc %{_pearname}-%{version}/gvt.svg
%{php_pear_dir}/%{_class}/*.php
