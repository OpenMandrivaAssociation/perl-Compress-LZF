%define	upstream_name	 Compress-LZF
%define	upstream_version 3.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:	Extremely light-weight Lempel-Ziv-Free compression
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/modules/by-module/Compress/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
LZF is an extremely fast (not that much slower than a pure memcpy) compression
algorithm. It is ideal for applications where you want to save some space but
not at the cost of speed. It is ideal for repetitive data as well. The module
is self-contained and very small (no large library to be pulled in).
It is also free, so there should be no problems incoporating this module into
commercial programs.

"I have no idea wether any patents in any countries apply to this algorithm,
but at the moment it is believed that it is free from any patents."

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.430.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 3.430.0-3
+ Revision: 680835
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.430.0-2mdv2011.0
+ Revision: 555696
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 3.430.0-1mdv2010.0
+ Revision: 406890
- rebuild using %%perl_convert_version

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.43-1mdv2009.1
+ Revision: 320936
- new version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.41-1mdv2009.1
+ Revision: 292032
- update to new version 3.41

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.11-3mdv2009.0
+ Revision: 256039
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.11-1mdv2008.1
+ Revision: 152954
- update to new version 3.11
- update to new version 3.11

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 3.1-2mdv2008.1
+ Revision: 151464
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-1mdv2008.1
+ Revision: 114477
- update to new version 3.1

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdv2008.1
+ Revision: 109525
- update to new version 2.0


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.71-1mdv2007.0
+ Revision: 131636
- 1.71

* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.7-1mdv2007.1
+ Revision: 105017
- first mdv package
- Create perl-Compress-LZF

