#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	MooseX
%define	pnam	ConfigFromFile
Summary:	MooseX::ConfigFromFile - An abstract Moose role for setting attributes from a configfile
Summary(pl.UTF-8):	MooseX::ConfigFromFile - Abstrakcyjna rola Moose do ustawiania atrybutów z pliku konfiguracyjnego
Name:		perl-MooseX-ConfigFromFile
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d473a4379f05f8ea8f7aeac1b1662d2a
URL:		http://search.cpan.org/dist/MooseX-ConfigFromFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Types::Path::Class) >= 0.04
BuildRequires:	perl-Moose >= 0.35
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file.
The actual implementation of reading the configuration file is left to
concrete subroles.

It declares an attribute configfile and a class method
new_with_config, and requires that concrete roles derived from it
implement the class method get_config_from_file.

Attributes specified directly as arguments to new_with_config
supercede those in the configfile.

MooseX::Getopt knows about this abstract role, and will use it if
available to load attributes from the file specified by the
commandline flag --configfile during its normal new_with_options.

%description -l pl.UTF-8
MooseX::ConfigFromFile - Abstrakcyjna rola Moose do ustawiania
atrybutów z pliku konfiguracyjnego

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MooseX/*.pm
%{_mandir}/man3/*
