%define upstream_name    Catalyst-View-JSON
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	JSON view for your data
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.6
BuildRequires:	perl(Catalyst::Plugin::Unicode)
BuildRequires:	perl(YAML)
BuildRequires:	perl(JSON) >= 1
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Test::More) >= 0.32
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Catalyst::View::JSON is a Catalyst View handler that returns stash
data in JSON format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
