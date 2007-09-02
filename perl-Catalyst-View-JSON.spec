%define realname Catalyst-View-JSON
%define name	perl-%{realname}
%define modprefix Catalyst
%define version	0.20
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	JSON view for your data
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.6
BuildRequires:	perl(JSON) >= 1
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Test::More) >= 0.32
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Catalyst::View::JSON is a Catalyst View handler that returns stash
data in JSON format.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}

