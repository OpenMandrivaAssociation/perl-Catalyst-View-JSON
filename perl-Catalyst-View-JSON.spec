%define upstream_name    Catalyst-View-JSON
%define upstream_version 0.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	JSON view for your data
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.600.0
BuildRequires:	perl(Catalyst::Plugin::Unicode)
BuildRequires:	perl(YAML)
BuildRequires:	perl(JSON) >= 1
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Test::More) >= 0.32
BuildRequires:	perl(MRO::Compat)

BuildArch:	noarch

%description
Catalyst::View::JSON is a Catalyst View handler that returns stash
data in JSON format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.330.0-1mdv2011.0
+ Revision: 653979
- update to new version 0.33

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.320.0-1mdv2011.0
+ Revision: 628763
- new version

* Wed Sep 22 2010 Shlomi Fish <shlomif@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 580528
- Upgrade to 0.31 and converted to lzma

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 536164
- update buildrequires:
- update to 0.30

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 517299
- update to 0.28

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 510968
- update to 0.27

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 420854
- update to 0.26

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 406310
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2010.0
+ Revision: 371664
- update to new version 0.25

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.24-3mdv2009.0
+ Revision: 255589
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2008.1
+ Revision: 178328
- update to new version 0.24

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2008.1
+ Revision: 174753
- new version

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.1
+ Revision: 152975
- update to new version 0.22
- update to new version 0.22

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2008.1
+ Revision: 105899
- update to new version 0.21
- update to new version 0.21

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.0
+ Revision: 78113
- new version


* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 0.11-1mdv2007.0
- Version 0.11

* Wed Apr 26 2006 Scott Karns <scottk@mandriva.org> 0.09-1mdk
- Initial Mdv RPM

