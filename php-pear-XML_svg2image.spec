%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	svg2image
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - converts a SVG file to a PNG/JPEG image
Summary(pl):	%{_pearname} - konwersja plików SVG do obrazków PNG/JPEG
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	952ba13f07b57b24f54288b8e333b29d
URL:		http://pear.php.net/package/XML_svg2image/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a SVG file to a PNG/JPEG image with the help of apache-batik
(java-program), needs therefore a PHP with ext/java compiled-in and
the batik files from http://xml.apache.org/batik/.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta przekszta³ca pliki SVG do obrazków PNG/JPEG przy pomocy
programu apache-batik (w Javie), dlatego wymaga PHP z rozszerzeniem
java i plików batik z http://xml.apache.org/batik/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
