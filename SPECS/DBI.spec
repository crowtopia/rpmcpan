Name:           %{iov_prefix}-DBI
Version:        1.631
Release:        1%{?dist}
Summary:        Database independent interface for Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBI/
Source0:        http://cpan.metacpan.org/authors/id/T/TI/TIMB/DBI-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{iov_prefix}
Requires:       %{iov_prefix}

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%prep
%setup -q -n DBI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBI*
%{perl_vendorarch}/DBD*
%{perl_vendorarch}/Win32/DBIODBC.pm
%{perl_vendorarch}/Bundle/DBI.pm
%{perl_vendorarch}/dbixs_rev.pl
%{_bindir}/*
%{vendormandir}/man3/*
%{vendormandir}/man1/*

%changelog
* Thu Jul 31 2014 David E. Wheeler <david.wheeler@iovation.com> 1.631-1
- Specfile autogenerated by cpanspec 1.78.
