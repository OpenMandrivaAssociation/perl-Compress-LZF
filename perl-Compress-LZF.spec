%define	module	Compress-LZF
%define	name	perl-%{module}
%define	version	3.11
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Compress::LZF - extremely light-weight Lempel-Ziv-Free compression
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/modules/by-module/Compress/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

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



