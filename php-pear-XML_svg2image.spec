# NOTE
# - imho it requires java ext, it is not optional? making it php4-only package
%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	XML_svg2image
Summary:	%{_pearname} - converts a SVG file to a PNG/JPEG image
Summary(pl.UTF-8):	%{_pearname} - konwersja plików SVG do obrazków PNG/JPEG
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2ec2aa629af1d0bac9af1dc9a0e6badc
URL:		http://pear.php.net/package/XML_svg2image/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	java-xmlgraphics-batik
Suggests:	php-java
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a SVG file to a PNG/JPEG image with the help of apache-batik
(java-program), needs therefore a PHP with ext/java compiled-in and
the batik files from <http://xml.apache.org/batik/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta przekształca pliki SVG do obrazków PNG/JPEG przy pomocy
programu apache-batik (w Javie), dlatego wymaga PHP z rozszerzeniem
java i plików batik z <http://xml.apache.org/batik/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/svg2image.php
